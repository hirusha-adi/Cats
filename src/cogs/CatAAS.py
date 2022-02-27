import os
import platform
import requests
from datetime import datetime


import discord
from discord.ext import commands

from src.utils.database import Embeds as EmbedsDB
from src.utils.database import Settings as SettingsDB


class CatAAS(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    def saveImage(self, url: str):
        try:
            r = requests.get(url).content
            with open("temp.png", "wb") as fimg:
                fimg.write(r)
            return True
        except:
            return False

    def saveGIF(self, url: str):
        try:
            r = requests.get(url).content
            with open("temp.gif", "wb") as fimg:
                fimg.write(r)
            return True
        except:
            return False

    def removeImage(self, filename: str = "temp.png"):
        os.system("rm -rf ./{delfname}".format(delfname=filename))

    @commands.command()
    async def cat(self, ctx):
        if self.saveImage(url="https://cataas.com/cat"):
            file = discord.File(f'temp.png', filename="temp.png")
            embed = discord.Embed(title="a Cat",
                                  color=0xcb42f5,
                                  timestamp=datetime.utcnow())
            embed.set_author(name=str(self.client.user.name),
                             icon_url=str(self.client.user.avatar_url))
            embed.set_image(url="attachment://temp.png")
            embed.set_footer(text=EmbedsDB.common["footer"].format(
                author_name=ctx.author.name), icon_url=str(ctx.author.avatar_url))
            await ctx.send(file=file, embed=embed)

            self.removeImage(filename="temp.png")

        else:
            embed = discord.Embed(title="An Error has Occured",
                                  description="Unable to load the Image from the API",
                                  color=0xcb42f5,
                                  timestamp=datetime.utcnow())
            embed.set_author(name=str(self.client.user.name),
                             icon_url=str(self.client.user.avatar_url))
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed.set_footer(text=EmbedsDB.common["footer"].format(
                author_name=ctx.author.name), icon_url=str(ctx.author.avatar_url))
            await ctx.send(embed=embed)

    @commands.command()
    async def gif(self, ctx):
        if self.saveGIF(url="https://cataas.com/cat/gif"):
            file = discord.File(f'temp.gif', filename="temp.gif")
            embed = discord.Embed(title="a Cat",
                                  color=0xcb42f5,
                                  timestamp=datetime.utcnow())
            embed.set_author(name=str(self.client.user.name),
                             icon_url=str(self.client.user.avatar_url))
            embed.set_image(url="attachment://temp.gif")
            embed.set_footer(text=EmbedsDB.common["footer"].format(
                author_name=ctx.author.name), icon_url=str(ctx.author.avatar_url))
            await ctx.send(file=file, embed=embed)

            self.removeImage(filename="temp.gif")

        else:
            embed = discord.Embed(title="An Error has Occured",
                                  description="Unable to load the GIF from the API",
                                  color=0xcb42f5,
                                  timestamp=datetime.utcnow())
            embed.set_author(name=str(self.client.user.name),
                             icon_url=str(self.client.user.avatar_url))
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed.set_footer(text=EmbedsDB.common["footer"].format(
                author_name=ctx.author.name), icon_url=str(ctx.author.avatar_url))
            await ctx.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(CatAAS(client))
