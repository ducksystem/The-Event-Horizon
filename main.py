import discord
import os
import schedule
import time

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('E!echo'):
    await message.channel.send ('echo echo echo... echooo....')

client.run(os.getenv('TOKEN'))