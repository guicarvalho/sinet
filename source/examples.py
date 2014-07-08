#!/usr/bin/env python
# -*- coding:utf8 -*-

import os

from Sinet import Sinet
from Hub import Hub
from Switch import Switch, SwitchBroadcast
from Host import Host
from Message import Message
from Router import Router

sinet = Sinet()
client_1 = Host('192.168.2.10', '255.255.255.0', '112:211:11:11')
client_2 = Host('192.168.2.20', '255.255.255.0', '113:1133:11:11')
client_3 = Host('192.168.2.30', '255.255.255.0', '11:22:11:22:11')


def menu():
    os.system('clear')
    print '%s MENU %s' % ('-' * 30, '-' * 40)
    op = int(raw_input('''
	1 - Criar ambiente com Hub
	2 - Criar ambiente com Switch s/ broadcast
	3 - Criar ambiente com Switch c/ broadcast
	4 - Criar ambiente com Roteador
	:'''))

    escolha(op)


def escolha(opcao):
    if opcao == 1:
        criar_ambiente_hub()
    elif opcao == 2:
        criar_ambiente_sw()
    elif opcao == 3:
        criar_ambiente_sw_broadcast()
    elif opcao == 4:
        criar_ambiente_roteador()
    else:
        menu()


def criar_ambiente_hub():
    hub = Hub(10, '192.168.2.1', '255.255.255.0', '22:22:22:22')
    sinet.initialize(hub)
    sinet.connect(client_1)
    sinet.connect(client_2)
    sinet.connect(client_3)
    msg = Message(client_1.address, client_2.address, u'Enviando um pacote ICMP.')
    sinet.run(msg)

def criar_ambiente_sw():
    sw = Switch(24, '192.168.2.1', '255.255.255.0', '22:22:11:22')
    sinet.initialize(sw)
    sinet.connect(client_1)
    sinet.connect(client_2)
    sinet.connect(client_3)
    sinet.run(Message(client_1.address, client_3.address, u'Pacote ICMP'))
    sinet.run(Message(client_1.address, client_3.address, u'Pacote ICMP'))
    sinet.run(Message(client_1.address, client_2.address, u'Pacote ICMP'))
    sinet.run(Message(client_1.address, client_2.address, u'Pacote ICMP'))
    sinet.run(Message(client_2.address, client_3.address, u'Pacote ICMP'))
    sinet.run(Message(client_3.address, client_2.address, u'Pacote ICMP'))


def criar_ambiente_sw_broadcast():
    sw = SwitchBroadcast(24, '192.168.2.1', '255.255.255.0', '22:22:11:22')
    sinet.initialize(sw)
    sinet.connect(client_1)
    sinet.connect(client_2)
    sinet.connect(client_3)
    sinet.run(Message(client_1.address, client_3.address, u'Pacote ICMP'))
    sinet.run(Message(client_1.address, client_3.address, u'Pacote ICMP'))
    sinet.run(Message(client_1.address, '192.168.2.255', u'Pacote ICMP'))


def criar_ambiente_roteador():
    pass


def main():
    menu()

if __name__ == '__main__':
    main()