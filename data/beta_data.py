import discord
from discord.ext import commands



class weapon(discord.ui.View):
        @discord.ui.button(label="com-15", style=discord.ButtonStyle.success)
        async def com_15(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="com-15", description="기본적인 호신용권총", color=0xadadad)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/22/COM-15Icon.png/375px-COM-15Icon.png")
            embed.set_image(url='https://hub.scpslgame.com/images/e/e8/COM-15_Inspect_Animation.gif')
            embed.set_footer(text='| 기본대미지=25\n| 해드샷대미지=50')
            await interaction.response.edit_message(embed=embed,view=attachment())

        @discord.ui.button(label="com-18", style=discord.ButtonStyle.success)
        async def com_18(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='COM-18', description="기본적인 호신용 권총", color=0x575757)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/2/2e/IconCom18.png/375px-IconCom18.png')
            embed.set_footer(text='기본대미지=20\n최대대미지=70\n',icon_url=('https://hub.scpslgame.com/images/thumb/3/3f/WEAPONCATNEW3.png/180px-WEAPONCATNEW3.png'))
            embed.set_author(name='weapon',icon_url=("https://hub.scpslgame.com/images/thumb/7/75/GuardIcon.png/180px-GuardIcon.png"))
            await interaction.response.edit_message(embed=embed,view=attachmant_com_18())

        @discord.ui.button(label="corssvec", style=discord.ButtonStyle.success)
        async def crossvec(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='Crossvec',url="https://en.scpslgame.com/index.php?title=Crossvec",description=str('구미호 병사의 표준 기관단총'),color=0x1700ff)
            embed.set_author(name='Lunae Defence',icon_url='https://hub.scpslgame.com/images/thumb/0/09/LunaeLogo.png/300px-LunaeLogo.png')
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/f/f0/CrossvecIcon.png/375px-CrossvecIcon.png')
            embed.set_image(url='https://hub.scpslgame.com/images/0/09/Crossvec_Equip_Animation.gif')
            embed.set_footer(text='기본피해량=24\n최대피해량=약84',icon_url='https://hub.scpslgame.com/images/thumb/4/46/Icon9x19mm.png/53px-Icon9x19mm.png')
            await interaction.response.edit_message(embed=embed,view=attachmant_corssvec())

        @discord.ui.button(label="ebsillon-11-SR",style=discord.ButtonStyle.success)
        async def ebsillon(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='MTF-E11-SR',url="https://en.scpslgame.com/index.php?title=MTF-E11-SR",description='구미호 표준 장비',color=0x1700ff)
            embed.set_author(name='Lunae Defence',icon_url='https://hub.scpslgame.com/images/thumb/0/09/LunaeLogo.png/300px-LunaeLogo.png')
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/9/96/E11SRIcon.png/375px-E11SRIcon.png')
            embed.set_image(url='https://hub.scpslgame.com/images/2/23/E-11_Inspect_Animation.gif')
            embed.set_footer(text='|Fire Rate:570\n|Damage Falloff:100m\n|Equip Time:0.73s\n|Pick-Up Time:0.8s\n|Weight:3.15kg\n|Length:87cm\n|Bullet Accuracy:0.05°\n|Hip Fire Accuracy:2°\n|aming accuracy:0.08°(with Bullet Accuracy)~0.13° (with Bullet Accuracy)',icon_url='https://hub.scpslgame.com/images/thumb/d/d7/Icon556x45.png/53px-Icon556x45.png')
            await interaction.response.edit_message(embed=embed,view=e_11_attachment())

        @discord.ui.button(label="AK",style=discord.ButtonStyle.success)
        async def ak(self, button:discord.ui.Button, interaction: discord.Integration):
            embed = discord.Embed(title="AK",description="혼돈의 반란 소충수의 표준무기",color=0x008F1C)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/3/33/NewAKIcon.png/375px-NewAKIcon.png")
            embed.set_image(url="https://hub.scpslgame.com/images/thumb/2/2f/AK_Render_2.jpg/1353px-AK_Render_2.jpg")



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
    @discord.ui.button(label="야간 조준경",style=discord.ButtonStyle.success)
    async def nw_crossvec(self,button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="야간조준경")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/24/CrossvecNightVision.png/80px-CrossvecNightVision.png")
        embed.add_field(name="배율:",value="1.85x")
        embed.add_field(name="무게:",value="+17%")
        embed.add_field(name="조준속도:",value="-25%")
        embed.add_field(name="준비시간",value="+0.22/s")
        embed.add_field(name="무게",value="+47%")
        await interaction.response.edit_message(embed=embed,view=attachmant_corssvec())
    @discord.ui.button(label="헤비베럴",style=discord.ButtonStyle.success)
    async def heavy_barrel(self,button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="extented berrel")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/4/4b/CrossvecBarrelLong.png/150px-CrossvecBarrelLong.png")
        embed.add_field(name="데미지",value="+5%")
        embed.add_field(name="관통력",value="+10%")
        embed.add_field(name="총알 정확도",value="+43%")
        embed.add_field(name="준비시간",value="+0.32/s")
        embed.add_field(name="길이",value="+35%")
        embed.add_field(name="무게",value="+23%")
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

class e_11_attachment(discord.ui.View):
    @discord.ui.button(label="Go home",style=discord.ButtonStyle.success)
    async def go_home(self,button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.edit_message(view=weapon())
        
    @discord.ui.button(label='홀호그램 조준경', style=discord.ButtonStyle.success)
    async def hs(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title='holograpic sight',color=0x1700ff)
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/7/7b/Holo_E11.png/75px-Holo_E11.png')
        embed.add_field(name='zoom:',value="1.05x")
        embed.add_field(name='무게:',value='+13%')
        await interaction.response.edit_message(embed=embed,view=e_11_attachment())

    @discord.ui.button(label='야간 조준경', style=discord.ButtonStyle.success)
    async def nvs(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title='night vision sight',color=0x1700ff)
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/b/bc/NV_E11.png/150px-NV_E11.png')
        embed.add_field(name='zoom:',value="3.3x")
        embed.add_field(name='조준속도:',value="-25%")
        embed.add_field(name='무게:',value='+35%')
        await interaction.response.edit_message(embed=embed,view=e_11_attachment())

    @discord.ui.button(label="드럼 탄창",style=discord.ButtonStyle.success)
    async def mag65(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="X65 FMJ mag")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/a/a1/Mag65FMJ.png/90px-Mag65FMJ.png")
        embed.add_field(name="탄약수용양",value="+25")
        embed.add_field(name="장전시간",value="+2/s")
        embed.add_field(name="weight",value="+79%")
        await interaction.response.edit_message(embed=embed,view=e_11_attachment())

    @discord.ui.button(label="Recoil-Reducing Stock",style=discord.ButtonStyle.success)
    async def mag65(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="Recoil-Reducing Stock")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/3/36/ShockStock.png/150px-ShockStock.png")
        embed.add_field(name="조준사격반동",value="-33.3")
        embed.add_field(name="길이",value="-1%")
        embed.add_field(name="준비시간",value="+0.08/s")
        embed.add_field(name="weight",value="+22%")
        await interaction.response.edit_message(embed=embed,view=e_11_attachment())

