import eel
import sqlite3
import os

eel.init('C:\\Users\\Makkov\\Desktop\\DBC')

@eel.expose
def create(name, path):
    print(f"{name}||||{path}")
    path = f"{path}"
    filepath = os.path.join(path, 'test.js')
    if not os.path.exists(path):
        os.makedirs(path)
    f = open(filepath, "a")


eel.start('index.html')
