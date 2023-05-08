class Email():
	def __init__(self, ids, dominio, tipo, contra, correo):
		self.__idCuenta = ids
		self.__dominio = dominio
		self.__tipodom = tipo
		self.__contraseña = contra
		self.__correo = correo 

	def Retorna_Email(self):
		return self.__idCuenta+'@'+self.__dominio+'.'+self.__tipodom

	def Get_Dominio(self):
		return self.__dominio

	def Crear_Cuenta(self, correo):
		self.__correo = correo
		print ("\nCorreo: ", self.__correo)
		print ("Contraseña: ", self.__contraseña)
		print ("Cuenta creada!\n")

	def Mostrar_Mensaje(self,persona):
		print ("Estimado "+persona+" te enviaremos tus mensajes a la dirección ",self.__correo)

	def Modifica_Contraseña(self,actual):
		if actual == self.__contraseña:
			nueva = input("Ingrese nueva contraseña: ")
			self.__contraseña = nueva
			print("Nueva contraseña: ",self.__contraseña)
		else:
			print("Contraseña incorrecta")