# Software de registro civil
import os
import csv
limpiar_pantalla="cls"
menu_inicio=1
menu1=0
menu2=0
menu3=0
menu4=0
menu5=0
menu6=0
registros=[]
registros_finales=()
os.system(limpiar_pantalla)
try:
    with open('registros.csv', mode='r', newline='') as archivo:
        leer=csv.reader(archivo)
        for i in leer:
            if i: registros_finales
except FileNotFoundError:
    print("Archivo no encontrado")
while menu_inicio==1:
    try:
        respuesta=int(input("Binevenido al registro civil. Ingrese una opcion\n1. Añadir registro\n2. Ver registros\n3. Eliminar registros\n4. Confirmar registro\n5. Ver registro final\n6. Guardar y salir\nRe: "))
        if respuesta==1:
            menu1=1
        elif respuesta==2:
            menu2=1
        elif respuesta==3:
            menu3=1
        elif respuesta==4:
            menu4=1
        elif respuesta==5:
            menu5=1
        elif respuesta==6:
            menu6=1
    except ValueError:
        print("Ingrese una opcion del 1 a 6")
        continue
    os.system(limpiar_pantalla)
    while menu1==1:
        reg=input("Ingrese el registro: ")
        registros.append(reg)
        res=int(input("¿Desea agregar otro registro?\n1. S1\n2. No\nRe: "))
        if res==1:
            menu1=1
        elif res==2:
            menu1=0
            menu_inicio=1
    os.system(limpiar_pantalla)
    while menu2==1:
        print(registros)
        res1=int(input("Presione 0 para volver al menu inicial: "))
        if res1==0:
            menu2=0
            menu_inicio=1
    os.system(limpiar_pantalla)
    while menu3==1:
        reg=input("Ingrese el registro que desea eliminar: ")
        registros.remove(reg)
        res2=int(input("¿Desea eliminar otro registro?\n1. Si\n2. No\nRe: "))
        if res2==1:
            menu3==1
        elif res2==2:
            menu3=0
            menu_inicio=1
    os.system(limpiar_pantalla)
    while menu4==1: # Al confirmar los registros la lista se transforma en tupla
        registros_finales=tuple(registros)
        print(registros_finales)
        res3=int(input("Presione 0 para volver al menu inicial: "))
        if res3==0:
            menu4=0
            menu_inicio=1
    os.system(limpiar_pantalla)
    while menu5==1:
        print(registros_finales)
        res4=int(input("Presione 0 para volver al menu inicial: "))
        if res4==0:
            menu5=0
            menu_inicio=1
    os.system(limpiar_pantalla)
    while menu6==1:
        with open('registros.csv', mode='w', newline='') as archivo:
            escribir=csv.writer(archivo)
            escribir.writerow([])
            for reg in (registros_finales):
                escribir.writerow([reg])
            print("Registros guardados en 'registros.csv'")
            menu6=0
            menu_inicio=0


