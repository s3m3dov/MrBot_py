#EN
import discord,random
from discord.ext import commands
from bot import client, get_prefix

class Member(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("BOT: Member extension is activated!")
    

    #Commands
    @commands.command(aliases=['8ball' , 'test', 'ask'])
    async def _8ball(self, ctx, *, question):
        _8b_responses = [' It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes - definitely.',
                'You may rely on it.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Don\'t count on it.',
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful.']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(_8b_responses)}')

def setup(client):
    client.add_cog(Member(client))
