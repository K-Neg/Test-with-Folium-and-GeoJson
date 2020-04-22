#https://medium.com/@louisartur53/an%C3%A1lise-e-visualiza%C3%A7%C3%A3o-espacial-de-dados-reais-em-python-com-folium-cd4650fc5930


import folium
import pandas as pd
import numpy as numpy
import json

url_aeroportos_publicos = 'https://drive.google.com/uc?authuser=0&id=1xHhzSTRDr6apDqeE5WWElet09HJ-msxj&export=download'

#import csv 
aeroportos_publicos =pd.read_csv(url_aeroportos_publicos,error_bad_lines=False, encoding="latin-1",sep=';')

#vizualizada rapida
print(aeroportos_publicos.head())

#dropa tudo a partir da 7 coluna
aeroportos_publicos = aeroportos_publicos.drop(aeroportos_publicos.columns[7:], axis=1)

#pega os nomes das colunas que estão na segunda linha via ILOC
aeroportos_publicos.columns = aeroportos_publicos.iloc[1]

#Elimina o resto de titulos de colunas que n servem e reseta o index
aeroportos_publicos= aeroportos_publicos.reindex(aeroportos_publicos.index.drop(0))
aeroportos_publicos= aeroportos_publicos.reindex(aeroportos_publicos.index.drop(1))
aeroportos_publicos = aeroportos_publicos.reset_index(drop=True)
print(aeroportos_publicos.head())


todos_estados_sem_nordeste=['AC','AM','AP','PA','RO','RR','TO','GO','MS','MT','ES','MG','RJ','SP','PR','RS','SC','DF']

def retirar_estados(df):
  for estado in todos_estados_sem_nordeste:
    aeroportos_publicos.drop(aeroportos_publicos[aeroportos_publicos.UF == estado].index,inplace = True)

retirar_estados(aeroportos_publicos)
aeroportos_publicos = aeroportos_publicos.reset_index(drop=True)


aeroportos_publicos.LATITUDE = (aeroportos_publicos.LATITUDE.str.split(r'[°\'"]',expand=True)).iloc[:, :3].astype('float').dot([1, 1./60, 1./3600])*-1

aeroportos_publicos.LONGITUDE = aeroportos_publicos.LONGITUDE.str.split(r'[°\'"]',expand=True).iloc[:, :3].astype('float').dot([1, 1./60, 1./3600])*-1

mapa_nordeste = folium.Map(location=[-8.8864889,-39.6786708],zoom_start=5.3,
                           tiles='Stamen Terrain')