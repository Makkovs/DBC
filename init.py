import eel
import sqlite3
import os

eel.init('C:\\Users\\Makkov\\Desktop\\DBC')

@eel.expose
def create(name, path, platform, program):
    print(name, path, platform, program)
    jp = {"JavaScript" : "bot.js", "Python" : "bot.py"}
    filepath = os.path.join(path, 'bot.js')
    if not os.path.exists(path):
        os.makedirs(path)
    f = open(filepath, "a")


eel.start('index.html')
