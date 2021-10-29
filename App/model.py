"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
#from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ist
from DISClib.Algorithms.Sorting import mergesort as mst
from DISClib.Algorithms.Sorting import quicksort as qst
from DISClib.Algorithms.Sorting import shellsort as sst
from datetime import date, time, datetime
import time
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

lista_todas_ciudad = []
lista_ciudad = []

# Construccion de modelos

def initCatalogo():
    
    catalogo = {'datos':None,
                'ciudades': None,
                'fechas': None,
                'avistamientos': None,
                'avistamientos_por_hora': None
                }
    
    catalogo['datos'] = lt.newList(datastructure='ARRAY_LIST')
    catalogo['ciudades'] = om.newMap(omaptype='RBT')
    catalogo['fechas'] = om.newMap(omaptype='RBT')
    catalogo['avistamientos'] = lt.newList(datastructure='ARRAYLIST')
    catalogo['avistamientos_por_hora'] = om.newMap(omaptype='RBT')
    
    return catalogo
    


# Funciones para agregar informacion al catalogo

def agregarDato(catalogo, dato):
    
    dato = nuevoDato(dato)
    lt.addLast(catalogo['datos'], dato)
    agregarCiudad(catalogo['ciudades'], dato)
    agregarFechas(catalogo['fechas'], dato)
    agregarHoraAvistamiento(catalogo['avistamientos_por_hora'], dato)
    
    
def nuevoDato(dato):
    
    tiempo = dato['datetime']
    lista_hora = tiempo.split(' ')
    hora = lista_hora[1]
    
    nuevoDato = {'tiempo': dato['datetime'],
            'ciudad': dato['city'],
            'estado': dato['state'],
            'pais': dato['country'],
            'tiempo_hora': hora,
            'forma': dato['shape'],
            'duracion_segundos': dato['duration (seconds)'],
            'duracion_horas/minutos': dato['duration (hours/min)'], 
            'latitud': dato['latitude'],
            'longitud': dato['longitude']
            }
    
    return nuevoDato
    
    
def agregarCiudad(catalogo, dato):
    
    existe = om.contains(catalogo, dato['ciudad'])
    lista_todas_ciudad.append(dato['ciudad'])
    
    if dato['ciudad'] not in lista_ciudad:
        lista_ciudad.append(dato['ciudad'])
    
    if existe:
        
        entry_ciudades = om.get(catalogo, dato['ciudad'])
        lista_ciudades = me.getValue(entry_ciudades)
        lt.addLast(lista_ciudades, dato)
        
    else:
        lista_ciudades = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lista_ciudades, dato)
        om.put(catalogo, dato['ciudad'], lista_ciudades)
        
        
def agregarFechas(catalogo, dato):
    
    existe = om.contains(catalogo, dato['tiempo'])
    
    if existe:
        entry_fechas = om.get(catalogo, dato['tiempo'])
        lista_fechas = me.getValue(entry_fechas)
        lt.addLast(lista_fechas, dato)
        
    else:
        lista_fechas = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lista_fechas, dato)
        om.put(catalogo, dato['tiempo'], lista_fechas)
        
        
def agregarHoraAvistamiento(catalogo, dato):
    
    hora = dato['tiempo_hora']
    existe = om.contains(catalogo, hora)
    
    if existe:
        entry_horas = om.get(catalogo, hora)
        lista_horas = me.getValue(entry_horas)
        lt.addLast(lista_horas, dato)
        
    else:
        lista_horas = lt.newList(datastructure='ARRAY_LIST')
        lt.addLast(lista_horas, dato)
        om.put(catalogo, hora, lista_horas)
    
        
def agregarAvistamientos(catalogo):
    
    lista = catalogo['avistamientos']
    
    for i in lista_ciudad:
        
        nuevoAvistamiento = {}
        cont = lista_todas_ciudad.count(i)
        
        nuevoAvistamiento['ciudad'] = i
        nuevoAvistamiento['num_avistamientos'] = cont
        
        lt.addLast(lista, nuevoAvistamiento)
    
    

# Funciones para creacion de datos

# Funciones de consulta

def alturaArbol(catalogo):
    return om.height(catalogo)


def elementosArbol(catalogo):
    return om.size(catalogo)


def infoCiudad(catalogo, ciudad):
    
    entry_ciudad = om.get(catalogo['ciudades'], ciudad)
    info_ciudad = me.getValue(entry_ciudad)
    
    return info_ciudad


def rangoLLaves(catalogo, hora_inicial, hora_final):
    return om.keys(catalogo, hora_inicial, hora_final)


def infoMap(catalogo, i):
    
    entry = om.get(catalogo, i)
    info = me.getValue(entry)
    return info


# Funciones utilizadas para comparar elementos dentro de una lista

def cmpFechaAvistamiento(fecha1, fecha2):
    
    fecha1_final = datetime.strptime(fecha1['tiempo'], '%Y-%m-%d %H:%M:%S')
    fecha2_final = datetime.strptime(fecha2['tiempo'], '%Y-%m-%d %H:%M:%S')
    
    if fecha1_final < fecha2_final:
        return True
    else:
        return False
    
    
def cmpFechaAvistamientoPrueba(fecha1, fecha2):
    
    if fecha1 < fecha2:
        return True
    else:
        return False
    
    
    
def cmpNumAvistamiento(av1, av2):
    
    av1_final = av1['num_avistamientos']
    av2_final = av2['num_avistamientos']
    
    if av1_final > av2_final:
        return True
    else: 
        return False
    
    
def cmpHoraAvistamiento(h1, h2):
    
    h1_final = h1['tiempo_hora']
    h2_final = h2['tiempo_hora']
    
    if h1_final < h2_final:
        return True
    elif h1_final == h2_final:
        
        fecha1 = h1['tiempo']
        fecha2 = h2['tiempo']
        
        return cmpFechaAvistamientoPrueba(fecha1, fecha2)
    
    else: 
        return False
    
    
    

# Funciones de ordenamiento

def insertion(datos, identificador): 
    
    if identificador == 1:
        lista_ordenada = ist.sort(datos, cmpFechaAvistamiento)
    elif identificador == 2:
        lista_ordenada = ist.sort(datos, cmpNumAvistamiento)
    elif identificador == 3:
        lista_ordenada = ist.sort(datos, cmpHoraAvistamiento)
    
    return lista_ordenada

def shell(datos, identificador):   
    
    if identificador == 1:
        lista_ordenada = sst.sort(datos, cmpFechaAvistamiento)
    elif identificador == 2:
        lista_ordenada = sst.sort(datos, cmpNumAvistamiento)
    elif identificador == 3:
        lista_ordenada = sst.sort(datos, cmpHoraAvistamiento)
    
    return lista_ordenada

def merge(datos, identificador):
    
    if identificador == 1:
        lista_ordenada = mst.sort(datos, cmpFechaAvistamiento)
    elif identificador == 2:
        lista_ordenada = mst.sort(datos, cmpNumAvistamiento)
    elif identificador == 3:
        lista_ordenada = mst.sort(datos, cmpHoraAvistamiento)
        
    
    return lista_ordenada

def quicksort(datos, identificador):
    
    if identificador == 1:
        lista_ordenada = qst.sort(datos, cmpFechaAvistamiento)
    elif identificador == 2:
        lista_ordenada = qst.sort(datos, cmpNumAvistamiento)
    elif identificador == 3:
        lista_ordenada = qst.sort(datos, cmpHoraAvistamiento)

    return lista_ordenada
