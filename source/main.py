# -*- coding: utf-8 -*-
"""
# Nombre:       main.py,datascraper.py
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
# Fichero principal
# Variables: scrape -> instancia de la clase datascraper
#            soup -> objeto tipo BeautifulSoup
#            allurls -> lista de url con datos en detalle de los vehículos 
"""

#importamos la clase
from datascraper import scraper

# url base de búsqueda                                                                      
url = 'https://publicaciones.carfactory.es/vehicles/5894?&channel=default&box=true&ext=0&BoxTitle=Buscador&contract=5894&maxRows=100'

# instanciamos la clase
scrape = scraper();
# creamos el objeto 
soup = scraper.parseurl(url);
#saber cuantas urls deben ser visitadas
allurls = scrape.findurls(soup);
print (allurls)

# recorremos las urls raspando los datos
for i in allurls:
    scrape.extractdata(scraper.parseurl(i))
scrape.writecsv()



