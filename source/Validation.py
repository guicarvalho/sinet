#!/usr/bin/env python
#-*- coding:utf8 -*-

class Validation(object):
	'''
	Classe de validação, contém os métodos para validar endereços IP e decodificar
	endereço de rede e broadcast do IP fornecido.
	'''
	def decode(self, ip_address, netmask):
		'''Retorna um dicionário com o endereço de rede e o de broadcast.'''
		ip_address = ip_address.split('.')
		netmask = netmask.split('.')

		broadcast = []
		rede = []

		for i in range(len(ip_address)):
			rede.append(int(ip_address[i]) & int(netmask[i]))
			broadcast.append((~int(netmask[i])&0xff) | int(rede[i]))

		return {'rede': rede, 'broadcast': broadcast}

	def valid_ip(self, ip_address):
		'''Vaerifica se o endereço IP passado é vádido'''
		explode = ip_address.split('.')

		if len(explode) < 4:
			return False

		for octeto in explode:
			try:
				if int(octeto) > 255 or int(octeto) < 0:
					return False
			except:
				# não é importante tratar o erro nesse caso
				pass

		return True