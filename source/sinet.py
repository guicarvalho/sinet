#!/usr/bin/env python
#-*- coding:utf8 -*-

# from Hub import Hub
from Switch import Switch, SwitchBroadcast
from Host import Host

def main():
	# hub = Hub(12, '192.168.0.1', '255.255.255.0', '192.168.0.1')
	# h1 = Host('192.168.0.10', '255.255.255.0', '192.168.0.1')
	# h2 = Host('192.168.0.11', '255.255.255.0', '192.168.0.1')
	# h3 = Host('192.168.0.12', '255.255.255.0', '192.168.0.1')
	# h4 = Host('192.168.0.13', '255.255.255.0', '192.168.0.1')
	# h5 = Host('192.168.0.14', '255.255.255.0', '192.168.0.1')

	# hub.connect(h1)
	# hub.connect(h2)
	# hub.connect(h3)
	# hub.connect(h4)
	# hub.connect(h5)

	# hub.send(h1, u'teste')
	# hub.send(h2)
	# hub.send(h3)
	# hub.send(h4, u'teste'
	# hub.send(h5)

	# switch = Switch(24, '192.168.0.5', '255.255.255.0', '192.168.0.1')
	# s2 = SwitchBroadcast(24, '192.168.0.10', '255.255.255.0', '192.168.0.1')
	# h1 = Host('192.168.0.10', '255.255.255.0', '192.168.0.1', '1-1-1-1-1-1-1-1')
	# h2 = Host('192.168.0.11', '255.255.255.0', '192.168.0.1', '2-2-2-2-2-2-2-2')
	# h3 = Host('192.168.0.12', '255.255.255.0', '192.168.0.1', '3-3-3-3-3-3-3-3')

	# switch.connect(h1)
	# switch.connect(h2)
	# switch.connect(h3)

	# switch.send(h1, h3, 'Fala brow')
	# switch.send(h1, h3, 'Fala brow')
	# switch.send(h1, h2, 'Fala brow2')
	# switch.send(h1, h2, 'Fala brow2')
	# switch.send(h2, h3, 'Fala brow3')
	# switch.send(h3, h2, 'Fala brow4')
	# # switch.camtable.show_all()

	# s2.connect(h1)
	# s2.connect(h2)
	# s2.connect(h3)
	# s2.send(h1, h2, 'Fala brow1')

	router = Router('192.168.0.1', '255.255.255.0', '192.168.0.1')

if __name__ == '__main__':
	main()		