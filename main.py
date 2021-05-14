import discord
from discord.ext import commands
import random
import os
from replit import db
from keep_alive import keep_alive

client = discord.Client()
client = commands.Bot(command_prefix='~')

def update_animelist(anime):
  if "animelist" in db.keys():
    animelist = db["animelist"]
    animelist.append (anime)
    db["animelist"] = animelist
  else:
    db["animelist"] = [anime]

response = [ 'JoJo no Kimyou na Bouken',
             'Vinland Saga',
             'Kaguya-sama: Love Is War ',
             'Gintama', 
             'Attack on Titan',
             'Naruto & Naruto Shippuden', 
             'HunterxHunter',
             'Bleach', 
             'One Piece', 
             'Dorohedoro', 
             'Mushoku Tensei',
             'Gakuen Babysitters', 
             'Grand Blue', 
             'Kobayashi-san chi no Maid dragon',
             'Fullmetal Alchemist: Brotherhood', 
             'Fairy Tail', 
             'Death Note',
             'One Punch Man', 
             'Mob Psycho 100', 
             'Steins;Gate',
             'Kimi no Na wa',
             'Haikyuu!!', 
             'Made in Abyss', 
             'Vinland Saga', 
             'Promised Neverland',
             'Kimetsu no Yaiba', 
             'Nichijou', 
             'Toradora!']
@client.event
async def on_ready():
    print("Franky is ready !")

options = response 
if "anime_list" in db.keys():
  options = options + db["anime_list"]
  
@client.event
async def on_message(message):
  msg = message.content


  if msg.startswith('~hello'):
    await message.channel.send("Suuuuuper !!")
  
  if msg.startswith('~ping'):
    await message.channel.send("Pong ! {}ms".format(round(client.latency * 1000)))

  if msg.startswith('~recommend'):
    question = msg.split("~recommend", 1)[1]
    await message.channel.send(">>>  Anime : {}\n {}".format(question, random.choice(options)))
  
  if msg.startswith("~new"):
    anime = msg.split("~new",1)[1]
    update_animelist(anime)
    await message.channel.send("New anime added.")

keep_alive()

client.run(os.getenv('TOKEN'))
