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
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def initCatalogo():
    
    catalogo = {'datos':None,
                'ciudades': None,
                'fechas': None
                }
    
    catalogo['datos'] = lt.newList(datastructure='ARRAY_LIST')
    catalogo['ciudades'] = om.newMap(omaptype='RBT')
    catalogo['fechas'] = om.newMap(omaptype='RBT')
    
    return catalogo
    


# Funciones para agregar informacion al catalogo

def agregarDato(catalogo, dato):
    
    dato = nuevoDato(dato)
    lt.addLast(catalogo['datos'], dato)
    agregarCiudad(catalogo['ciudades'], dato)
    agregarFechas(catalogo['fechas'], dato)
    
    
def nuevoDato(dato):
    
    nuevoDato = {'tiempo': dato['datetime'],
            'ciudad': dato['city'],
            'estado': dato['state'],
            'pais': dato['country'],
            'duracion_segundos': dato['duration (seconds)'],
            'duracion_horas/minutos': dato['duration (hours/min)'], 
            'latitud': dato['latitude'],
            'longitud': dato['longitude']
            }
    
    return nuevoDato
    
    
def agregarCiudad(catalogo, dato):
    
    existe = om.contains(catalogo, dato['ciudad'])
    
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
    
    

# Funciones para creacion de datos

# Funciones de consulta

def alturaArbol(catalogo):
    return om.height(catalogo)

def elementosArbol(catalogo):
    return om.size(catalogo)

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
