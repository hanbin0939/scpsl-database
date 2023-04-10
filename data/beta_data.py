import discord
from discord.ext import commands
token = "MTA4MzYyNDg4MDA3NzAxMzA5Mw.GSXwaW.6vjcRQZO9MOPBxoZi7ojYOnMDDGP3qw7YNuN-g"


class weapon(discord.ui.View):
        @discord.ui.button(label="com-15", style=discord.ButtonStyle.success)
        async def com_15(self, button, interaction):
            embed = discord.Embed(title="com-15", description="기본적인 호신용권총", color=0xadadad)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/22/COM-15Icon.png/375px-COM-15Icon.png")
            embed.set_image(url='https://hub.scpslgame.com/images/e/e8/COM-15_Inspect_Animation.gif')
            embed.set_footer(text='| 기본대미지=25\n| 해드샷대미지=50')
            await interaction.response.edit_message(embed=embed,view=attachment())

        @discord.ui.button(label="com-18", style=discord.ButtonStyle.success)
        async def com_18(self, button, interaction):
            embed = discord.Embed(title='COM-18', description="기본적인 호신용 권총", color=0x575757)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/2/2e/IconCom18.png/375px-IconCom18.png')
            embed.set_footer(text='기본대미지=20\n최대대미지=70\n',icon_url=('https://hub.scpslgame.com/images/thumb/3/3f/WEAPONCATNEW3.png/180px-WEAPONCATNEW3.png'))
            embed.set_author(name='weapon',icon_url=("https://hub.scpslgame.com/images/thumb/7/75/GuardIcon.png/180px-GuardIcon.png"))
            await interaction.response.edit_message(embed=embed,view=attachmant_com_18())

        @discord.ui.button(label="corssvec", style=discord.ButtonStyle.success)
        async def crossvec(self,button,interaction):
            embed = discord.Embed(title='Crossvec',url="https://en.scpslgame.com/index.php?title=Crossvec",description=str('구미호 병사의 표준 기관단총'),color=0x1700ff)
            embed.set_author(name='Lunae Defence',icon_url='https://hub.scpslgame.com/images/thumb/0/09/LunaeLogo.png/300px-LunaeLogo.png')
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/f/f0/CrossvecIcon.png/375px-CrossvecIcon.png')
            embed.set_image(url='https://hub.scpslgame.com/images/0/09/Crossvec_Equip_Animation.gif')
            embed.set_footer(text='기본피해량=24\n최대피해량=약84',icon_url='https://hub.scpslgame.com/images/thumb/4/46/Icon9x19mm.png/53px-Icon9x19mm.png')
            await interaction.response.edit_message(embed=embed,view=attachmant_corssvec())



class attachment(discord.ui.View):
    @discord.ui.button(label='소음기', style=discord.ButtonStyle.gray)
    async def sp(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="Suppressor",description=str('''총알 정확도:+25%\n총소리:-60%\n준비시간:+0.17/s\n길이:+94\n무게:+46%'''))
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/c/cd/COM-15Suppressor.png/180px-COM-15Suppressor.png')
        await interaction.response.edit_message(embed=embed)
    @discord.ui.button(label='17발 탄창', style=discord.ButtonStyle.gray)
    async def big_mag(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title='Extended MAG',description='''ammo + 5\n준비시간:+0.06/s\n무게:+46%''')
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/5/54/COM-15ExtendedMag.png/90px-COM-15ExtendedMag.png')
        await interaction.response.edit_message(embed=embed)
    @discord.ui.button(label='go back', style=discord.ButtonStyle.gray)
    async def go_back(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="COM-15", description="기본적인 호신용권총", color=0xadadad)
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/2/22/COM-15Icon.png/375px-COM-15Icon.png')
        embed.set_image(url='https://hub.scpslgame.com/images/e/e8/COM-15_Inspect_Animation.gif')
        embed.set_author(name='weapon')
        embed.set_footer(text='| 기본대미지=25\n| 해드샷대미지=50',icon_url='https://hub.scpslgame.com/images/thumb/3/3f/WEAPONCATNEW3.png/180px-WEAPONCATNEW3.png')
        await interaction.response.edit_message(embed=embed,view=attachment())
    @discord.ui.button(label='go home', style=discord.ButtonStyle.gray)
    async def go_home(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.edit_message(view=weapon())

class attachmant_com_18(discord.ui.View):
    @discord.ui.button(label='소음기', style=discord.ButtonStyle.gray)
    async def supessor(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="소음기")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/0/06/COM18Suppressor.png/195px-COM18Suppressor.png")
        embed.add_field(name="총알정확도",value="+25%")
        embed.add_field(name="총소리",value="-60%")
        embed.add_field(name="준비시간",value="+0.09/s")
        embed.add_field(name="길이",value="+92%")
        embed.add_field(name="weight",value="+49%")
        await interaction.response.edit_message(embed=embed,view=attachmant_com_18())
    @discord.ui.button(label="heavy barrel",style=discord.ButtonStyle.success)
    async def heavy_barrel(self,button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="heavy barrel")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/b/ba/COM18Heavy.png")
        embed.add_field(name="damage",value="+15%")
        embed.add_field(name="관총력",value="+25%")
        embed.add_field(name="총알정확도",value="+11%")
        embed.add_field(name="준비시간",value="+0.09/s")
        embed.add_field(name="발사속도",value="-35%")
        embed.add_field(name="길이",value="+45%")
        embed.add_field(name="weight",value="+69%")
        await interaction.response.edit_message(embed=embed,view=attachmant_com_18())
    @discord.ui.button(label="레이저 사이트",style=discord.ButtonStyle.success)
    async def lazer_sight(self,button:discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="lazer sight")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/6/69/COM18Laser.png")
        embed.add_field(name="지향사격 정확도:",value="+233%")
        embed.add_field(name="준비시간:",value="+233%")
        embed.add_field(name="지향사격 정확도:",value="+0.03/s")
        embed.add_field(name="무게:",value="+28%")
        await interaction.response.edit_message(embed=embed,view=attachmant_com_18())
    @discord.ui.button(label="레이저 사이트",style=discord.ButtonStyle.success)
    async def jhpx15(self,button:discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="jhp mag")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/4/4a/Mag15JHP.png/50px-Mag15JHP.png")
        embed.add_field(name="데미지:",value="+20%")
        embed.add_field(name="관통력:",value="-70%")
        await interaction.response.edit_message(embed=embed,view=attachmant_com_18())
    @discord.ui.button(label='go back', style=discord.ButtonStyle.gray)
    async def go_back(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title='COM-18', description="기본적인 호신용 권총", color=0x575757)
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/2/2e/IconCom18.png/375px-IconCom18.png')
        embed.set_footer(text='기본대미지=20\n최대대미지=70\n',icon_url=('https://hub.scpslgame.com/images/thumb/3/3f/WEAPONCATNEW3.png/180px-WEAPONCATNEW3.png'))
        embed.set_author(name='weapon',icon_url=("https://hub.scpslgame.com/images/thumb/7/75/GuardIcon.png/180px-GuardIcon.png"))
        await interaction.response.edit_message(embed=embed,view=attachmant_com_18())
    @discord.ui.button(label='go home', style=discord.ButtonStyle.gray)
    async def go_home(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.edit_message(view=weapon())

    
class attachmant_corssvec(discord.ui.View):
    @discord.ui.button(label="홀로그램 조준경",style=discord.ButtonStyle.success)
    async def holo_crossvec(self,button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="홀로그램 사이트")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/b/b5/CrossvecHoloSight.png/80px-CrossvecHoloSight.png")
        embed.add_field(name="배율:",value="1.05x")
        embed.add_field(name="무게:",value="+17%")
        await interaction.response.edit_message(embed=embed,view=attachmant_corssvec())
    @discord.ui.button(label="go back",style=discord.ButtonStyle.success)
    async def go_back(self,button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title='Crossvec',url="https://en.scpslgame.com/index.php?title=Crossvec",description=str('구미호 병사의 표준 기관단총'),color=0x1700ff)
        embed.set_author(name='Lunae Defence',icon_url='https://hub.scpslgame.com/images/thumb/0/09/LunaeLogo.png/300px-LunaeLogo.png')
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/f/f0/CrossvecIcon.png/375px-CrossvecIcon.png')
        embed.set_image(url='https://hub.scpslgame.com/images/0/09/Crossvec_Equip_Animation.gif')
        embed.set_footer(text='기본피해량=24\n최대피해량=약84',icon_url='https://hub.scpslgame.com/images/thumb/4/46/Icon9x19mm.png/53px-Icon9x19mm.png')
        await interaction.response.edit_message(embed=embed,view=attachmant_corssvec())
    @discord.ui.button(label="go home",style=discord.ButtonStyle.success)
    async def go_home(self,button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.edit_message(view=weapon())


