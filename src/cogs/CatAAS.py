import os
import platform
from datetime import datetime

import discord
from discord.ext import commands

from src.utils.database import Embeds as EmbedsDB
from src.utils.database import Settings as SettingsDB


class CatAAS(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def cat(self, ctx):
        embed = discord.Embed(title="a Cat",
                              color=0xcb42f5,
                              timestamp=datetime.utcnow())
        embed.set_author(name=str(self.client.user.name),
                         icon_url=str(self.client.user.avatar_url))
        embed.set_thumbnail(url="https://cataas.com/cat")
        embed.set_footer(text=EmbedsDB.common["footer"].format(
            author_name=ctx.author.name))
        await ctx.send(embed=embed)

    # @commands.command()
    # async def clean(self, ctx, amount=5):
    #     if amount <= 100:
    #         pass

    #     else:
    #         embed = discord.Embed(title="An Error has Occured",
    #                               description="",
    #                               color=0xcb42f5,
    #                               timestamp=datetime.utcnow())
    #         embed.set_author(name=str(self.client.user.name),
    #                          icon_url=str(self.client.user.avatar_url))
    #         embed.set_thumbnail(
    #             url="https://cdn.discordapp.com/attachments/877796755234783273/879298565380386846/sign-red-error-icon-1.png")
    #         embed.set_footer(text=EmbedsDB.common["footer"].format(
    #             author_name=ctx.author.name))
    #         await ctx.send(embed=embed)


def setup(client: commands.Bot):
    client.add_cog(CatAAS(client))
