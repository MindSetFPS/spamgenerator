# encoding: utf-8

import pyperclip
import emoji
from datetime import date

today = date.today()

dias_de_semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

if today.weekday() == 6:
    dia = 'Lunes'
else:
    dia = dias_de_semana[today.weekday() + 1]

comida1 = input('Comida 1:')
comida2 = input('Comida 2:')

text = f'Hola, soy Doña Mary de la cocina economica. \nMañana {dia} tenemos: 🍽🍴\n👉 {comida1}🍗\n👉 {comida2}🍲\nTe agradeceria si le das Like a nuestra pagina: https://www.facebook.com/Cocina-Economica-Mary-115954489868469\nWhatsapp: 9992256740'

print(text)

pyperclip.copy(text)
pyperclip.paste()
