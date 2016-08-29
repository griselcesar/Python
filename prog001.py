#!/usr/bin/python
#-*- coding:utf-8 -*-

# Definimos las funciones del menú
def sumar(x,y):
	resultado = x + y
	return resultado

def resta(x,y):
	resultado = x - y
	return resultado

def multiplicacion(x,y):
	resultado = x * y
	return resultado

# Creamos la función menú
def menu():
	opcion = 0
	while (opcion!=1):
		print "1- Salir\n2- Sumar\n3- Resta\n4- Multiplicar"
		opcion = int(raw_input("Ingrese una opción: "))
		if (opcion == 2):
			res = sumar(a,b)
			print "Resultado: %d+%d=%d" %(a, b, res)
			print "========================="
		if (opcion == 3):
			res = resta(a,b)
			print "Resultado: %d-%d=%d" %(a, b, res)
			print "========================="
		if (opcion == 4):
			res = multiplicacion(a,b)
			print "Resultado: %d*%d=%d" %(a, b, res)
			print "========================="

# Realizamos la petición de los datos al Usuario
print "Primer Programa en Python"

a = int(raw_input("Valor de A: "))
b = int(raw_input("Valor de B: "))

# Desplegamos el Menú de Opciones
menu()

# Despedida del Programa
print "================================"
print "= Gracias por usar el programa ="
print "================================"