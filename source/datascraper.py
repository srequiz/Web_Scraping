# -*- coding: utf-8 -*-
"""
# Nombre:       datascraper.py
# Propósito:    Web Scraping con BeautifulSoup - Practica UOC Tipología y ciclo de vida de los datos
#
# Origen:        Propio
# Autor:         Jonathán Rodriguez Naranjo
#
# Creación:      12 de Noviembre de 2018
# Historia:
#
# Dependencias:  datascraper, requests,BeautifulSoup,os,time
# Licencia:      Released Under CC BY-NC-SA 4.0 License
# 
# Fichero clase
# Métodos: __init__ -> Creación/incialización  
#            parseurl -> Obtiene el contenido de una url retornando en un objeto (BeautifulSoup)
#            findurls -> Dado un objeto (BeautifulSoup) retorna las url contenidas en una lista
#            extractdata -> Dado un objeto (BeautifulSoup) retorna los datos de los vehículos en una lista
#            writecsv -> Crea el fichero csv con los datos obtenidos 
"""

import requests
from bs4 import BeautifulSoup
import os
import time

class scraper():

        
        def __init__(self):
            self.urlbase = 'https://publicaciones.carfactory.es'
            self.colnames=["Precio","Marca","Modelo","Potencia","Version","Puertas","Combustible","Plazas","Co2","Color","Año","Km","Cambio"]
            self.cars = []
            self.cars.append(self.colnames)
            self.filename = "pricescar.csv"
            self.filepath = os.path.join(os.path.dirname(__file__), self.filename)
            
        def parseurl (url):
            time.sleep(5)
            page = requests.get(url)
            if (page.status_code==200):
                    return BeautifulSoup(page.content, "html.parser")
            
        
        def findurls (self,hsoup):
            tmpsoup = BeautifulSoup(''.join(map(str, hsoup.find_all('a',attrs={'class':'fblack'}))),features="lxml")
            return [self.urlbase + a['href'] for a in tmpsoup.find_all('a', href=True) if a.text]
               
        
        def extractdata(self,esoup):
              if (esoup):
                  tmp = BeautifulSoup(''.join(map(str, esoup.select("#ftcol2,#ftcol4,#ftcol6"))),features="lxml")    
                  price = esoup.find('b', attrs={'class':'fred'})
                  ltmp =[price.text.strip('\n\r€ ')]
                  for a in tmp.find_all('span'):
                      ltmp.append(a.text)
                  print (ltmp)
                  return self.cars.append(ltmp)
                   
                  
        def writecsv (self):
            file = open( self.filename, "w")
            for i in range(len(self.cars)):
                for j in range(len(self.cars[i])):
                    file.write(self.cars[i][j] + ",");
                file.write("\n");
            file.close()
            