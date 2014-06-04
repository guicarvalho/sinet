#!/usr/bin/env python
#-*- coding:utf8 -*-

class CAMTable(object):
	'''Content Addressable Table'''
	def __init__(self):
		self.table = {}

	def add(self, host, port):
		'''guarda o endereço MAC e o tempo para expirar'''
		self.table[host.mac] = [port, 10]

	def get_port(self, host):
		'''Retorna o número da porta em que o host está conectado com o switch.'''
		return self.table.get(host.mac)[0]

	def show_all(self):
		'''Exibe todas as entradas na CAM'''
		for key in self.table.iterkeys():
			print 'MAC=>%s - PORT=>%d' % (key, self.table[key][0])

class Switch(object):
	def __init__(self, max_num_port, address, netmask, gateway):
		self.hosts = []
		self.max_num_port = max_num_port
		self.address = address
		self.netmask = netmask
		self.gateway = gateway
		self.camtable = CAMTable()

	def connect(self, host):
		if self.max_num_port > len(self.hosts):
			self.hosts.append(host)
			port = self.hosts.index(host)

	def desconnect(self, host):
		self.hosts.remove(host)

	def learning(self, host):
		port = self.hosts.index(host)
		self.camtable.add(host, port)

	def flooding(self, sender, message):
		print 'Flooding ...'
		for h in self.hosts:
			if h != sender:
				h.ping(message)

	def filtering(self, receiver, message):
		port = self.camtable.get_port(receiver)
		if port is not None:
			print 'Filtering ...'
			self.hosts[port].ping(message)
			return True
		return False

	def aging(self):
		pass

	def send(self, sender, receiver, message):
		try:
			find = self.filtering(receiver, message) # pergunto se já conheço
		except:
			self.flooding(sender, message)
			
		# switch aprende as portas
		self.learning(sender)
		self.learning(receiver)

class SwitchBroadcast(Switch):
	def broadcast(self):
		print 'NUM.PORT=> %d' % self.max_num_port
		print 'ADDRESS IP=> %s' % self.address
		print 'MASK=> %s' % self.netmask
		print u'Esse Python é só na sacanagem!'