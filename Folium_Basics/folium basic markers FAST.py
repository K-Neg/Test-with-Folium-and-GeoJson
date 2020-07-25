# extract data
latitude = df.latitude.values
longitude = df.longitude.values
nomes = df.nome.value

# create a map 
mapa = folium.Map(location=[-8.0298747,-34.9670771],
                  zoom_start=11, )

# add markers
for lat, lon, nome in zip(latitude, longitude, nomes):
    folium.Marker(location=[float(lat), float(lon)], popup=nome).add_to(mapa)

#save as html
mapa.save('map.html')

#show maps
mapa