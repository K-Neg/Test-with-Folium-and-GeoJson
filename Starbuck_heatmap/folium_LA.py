import folium
import pandas as pd
import json
from folium import plugins

#CSV -  store location
df = pd.read_csv('starbucksInLACounty.csv')

#shape Los Angeles
with open('laMap.geojson') as f:
	laArea = json.load(f)

#start map as folium object
mapa = folium.Map(location=[34.0522,-118.2437], tiles='Stamen Toner', zoom_start=9)

#add shape
folium.GeoJson(laArea).add_to(mapa)

#extract latitude longitude 
#plot dots as circles
for i,row in df.iterrows():
    folium.CircleMarker((row.latitude,row.longitude), radius=3, weight=2, color='red', fill_color='red', fill_opacity=.5).add_to(mapa)

#save map as html
mapa.save('laPointMap.html')

#########################
#Choroplet MAP

#group by ZIP CODE (CEP)
#groupby as pandas method

numStoresSeries = df.groupby('zip').count().id
#blank df for test
numStoresByZip = pd.DataFrame()

#add a zipcode and store count colum
numStoresByZip['zipcode'] = [str(i) for i in numStoresSeries.index]
numStoresByZip['numStores'] = numStoresSeries.values

#folium.Choropleth(geo_path='laZips.geojson', geo_data=numStoresByZip, columns=['zipcode', #'numStores'], key_on='feature.properties.zipcode', fill_color='YlGn', fill_opacity=1)


folium.Choropleth(
    geo_data='laZips.geojson',
    name='choropleth',
    data=numStoresByZip,
    columns=['zipcode', 'numStores'],
    key_on='feature.properties.zipcode',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Unemployment Rate (%)'
).add_to(mapa)

mapa.save('laChoropleth.html')


#########################
#Heat Map

#initialize the LA County map
laMap = folium.Map(location=[34.0522,-118.2437], tiles='Stamen Toner', zoom_start=9)

#add the shape of LA County to the map
folium.GeoJson(laArea).add_to(laMap)

#for each row in the Starbucks dataset, plot the corresponding latitude and longitude on the map
for i,row in df.iterrows():
    folium.CircleMarker((row.latitude,row.longitude), radius=3, weight=2, color='red', fill_color='red', fill_opacity=.5).add_to(laMap)

#add the heatmap. The core parameters are:
#--data: a list of points of the form (latitude, longitude) indicating locations of Starbucks stores

#--radius: how big each circle will be around each Starbucks store

#--blur: the degree to which the circles blend together in the heatmap

laMap.add_child(plugins.HeatMap(data=df[['latitude', 'longitude']].as_matrix(), radius=25, blur=10))

#save the map as an html
laMap.save('laHeatmap.html')