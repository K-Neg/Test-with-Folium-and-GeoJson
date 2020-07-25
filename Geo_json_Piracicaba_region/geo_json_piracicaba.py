import folium
import json
import pandas as pd
import matplotlib as plt
import requests

#https://servicodados.ibge.gov.br/api/v2/malhas/3506?formato=application/vnd.geo+json
#"https://servicodados.ibge.gov.br/api/v2/malhas/?formato=application/vnd.geo+json"

geo_path = "https://servicodados.ibge.gov.br/api/v2/malhas/3506?formato=application/vnd.geo+json"
#-22.722585, -47.643561 Piracity coordinates

mapa1 = folium.Map(
	location=[-22.722585,-47.643561],
	tiles='Stamen Toner',
	zoom_start=5)

geo_arquivo = requests.get(geo_path)
geo_arquivo2 = geo_arquivo.json()

folium.GeoJson(geo_arquivo2).add_to(mapa1)

mapa1.save('pira1.html')
