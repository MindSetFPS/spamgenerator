# encoding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import time

import pyperclip
import emoji
from datetime import date

#Configurar Selenium
browser = webdriver.Firefox(executable_path='./geckodriver')
browser.get("https://web.whatsapp.com/")
empezar = input('Presiona Enter despues de haber iniciado sesion')

contact = "Mama"

clientes = ["Lupita", "Nelly", "Coppel Pedro Cajas", "Coppel Eloisa Puerto", "Coppel Doña Maggui", "Coppel Joel Ropa",  "Coppel Naomi Banco", "Coppel Fernanda Cajas", "Coppel Yessy", "Coppel Gustavo Movistar", "Coppel Victor Movistar", "Coppel Bianca Castro", "Coppel Rosita", "Coppel Carlos Banco", "Coppel Gaby Paqueteria", "Coppel Adriana Afore", "Coppel Damian", "Coppel Mariana Banco", "Coppel Perla" ]

today = date.today()

dias_de_semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

#Tomar el dia de la semana y aumentarle 1
if today.weekday() == 6:
    dia = 'Lunes'
else:
    dia = dias_de_semana[today.weekday() + 1]

comida1 = input('Comida 1:')
comida2 = input('Comida 2:')

text = f'Hola, soy Doña Mary de la cocina economica. \nMañana {dia} tenemos: 🍽🍴\n👉 {comida1}🍗\n👉 {comida2}🍲\nTe agradeceria si le das Like a nuestra pagina: https://www.facebook.com/Cocina-Economica-Mary-115954489868469\nWhatsapp: 9992256740'

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
    time.sleep(2)
    input_box.send_keys(text + Keys.ENTER)

print(text)

