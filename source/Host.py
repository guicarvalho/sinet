#!/usr/bin/env python
# -*- coding:utf8 -*-


class Host(object):
    def __init__(self, address, netmask, mac):
        self.address = address
        self.netmask = netmask
        self.mac = mac

    # def ping(self, message):
        # print 'received by %s -- %s' % (self.address, message)
    def recv(self, message=None):
        if message is not None:
            print 'origem: %s' % message.origin
            print 'destino: %s' % message.destino
            print 'payload: %s' % message.payload
            print 'Meu ip: %s' % self.address