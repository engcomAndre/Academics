# -*- coding: utf-8 -*-

import wx

from multiprocessing import Process, Queue
from threading import Thread, Semaphore
from datetime import datetime, timedelta
import random


num_channels = None #Quantidade de canais.
num_hospedes = None #Quantidade de hóspedes(threads) da aplicação.
time_tv_ini = None #Tempo mínimo de TV que pode ser sorteado para o hóspede.
time_tv_finish = None #Tempo máximo de TV que pode ser sorteado para o hóspede.
time_rest_ini = None #Tempo mínimo de Descanso que pode ser sorteado para o hóspede.
time_rest_finish = None #Tempo máximo de Descanso que pode ser sorteado para o hóspede.
current_channel = None #Canal atual.

list_mutex = [] #Lista de semáforo para cada canal.
semaphore_tv = Semaphore() #Semáforo que controla o Controle da TV.
list_channel = [] #Lista da quantidade de hóspedes em cada canal.
list_hospede = [] #Lista de objetos Hóspede.


class Hospede(Thread):
    def __init__(self, num, queue):
        """
        Construtor da thread.
        """
        super(Hospede, self).__init__()
        self._num = num
        self._channel = random.randrange(1, num_channels+1) #Seleciona o canal preferido do hóspede.
        self._time = random.randrange(time_tv_ini, time_tv_finish) #Seleciona o tempo que o hóspede vai ficar assistindo tv.
        self._time_rest = random.randrange(time_rest_ini, time_rest_finish) #Seleciona o tempo que o hóspede vai ficar descansando.
        self._stop = False
        self._queue = queue #Referência ao objeto fila para comunicação com a GUI.

        self._queue.put(["write_guest", "Num: {0} CH: {1};{2}"\
                        .format(self._num, self._channel, self._num)])
        self._queue.put(["change_tv", "{0};{1}".format(self._time, self._num)])
        self._queue.put(["change_rest", "{0};{1}".format(self._time_rest, self._num)])
        self.update_status()
        

        self._queue.put(["update_log", "Criado hospede: {0} CH: {1} TIME: {2}".format(self._num, self._channel, self._time)])

    def run(self):
        """
        Função executada quando a thread é iniciada.
        """
        global list_mutex
        global list_channel
        global semaphore_tv

        index = self._channel-1 #Index da lista reduzindo 1, porque os canais começam em 1 e o index em 0.
        while not self._stop:
            self._queue.put(["running", "-;{0}".format(self._num)])
            self.update_status("b")
            list_mutex[index].acquire()
            self.update_status()
            if list_channel[index] == 0:
                self.update_status("b")
                semaphore_tv.acquire()
                self._queue.put(["update_log", "Hospede {0} pegou o controle.".format(self._num)])
                self.update_status()
                list_channel[index] += 1
                list_mutex[index].release()
            else:
                list_channel[index] += 1
                list_mutex[index].release()
            self.watch()
            self.update_status("b")
            list_mutex[index].acquire()
            self.update_status()
            list_channel[index] -= 1
            if list_channel[index] == 0:
                semaphore_tv.release()
            list_mutex[index].release()
            self.resting()

    def watch(self):
        """
        Função que executa a ação de assistir tv.
        """
        global current_channel
        
        start = datetime.now()
        now = datetime.now()
        print "Hospede {0} assistindo tv.".format(self._num)
        
        count = 0
        count_time = 0
        if current_channel != self._channel:
            current_channel = self._channel
            self._queue.put(["update_log", "Canal atual: {0}".format(current_channel)])
            self._queue.put(["change_ch", "{0}".format(current_channel)])
        current_sec = (now-start).seconds
        while current_sec <= self._time:
            #Os if's são responsáveis pela animação
            if count == 0:
                self._queue.put(["running", "-;{0}".format(self._num)])
            elif count == 10000:
                self._queue.put(["running", "--;{0}".format(self._num)])
            elif count == 20000:
                self._queue.put(["running", "-->;{0}".format(self._num)])
            elif count == 30000:
                count = 0

            if count_time == 100000:
                self._queue.put(["change_tv", "{0};{1}".format(self._time-current_sec, self._num)])
                count_time = 0
            count_time += 1

            now = datetime.now()
            current_sec = (now-start).seconds
            count += 1
        print "Hospede {0} terminou de assistir tv.".format(self._num)
        self._queue.put(["change_tv", "{0};{1}".format(self._time, self._num)])

    def resting(self):
        """
        Função que executa a ação de ficar descansando.
        """

        start = datetime.now()
        now = datetime.now()
        self.update_status("r")
        count = 0
        count_time = 0

        current_sec = (now-start).seconds
        while current_sec <= self._time_rest:
            #Os if's são responsáveis pela animação
            if count == 0:
                self._queue.put(["running", "-;{0}".format(self._num)])
            elif count == 10000:
                self._queue.put(["running", "--;{0}".format(self._num)])
            elif count == 20000:
                self._queue.put(["running", "-->;{0}".format(self._num)])
            elif count == 30000:
                count = 0


            now = datetime.now()
            if count_time == 100000:
                self._queue.put(["change_rest", "{0};{1}".format(self._time_rest-current_sec, self._num)])
                count_time = 0
            count_time += 1
            current_sec = (now-start).seconds
            count += 1
        self._queue.put(["change_rest", "{0};{1}".format(self._time_rest, self._num)])

    def stop(self):
        """
        Função para fazer com que a thread seja encerrada.
        """
        self._stop = True

    def update_status(self, mode="w"):
        """
        Função responsável por enviar mensagem para a GUI para atualizar o status da thread.
        """

        if mode == "r":
            self._queue.put(["update_status", "Status: Descansando;{0}".format(self._num)])
        elif mode == "b":
            self._queue.put(["update_status", "Status: Bloqueado;{0}".format(self._num)])
        elif mode == "w":
            self._queue.put(["update_status", "Status: Assistindo TV;{0}".format(self._num)])


def start_thread():
    """
    Função que é inicializada em outro processo e é responsável pela execução das threads.
    """
    for i in range(0, num_hospedes):
        list_hospede[i].start()

    while True:
        pass


class MyPanel(wx.Panel):
    """
    Classe Panel, responsável por grande parte da GUI. Aonde todos os desenhos acontecem.
    """
    def __init__(self, parent):
        """
        Construtor do Panel. Inicia a primeira tela da aplicação e algumas variáveis.
        """
        self._queue = Queue() #Objeto Queue responsável pela comunicação com as threads.

        wx.Panel.__init__(self, parent)

        ###Desenha a primeira tela
        self.frame = parent #Armazena referência ao frame(pai) do Panel.
 
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        controlSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.widgetSizer = wx.BoxSizer(wx.VERTICAL)
 
        text = wx.StaticText(self, label="Quantidade de Hospedes")
        self.widgetSizer.Add(text, flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        self.tc1 = wx.TextCtrl(self)
        self.widgetSizer.Add(self.tc1, flag=wx.LEFT, border=5)

        text = wx.StaticText(self, label="Quantidade de Canais")
        self.widgetSizer.Add(text, flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        self.tc2 = wx.TextCtrl(self)
        self.widgetSizer.Add(self.tc2, flag=wx.LEFT, border=5)

        text = wx.StaticText(self, label="Tempo de TV (Inicio)")
        self.widgetSizer.Add(text, flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        self.tc3 = wx.TextCtrl(self)
        self.widgetSizer.Add(self.tc3, flag=wx.LEFT, border=5)

        text = wx.StaticText(self, label="Tempo de TV (Fim)")
        self.widgetSizer.Add(text, flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        self.tc4 = wx.TextCtrl(self)
        self.widgetSizer.Add(self.tc4, flag=wx.LEFT, border=5)

        text = wx.StaticText(self, label="Tempo de descanso (Inicio)")
        self.widgetSizer.Add(text, flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        self.tc5 = wx.TextCtrl(self)
        self.widgetSizer.Add(self.tc5, flag=wx.LEFT, border=5)

        text = wx.StaticText(self, label="Tempo de descanso (Fim)")
        self.widgetSizer.Add(text, flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        self.tc6 = wx.TextCtrl(self)
        self.widgetSizer.Add(self.tc6, flag=wx.LEFT, border=5)

        self.addButton = wx.Button(self, label="OK")
        self.addButton.Bind(wx.EVT_BUTTON, self.buttonOk)
        controlSizer.Add(self.addButton, 0, wx.CENTER|wx.ALL, 5)        
 
        self.mainSizer.Add(self.widgetSizer, 0, wx.CENTER|wx.ALL, 10)
        self.mainSizer.Add(controlSizer, 0, wx.CENTER)
 
        self.SetSizer(self.mainSizer)
        ###

    def createUI(self):
        """
        Função responsável pelo desenho da segunda interface.
        """
        #Criando interface
        self.frame.SetSizeWH(800, 600)
        
        for child in self.GetChildren(): 
            child.Destroy() 

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.widgetSizer = wx.BoxSizer(wx.VERTICAL)

        channel_box = wx.BoxSizer(wx.HORIZONTAL)
        self.widgetSizer.Add(channel_box, 0, wx.LEFT)
        self.channel_text = wx.StaticText(self, label="Canal Atual: --")
        channel_box.Add(self.channel_text, 0, wx.LEFT)

        self.list_box = [] #Lista que armazena uma tupla os objetos para mostrar as informações e status dos hóspedes.
        
        for i in range(0, num_hospedes):
            self.list_box.append((wx.BoxSizer(wx.HORIZONTAL), 
                            wx.StaticText(self, label=""),
                            wx.StaticText(self, label=""),
                            wx.StaticText(self, label=""),
                            wx.StaticText(self, label=""),
                            wx.StaticText(self, label="")
                            ))
            self.list_box[i][0].Add(self.list_box[i][1], flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
            self.list_box[i][0].Add(self.list_box[i][2], flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
            self.list_box[i][0].Add(self.list_box[i][3], flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
            self.list_box[i][0].Add(self.list_box[i][4], flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
            self.list_box[i][0].Add(self.list_box[i][5], flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
            self.widgetSizer.Add(self.list_box[i][0], 0, wx.LEFT)

        self.logDisplay = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.TE_READONLY)

        self.mainSizer.Add(self.widgetSizer, 0, wx.LEFT|wx.ALL, 10)
        self.mainSizer.Add(self.logDisplay, 1, wx.EXPAND|wx.ALL, 10)
        self.SetSizer(self.mainSizer)

        self.refresh()

    def initGuests(self):
        for i in range(0, num_channels):
            #Cria os objetos semáforos de cada canal
            #e inicializa com 0 cada posição da lista contador de canais.
            list_mutex.append(Semaphore())
            list_channel.append(0)
        for i in range(0, num_hospedes):
            #Cria as threads Hóspedes.
            list_hospede.append(Hospede(i, self._queue))

        self.createUI()

        self._p = Process(target=start_thread)
        self._p.start()

        #Timer responsável por ficar chamando a função para verificar se há alguma mensagem na Queue.
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.verify_queue, self.timer)
        self.timer.Start(50)

    def verify_queue(self, t):
        """
        Função responsável por capturar as mensagens transferidas pela Queue.
        """
        q = self._queue.get()
        if q[0] == "write_guest":
            self.write_guest(q[1])
        elif q[0] == "update_status":
            self.update_thread_status(q[1])
        elif q[0] == "update_log":
            self.update_log(q[1])
        elif q[0] == "running":
            self.running_threads(q[1])
        elif q[0] == "change_ch":
            self.change_channel(q[1])
        elif q[0] == "change_tv":
            self.change_tvtime(q[1])
        elif q[0] == "change_rest":
            self.change_resttime(q[1])

        self.refresh()

    def change_channel(self, msg):
        """
        Função para alterar a visualização do Canal Atual.
        """

        self.channel_text.SetLabel("Canal Atual: {0}".format(msg))

    def change_tvtime(self, msg):
        """
        Função que atualiza o tempo de tv restante.
        """
        msg, num = msg.split(";")

        self.list_box[int(num)][2].SetLabel("TV TIME: " + msg)

    def change_resttime(self, msg):
        """
        Função que atualiza o tempo de descanso restante.
        """
        msg, num = msg.split(";")

        self.list_box[int(num)][3].SetLabel("REST TIME: " + msg)

    def update_thread_status(self, msg):
        """
        Função que atualiza a mensagem de status da thread.
        """
        msg, num = msg.split(";")

        self.list_box[int(num)][4].SetLabel(msg)

    def update_log(self, msg):
        """
        Função que adiciona mensagem a caixa de texto de log.
        """
        msg = msg
        self.logDisplay.AppendText( msg + "\n" )

    def write_guest(self, msg):
        """
        Função que escreve as informações iniciais do hóspede.
        """

        msg, num = msg.split(";")

        self.list_box[int(num)][1].SetLabel(msg)
        self.Fit()
        self.frame.Layout()

    def running_threads(self, msg):
        """
        Função que imprime a 'animação' da thread.
        """

        msg, num = msg.split(";")

        self.list_box[int(num)][5].SetLabel(msg)

    def refresh(self):
        """
        Função que atualiza a tela, fazendo com que todos os elementos
        fiquem no seu lugar corretamente.
        """

        self.mainSizer.Layout()
        self.frame.fSizer.Layout()
        self.Fit()
        self.frame.Layout()
 
    def buttonOk(self, event):
        """
        Função que está associada ao botão 'OK' da primeira tela.
        É responsável por coletar o valor das caixas de texto e gravar nas variáveis.
        E chama a função que irá inicializar os hóspedes e a segunda tela.
        """

        global num_channels
        global num_hospedes
        global time_tv_ini
        global time_tv_finish
        global time_rest_ini
        global time_rest_finish

        num_channels = int(self.tc2.GetValue())
        num_hospedes = int(self.tc1.GetValue())
        time_tv_ini = int(self.tc3.GetValue())
        time_tv_finish = int(self.tc4.GetValue())
        time_rest_ini = int(self.tc5.GetValue())
        time_rest_finish = int(self.tc6.GetValue())

        self.initGuests()


class MyFrame(wx.Frame):
    """
    Classe do Frame principal da GUI.
    """
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Hospedes")
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
            self.panel._p.terminate()
        except BaseException:
            pass
        self.Destroy()
 
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()