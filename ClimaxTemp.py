# !pip install requests
import requests
from IPython.display import clear_output

#API
API_KEY = "a44732faf772a15a554b72afc1045161"
cidade = "São Paulo"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)
dicionariojson = requisicao.json()

#Entrada
print ("_--Climax Temp--_")
cidade = input ("Digite uma Cidade : ") 
clear_output()

#Requests
descricao = dicionariojson["weather"][0]["description"]
temperatura = dicionariojson["main"]["temp"]
maxima = dicionariojson["main"]["temp_max"]
minima = dicionariojson["main"]["temp_min"]

#conversao para Cº
temperatura = temperatura - 273.15
maxima = maxima - 273.15
minima = minima - 273.15

print(f"_--Climax Temp--_ \n\n Cidade: {cidade}\n Temperatura: {round(temperatura)}ºC\n Tempo: {descricao}\n\n Máxima: {round(maxima)}\n Minima: {round(minima)}")
