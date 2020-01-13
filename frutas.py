import skfuzzy as fuzz
import matplotlib.pyplot as plt
import numpy as np
from skfuzzy import control as ctrl

def reglas(forma, firmeza, cobertura, comercializacion):
	regla1 = ctrl.Rule(forma['Angosta'] & firmeza['Verde'] & cobertura['Leve'], comercializacion['Exportable'])
	regla2 = ctrl.Rule(forma['Angosta'] & firmeza['Verde'] & cobertura['Parcial'], comercializacion['Comercial'])
	regla3 = ctrl.Rule(forma['Angosta'] & firmeza['Verde'] & cobertura['Completa'], comercializacion['Desecho'])
	regla4 = ctrl.Rule(forma['Angosta'] & firmeza['Madura'] & cobertura['Leve'], comercializacion['Exportable'])
	regla5 = ctrl.Rule(forma['Angosta'] & firmeza['Madura'] & cobertura['Parcial'], comercializacion['Comercial'])
	regla6 = ctrl.Rule(forma['Angosta'] & firmeza['Madura'] & cobertura['Completa'], comercializacion['Desecho'])
	regla7 = ctrl.Rule(forma['Angosta'] & firmeza['Podrida'] & cobertura['Leve'], comercializacion['Desecho'])
	regla8 = ctrl.Rule(forma['Angosta'] & firmeza['Podrida'] & cobertura['Parcial'], comercializacion['Desecho'])
	regla9 = ctrl.Rule(forma['Angosta'] & firmeza['Podrida'] & cobertura['Completa'], comercializacion['Desecho'])
	regla10 = ctrl.Rule(forma['Normal'] & firmeza['Verde'] & cobertura['Leve'], comercializacion['Exportable'])
	regla11 = ctrl.Rule(forma['Normal'] & firmeza['Verde'] & cobertura['Parcial'], comercializacion['Exportable'])
	regla12 = ctrl.Rule(forma['Normal'] & firmeza['Verde'] & cobertura['Completa'], comercializacion['Desecho'])
	regla13 = ctrl.Rule(forma['Normal'] & firmeza['Madura'] & cobertura['Leve'], comercializacion['Exportable'])
	regla14 = ctrl.Rule(forma['Normal'] & firmeza['Madura'] & cobertura['Parcial'], comercializacion['Exportable'])
	regla15 = ctrl.Rule(forma['Normal'] & firmeza['Madura'] & cobertura['Completa'], comercializacion['Desecho'])
	regla16 = ctrl.Rule(forma['Normal'] & firmeza['Podrida'] & cobertura['Leve'], comercializacion['Desecho'])
	regla17 = ctrl.Rule(forma['Normal'] & firmeza['Podrida'] & cobertura['Parcial'], comercializacion['Desecho'])
	regla18 = ctrl.Rule(forma['Normal'] & firmeza['Podrida'] & cobertura['Completa'], comercializacion['Desecho'])
	regla19 = ctrl.Rule(forma['Ancha'] & firmeza['Verde'] & cobertura['Leve'], comercializacion['Exportable'])
	regla20 = ctrl.Rule(forma['Ancha'] & firmeza['Verde'] & cobertura['Parcial'], comercializacion['Exportable'])
	regla21 = ctrl.Rule(forma['Ancha'] & firmeza['Verde'] & cobertura['Completa'], comercializacion['Desecho'])
	regla22 = ctrl.Rule(forma['Ancha'] & firmeza['Madura'] & cobertura['Leve'], comercializacion['Exportable'])
	regla23 = ctrl.Rule(forma['Ancha'] & firmeza['Madura'] & cobertura['Parcial'], comercializacion['Comercial'])
	regla24 = ctrl.Rule(forma['Ancha'] & firmeza['Madura'] & cobertura['Completa'], comercializacion['Desecho'])
	regla25 = ctrl.Rule(forma['Ancha'] & firmeza['Podrida'] & cobertura['Leve'], comercializacion['Desecho'])
	regla26 = ctrl.Rule(forma['Ancha'] & firmeza['Podrida'] & cobertura['Parcial'], comercializacion['Desecho'])
	regla27 = ctrl.Rule(forma['Ancha'] & firmeza['Podrida'] & cobertura['Completa'], comercializacion['Desecho'])
	return [regla1, regla2, regla3, regla4, regla5, regla6, regla7, regla8, regla9, regla10, regla11, regla12, regla13, regla14, regla15, regla16, regla17, regla18, regla19, regla20, regla21, regla22, regla23, regla24, regla25, regla26, regla27] 

def graficar(x, y, nombres, xlabel, ylabel, title):
	plt.figure(title)
	cont = 0
	for variableLinguistica in y:
		plt.plot(x, y[cont], label=nombres[cont])
		cont = cont + 1
	plt.legend(numpoints=1)
	plt.ylabel(ylabel)
	plt.xlabel(xlabel)
	plt.title(title)
	return

def coberturaFruto():
	cobertura = ctrl.Antecedent(np.arange(0, 100), 'Cobertura')
	cobertura['Leve'] = coberturaLeve(cobertura)
	cobertura['Parcial'] = coberturaParcial(cobertura)
	cobertura['Completa'] = coberturaCompleta(cobertura)
	graficar(cobertura.universe, [cobertura['Leve'].mf, cobertura['Parcial'].mf, cobertura['Completa'].mf], ['Leve', 'Parcial', 'Completa'], "Cobertura del fruto (%)", "Grado de pertenencia", "Cobertura")
	return cobertura

def firmezaDelFruto():
	firmeza = ctrl.Antecedent(np.arange(0, 100), 'Firmeza')
	firmeza['Verde'] = frutaVerde(firmeza)
	firmeza['Madura'] = frutaMadura(firmeza)
	firmeza['Podrida'] = frutaPodrida(firmeza)
	graficar(firmeza.universe, [firmeza['Verde'].mf, firmeza['Madura'].mf, firmeza['Podrida'].mf], ['Verde', 'Madura', 'Podrida'], "Firmeza del fruto (%)", "Grado de pertenencia", "Firmeza")
	return firmeza

def formaFruto():
	forma = ctrl.Antecedent(np.arange(0, 3), 'Forma')
	forma['Angosta'] = frutaAngosta(forma)
	forma['Normal'] = frutaNormal(forma)
	forma['Ancha'] = frutaAncha(forma)
	graficar(forma.universe, [forma['Angosta'].mf, forma['Normal'].mf, forma['Ancha'].mf], ['Angosta', 'Normal', 'Ancha'], "Forma del fruto (mm)", "Grado de pertenencia", "Forma")
	return forma

def comercializacion():
	comercializacion = ctrl.Consequent(np.arange(0, 100), 'Comercializacion')
	comercializacion['Desecho'] = fuzz.trapmf(comercializacion.universe, [0, 0, 15, 45])
	comercializacion['Comercial'] = fuzz.trimf(comercializacion.universe, [15, 45, 75])
	comercializacion['Exportable'] = fuzz.trapmf(comercializacion.universe, [45, 75, 100, 100])
	graficar(comercializacion.universe, [comercializacion['Desecho'].mf, comercializacion['Comercial'].mf, comercializacion['Exportable'].mf], ['Desecho', 'Comercial', 'Exportable'], "Calidad del fruto (%)", "Grado de pertenencia", "Calidad")
	return comercializacion

def frutaAngosta(forma):
	# Funcion de pertenencia para forma de angosta de fruta
	angosta = fuzz.trapmf(forma.universe, [0, 0, 0.5, 1])
	return angosta

def frutaNormal(forma):
	# Funcion de pertenencia para forma de normal de fruta
	normal = fuzz.trimf(forma.universe, [0.5, 1, 1.5])
	return normal

def frutaAncha(forma):
	# Funcion de pertenencia para forma ancha de fruta
	ancha = fuzz.trapmf(forma.universe, [1.5, 2, 3, 3])
	return ancha

def coberturaLeve(cobertura):
	# Funcion de pertenencia para cobertura de manchas leve
	leve = fuzz.trapmf(cobertura.universe, [0, 0, 15, 45])
	return leve

def coberturaParcial(cobertura):
	# Funcion de pertenencia para cobertura de manchas parcial
	parcial = fuzz.trimf(cobertura.universe, [15, 45, 75])
	return parcial

def coberturaCompleta(cobertura):
	# Funcion de pertenencia para cobertura de manchas completa
	completa = fuzz.trapmf(cobertura.universe, [45, 75, 100, 100])
	return completa

def frutaVerde(firmeza):
	# Funcion de pertenencia para fruta verde
	verde = fuzz.trapmf(firmeza.universe, [0, 0, 15, 45])
	return verde

def frutaMadura(firmeza):
	# Funcion de pertenencia para fruta madura
	madura = fuzz.trimf(firmeza.universe, [15, 45, 75])
	return madura

def frutaPodrida(firmeza):
	# Funcion de pertenencia para fruta podrida
	podrida = fuzz.trapmf(firmeza.universe, [45, 75, 100, 100])
	return podrida

def entradaUsuario():

	while True:
		altura = input('Ingrese la altura de la Cereza [18, 32] mm: ')
		if 18 <= int(altura) <= 32:
			break
		else:
			print("Ingrese un valor entre 18  y 32")

	while True:
		diametro = input('Ingrese el diametro del fruto [18, 32] mm: ')
		if 18 <= int(diametro) <= 32:
			break
		else:
			print("Ingrese un valor entre 18  y 32")

	while True:
		transparencia = input('Ingrese la transparencia del fruto [0, 100] %: ')
		if 0 <= int(transparencia) <= 100:
			break
		else:
			print("Ingrese un valor entre 0  y 100")

	while True:
		cobertura = input('Ingrese la cobertura de las manchas del fruto [0, 100] %: ')
		if 0 <= int(cobertura) <= 100:
			break
		else:
			print("Ingrese un valor entre 0  y 100")


	return altura, diametro, transparencia, cobertura

def salidaEmbalaje(diametro, comercio):
	if(comercio == "Desecho"):
		return 16
	if(diametro == 18):
		return 1
	elif(diametro == 19):
		return 2
	elif(diametro == 20):
		return 3
	elif(diametro == 21):
		return 4
	elif(diametro == 22):
		return 5
	elif(diametro == 23):
		return 6
	elif(diametro == 24):
		return 7
	elif(diametro == 25):
		return 8
	elif(diametro == 26):
		return 9
	elif(diametro == 27):
		return 10
	elif(diametro == 28):
		return 11
	elif(diametro == 29):
		return 12
	elif(diametro == 30):
		return 13
	elif(diametro == 31):
		return 14
	elif(diametro == 32):
		return 15

def escribirArchivoSalida(resultadoComercio, altura, diametro, transparencia, cobertura):
	
	nombreArchivo = "Cereza_"+str(altura)+"_"+str(diametro)+"_"+str(transparencia)+"_"+str(cobertura)+".txt"
	archivo = open(nombreArchivo, "w")
	archivo.write("Niveles capturados: \n")
	archivo.write("	Calibre: "+str(diametro)+" mm \n")
	resultadoForma = float(diametro) / altura
	forma = ""
	if(resultadoForma < 0.50 ):
		forma = "Angosta"
	elif(0.50 <= resultadoForma < 1.50):
		forma = "Normal"
	else:
		forma = "Ancha"
	archivo.write("	Forma: "+forma+"\n")
	firmeza = ""
	if(transparencia < 30):
		firmeza = "Verde"
	elif(30 <= transparencia < 60):
		firmeza = "Madura"
	else:
		firmeza = "Podrida"
	archivo.write("	Firmeza de la pulpa: "+firmeza+"\n")
	resultadoCobertura = ""
	if(cobertura < 30):
		resultadoCobertura = "Leve"
	elif(30 <= cobertura < 60):
		resultadoCobertura = "Parcial"
	else:
		resultadoCobertura = "Completa"
	archivo.write("	Cobertura de manchas: "+resultadoCobertura+"\n")
	comercio = ""
	if(resultadoComercio < 30):
		comercio = "Desecho"
	elif(30 <= resultadoComercio < 60):
		comercio = "Comercial"
	else:
		comercio = "Exportable"
	archivo.write("Comercializacion: "+comercio+"\n")
	salida = salidaEmbalaje(diametro, comercio)
	archivo.write("Numero salida: "+str(salida))

def main():
	altura, diametro, transparencia, cobertura = entradaUsuario()
	firmezaAntecedente = firmezaDelFruto()
	coberturaAntecedente = coberturaFruto()
	formaAntedecedente = formaFruto()
	comercioConsecuente = comercializacion()
	resultadoReglas = reglas(formaAntedecedente, firmezaAntecedente, coberturaAntecedente, comercioConsecuente)
	controlador = ctrl.ControlSystem(resultadoReglas)
	resultadoSimulacion = ctrl.ControlSystemSimulation(controlador)
	resultadoSimulacion.input['Firmeza'] = transparencia
	resultadoSimulacion.input['Cobertura'] = cobertura
	resultadoSimulacion.input['Forma'] = float(diametro) / altura
	resultadoSimulacion.compute()
	resuladoComercio = int(resultadoSimulacion.output['Comercializacion'])
	escribirArchivoSalida(resuladoComercio, altura, diametro, transparencia, cobertura)

	# Resultados Antecedentes
	firmezaAntecedente.view(sim=resultadoSimulacion)
	coberturaAntecedente.view(sim=resultadoSimulacion)
	formaAntedecedente.view(sim=resultadoSimulacion)

	# Resultado Consecuente
	comercioConsecuente.view(sim=resultadoSimulacion)

	plt.show()

main()