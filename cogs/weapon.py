import discord
from discord.ext import commands
from discord.commands import Option
from data_rework.weapon_rework import weapon_view
from data.weaponary import weapon
from data_rework.archive import archive_view



class weaponary(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @discord.slash_command(name="archive_weapon",description="이 커맨드는 오직 일부유저만 호환됩니다...")
    async def old_weapon(self,ctx):
        await ctx.respond(view=archive_view())


    @discord.slash_command(name="weaponary_rework")
    async def weapon(self,ctx,
        text: Option(str,"옵션을 소르세요",choices=["button(삭제 예정)","select"])):
        if text == "select":
            await ctx.respond(view=weapon_view())
        if text == "button(삭제 예정)":
            await ctx.respond(view=weapon())
            await ctx.send("이기능은 삭제될 예정입니다..")

    @old_weapon.error
    async def old_weapon_er(self,ctx,error):
        await ctx.respond(error)
            
def setup(bot):
    bot.add_cog(weaponary(bot))
    
