print('Programa para leer texto y procesar informacion de ella')
print('-------------------------------------------------------')
Vocales=[]
Consonantes=[]
Numeros=[]
Caracteres=[]
cvoca=0
ccons=0
cnume=0
ccara=0
lista=[]
resultados=[]
ruta=input('Introdusca la ruta de destino del texto: ')

import os.path
if os.path.exists(ruta):
    buscar=input('Introdusca texto a buscar: ')
    contar=0
    encontrado=0
    texto=open(ruta)
    linea=texto.readline()
    while linea!='':
        print (linea)
        contar=contar+1
        linea=texto.readline()
        for x in linea:
            if x in 'aeiou':
                Vocales.append(x)
                cvoca=cvoca+1
            elif x in 'qwrtypsdfghjklzxcvbnmñ':
                Consonantes.append(x)
                ccons=ccons+1
            elif x in '0123456789':
                Numeros.append(x)
                cnume=cnume+1
            else:
                Caracteres.append(x)
                ccara=ccara+1
        if linea.find(buscar)>=0:
            encontrado=encontrado+1
        else:
            encontrado=encontrado
    texto.close()
    contar=(contar-1)
    print('Se han contado',str(contar),'lineas en el texto')
    print('Vocales',Vocales)
    print('Se encontraron',cvoca,'vocales')
    print('Consonantes',Consonantes)
    print('Se encontraron',ccons,'consonantes')
    print('Numeros',Numeros)
    print('Se encontraron',cnume,'numeros')
    print('Caracteres',Caracteres)
    print('Se han encontrado',ccara,'caracteres')
    texto=open(ruta) 
    archivo=texto.readlines()
    texto.close()
    for x in archivo:
       lista += x.split()
    lista.sort()
    listado = set(lista)
    listado = list(listado)
    listado.sort()
    for numero in listado:
        resultados.append((lista.count(numero), numero))
    resultados.sort(reverse=True)
    print ('La cantidad de veces que se repite una palabra es: ',resultados)
    if encontrado>=1:
        print("Se encontro la cadena "+buscar+ ", y se repite "+ str(encontrado)+" Veces")
    else:
        print("No se encontro la cadena "+buscar)        
else:
    print("El fichero no existe o no pudo ser abierto")
