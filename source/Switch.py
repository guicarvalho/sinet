#!/usr/bin/env python
#-*- coding:utf8 -*-

from Validation import Validation

class CAMTable(object):
	'''Content Addressable Table'''
	def __init__(self):
		self.table = {}

	def add(self, host, port):
		'''guarda o endereço MAC e o tempo para expirar'''
		self.table[host.mac] = [port, 1]

	def get_port(self, host):
		'''Retorna o número da porta em que o host está conectado com o switch.'''
		return self.table.get(host.mac)[0]

	def size(self):
		return len(self.table)

	# def decrement_time(self):
	# 	table = self.table.copy()
	# 	for key in table.iterkeys():
	# 		list_values = self.table[key]

	# 		if list_values[1] > 0:
	# 			list_values[1] -= 1
	# 			self.table[key] = list_values
	# 		else:
	# 			del self.table[key]

class Switch(object):
	def __init__(self, max_num_port, address, netmask, gateway):
		self.hosts = []
		self.max_num_port = max_num_port
		self.address = address
		self.netmask = netmask
		self.gateway = gateway

		self.create_CAM_table()

	def create_CAM_table(self):
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
		finally:
			# switch aprende as portas
			self.learning(sender)
			self.learning(receiver)

class SwitchBroadcast(Switch):

	def send(self, sender, receiver, message):
		try:
			validation = Validation()
			broadcast = validation.decode(self.address, self.netmask)['broadcast']

			# se o endereço for de broadcast da rede então a mensagem é disparada para todos
			if receiver.address == broadcast:
				self.flooding(sender, message)
			else:
				find = self.filtering(receiver, message) # pergunto se já conheço
		except Exception, e:
			print e
			self.flooding(sender, message)
		finally:
			# switch aprende as portas
			self.learning(sender)
			self.learning(receiver)