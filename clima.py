import requests
import json

name_city = str(input("Digite Sua Cidade: "))
name_state = str(input("Digite Seu Estado Abreviado: "))

def ID(cidade, estado):
    city = str(cidade)
    state = str(estado)
    requisicao = requests.get("https://api.hgbrasil.com/weather?key=40acff95&city_name="+ name_city +","+ name_state +"")
    jsn = json.loads(requisicao.text)
    return jsn

def Status(json):
    json = json
    print("################################################################################")
    print("Dia " + str(json['results']['date']) + " às " + str(json['results']['time']))   # Horario e Dia
    print("Condicao: " + str(json['results']['description']))                              # descricao
    print("Cidade: " + str(json['results']['city']))                                       # cidade
    print("Nivel de Humidade: " + str(json['results']['humidity'] + "%"))                  # humidade
    print("Temperatura de: " + str(json['results']['temp']) + "°")                         # temperatura
    print("################################################################################")


name = ID(name_city, name_state)
show = Status(name)
