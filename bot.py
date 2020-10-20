#EN
import discord, random, os, json
from discord.ext import commands, tasks 
from itertools import cycle

def get_prefix(client, message):    
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client  = commands.Bot(command_prefix = get_prefix)
token = "Njk2MDA3MjUwNDM4NzgyOTg2.Xoifsg.-nNBnCPeniPf7HiuQ8FhEeLuSHU"
status = cycle(['!!help', '#stayhome'])

@client.event
async def on_ready():
    change_status.start()
    print("Bot is online now.")

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(next(status)))

#Events
@client.event
async def on_command_error(ctx, error):
    if isinstance (error, commands.CommandNotFound):
        await ctx.send('Invalid command is used.')

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '!!'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

#Commands
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
        
    await ctx.send(f'Prefix changed to: **{prefix}**')



client.run(token)


"""
def is_it_me(ctx):
    return ctx.author.id == 546320585165111336
@client.command()
@commands.check(is_it_me)
async def example(ctx):
    await ctx.send(f'Hi, I am {ctx.author}')
"""