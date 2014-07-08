#!/usr/bin/env python
# -*- coding:utf8 -*-


class Hub(object):
    def __init__(self, max_num_port, address, netmask, mac):
        self.hosts = []
        self.max_num_port = max_num_port
        self.address = address
        self.netmask = netmask
        self.mac = mac

    def connect(self, host):
        if self.max_num_port > len(self.hosts):
            self.hosts.append(host)

    def run(self, message):
        for host in self.hosts:
            if host.address != message.origin:
                host.recv(message)
                print '-' * 50