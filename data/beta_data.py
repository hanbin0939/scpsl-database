import discord
from discord.ext import commands
from data.scp_data import skill_079,Button_173
        

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
        
        @discord.ui.button(label="FSP-9", style=discord.ButtonStyle.success)
        async def fsp_9(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="fsp-9",description="시설경비의 기본무기",color=0x5B6370)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/4/4d/FSP-9Icon.png/375px-FSP-9Icon.png")
            await interaction.response.edit_message(embed=embed,view=weapon())
            

        @discord.ui.button(label="corssvec", style=discord.ButtonStyle.success)
        async def crossvec(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='Crossvec',url="https://en.scpslgame.com/index.php?title=Crossvec",description=str('구미호 병사의 표준 기관단총'),color=0x70C3FF)
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
            await interaction.response.edit_message(embed=embed,view=e_11_attachment())

        @discord.ui.button(label="AK",style=discord.ButtonStyle.success)
        async def ak(self, button:discord.ui.Button, interaction: discord.Integration):
            embed = discord.Embed(title="AK",description="혼돈의 반란 소충수의 표준무기",color=0x008F1C)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/3/33/NewAKIcon.png/375px-NewAKIcon.png")
            embed.set_image(url="https://hub.scpslgame.com/images/thumb/2/2f/AK_Render_2.jpg/1353px-AK_Render_2.jpg")
            await interaction.response.edit_message(embed=embed,view=weapon())

        @discord.ui.button(label="logicer",style=discord.ButtonStyle.success)
        async def ak(self, button:discord.ui.Button, interaction: discord.Integration):
            embed = discord.Embed(title="logicer",description="혼돈의 반란 기관총",color=0x0D7D35)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/d/d4/LogicerIcon.png/250px-LogicerIcon.png")
            embed.set_image(url="https://hub.scpslgame.com/images/2/23/Logicer_Inspect_New.gif")
            await interaction.response.edit_message(embed=embed,view=logicar_attachment())

        @discord.ui.button(label="shoutgun",style=discord.ButtonStyle.success)
        async def shoutgun(self, button:discord.ui.Button, interaction: discord.Integration):
            embed = discord.Embed(title="shoutgun",description="혼돈의 반란의 산탄총",color=0x006826)
            embed.set_author(name="chaous insergency",icon_url="https://hub.scpslgame.com/images/thumb/e/ef/ChaosIcon.png/120px-ChaosIcon.png",url="https://en.scpslgame.com/index.php?title=Chaos_Insurgent#Marauder%20")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/e/ee/ShotgunIcon.png/375px-ShotgunIcon.png")
            embed.set_image(url="https://hub.scpslgame.com/images/1/17/Shotgun_Inspect_New.gif")
            await interaction.response.edit_message(embed=embed,view=shoutgun_attachment())



class shoutgun_attachment(discord.ui.View):
    @discord.ui.button(label="double-shot-system",style=discord.ButtonStyle.green)
    async def dbs(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="Double shot system",description="super shoutgun",color=0x006826)
        embed.set_author(name="chaous insergency",icon_url="https://hub.scpslgame.com/images/thumb/e/ef/ChaosIcon.png/120px-ChaosIcon.png",url="https://en.scpslgame.com/index.php?title=Chaos_Insurgent#Marauder%20")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/a/af/TriggerDouble.png/80px-TriggerDouble.png")
        embed.add_field(name="특수기능",value="**2발이 즉시 발사됩니다!**")
        embed.add_field(name="발사속도",value="-40%")
        embed.add_field(name="패턴 일관성",value="-35%")
        await interaction.response.edit_message(embed=embed,view=shoutgun_attachment())

    @discord.ui.button(label="Extended Barrel",style=discord.ButtonStyle.green)
    async def berrel_shoutgun(self,button: discord.ui.Button,interaction: discord.Interaction):
        embed = discord.Embed(title="Extended Barrel",description="관통력을 늘려줍니다.",color=0x006826)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/d/d9/ShotgunLongBarrel.png/150px-ShotgunLongBarrel.png")
        embed.add_field(name="Penetration ",value="+100%")
        embed.add_field(name="Pellet Spread ",value="-10%")
        embed.add_field(name="Length ",value="+17%")
        embed.add_field(name="Weight ",value="+23%")
        await interaction.response.edit_message(embed=embed,view=shoutgun_attachment())
    @discord.ui.button(label="Laser Sight",style=discord.ButtonStyle.green)
    async def lazer_shoutgun(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="Laser Sight",description="지향사격 정확도를 높혀줍니다.")
        embed.add_field(name="지향사격 정확도 ",value="+100%")
        embed.add_field(name="Weight ",value="+5%")
        await interaction.response.edit_message(embed=embed,view=shoutgun_attachment())
    @discord.ui.button(label="go home",style=discord.ButtonStyle.green)
    async def go_home(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.edit_message(view=weapon())


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
        embed = discord.Embed(title="홀로그램 사이트",color=0x70C3FF)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/b/b5/CrossvecHoloSight.png/80px-CrossvecHoloSight.png")
        embed.add_field(name="배율:",value="1.05x")
        embed.add_field(name="무게:",value="+17%")
        await interaction.response.edit_message(embed=embed,view=attachmant_corssvec())
    @discord.ui.button(label="야간 조준경",style=discord.ButtonStyle.success)
    async def nw_crossvec(self,button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="야간조준경",color=0x70C3FF)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/24/CrossvecNightVision.png/80px-CrossvecNightVision.png")
        embed.add_field(name="배율:",value="1.85x")
        embed.add_field(name="무게:",value="+17%")
        embed.add_field(name="조준속도:",value="-25%")
        embed.add_field(name="준비시간",value="+0.22/s")
        embed.add_field(name="무게",value="+47%")
        await interaction.response.edit_message(embed=embed,view=attachmant_corssvec())
    @discord.ui.button(label="헤비베럴",style=discord.ButtonStyle.success)
    async def heavy_barrel(self,button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="extented berrel",color=0x70C3FF)
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
        embed = discord.Embed(title='Crossvec',url="https://en.scpslgame.com/index.php?title=Crossvec",description=str('구미호 병사의 표준 기관단총'),color=0x70C3FF)
        embed.set_author(name='Lunae Defence',icon_url='https://hub.scpslgame.com/images/thumb/0/09/LunaeLogo.png/300px-LunaeLogo.png')
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/f/f0/CrossvecIcon.png/375px-CrossvecIcon.png')
        embed.set_image(url='https://hub.scpslgame.com/images/0/09/Crossvec_Equip_Animation.gif')
        embed.set_footer(text='기본피해량=24\n최대피해량=약84',icon_url='https://hub.scpslgame.com/images/thumb/4/46/Icon9x19mm.png/53px-Icon9x19mm.png')
        await interaction.response.edit_message(embed=embed,view=attachmant_corssvec())

    @discord.ui.button(label="소음기",style=discord.ButtonStyle.success)
    async def crossvec_suppressor(self,button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="소음기",description="총소리를 줄여줍니다.",color=0x70C3FF)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/4/4a/CrossvecBarrelSupp.png/180px-CrossvecBarrelSupp.png")
        embed.add_field(name="총소리",value="-65%")
        embed.add_field(name="총알정확도",value="+25%")
        embed.add_field(name="준비시간",value="+0.32/s")
        embed.add_field(name="길이",value="+29%")
        embed.add_field(name="무게",value="+13%")
        await interaction.response.edit_message(embed=embed,view=attachmant_corssvec())

    @discord.ui.button(label="go home",style=discord.ButtonStyle.red)
    async def go_home(self,button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.edit_message(view=weapon())

class e_11_attachment(discord.ui.View):
    @discord.ui.button(label="Go home",style=discord.ButtonStyle.gray)
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
        embed = discord.Embed(title="X65 FMJ mag",color=0x1700ff)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/a/a1/Mag65FMJ.png/90px-Mag65FMJ.png")
        embed.add_field(name="탄약수용양",value="+25")
        embed.add_field(name="장전시간",value="+2/s")
        embed.add_field(name="weight",value="+79%")
        await interaction.response.edit_message(embed=embed,view=e_11_attachment())

    @discord.ui.button(label="손잡이",style=discord.ButtonStyle.success)
    async def grip_e_11(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="Foregrip",color=0x1700ff)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/c/c8/GripE11.png/60px-GripE11.png")
        embed.add_field(name="반동",value="-33.3")
        embed.add_field(name="조준속도",value="-15%")
        embed.add_field(name="weight",value="+8%")
        await interaction.response.edit_message(embed=embed,view=e_11_attachment())
    
    @discord.ui.button(label="Recoil-Reducing Stock	",style=discord.ButtonStyle.success)
    async def recoilstock_e_11(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="Recoil-Reducing Stock",color=0x1700ff)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/3/36/ShockStock.png/150px-ShockStock.png")
        embed.add_field(name="조준사격반동",value="-33.3")
        embed.add_field(name="길이",value="-1%")
        embed.add_field(name="준비시간",value="+0.08/s")
        embed.add_field(name="weight",value="+22%")
        await interaction.response.edit_message(embed=embed,view=e_11_attachment())
    
    @discord.ui.button(label="레이저 사이트",style=discord.ButtonStyle.success)
    async def lz_e_11(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="Laser Sight",color=0x1700ff)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/a/ac/LaserE11.png/60px-LaserE11.png")
        embed.add_field(name="지향사격정확도",value="+100.0%")
        embed.add_field(name="weight",value="+11%")
        await interaction.response.edit_message(embed=embed,view=e_11_attachment())

    @discord.ui.button(label="rife body",style=discord.ButtonStyle.success)
    async def rife_body(self,buttom: discord.ui.Button, interaction: discord.Integration):
        embed = discord.Embed(title="Rife body",description="조준사격 정확도를 늘려줍니다.",color=0x1700ff)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/28/RifleBody.png/150px-RifleBody.png")
        embed.add_field(name="데미지:",value="+7.5%")
        embed.add_field(name="관통력:",value="+12.5%")
        embed.add_field(name="발사속도:",value="-10%")
        embed.add_field(name="준비시간:",value="+0.13/s")
        embed.add_field(name="지향사격 정확도:",value="-26%")
        embed.add_field(name="길이",value="+20%")
        embed.add_field(name="무게",value="+46%")
        await interaction.response.edit_message(embed=embed,view=e_11_attachment())
    @discord.ui.button(label="muzzle brake",style=discord.ButtonStyle.success)
    async def muzzle_brake(self,buttom: discord.ui.Button, interaction: discord.Integration):
        embed = discord.Embed(title="muzzle brake",description="반동을 줄여줍니다.",color=0x1700ff)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/b/b3/MuzzleBrake_0.png/60px-MuzzleBrake_0.png")
        embed.add_field(name="반동:",value="-10%")
        embed.add_field(name="준비시간:",value="+0.13/s")
        embed.add_field(name="지향사격 정확도:",value="-26%")
        embed.add_field(name="길이",value="+20%")
        embed.add_field(name="무게",value="+46%")
class logicar_attachment(discord.ui.View):
    @discord.ui.button(label="Go home",style=discord.ButtonStyle.gray)
    async def go_home(self,button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.edit_message(view=weapon())
    @discord.ui.button(label="Red dot",style=discord.ButtonStyle.success)
    async def lg_reddot(self,buttom: discord.ui.Button, interaction: discord.Integration):
        embed = discord.Embed(title="Red dot sight",color=0x0D7D35)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/4/41/LogicerDotSight.png/90px-LogicerDotSight.png")
        embed.add_field(name="배울",value="1.05x")
        embed.add_field(name="무게",value="+2%")
        await interaction.response.edit_message(embed=embed,view=logicar_attachment())
    @discord.ui.button(label="NV scope",style=discord.ButtonStyle.success)
    async def nv_scope(self,buttom: discord.ui.Button, interaction: discord.Integration):
        embed = discord.Embed(title="야간 조준경",description="3배율 야간 조준경",color=0x0D7D35)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/29/LogicerScopeNV.png/90px-LogicerScopeNV.png")
        embed.add_field(name="zoom",value="2.25x")
        embed.add_field(name="조준속도",value="-25%")
        embed.add_field(name="무게",value="+12%")
        await interaction.response.edit_message(embed=embed,view=logicar_attachment())
    @discord.ui.button(label="muzzle brake",style=discord.ButtonStyle.success)
    async def muzzle_brake(self,buttom: discord.ui.Button, interaction: discord.Integration):
        embed = discord.Embed(title="보정기",description="반동을 줄여줍니다.",color=0x0D7D35)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/1/1a/LogicerMuzzleBrake.png/110px-LogicerMuzzleBrake.png")
        embed.add_field(name="반동",value="-30%")
        embed.add_field(name="준비시간",value="+0.01/s")
        embed.add_field(name="총소리",value="+20%")
        embed.add_field(name="길이",value="+7%")
        embed.add_field(name="무게",value="+3%")
        await interaction.response.edit_message(embed=embed,view=logicar_attachment())