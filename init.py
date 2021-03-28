import eel
import sqlite3
import os
import re
#import json

eel.init('C:\\Users\\Makkov\\Desktop\\Python\\DBC\\gui')

@eel.expose 
def create(name, platform, program): #созданиие проекта
    jp = {"j2" : "bot.js", "p2" : "bot.py"} #словарь языки файл
    if program != 'j2': return
    filepath = os.path.join(f'.\\projects\\{name}', jp[program]) #создание файла
    if not os.path.exists(f'.\\projects\\{name}'): 
        os.makedirs(f'.\\projects\\{name}')
    f = open(filepath, "w") 
    f.write('''
const Discord = require('discord.js'); 
const { inspect } = require('util'); 
const fs = require('fs') 
const sqlite3 = require('sqlite3').verbose(); 

let config = require('./settings.json'); 

const client = new Discord.Client(); 

let token = config.token; 
let prefix = config.prefix; 
let ownerid = ''; 

client.on('ready', () => { 
    client.user.setPresence({ 
        status: 'online', 
        activity: { 
            type: 'PLAYING', 
            name: `Bot online`, 
        }, 
    }); 
}) 

function random(min, max) { 
    return Math.floor(Math.random() * (max - min + 1) ) + min; 
} 

client.on('message', async message =>{ 
    let userid = message.author.id; 
    if (message.author.bot) return; 
    if (!message.content.startsWith(prefix)) return; 
    let args = message.content.slice(prefix.length).trim().split(' '); 
    let command = args.shift().toLowerCase(); 
}) 
''')
    filepath = os.path.join(f'.\\projects\\{name}', f"settings.json") #settinsg.json создание
    jsonf = open(filepath, "w")
    jsonf.write('''
{ 
    "token" : "token", 
    "prefix" : "!"
}  
''')
    jsonf.close()
    f.close()

eel.get_opens(os.listdir(path=".\\projects"), len(os.listdir(path=".\\projects")))

idd = 'Null'
@eel.expose
def openProject(idn):
    idd = idn

def get_commands_l(idn): 
    if idd != 'Null':
        cmds = []
        with open(f'.\\projects\\{idn}\\bot.js', 'r+') as file:
            for line in file:
                if "if(command == " in line:
                    name0 = line.split("if(command == '")[1]
                    name = name0.split("'){")[0]
                    cmds.append(name)
        return cmds

eel.get_commands(get_commands_l(idd))

eel.start('index.html') #ell start