#!/usr/bin/env python
# -*- coding:utf8 -*-

class RouterTable(object):
    '''Simula a tabela de roteamento, onde ficam salvas as rotas'''

    def __init__(self):
        self.table = []

    def add(self, address, switch, interface):
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

    def show_all(self):
        '''Exibe todas as rotas registradas na tabela'''
        for line in self.table:
            print line


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
        for i in self.router_table.table:
            if address == i['address']:
                return True
        return False

    def print_routes(self):
        self.router_table.show_all()

    def send(self, sender, receiver, message):
        if self.find_route(receiver.address):
            receiver.ping(message)
        else:
            print u'Não conheço a rota ... encaminhando para o gateway.'