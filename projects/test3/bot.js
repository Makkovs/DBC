
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
