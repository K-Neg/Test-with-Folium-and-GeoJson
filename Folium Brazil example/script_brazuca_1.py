#https://medium.com/@datalivre/folium-d6036a9ad29c


import folium
import json
import pandas as pd
import matplotlib as plt
from branca.colormap import linear #para a escala de cor

br_estados ='br_states.json'
geo_json_data=json.load(open(br_estados))
desemprego = pd.read_csv('taxa_desemprego_br.csv', sep=';',
	decimal=',',usecols=['Sigla','4º trimestre 2018'])

#head dos dados
print(desemprego.head(3))	

#renomeando as colunas
desemprego.rename(columns={
	'Sigla':'UF',
	'4º trimestre 2018':'4T 2018'},
	inplace=True)

#conferindo o rename
print(desemprego.head(0))	

#Ver a distribuição dos valores
print(desemprego.describe())

#Puxa valores MIN e MAX para escala de coloar
#derivado do describe
vmin=desemprego.min()
vmax=desemprego.max()

#cria a escala de cor baseado em max e min
colormap = linear.YlOrRd_09.scale(vmin[1],vmax[1])

desemprego_br_2018 = \
desemprego.set_index('UF')['4T 2018']


#cria o mapa FOLIUM
mapa = folium.Map(\
	#width=600,height=400,\
	location=[-15.77972, -47.92972],\
	tiles='Stamen Toner', #ok
	#tiles='OpenStreetMap',\ #ok
	#tiles='MapboxBright',\
	#tiles='Mapbox Control Room',\ #FALHOU
	#tiles='Cloudmade',\ FALHOU
	#tiles='CartoDB',\ #FALHOU
	zoom_start=5)

#GEO MAPA SIMPLES

#Adicona a layer geografica - func basica
#folium.GeoJson(geo_json_data).add_to(mapa)
#folium.GeoJson(SuaGeoData , Style : fundo/contorno/bitola)
folium.GeoJson(geo_json_data,
	style_function=lambda feature: {
	'fillColor': 'green',
	'color': 'darkred',
	'weight': 2,
	}
	).add_to(mapa)

mapa.save('Brazilzaum_SIMPLES.html')

#MAPA CHOROPLETH

folium.GeoJson(geo_json_data,
	name='4º Tri 2018',
	style_function=lambda feature:{
	'fillColor':
	colormap(desemprego_br_2018[feature['id']]),
	'color': 'black',
	'weight': 0.3,
	}
	).add_to(mapa)

colormap.caption = 'Taxa de desemprego no Brasil 2018'
colormap.add_to(mapa)

folium.LayerControl(collapsed=False).add_to(mapa)
mapa.save('taxa_br_2018.html')