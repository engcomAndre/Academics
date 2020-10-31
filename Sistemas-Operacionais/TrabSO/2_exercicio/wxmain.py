# -*- coding: utf-8 -*-
__AUTHOR__ = ['Alfredo Miranda', 'Mikhail Pedrosa', 'Yuri Reis']
__DESCRIPTION__ = 'Aplicação que simula vários processos e um módulo detector de deadlock do Sistema Operacional.'
__DATE__ = '17/10/13'
__VERSION__ = "1.4"

import wx
import random
import time
from threading import Thread, Semaphore, Event

MAX_RESOURCES = 10
MAX_PROCESSES = 15

#Lista com os objetos Resources criados
resources = []
#Lista com os objetos MyProcess existentes atualmente no sistema
processes = []
#Lista responsável por armazenar as mensagens de comunicação entre a GUI e as Threads
list_message = []

#Dicionário(Matriz A) (resource code: key, quantidade atual: value)
dic_resources = {}
#Semáforo responsável pelo dic_resources
semaphore = Semaphore()

#Variável que armazena a quantidade de recursos definida na primeira tela
qnt_resource = 0
#Contador de processos no programa
count_process = 0

DT_SO = None


class Resource(object):
    """
    Classe Resource que implementa os Recursos.
    """
    def __init__(self, code, name, qnt):
        self.code = code
        self.name = name
        self.qnt = int(qnt)


class MyProcess(Thread):
    """
    Classe MyProcess que implementa os processos.
    """
    def __init__(self, code, d_ts, d_tu):
        """
        Construtor da thread.
        """
        super(MyProcess, self).__init__()
        self.code = code
        self._stop = False
        #Tempo para requisição de um recurso
        self.d_ts = d_ts
        #Tempo de utilização de recurso
        self.d_tu = d_tu
        #Lista com os recursos alocados e seus contadores de tempo
        self.resources = []
        #Dicionário(Linha da Matriz C) com a quantidade de recursos alocados
        self.resources_allocated = {}
        #Dicionário(Linha da Matriz R) com a quantidade de recursos requisitados
        self.resources_request = {}
        for r in resources:
            #Zerando os contadores para cada recurso
            self.resources_allocated[r.code] = 0
            self.resources_request[r.code] = 0
        #Código de requisição
        self.code_requesting = None
        #Objeto Event que será utilizado para a thread dormir no Request
        self.event = Event()
        self.status = "Okay"
        list_message.append("Processo {0} criado.". format(self.code))

    def run(self):
        """
        Função executada quando a thread é iniciada.
        """
        count_ts = 0
        while not self._stop:
            if count_ts == self.d_ts:
                self.request()
                if self._stop:
                    break
                count_ts = 0
            self.use()
            time.sleep(1)
            count_ts += 1
        self.free()
        list_message.append("Processo {0} foi encerrado.".format(self.code))

    def request(self):
        global dic_resources
        self.code_requesting = random.randrange(0, qnt_resource)

        if resources[self.code_requesting].qnt > self.resources_allocated[self.code_requesting]:
            self.resources_request[self.code_requesting] += 1
            list_message.append("Processo {1} requisitou o recurso {0}.".format(self.code_requesting, self.code))
            while not self._stop:
                self.status = "Requisitando"
                semaphore.acquire()
                if dic_resources[self.code_requesting] == 0:
                    #Aguardando liberarem recurso requisitado.
                    semaphore.release()
                    self.event.wait()
                    self.event.clear()
                else:
                    #Alocando recurso
                    dic_resources[self.code_requesting] -= 1
                    self.resources.append([self.code_requesting, self.d_tu])
                    self.resources_request[self.code_requesting] -= 1
                    self.resources_allocated[self.code_requesting] += 1
                    semaphore.release()
                    break
        self.code_requesting = None
        self.status = "Okay"

    def use(self):
        for r in self.resources:
            r[1] -= 1
            if r[1] == 0:
                #Liberando recurso
                semaphore.acquire()
                dic_resources[r[0]] += 1
                self.resources_allocated[r[0]] -= 1
                list_message.append("Processo {1} liberou o recurso {0}.".format(r[0], self.code))
                for p in processes:
                    if not self == p:
                        #Acordando os processos que estão requisitando esse recurso
                        if p.code_requesting == r[0]:
                            p.event.set()
                semaphore.release()
        self.resources = filter(lambda x: x[1], self.resources)

    def free(self):
        """
        Função responsável por liberar todos os recursos
        alocados para esse processo.
        """
        for r in self.resources:
            semaphore.acquire()
            dic_resources[r[0]] += 1
            for p in processes:
                if not self == p:
                    if p.code_requesting == r[0]:
                        #Acordando os processos que estão requisitando esse recurso
                        p.event.set()
            semaphore.release()

    def stop(self):
        """
        Função para fazer com que a thread seja encerrada.
        """
        self._stop = True


class Manager(Thread):
    """
    Classe Manager que implementa o S.O., responsável
    por detectar os deadlocks.
    """
    def __init__(self, num):
        """
        Construtor da thread.
        """
        super(Manager, self).__init__()
        self.num = num
        self.dt = DT_SO
        self._stop = False

    def run(self):
        """
        Função executada quando a thread é iniciada.
        """

        while not self._stop:
            #Salva os dados e executa o processamento em cima de uma matriz estática
            matriz_a = {}
            matriz_c = {}
            matriz_r = {}
            marked = []

            #Bloqueia o semáforo e faz uma cópia de todos os dados (snapshot)
            semaphore.acquire()
            
            for r in dic_resources:
                matriz_a[r] = dic_resources[r]
            
            for p in processes:
                matriz_c[p.code] = {}
                matriz_r[p.code] = {}
                for r in dic_resources:
                    matriz_c[p.code][r] = p.resources_allocated[r]
                    matriz_r[p.code][r] = p.resources_request[r]
            
            semaphore.release()

            for i in range(0, count_process):
                #Lista de processos que não puderam ser executados
                marked = []
                for p in matriz_r:
                    for r in matriz_r[p]:
                        if matriz_r[p][r] > matriz_a[r]:
                            marked.append(p)
                            break
                    #Desalocar os recursos
                    if p not in marked:
                        for r in matriz_r[p]:
                            matriz_a[r] = (matriz_a[r] - matriz_r[p][r]) + matriz_r[p][r] + matriz_c[p][r]
                            matriz_r[p][r] = 0
                            matriz_c[p][r] = 0

            for p in processes:
                if p.code in marked:
                    p.status = "Deadlock"

            time.sleep(self.dt)

    def stop(self):
        """
        Função para fazer com que a thread seja encerrada.
        """
        self._stop = True


class MyPanel(wx.Panel):
    """
    Classe Panel, responsável por grande parte da GUI. Aonde todos os desenhos acontecem.
    """

    def __init__(self, parent):
        """
        Construtor do Panel. Inicia a primeira tela da aplicação e algumas variáveis.
        """
        wx.Panel.__init__(self, parent)

        #Armazena referência ao frame(pai) do Panel.
        self.frame = parent
        self.count = 0
        self.txt = ""
        self.first_ui()

    def first_ui(self):
        """
        Função responsável por desenha a primeira tela.
        Tela que recebe a quantidade de Recursos.
        """

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        controlSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.widgetSizer = wx.BoxSizer(wx.VERTICAL)

        text = wx.StaticText(self, label="Quantidade de Recursos")
        self.widgetSizer.Add(text, flag=wx.TOP | wx.CENTER | wx.BOTTOM, border=5)
        self.tc1 = wx.TextCtrl(self)
        self.widgetSizer.Add(self.tc1, flag=wx.CENTER, border=5)
        text = wx.StaticText(self, label="Tempo de verificação do S.O.")
        self.widgetSizer.Add(text, flag=wx.TOP | wx.CENTER | wx.BOTTOM, border=5)
        self.tc2 = wx.TextCtrl(self)
        self.widgetSizer.Add(self.tc2, flag=wx.CENTER, border=5)


        addButton = wx.Button(self, label="OK")
        addButton.Bind(wx.EVT_BUTTON, self.buttonOne)
        controlSizer.Add(addButton, 0, wx.CENTER | wx.ALL, 5)

        self.mainSizer.Add(self.widgetSizer, 0, wx.CENTER | wx.ALL, 10)
        self.mainSizer.Add(controlSizer, 0, wx.CENTER)

        self.SetSizer(self.mainSizer)

    def second_ui(self):
        """
        Função responsável pelo desenho da segunda interface.
        Interface responsável por receber as informações dos recursos
        """
        #Criando interface
        height = (qnt_resource * 150) + 50
        self.frame.SetSizeWH(200, height)

        for child in self.GetChildren():
            child.Destroy()

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.widgetSizer = wx.BoxSizer(wx.VERTICAL)
        controlSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.list_box_resources = []

        for i in range(0, qnt_resource):
            self.list_box_resources.append(((wx.StaticText(self, label="Nome:"), wx.TextCtrl(self)),
                                            (wx.StaticText(self, label="Número de Instâncias:"), wx.TextCtrl(self))))
            self.widgetSizer.Add(self.list_box_resources[i][0][0], flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
            self.widgetSizer.Add(self.list_box_resources[i][0][1], flag=wx.LEFT, border=5)
            self.widgetSizer.Add(self.list_box_resources[i][1][0], flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
            self.widgetSizer.Add(self.list_box_resources[i][1][1], flag=wx.LEFT, border=5)

        addButton = wx.Button(self, label="OK")
        addButton.Bind(wx.EVT_BUTTON, self.buttonTwo)
        controlSizer.Add(addButton, 0, wx.CENTER | wx.ALL, 5)

        self.mainSizer.Add(self.widgetSizer, 0, wx.LEFT | wx.ALL, 10)
        self.mainSizer.Add(controlSizer, 0, wx.CENTER | wx.ALL, 10)

        self.SetSizer(self.mainSizer)

        self.refresh()

    def third_ui(self):
        """
        Função responsável pelo desenho da terceira interface.
        """
        #Criando interface
        height = 600
        self.frame.SetSizeWH(800, height)

        for child in self.GetChildren():
            child.Destroy()

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.widgetSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.rSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.logSizer = wx.BoxSizer(wx.HORIZONTAL)
        controlSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.logDisplay = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.pDisplay = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.rDisplay1 = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.rDisplay2 = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY)

        self.killText = wx.TextCtrl(self)
        text1 = wx.StaticText(self, label="T.U.")
        self.tuText = wx.TextCtrl(self)
        text2 = wx.StaticText(self, label="T.R.")
        self.trText = wx.TextCtrl(self)
        killButton = wx.Button(self, label="Kill Process")
        killButton.Bind(wx.EVT_BUTTON, self.kill)
        createButton = wx.Button(self, label="Create Process")
        createButton.Bind(wx.EVT_BUTTON, self.create)

        controlSizer.Add(self.killText, 0, wx.LEFT, 5)
        controlSizer.Add(killButton, 0, wx.LEFT | wx.ALL, 5)
        controlSizer.Add(text1, 0, wx.RIGHT | wx.ALL, 5)
        controlSizer.Add(self.tuText, 0, wx.RIGHT | wx.ALL, 5)
        controlSizer.Add(text2, 0, wx.RIGHT | wx.ALL, 5)
        controlSizer.Add(self.trText, 0, wx.RIGHT | wx.ALL, 5)
        controlSizer.Add(createButton, 0, wx.RIGHT | wx.ALL, 5)

        self.logSizer.Add(self.logDisplay, 1, wx.EXPAND | wx.ALL, 10)
        self.rSizer.Add(self.rDisplay1, 1, wx.EXPAND | wx.ALL, 10)
        self.rSizer.Add(self.rDisplay2, 1, wx.EXPAND | wx.ALL, 10)
        self.widgetSizer.Add(self.pDisplay, 1, wx.EXPAND | wx.ALL, 10)

        self.mainSizer.Add(self.rSizer, 1, wx.EXPAND | wx.ALL, 10)
        self.mainSizer.Add(self.logSizer, 1, wx.EXPAND | wx.ALL, 10)
        self.mainSizer.Add(self.widgetSizer, 1, wx.EXPAND | wx.ALL, 10)
        self.mainSizer.Add(controlSizer, 0, wx.CENTER | wx.ALL, 10)

        txt_resources = "Recursos Totais\n"
        for r in resources:
            txt_resources += "ID: {0} | Nome: {1} | " \
                             "Qnt Total: {2}\n".format(r.code, r.name, r.qnt)
        self.rDisplay1.SetValue(txt_resources)

        self.SetSizer(self.mainSizer)

        self.refresh()

        self.manager = Manager(1)
        self.manager.start()

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_box, self.timer)
        self.timer.Start(50)

    def refresh(self):
        """
        Função que atualiza a tela, fazendo com que todos os elementos
        fiquem no seu lugar corretamente.
        """

        self.mainSizer.Layout()
        self.frame.fSizer.Layout()
        self.Fit()
        self.frame.Layout()

    def buttonOne(self, event):
        """
        Função que está associada ao botão 'OK' da primeira tela.
        É responsável por coletar o valor da caixa de texto e gravar na variável.
        E chama a função que irá inicializar a segunda tela.
        """

        global qnt_resource
        global DT_SO

        try:
            qnt_resource = int(self.tc1.GetValue())
            DT_SO = int(self.tc2.GetValue())
        except ValueError:
            pass

        if qnt_resource and DT_SO:
            if qnt_resource <= MAX_RESOURCES:
                self.second_ui()

    def buttonTwo(self, event):
        """
        Função que está associada ao botão 'OK' da segunda tela.
        É responsável por coletar o valor das caixas de texto e gravar nas variáveis.
        E chama a função que irá inicializar a terceira tela e a thread Manager.
        """
        global resources
        i = 0
        for r in self.list_box_resources:
            resources.append(Resource(i, r[0][1].GetValue(), r[1][1].GetValue()))
            i += 1

        for r in resources:
            dic_resources[r.code] = r.qnt

        self.third_ui()

    def kill(self, event):
        """
        Função responsável por verificar a existência daquele
        ID requisitado e matar o processo.
        """
        try:
            code = int(self.killText.GetValue())
            proc = None
            for p in processes:
                if p.code == code:
                    proc = p
                    proc.stop()
                    proc.event.set()
            if proc is not None:
                processes.remove(proc)
            self.killText.SetValue("")
        except ValueError:
            pass

    def create(self, event):
        """
        Função responsável por criar os processos e adicionar
        à lista de processos e incrementar o contador.
        """
        global count_process

        try:
            d_ts = int(self.trText.GetValue())
            d_tu = int(self.tuText.GetValue())

            if len(processes) < MAX_PROCESSES:
                processes.append(MyProcess(count_process, d_ts, d_tu))
                processes[-1].start()
                count_process += 1

                self.trText.SetValue("")
                self.tuText.SetValue("")

                self.refresh()
        except ValueError:
            pass

    def update_box(self, event):
        """
        Função responsável por atualizar as informações
        nas caixas de texto.
        """
        txt = "Processos\n"
        count = 0
        for p in processes:
            txt += "ID: {0} Status: {1} | " \
                   "TU: {2} TR: {3} | " \
                   "RR: {4} ".format(p.code, p.status, p.d_tu, p.d_ts, p.code_requesting)
            if p.resources:
                txt += "R.U.: {0}".format(zip(*p.resources)[0])
            else:
                txt += "R.U.: Nenhum recurso alocado."
            if count % 2 != 0:
                txt += "\n"
            else:
                txt += " <-----> "
            count += 1
        self.pDisplay.SetValue(txt)
        self.pDisplay.ShowPosition(800)

        txt = "Recursos Disponíveis\n"
        for r in dic_resources:
            txt += "ID: {0} | Qnt: {1}\n".format(r, dic_resources[r])
        self.rDisplay2.SetValue(txt)
        while list_message:
            self.logDisplay.AppendText(list_message.pop(0)+"\n")


class MyFrame(wx.Frame):
    """
    Classe do Frame principal da GUI.
    """

    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Detector de Deadlocks")
        self.fSizer = wx.BoxSizer(wx.VERTICAL)
        self.panel = MyPanel(self)
        self.fSizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(self.fSizer)
        self.Fit()
        self.Show()

        self.Bind(wx.EVT_CLOSE, self.close)

    def close(self, event):
        """
        Encerra o processo com as threads dos hóspedes e destrói o Frame.
        """
        try:
            #self.panel._p.terminate()
            for p in processes:
                p.stop()
            self.panel.manager.stop()
        except BaseException:
            pass
        self.Destroy()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
