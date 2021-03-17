import eel
import sqlite3
import os
import json

eel.init('C:\\Users\\Makkov\\Desktop\\Python\\DBC\\gui')

@eel.expose 
def create(name, platform, program): #созданиие проекта
    jp = {"j2" : "bot.js", "p2" : "bot.py"} #словарь языки файл
    filepath = os.path.join(f'.\\projects\\{name}', jp[program]) #создание файла
    if not os.path.exists(f'.\\projects\\{name}'): 
        os.makedirs(f'.\\projects\\{name}')
    f = open(filepath, "a") 
    filepath = os.path.join(f'.\\projects\\{name}', f"settings.json") #settinsg.json создание
    if not os.path.exists(f'.\\projects\\{name}'):
        os.makedirs(f'.\\projects\\{name}') 
    jsonf = open(filepath, "a")

eel.start('index.html') #ell start