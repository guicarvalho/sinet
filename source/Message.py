#!/usr/bin/env python
# -*- coding:utf8 -*-


class Message(object):
    def __init__(self, origin, destino, payload):
        self.origin = origin
        self.destino = destino
        self.payload = payload