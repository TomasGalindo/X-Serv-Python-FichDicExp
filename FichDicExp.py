#! /usr/bin/python3

#Vamos a utilizar la forma utilizando la funcion split
fich = open("/etc/passwd")

lineas = fich.readlines()
diccionario = {}
for linea in lineas:
	palab_linea = linea.split(":")
	ident = palab_linea[0]
	shell = palab_linea[-1][:-1]		#el ultimo corchete es para que no coja el ultimo \n
	diccionario[ident] = shell			#guarda en el diccionario el identificador y la shell


for prueba in diccionario:				#escribe todos los componentes del diccionario
	print(prueba,diccionario[prueba])
 

try:
	user = "imaginario"		#si ponemos root no salta a la parte "except"
	print(diccionario[user])
except:
	print("No existe " + user )


