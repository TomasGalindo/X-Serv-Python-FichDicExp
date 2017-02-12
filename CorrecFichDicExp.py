#! /usr/bin/python3

# Correccion del ejercicio FichDicExp

fich = open("/etc/passwd")

lineas = fich.readlines()
diccionario = {}
for linea in lineas:
    palab_linea = linea.split(":")
    ident = palab_linea[0]
    shell = palab_linea[-1][:-1]    # [:-1] para que no coja el ultimo \n
    diccionario[ident] = shell      # guarda en el diccionario el id y la shell

# escribe por pantalla todos los componentes del diccionario
for prueba in diccionario:
    print(prueba, diccionario[prueba])

# Guardo los usuarios que quiero buscar en una lista
usuarios = ['imaginario', 'root']

# Bucle for para que recorra toda la lista
# En la excepcion ponemos KeyError para que solo pase por esa zona cuando
# ocurre dicha excepcion
for usuario in usuarios:
    try:
        print("La shell de " + usuario + " es " + diccionario[usuario])
    except KeyError:
        print("El usuario " + usuario + " no existe")
