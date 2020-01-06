import skfuzzy as fuzz
import matplotlib.pyplot as plt
import numpy as np

def entradaUsuario():
	altura = input('Ingrese la altura de la Cereza (mm): ')
	diametro = input('Ingrese el diametro del fruto (mm): ')
	transparencia = input('Ingrese la transparencia del fruto (%): ')
	cobertura = input('Ingrese la cobertura de las manchas del fruto (%): ')
	return altura, diametro, transparencia, cobertura


def main():
	print('Hola Mundo')
	altura, diametro, transparencia, cobertura = entradaUsuario()

main()