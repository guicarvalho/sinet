#!/usr/bin/env python
#-*- coding:utf8 -*-

class Hub(object):
	def __init__(self, max_num_port, address, netmask, gateway):
		self.hosts = []
		self.max_num_port = max_num_port
		self.address = address
		self.netmask = netmask
		self.gateway = gateway

	def connect(self, host):
		if self.max_num_port > len(self.hosts):
			self.hosts.append(host)

	def desconnect(self, host):
		self.hosts.remove(host)

	def send(self, host, message):
		for h in self.hosts:
			if h.address != host.address:
				h.ping(message)
		print '-'*50