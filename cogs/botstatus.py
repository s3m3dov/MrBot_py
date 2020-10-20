#EN
import discord
from discord.ext import commands
from bot import client

zaza=client


class BotStatus(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    #events
    @commands.Cog.listener()
    async def on_ready(self):
        print("BOT: BotStatus extension is activated")
    
    #commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f':ping_pong: Pong! **{round(zaza.latency*1000)}ms**')

def setup(client):
    client.add_cog(BotStatus(client))