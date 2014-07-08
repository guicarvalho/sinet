#!/usr/bin/env python
# -*- coding:utf8 -*-

import threading

from Host import Host


class Sinet(object):
    def __init__(self):
        self.host = None

    def initialize(self, host):
        self.host = host

    def connect(self, host):
        th = threading.Thread(target=self.cria_host, args=(host, ))
        th.start()

    def cria_host(self, host):
        if self.host is not None:
            h = Host(host.address, host.netmask, host.mac)
            self.host.connect(h)

    def run(self, message):
        self.host.run(message)
