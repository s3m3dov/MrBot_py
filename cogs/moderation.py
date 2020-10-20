#EN
import discord, json
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("BOT: Moderation extension is activated!")

    #Commands
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'**{amount}** messages have been deleted!')
        
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send('Please specify an amount of messages to delete.')

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)


    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')


    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member : discord.Member):
        guild = ctx.guild

        for role in guild.roles:
            if role.name == 'Muted':
                await member.add_roles(role)
                await ctx.send(f'{member.mention} has been muted by {ctx.author.mention}.')
                return

                overwrite = discord.PermissionOverwrite(send_messages=False)
                newRole = await guild.create_role(name="Muted")

                for channel in guild.text_channels:
                    await channel.set_permissions(newRole, overwrite=overwrite)
                
                await member.add_roles(newRole)
                await ctx.send(f'{member.mention} has been muted by {ctx.author.mention}.')


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member : discord.Member):
        guild = ctx.guild

        for role in guild.roles:
            if role.name == "Muted":
                await member.remove_roles(role)
                await ctx.send(f'{member.mention} has been unmuted by {ctx.author.mention}.')
                return




def setup(client):
    client.add_cog(Moderation(client))