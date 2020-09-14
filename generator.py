# encoding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import time
import random

import emoji
from datetime import date

#Configurar Selenium
browser = webdriver.Firefox(executable_path='./geckodriver')
browser.get("https://web.whatsapp.com/")

clientes = ["Lupita", "Coppel Pedro Cajas", "Coppel Eloisa Puerto", "Coppel Doña Maggui", "Coppel Joel Ropa",  "Coppel Naomi Banco", "Coppel Fernanda Cajas", "Coppel Yessy", "Coppel Gustavo Movistar", "Coppel Victor Movistar", "Coppel Bianca Castro", "Coppel Rosita", "Coppel Carlos Banco", "Coppel Gaby Paqueteria", "Coppel Adriana Afore", "Coppel Damian", "Coppel Mariana Banco", "Coppel Perla", "Coppel Rosario", "Coppel Ruby", "Coppel Carlos Zapateria", "Coppel Guillermo Mendez", "Coppel Carlos Telefonia", "Coppel Yonatan" , "Coppel Sharid", "Coppel Pablo", "Coppel Yaritza", "Coppel Dulce", "Coppel Mayra", "Coppel Daniel Pech", "Coppel Citlali" ]

print(len(clientes))

empezar = input('Presiona Enter despues de haber iniciado sesion')

today = date.today()

dias_de_semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

#Tomar el dia de la semana y aumentarle 1
if today.weekday() == 6:
    dia = 'Lunes'
else:
    dia = dias_de_semana[today.weekday() + 1]

comida1 = "Pechuga Empanizada"
comida2 = "Chilaquiles de Mole"

linkComida1 = "https://rebrand.ly/PechugaEmpanizada"
linkComida2 = "http://rebrand.ly/ChilaquilesDeMole"

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


text2 = f'Nuevo metodo de pago: Mercado pago\nPara comprar\n 1.-Abre el link de la comida que quieras comprar\n2.-Si tienes cuenta de MercadoPago, seleccionala, sino, selecciona cualquier metodo, llena los campos y escribe tu correo. \n 3.- Al terminar de procesarse el pago, manda tu numero de folio.\n 4.- Una vez que te hayas registrado, se habran guardado tus metodos de pago.'

text = f'Hola, soy Doña Mary de la cocina economica. \nMañana {dia} tenemos: 🍽🍴\n👉 *{comida1}*🍗: {linkComida1} \n👉 *{comida2}*  🍲: {linkComida2} \nTe agradeceria si le das Like a nuestra pagina: https://www.facebook.com/Cocina-Economica-Mary-115954489868469\nWhatsapp: 9992256740'

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