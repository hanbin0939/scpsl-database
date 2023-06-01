import discord
from discord.ext import commands
from data_rework.weapon_rework import weapon_view

class weaponary(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @discord.slash_command(name="weaponary")
    async def weapon(self,ctx):
        await ctx.respond(view=weapon_view())

def setup(bot):
    bot.add_cog(weaponary(bot))
    
