import os
import platform
from datetime import datetime

import aiohttp
import discord
import requests
import random
from discord.ext import commands
from src.utils.database import Embeds as EmbedsDB
from src.utils.database import Settings as SettingsDB


class TheCat(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    def saveImage(self, url: str):
        try:
            r = requests.get(url)
            with open("temp.png", "wb") as fimg:
                fimg.write(r.content)
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
    async def gif(self, ctx, *, text=None):
        if text is None:
            final_url = "https://cataas.com/cat/gif"
        else:
            final_url = f"https://cataas.com/cat/gif/says/{text}"

        if self.saveGIF(url=final_url):
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

    @commands.command()
    async def breed(self, ctx, *, text=None):
        url = "https://api.thecatapi.com/v1/breeds"

        async with aiohttp.ClientSession() as pornSession:
            async with pornSession.get(url) as jsondata:
                if not 300 > jsondata.status >= 200:
                    embed = discord.Embed(title="An Error has Occured",
                                          description="Bad status code from API",
                                          color=0xcb42f5,
                                          timestamp=datetime.utcnow())
                    embed.set_author(name=str(self.client.user.name),
                                     icon_url=str(self.client.user.avatar_url))
                    embed.set_thumbnail(
                        url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                    embed.set_footer(text=EmbedsDB.common["footer"].format(
                        author_name=ctx.author.name), icon_url=str(ctx.author.avatar_url))
                    await ctx.send(embed=embed)

                try:
                    result = await jsondata.json()
                except Exception as e:
                    embed = discord.Embed(title="An Error has Occured",
                                          description=f"Unable to convert fetched data to JSON from API: {e}",
                                          color=0xcb42f5,
                                          timestamp=datetime.utcnow())
                    embed.set_author(name=str(self.client.user.name),
                                     icon_url=str(self.client.user.avatar_url))
                    embed.set_thumbnail(
                        url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
                    embed.set_footer(text=EmbedsDB.common["footer"].format(
                        author_name=ctx.author.name), icon_url=str(ctx.author.avatar_url))
                    await ctx.send(embed=embed)

        data = result[random.randint(1, len(result) - 1)]

        embed = discord.Embed(title=f"{data['name']}",
                              description=f"{data['description']}",
                              color=0xcb42f5,
                              timestamp=datetime.utcnow())
        embed.set_author(name=str(self.client.user.name),
                         icon_url=str(self.client.user.avatar_url))
        embed.set_image(url=f"{data['image']['url']}")
        embed.add_field(name="Links",
                        value=f"CFA: {data['cfa_url']}\nVetStreet: {data['vetstreet_url']}\nVCA Hospitals: {data['vcahospitals_url']}",
                        inline=False)
        embed.add_field(name="Temperament",
                        value=f"{data['temperament']}",
                        inline=False)
        embed.add_field(name="Country Of Origin",
                        value=f"Origin: {data['origin']}\nCountry Code: {data['country_code']}",
                        inline=False)
        embed.add_field(name="Lifespan",
                        value=f"{data['life_span']}",
                        inline=False)
        embed.add_field(name="Wikipedia",
                        value=f"{data['wikipedia_url']}",
                        inline=False)
        embed.add_field(name="Stats 1",
                        value=f"Indoor: {data['indoor']}\nLap: {data['lap']}\nAdaptability: {data['adaptability']}\nAffection Level: {data['affection_level']}\nChild Friendly: {data['child_friendly']}\nDog Friendly: {data['dog_friendly']}\nEnergy Level: {data['energy_level']}\nGrooming: {data['grooming']}",
                        inline=False)
        embed.add_field(name="Stats 2",
                        value=f"Health Issues: {data['health_issues']}\nIntelligence: {data['intelligence']}\nShedding Level: {data['shedding_level']}\nSocial Needs: {data['social_needs']}\nStranger Friendly: {data['stranger_friendly']}\nVocalisation: {data['vocalisation']}\nExperimental: {data['experimental']}",
                        inline=False)
        embed.set_footer(text=EmbedsDB.common["footer"].format(
            author_name=ctx.author.name), icon_url=str(ctx.author.avatar_url))
        await ctx.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(TheCat(client))
