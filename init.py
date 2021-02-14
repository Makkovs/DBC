import eel
import sqlite3
import os

eel.init('C:\\Users\\Makkov\\Desktop\\DBC')

@eel.expose
def create(name, path, platform, program):
    jp = {"j2" : "bot.js", "p2" : "bot.py"}
    filepath = os.path.join(path, jp[program])
    if not os.path.exists(path):
        os.makedirs(path)
    f = open(filepath, "a")


eel.start('index.html')
