#!/usr/bin/env python
#*-* coding:utf-8 *-*

x = int(raw_input('Ingrese un número:'))
i = 1

while i < 11:
	print "%d x %d = %d" %(x,i,x * i)
	i=i+1