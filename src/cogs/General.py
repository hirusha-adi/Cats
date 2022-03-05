import json
import os
import platform
import time
from datetime import datetime, timedelta

import discord
from discord.ext import commands
from src.utils.database import Embeds as EmbedsDB
from src.utils.database import Settings as SettingsDB


class General(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        self.client.remove_command('help')

        self.start_time = None

        with open(os.path.join(os.getcwd(), "database", "bot_website.json"), "r", encoding="utf-8") as jsondatafile:
            self.website_data = json.load(jsondatafile)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Discord.py API version: {discord.__version__}')
        print(f'Python version: {platform.python_version()}')
        print(f'Logged in as {self.client.user.name}')
        self.start_time = time.time()
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{SettingsDB.main['prefix']}help"))
        print('Bot is ready!')

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title="Response Time",
                              color=0xcb42f5,
                              timestamp=datetime.utcnow())
        embed.set_author(name=str(self.client.user.name),
                         icon_url=str(self.client.user.avatar_url))
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/877796755234783273/879311068097290320/PngItem_1526969.png")
        embed.add_field(
            name=f"Ping :timer:", value=f"{round(self.client.latency * 1000)} ms", inline=False)
        embed.set_footer(text=EmbedsDB.common["footer"].format(
            author_name=ctx.author.name))
        await ctx.send(embed=embed)

    @commands.command()
    async def uptime(self, ctx):
        current_time = time.time()()
        difference = int(round(current_time - self.start_time))
        text = str(timedelta(seconds=difference))

        embed = discord.Embed(title="Response Time",
                              color=0xcb42f5,
                              timestamp=datetime.utcnow())
        embed.set_author(name=str(self.client.user.name),
                         icon_url=str(self.client.user.avatar_url))
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/877796755234783273/879311068097290320/PngItem_1526969.png")
        embed.add_field(name="The bot was online for: ",
                        value=f":alarm_clock: {text}", inline=False)
        embed.set_footer(text=EmbedsDB.common["footer"].format(
            author_name=ctx.author.name))
        await ctx.send(embed=embed)

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def clean(self, ctx, amount=5):
        if amount <= 100:
            amttdel = amount + 1
            await ctx.channel.purge(limit=amttdel, check=lambda m: m.author == self.client.user)

            if str(amount) == "1":
                msgtxt = "message"
            else:
                msgtxt = "messages"

            embed = discord.Embed(title="Response Time",
                                  color=0xcb42f5,
                                  timestamp=datetime.utcnow())
            embed.set_author(name=str(self.client.user.name),
                             icon_url=str(self.client.user.avatar_url))
            embed.set_thumbnail(
                url="https: // cdn.discordapp.com/attachments/877796755234783273/947462345595162725/6652966_preview.png")
            embed.add_field(
                name="Action", value=f"Deleted {amount} {msgtxt} sent by {self.client.user.name}!", inline=False)
            embed.set_footer(text=EmbedsDB.common["footer"].format(
                author_name=ctx.author.name))
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(title="An Error has Occured",
                                  description="",
                                  color=0xcb42f5,
                                  timestamp=datetime.utcnow())
            embed.set_author(name=str(self.client.user.name),
                             icon_url=str(self.client.user.avatar_url))
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
            embed.set_footer(text=EmbedsDB.common["footer"].format(
                author_name=ctx.author.name))
            await ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title=f"{self.client.user.name}'s Functionalities",
                              description="Visit http://bot.cats.hirusha.xyz for additional information",
                              color=0xcb42f5,
                              timestamp=datetime.utcnow())
        embed.set_author(name=str(self.client.user.name),
                         icon_url=str(self.client.user.avatar_url))

        embed.add_field(
            name=f";help",
            value=f"Show this help message",
            inline=False)

        for k1, v1 in self.website_data["HELP"]["tables"][0]["Cat As A Service"]["table_rows"].items():
            if k1 == ";help":
                continue
            else:
                embed.add_field(
                    name=f"{k1}",
                    value=f"{v1}",
                    inline=False)

        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/877796755234783273/949508329863008256/PngItem_3861311.png")
        embed.set_footer(text=EmbedsDB.common["footer"].format(
            author_name=ctx.author.name))
        await ctx.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(General(client))
