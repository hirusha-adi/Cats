import os

import discord
from discord.ext import commands

from src.utils.database import Settings as SettingsDB

with open("token.txt", "r", encoding="utf-8") as tokenfile:
    token = tokenfile.read()
bot_prefix = SettingsDB.main["prefix"]

client = commands.Bot(command_prefix=bot_prefix)

for filename in os.listdir('./src/cogs'):
    if filename.endswith('.py'):
        try:
            client.load_extension(f'src.cogs.{filename[:-3]}')
            print(f"[+] Loaded: src.cogs.{filename[:-3]}")
        except Exception as excl:
            print(
                f"[+] Unable to load: src.cogs.{filename[:-3]}  :  {excl}")


@client.event
async def on_message(message):
    if client.user == message.author:
        return
    await client.process_commands(message)

client.run(token)
