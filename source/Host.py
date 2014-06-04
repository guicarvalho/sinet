#!/usr/bin/env python
#-*- coding:utf8 -*-

class Host(object):
	def __init__(self, address, netmask, gateway, mac):
		self.address = address
		self.netmask = netmask
		self.gateway = gateway
		self.mac = mac

	def ping(self, message):
		print 'received by %s -- %s' % (self.address, message)