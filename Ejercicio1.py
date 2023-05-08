from ClaseEmail import *
import csv

def Crear_Objeto_Por_Direccion(email):
	print("Correo: "+email)
	x = email.split("@")
	y = x[1].split(".")
	ids = x[0]
	dominio = y[0]
	tipo = y[1]
	contra = input("Ingrese contraseña: ")
	correo = email
	unMail = Email(ids,dominio,tipo,contra,correo)

	return unMail

def Mensaje():
	nombre = input("Ingrese tu nombre: ")
	unMail = Crear_Objeto_Por_Direccion()
	unMail.Mostrar_Mensaje(nombre)

	return unMail

def Modificar_Contra(Instancia):
 	actual = input("Ingrese contraseña actual: ")
	Instancia.Modifica_Contraseña(actual)

def Verifica_Validez(lista):
	lista_instancias = []
	for correo in lista:
		if correo.count('@') > 0:
			unMail = Crear_Objeto_Por_Direccion(correo)
			unMail.Crear_Cuenta(correo)
			lista_instancias.append(unMail)
		else: 
			print("La direccion "+correo+" es incorrecta!!\n")

	return lista_instancias

def Indicar_Dominios(lista_instancias):
	dominio = input("Ingresar dominio: ")
	y = 0
	cont = 0
	while y<len(lista_instancias):
		if dominio == lista_instancias[y].Get_Dominio():
			cont+=1
		y+=1

	print("Cantidad de emails con ese dominio: ",cont)


if __name__ == '__main__':

	#Item 1
	# unMail = Mensaje()	
	#Item 2							
	# Modificar_Contra(unMail)	
	#Item 3 						
	# unMail = Crear_Objeto_Por_Direccion(email)		
	
	#Item 4													
	'''archivo = open('DatosEmail.csv')
	reader = csv.reader(archivo,delimiter=',')
	lista = []

	for fila in reader:
		lista.extend(fila)

	lista_instancias = Verifica_Validez(lista)
	Indicar_Dominios(lista_instancias) '''