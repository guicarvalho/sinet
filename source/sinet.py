#!/usr/bin/env python
#-*- coding:utf8 -*-

import os

from Hub import Hub
from Switch import Switch, SwitchBroadcast
from Host import Host
from Router import Router

def menu():
	os.system('clear')
	print '%s MENU %s' % ('-'*30, '-'*40)
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
	h1 = Host('192.168.0.10', '255.255.255.0', '192.168.0.1', '1-1-1-1-1-1-1-1')
	h2 = Host('192.168.0.11', '255.255.255.0', '192.168.0.1', '2-2-2-2-2-2-2-2')
	h3 = Host('192.168.0.12', '255.255.255.0', '192.168.0.1', '3-3-3-3-3-3-3-3')

	hub =  Hub(12, '192.168.0.1', '255.255.255.0', '192.168.0.1')

	hub.connect(h1)
	hub.connect(h2)
	hub.connect(h3)
	
	hub.send(h1, u'Alguns bits que estou mandando aqui de boas.')

def criar_ambiente_sw():	
	h1 = Host('192.168.0.10', '255.255.255.0', '192.168.0.1', '1-1-1-1-1-1-1-1')
	h2 = Host('192.168.0.11', '255.255.255.0', '192.168.0.1', '2-2-2-2-2-2-2-2')
	h3 = Host('192.168.0.12', '255.255.255.0', '192.168.0.1', '3-3-3-3-3-3-3-3')

	switch = Switch(24, '192.168.0.5', '255.255.255.0', '192.168.0.1')
	
	switch.connect(h1)
	switch.connect(h2)
	switch.connect(h3)

	switch.send(h1, h3, u'Alguns bits que estou mandando aqui de boas.')
	switch.send(h1, h3, u'Alguns bits que estou mandando aqui de boas.')
	switch.send(h1, h2, u'Alguns bits que estou mandando aqui de boas.')
	switch.send(h1, h2, u'Alguns bits que estou mandando aqui de boas.')
	switch.send(h2, h3, u'Alguns bits que estou mandando aqui de boas.')
	switch.send(h3, h2, u'Alguns bits que estou mandando aqui de boas.')

def criar_ambiente_sw_broadcast():
	h1 = Host('192.168.0.10', '255.255.255.0', '192.168.0.1', '1-1-1-1-1-1-1-1')
	h2 = Host('192.168.0.11', '255.255.255.0', '192.168.0.1', '2-2-2-2-2-2-2-2')
	h3 = Host('192.168.0.12', '255.255.255.0', '192.168.0.1', '3-3-3-3-3-3-3-3')
	broadcast = Host('192.168.0.255', '255.255.255.0', '192.168.0.1', 'b-b-b-b-b-b-b-b')

	switch = SwitchBroadcast(24, '192.168.0.5', '255.255.255.0', '192.168.0.1')
	
	switch.connect(h1)
	switch.connect(h2)
	switch.connect(h3)
	switch.connect(broadcast)

	switch.send(h1, broadcast, u'Alguns bits que estou mandando aqui de boas.')

def criar_ambiente_roteador():
	pass

def main():
	menu()

	# router = Router('192.168.0.1', '255.255.255.0', '192.168.0.1')
	# router2 = Router('192.168.1.1', '255.255.255.0', '192.168.1.10')
	# router.connect(h1)
	# router2.connect(h2)
	# router.connect(router2)
	# router.add_route('192.168.0.11', '192.168.1.1', '3')
	# router.send(h1, h2, 'Estamos entre camaradas')

	# router.print_routes()

if __name__ == '__main__':
	main()		