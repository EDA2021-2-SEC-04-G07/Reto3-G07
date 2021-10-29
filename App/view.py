"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from datetime import date, time, datetime
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Contar los avistamientos en una ciudad")
    print("3- Contar los avistamientos por duración")
    print("4- Contar los avistamientos por Hora/Minutos del día")
    print("5- Contar los avistamientos en un rango de fechas")
    print("6- Contar los avistamientos de una zona geográfica")
    print("7- Visualiizar los avistamientos de una zona geográfica")
    
catalogo = None


def cargarDatos(catalogo, datos):
    controller.cargarDatos(catalogo, datos)
    

archivo_datos = 'UFOS-utf8-small.csv'

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        
        catalogo = controller.initCatalogo()
        cargarDatos(catalogo, archivo_datos)
        print('2')
        

    elif int(inputs[0]) == 2:
        
        #Lab 8
        print('Altura del árbol: ', controller.alturaArbol(catalogo['ciudades']))
        print('Elementos en el árbol: ', controller.elementosArbol(catalogo['ciudades']))
        
        #Req 1
        
        ciudad = input('Contar los avistamientos en la ciudad de: ')
        
        info_ciudad = controller.infoCiudad(catalogo, ciudad)
        info_ciudad_ordenada = controller.llamarMerge(info_ciudad, identificador=1)
        primeros3 = lt.subList(info_ciudad_ordenada, 1, 3)
        ultimos3 = lt.subList(info_ciudad_ordenada, lt.size(info_ciudad_ordenada)-2, 3)
        cantidad_ciudades = controller.elementosArbol(catalogo['ciudades'])
        #avistamientos_ciudad_ordenados = controller.llamarMerge(catalogo['avistamientos'], identificador = 2)
        #top_5_avistamientos = lt.subList(avistamientos_ciudad_ordenados, 1, 5)
        
        #print('Existen {} ciudades diferentes con avistamientos'.format(cantidad_ciudades))
        #print('El top 5 de ciudades con más avistamientos es: \n')
        #print('   Ciudad    |    Número de avistamientos\n')
        
        #for i in lt.iterator(top_5_avistamientos):
            #print('  {}            {}'.format(i['ciudad'], i['num_avistamientos']))
        
        print('==================================================\n')
        print('Hay {} avistamientos en la ciudad: {}'.format(lt.size(info_ciudad_ordenada), ciudad))
        print('Los primeros y los últimos 3 avistamientos en la ciudad son: \n')
        print('    Fecha y hora    |    Ciudad    |    Estado    |    País    |    Forma    |    Duración (segundos)')
        
        for i in lt.iterator(primeros3):
            print('{}    {}    {}    {}    {}    {}'.format(i['tiempo'], i['ciudad'], i['estado'], i['pais'], i['forma'], i['duracion_segundos']))
        for i in lt.iterator(ultimos3):
            print('{}    {}    {}    {}    {}    {}'.format(i['tiempo'], i['ciudad'], i['estado'], i['pais'], i['forma'], i['duracion_segundos']))
                    
    
    elif int(inputs[0]) == 3:
        pass
    
    elif int(inputs[0]) == 4:
        
        hora_inicial = input('Digite la hora inicial: ')
        hora_final = input('Digite la hora final: ')
        
        rango_horas = controller.rangoLLaves(catalogo['avistamientos_por_hora'], hora_inicial, hora_final)
        info_horas = lt.newList(datastructure='ARRAY_LIST')
        print('2')
        
        for i in lt.iterator(rango_horas):
            info = controller.infoMap(catalogo['avistamientos_por_hora'], i)
            
            for j in lt.iterator(info):
                lt.addLast(info_horas, j)
            
        info_hora_ordenada = controller.llamarMerge(info_horas, identificador=3)
        primeros3 = lt.subList(info_hora_ordenada, 1, 3)
        ultimos3 = lt.subList(info_hora_ordenada, lt.size(info_hora_ordenada)-2, 3)
        primerElemento = lt.lastElement(ultimos3)
        info_primer_elemento = controller.infoMap(catalogo['avistamientos_por_hora'], primerElemento['tiempo_hora'])
         
        print('Existen {} avistamientos con diferentes tiempos'.format(controller.elementosArbol(catalogo['avistamientos_por_hora'])))
        print('El avistamiento más tardío es: \n')
        print('    Hora    |    Cantidad    \n')
        print('{}     {}\n'.format(primerElemento['tiempo_hora'], lt.size(info_primer_elemento)))
        print('Existen {} avistamientos entre {} y {} \n'.format(lt.size(info_horas), hora_inicial, hora_final))
        print('    Fecha y hora    |    Hora    |    Ciudad    |    Estado    |    País    |    Forma    |    Duración    ')
        print('===========================================================================================================')
        
        for i in lt.iterator(primeros3):
            print('{}    {}    {}    {}    {}    {}    {}'.format(i['tiempo'], i['tiempo_hora'], i['ciudad'], i['estado'], i['pais'], i['forma'], i['duracion_segundos']))
            
        for i in lt.iterator(ultimos3):
            print('{}    {}    {}    {}    {}    {}    {}'.format(i['tiempo'], i['tiempo_hora'], i['ciudad'], i['estado'], i['pais'], i['forma'], i['duracion_segundos']))
            
            
        
    
    elif int(inputs[0]) == 5:
        pass
    
    elif int(inputs[0]) == 6:
        pass
    
    elif int(inputs[0]) == 7:
        pass

    else:
        sys.exit(0)
sys.exit(0)
