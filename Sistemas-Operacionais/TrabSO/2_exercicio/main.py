# -*- coding: utf-8 -*-
__author__ = 'alfredo'
__version__ = '0.1'

import wx
import random
import time
from multiprocessing import Process, Queue
from threading import Thread, Semaphore

resources = []
processes = []
dic_resources = {}
max_resource = 10
semaphore = Semaphore()
qnt_resource = 0
process = []


class Resource(object):
    def __init__(self, code, name, qnt):
        self.code = code
        self.name = name
        self.qnt = int(qnt)


class MyProcess(Thread):
    def __init__(self, code, queue=None):
        """
        Construtor da thread.
        """
        super(MyProcess, self).__init__()
        self.code = code
        self._stop = False
        #Tempo para requisição de um recurso
        self.d_ts = random.randrange(1, 10)
        #Tempo de utilização de recurso
        self.d_tu = random.randrange(1, 10)
        #Lista com os recursos alocados
        self.resources = []
        #Variável para verificar se o processo está em estado de requisição
        self.requesting = False
        #Variável para verificar se o SO já verificou esse processo
        self.v_so = []
        #Código de requisição
        self.code_requesting = 0
        print("Processo {0} criado = {1} - {2}". format(self.code, self.d_tu, self.d_ts))

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

    def request(self):
        count = 0
        global dic_resources
        self.code_requesting = random.randrange(0, qnt_resource)

        soma = 0
        for r in self.resources:
            if r[0] == self.code_requesting:
                soma += 1
        if resources[self.code_requesting].qnt > soma:
            print("{0} requisitando {1}".format(self.code, self.code_requesting))
            self.requesting = True
            while not self._stop:
                semaphore.acquire()
                if dic_resources[self.code_requesting] == 0:
                    semaphore.release()
                    time.sleep(0.5)
                else:
                    dic_resources[self.code_requesting] -= 1
                    self.resources.append([self.code_requesting, self.d_tu])
                    semaphore.release()
                    break
                count += 1
            self.requesting = False
        else:
            print("Já tem todos os recursos.")

    def use(self):
        print("{0} executando.".format(self.code))
        for r in self.resources:
            r[1] -= 1
            if r[1] == 0:
                semaphore.acquire()
                dic_resources[r[0]] += 1
                print("{1} liberando recurso {0}".format(r[0], self.code))
                print("Recurso {0} agora está com {1}".format(r[0], dic_resources[r[0]]))
                semaphore.release()
        self.resources = filter(lambda x: x[1], self.resources)

    def free(self):
        for r in self.resources:
            semaphore.acquire()
            dic_resources[r[0]] += 1
            semaphore.release()

    def stop(self):
        """
        Função para fazer com que a thread seja encerrada.
        """
        self._stop = True


class Manager(Thread):
    def __init__(self, num, dt, queue):
        """
        Construtor da thread.
        """
        super(Manager, self).__init__()
        self.num = num
        #self.dt = dt
        self.dt = 10
        self._stop = False
        self.count = 0

    def run(self):
        """
        Função executada quando a thread é iniciada.
        """
        while not self._stop:
            resources_available = []
            for p in processes:
                if p.requesting is False:
                    for r in p.resources:
                        if not r[0] in resources_available:
                            resources_available.append(r[0])
            print (resources_available)
            for p in processes:
                if p.requesting is True and not p.code_requesting in resources_available:
                    for p2 in processes:
                        if p2 != p and p2.requesting is True:
                            #print zip(*p2.resources)
                            if len(p2.resources):
                                if p.code_requesting in zip(*p2.resources)[0]:
                                    if p.code in p2.v_so:
                                        #P está em deadlock
                                        print("COUNT = {0}".format(self.count))
                                        print("{0} está em deadlock.".format(p.code))
                                        p2.v_so.remove(p.code)
                                    else:
                                        p2.v_so.append(p.code)
            time.sleep(self.dt)
            self.count += 1

    def stop(self):
        """
        Função para fazer com que a thread seja encerrada.
        """
        self._stop = True


def main():
    global qnt_resource
    qnt_resource = int(raw_input("Quantidade de recursos(max 10): "))
    if qnt_resource > 10:
        raise ValueError("Valor não pode ser maior que 10.")

    for i in range(0, qnt_resource):
        name = raw_input("Nome do recurso: ")
        qnt = raw_input("Quantidade de instâncias do recurso: ")
        resources.append(Resource(i, name, qnt))
    for r in resources:
        dic_resources[r.code] = r.qnt
    print("-------------------------------------------------")
    qnt_process = int(raw_input("Quantidade de processos(max 15): "))
    for i in range(0, qnt_process):
        processes.append((MyProcess(i)))
    for i in processes:
        i.start()
    manager = Manager(1, 0.5, None)
    manager.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        for p in processes:
            p.stop()
        manager.stop()

if __name__ == "__main__":
    main()
