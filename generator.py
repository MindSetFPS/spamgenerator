# encoding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from colorama import Fore, Back, Style, init

import time
import random

import emoji
from datetime import date

init()

listaComidas = [
    {
        "name" : "Pechuga Empanizada",
        "link" : "https://rebrand.ly/PechugaEmpanizada",
        "n" : 0
    },
    {
        "name" : "Frijol con Puerco",
        "link" : "https://rebrand.ly/FrijolConPuerco",
        "n" : 1
    },{
        "name" : "Fajitas de Pollo",
        "link" : "https://rebrand.ly/FajitasDePollo",
        "n" : 2
    },{
        "name" : "Chilaquiles de Mole",
        "link" : "http://rebrand.ly/ChilaquilesDeMole",
        "n" : 3
    },{
        "name" : "Pechuga a la Plancha en Crema de Chipotle",
        "link" : "https://rebrand.ly/PechugaPlanchaCremaChipotle",
        "n" : 4
    },{
        "name" : "Pozole",
        "link" : "https://rebrand.ly/Pozole",
        "n" : 5
    },{
        "name" : "Relleno Negro", 
        "link" : "https://rebrand.ly/RellenoNegro",
        "n" : 6
    }
    ,{
        "name" : "Carne Molida",
        "link" : "https://rebrand.ly/CarneMolida",
        "n" : 7
    },{
        "name" : "Pechuga Parmesana",
        "link" : "https://rebrand.ly/PechugaParmesana",
        "n" : 8
    },{
        "name" : "Poc Chuc",
        "link" : "https://rebrand.ly/PocChuc",
        "n" : 9
    },{
        "name" : "Tortitas de Papa",
        "link" : "https://rebrand.ly/TortitasDePapa",
        "n" : 10
    },{
        "name": "Bistec Con Papa",
        "link" : "https://rebrand.ly/BistecPapa",
        "n" : 11
    },{
        "name" : "Pollo en Mole",
        "link" : "https://rebrand.ly/MolePollo",
        "n" : 12
    },{
        "name" : "Carnitas Estilo Michoacan",
        "link" : "https://rebrand.ly/CarnitasEstiloMichoacan",
        "n" : 13
    },{
        "name" : "Potaje de Lentejas",
        "link" : "https://rebrand.ly/PotajeDeLentejas",
        "n"  : 14

    },{
        "name": "Fajitas de Puerco",
        "link": "https://rebrand.ly/FajitasDePuerco",
        "n" : 15
    }
]
    #PechugaEmpanizada = 
    #ChilaquilesMole = 
    #Tortitas de Carne
    #Tortitas de Papa
    #Relleno Negro
    #Puchero
    #Frijol con Puerco
    #Carne Molida Con Papa y Zanahoria 
    #Fajitas de Pollo
    #Albondigas Con Fideo
    #Poc Chuc 
    #Pescado Empanizado
    #Pechuga en Crema de Chipotle
    #Asado Rojo
    #Potaje de Lentejas
    #Pollo en Mole
    #Puerco Entomatado
    #Chuletas Fritas
    #Pollo Asado con Sopa

def aksForInput(skip = 550):

    print( Fore.WHITE + Back.MAGENTA + Style.BRIGHT + "Selecciona 2 comidas")

    for platillo in listaComidas:

        if int(platillo["n"]) == int(skip):
            pass
        else:
            print( Style.BRIGHT + Back.CYAN + str(platillo["n"]) + ') ' + platillo["name"] )
    
    print(Style.RESET_ALL)
        

def run():
    print(chr(27) + "[2J") #Limpiar pantalla

    aksForInput()
    firstMenu = int(input())
    print(chr(27) + "[2J") #Limpiar pantalla

    aksForInput(firstMenu)
    secondMenu = int(input())

    #Configurar Selenium
    browser = webdriver.Firefox(executable_path='./geckodriver')
    browser.get("https://web.whatsapp.com/")

    clientes = ["Lupita", "Vertiche Juan", "Coppel Pedro Cajas", "Coppel Eloisa Puerto", "Coppel Doña Maggui", "Coppel Joel Ropa",  "Coppel Naomi Banco", "Coppel Fernanda Cajas", "Coppel Yessy", "Coppel Gustavo Movistar", "Coppel Victor Movistar", "Coppel Bianca Castro", "Coppel Rosita", "Coppel Carlos Banco", "Coppel Gaby Paqueteria", "Coppel Adriana Afore", "Coppel Damian", "Coppel Mariana Banco", "Coppel Perla", "Coppel Rosario", "Coppel Ruby", "Coppel Carlos Zapateria", "Coppel Guillermo Mendez", "Coppel Carlos Telefonia", "Coppel Yonatan" , "Coppel Sharid", "Coppel Pablo", "Coppel Yaritza", "Coppel Dulce", "Coppel Mayra", "Coppel Daniel Pech", "Coppel Citlali", "Coppel Lizzeth", "Flexi", "Flexi 3", "Loteria", "Coppel Iyari", "Vertiche Luis", "Michelle", "Radioshack Uriel" ]

    print(str(len(clientes)) + " Personas recibiran este Mensaje" )

    empezar = input('Presiona Enter despues de haber iniciado sesion')

    today = date.today()

    dias_de_semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

    #Tomar el dia de la semana y aumentarle 1
    if today.weekday() == 6:
        dia = 'Lunes'
    else:
        dia = dias_de_semana[today.weekday() + 1]

    text = f'Hola, soy Doña Mary de la cocina economica. \nMañana {dia} tenemos: 🍽🍴\n👉 *{listaComidas[firstMenu]["name"]}*🍗: {listaComidas[firstMenu]["link"]} \n👉 *{listaComidas[secondMenu]["name"]}*  🍲: {listaComidas[secondMenu]["link"]} \nTe agradeceria si le das Like a nuestra pagina: https://www.facebook.com/Cocina-Economica-Mary-115954489868469\nWhatsapp: 9992256740'

    print(text)

    #Enviar el mensaje a cada cliente
    for e in clientes:
        print(e)

        #Encontrar bucador de Contactos y dar click
        search_bar = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
        search_bar.click()
        search_bar.send_keys(e)
        time.sleep(5)
        search_bar.clear()

        #Buscar contacto y darle click
        selected_contact = browser.find_element_by_xpath("//span[@title='"+e+"']")
        selected_contact.click()

        #Buscar campo de texto del mensaje y enviarlo
        inp_xpath = '//div[@class="_3FRCZ copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
        input_box = browser.find_element_by_xpath(inp_xpath)
        time.sleep(random.randint(1, 5))
        input_box.send_keys(text + Keys.ENTER)

    empezar = input('Presiona Enter para salir')
    browser.quit()

if __name__ == "__main__":
    run()