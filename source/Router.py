#!/usr/bin/env python
#-*- coding:utf8 -*-

class RouterTable(object):
	'''Simula a tabela de roteamento, onde ficam salvas as rotas'''
	def __init__(self):
		self.table = []

	def add(self, address, siwtch, interface):
		'''Adiciona um registro de rota para a tabela de rotas.'''
		self.table.append({'address': address, 'switch': switch, 'interface': interface})

	def find(self, address):
		'''
		Procura a rota para o endereço IP informado, e devolve nulo se não existir entrada para o endereço
		ou devolve o endereço do switch e a interface para fazer a comunicação.
		'''
		for reg in self.table:
			if reg['address'] == address:
				return (reg['switch'], reg['interface'])
		return None


class Router(object):
	def __init__(self, address, netmask, gateway):
		self.hosts = []
		self.address = address
		self.netmask = netmask
		self.gateway = gateway
		self.router_table = RouterTable()

	def connect(self, host):
		self.hosts.append(host)

	def add_route(self, address, switch, interface):
		self.router_table.add(address, switch, interface)

	def find_route(self, address):
		try:
			# procura na tabela de rotas se existe rota para aquele endereço
			pos = hosts.index(host)
			return hosts[pos]
		except:
			# caso não encontre retorna null
			return None

	def send(self, sender, receiver, message):
		if find_route(receiver.address):
			receiver.ping(message)
		else:
			print 'Envia para o gateway pq eu não sei a rota'