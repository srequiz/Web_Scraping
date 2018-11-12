# Web Scraping - Practica UOC Tipología y ciclo de vida de los datos 

El objetivo de esta actividad será la creación de un dataset a partir de los datos contenidos de una web de venta de vehículos.
Para obtener el dataset se extraen los datos mediante la técnica de raspado de los datos disponibles en una web. Esto nos permite obtener aquella información útil para un proyecto de datos que se encuentra disponible en Internet.

## Bibliotecas utilizadas

pip3 install builtwith.
pip3 install python-whois.
pip3 install requests.
pip3 install beautifulsoup4.

## Miembro del equipo

Jonathán Rodriguez Naranjo

## Ficheros del código fuente

main.py:Fichero de ejecución

datascraper.py:Clase scraper 
Se compone de los siguientes métodos:

    __init__ -> Creación/incialización  
    parseurl -> Obtiene el contenido de una url retornando en un objeto (BeautifulSoup)
    findurls -> Dado un objeto (BeautifulSoup) retorna las url contenidas en una lista
    extractdata -> Dado un objeto (BeautifulSoup) retorna los datos de los vehículos en una lista
    writecsv -> Crea el fichero csv con los datos obtenidos 
    
    
   
