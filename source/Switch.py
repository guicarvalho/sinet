#!/usr/bin/env python
# -*- coding:utf8 -*-

from Validation import Validation


class CAMTable(object):
    """Content Addressable Table"""

    def __init__(self):
        self.table = {}

    def add(self, host, port):
        """guarda o endereço MAC e o tempo para expirar"""

        self.table[host.mac] = [port, 1]

    def get_port(self, host):
        """Retorna o número da porta em que o host está conectado com o switch."""
        return self.table.get(host.mac)[0]

    def size(self):
        return len(self.table)

class Switch(object):
    def __init__(self, max_num_port, address, netmask, mac):
        self.hosts = []
        self.max_num_port = max_num_port
        self.address = address
        self.netmask = netmask
        self.mac = mac
        self.cam_table = CAMTable()

    def connect(self, host):
        if self.max_num_port > len(self.hosts):
            self.hosts.append(host)

    def learning(self, host):
        for h in self.hosts:
            if h.address == host:
                self.cam_table.add(h, self.hosts.index(h))
                break

    def flooding(self, message):
        print 'Flooding ...'
        for h in self.hosts:
            if h.address != message.origin:
                h.recv(message)
                print '-' * 50

    def filtering(self, message):
        port = None

        for h in self.hosts:
            if h.address == message.destino:
                port = self.cam_table.get_port(h)

        if port is not None:
            print 'Filtering ...'
            self.hosts[port].recv(message)
            return True
        return False

    def aging(self):
        pass

    def run(self, message):
        try:
            self.filtering(message)  # pergunto se já conheço
        except:
            self.flooding(message)
        finally:
            # switch aprende as portas
            self.learning(message.origin)
            self.learning(message.destino)


class SwitchBroadcast(Switch):
    def run(self, message):
        try:
            validation = Validation()
            broadcast = validation.decode(self.address, self.netmask)['broadcast']

            # se o endereço for de broadcast da rede então a mensagem é disparada para todos
            if message.destino.address == broadcast:
                self.flooding(message)
            else:
                self.filtering(message)  # pergunto se já conheço
        except:
            self.flooding(message)
        finally:
            # switch aprende as portas
            self.learning(message.origin)
            self.learning(message.destino)