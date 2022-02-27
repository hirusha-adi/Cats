import os
import platform
import time
from datetime import datetime, timedelta

import discord
from discord.ext import commands

from src.utils.database import Embeds as EmbedsDB


class General(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

        self.client.remove_command('help')

        self.start_time = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Discord.py API version: {discord.__version__}')
        print(f'Python version: {platform.python_version()}')
        print(f'Logged in as {self.client.user.name}')
        self.start_time = time.time()
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f";help"))
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
