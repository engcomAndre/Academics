# -*- coding: utf-8 -*-

from threading import Thread, Semaphore
from datetime import datetime, timedelta
import random

num_channels = 10
num_hospedes = 10

list_mutex = []
semaphore_tv = Semaphore()
list_channel = []
list_hospede = []

class Hospede(Thread):
	def __init__(self, num):
		super(Hospede, self).__init__()
		self._num = num
		self._channel = random.randrange(1, num_channels)
		self._time = random.randrange(1, 10)
		self._stop = False
		self._resting = False
		self._counter = self._time*10000
		print "Criado hospede: {0} CH: {1} TIME: {2}".format(self._num, self._channel, self._time)

	def run(self):
		global list_mutex
		global list_channel
		global semaphore_tv

		index = self._channel-1
		while not self._stop:
			if not self._resting:
				list_mutex[index].acquire()
				if list_channel[index] == 0:
					semaphore_tv.acquire()
					list_channel[index] += 1
					list_mutex[index].release()
				else:
					list_channel[index] += 1
					list_mutex[index].release()
				self.watch()
				list_mutex[index].acquire()
				list_channel[index] -= 1
				if list_channel[index] == 0:
					semaphore_tv.release()
				list_mutex[index].release()
				self.resting()
			else:
				#print "Vindo pro descanso: {0}".format(self._num)
				self.resting()

	def watch(self):
		start = datetime.now()
		now = datetime.now()
		print "Rolando channel: {0}".format(self._num)
		while (now-start).seconds < self._time:
			now = datetime.now()

	def resting(self):
		self._resting = True
		if self._counter > 0:
			self._counter -= 1
			#print "Thread {0} descansando.".format(self._num)
		else:
			self._counter = self._time*100000
			self._resting = False

	def stop(self):
		print "Parando hospede: {0}".format(self._num)
		self._stop = True

def main():
	for i in range(0, num_channels):
		list_mutex.append(Semaphore(1))
		list_channel.append(0)
	for i in range(0, num_hospedes):
		list_hospede.append(Hospede(i))
		list_hospede[i].start()

	try:
		while True:
			pass
	except:
		for thread in list_hospede:
			thread.stop()

if __name__ == '__main__':
	main()