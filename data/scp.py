import discord

class skill_079(discord.ui.View):
    @discord.ui.button(label="go home",style=discord.ButtonStyle.green)
    async def go_home(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.edit_message(view=scp_classes())

    @discord.ui.button(label="Open/Close Doors (Active)", style=discord.ButtonStyle.red)
    async def skill_1(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed=discord.Embed(title="open or close the door",color=0x8080FF)
        embed.set_author(name="SCP079",icon_url="https://hub.scpslgame.com/images/thumb/2/20/LCZ_CCTV.png/315px-LCZ_CCTV.png",url="https://en.scpslgame.com/index.php?title=SCP-079")
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/6/64/682CCDoorIcon.png/75px-682CCDoorIcon.png')
        await interaction.response.edit_message(embed=embed,view=skill_079())

    @discord.ui.button(label="Lockdown (Active)", style=discord.ButtonStyle.red)
    async def skill_2(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed=discord.Embed(title="Lockdown (Active)",description="Lockdown a room and turn off its lights, allowing SCP-173 to move freely.",color=0x8080FF)
        embed.set_author(name="SCP079",icon_url="https://hub.scpslgame.com/images/thumb/4/41/HCZ_CCTV.png/315px-HCZ_CCTV.png",url="https://en.scpslgame.com/index.php?title=SCP-079")
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/957968823703719958/1032072439527645254/unknown.png')
        await interaction.response.edit_message(embed=embed,view=skill_079())

    @discord.ui.button(label="Tesla Overcharge (Active)", style=discord.ButtonStyle.red)
    async def skill_3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed=discord.Embed(title="Tesla Overcharge (Active)",description="Activate Tesla Gates on anyone who walks through.",color=0x8080FF)
        embed.set_author(name="SCP079",icon_url="https://hub.scpslgame.com/images/thumb/c/c1/EZ_CCTV.png/315px-EZ_CCTV.png",url="https://en.scpslgame.com/index.php?title=SCP-079")
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/e/e4/079tesla2.png')
        await interaction.response.edit_message(embed=embed,view=skill_079())                 
                        
    @discord.ui.button(label="Zone Blackout", style=discord.ButtonStyle.red)
    async def skill_4(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed=discord.Embed(title="Zone Blackout",description="At tire5 079 can black out the one zone to uses 200AP 60sec and cooldown 90sec",color=0x8080FF)
        embed.set_author(name="SCP079",icon_url="https://hub.scpslgame.com/images/thumb/c/c1/EZ_CCTV.png/315px-EZ_CCTV.png",url="https://en.scpslgame.com/index.php?title=SCP-079")
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/7/74/ChaosCarIsLowOnGas.png/75px-ChaosCarIsLowOnGas.png')
        await interaction.response.edit_message(embed=embed,view=skill_079())
                        
    @discord.ui.button(label="Breach Scanner", style=discord.ButtonStyle.red)
    async def skill_6(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed=discord.Embed(title="Breach scanner",description="기능:일정시간마다 생존자를 스캔",color=0x8080FF)
        embed.set_author(name="SCP079",icon_url="https://hub.scpslgame.com/images/thumb/2/20/LCZ_CCTV.png/315px-LCZ_CCTV.png",url="https://en.scpslgame.com/index.php?title=SCP-079")
        await interaction.response.edit_message(embed=embed,view=skill_079())
                        
    @discord.ui.button(label="Alpha Warhead Control", style=discord.ButtonStyle.red,disabled=True)
    async def skill_7(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed=discord.Embed(title="alpha warhead overdrive",description="ATTENTION! This feature has yet to be added to the beta.",color=0xEC2222)
        embed.set_author(name="tear5",icon_url="https://hub.scpslgame.com/images/thumb/9/9a/SCPCAT_079.png/180px-SCPCAT_079.png")
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/f/fe/NEWWarheadCAT.png/180px-NEWWarheadCAT.png')
        await interaction.response.edit_message(embed=embed)

class Button_173(discord.ui.View):
        @discord.ui.button(label="go home",style=discord.ButtonStyle.green)
        async def go_home(self, button: discord.ui.Button, interaction: discord.Interaction):
            await interaction.response.edit_message(view=scp_classes())

        @discord.ui.button(label="철근 콘크리트", style=discord.ButtonStyle.red)
        async def skill_1(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="철근 콘크리트[활성화]", description="총알저항 보호막 제공(HS)", color=0xEC2222)
            embed.set_author(name="scp173 skill",icon_url="https://hub.scpslgame.com/images/thumb/0/0d/173_Icon_new.png/180px-173_Icon_new.png")
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/f/fd/CATSHIELD.png/160px-CATSHIELD.png')
            await interaction.response.edit_message(embed=embed)
        @discord.ui.button(label="웅덩이", style=discord.ButtonStyle.red)
        async def skill_2(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="웅덩이", description="이동속도 감소하는 진흑 생성", color=0xEC2222)
            embed.set_author(name="scp173 skill",icon_url="https://hub.scpslgame.com/images/thumb/0/0d/173_Icon_new.png/180px-173_Icon_new.png")
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/a/a1/CATSPRINT.png/180px-CATSPRINT.png')
            await interaction.response.edit_message(embed=embed)
        @discord.ui.button(label="목꺽기", style=discord.ButtonStyle.red)
        async def skill_2(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="목꺽기", description="공격키", color=0xEC2222)
            embed.set_author(name="scp173 skill",icon_url="https://hub.scpslgame.com/images/thumb/0/0d/173_Icon_new.png/180px-173_Icon_new.png")
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/b/b7/Left_Click.png')
            await interaction.response.edit_message(embed=embed)
        @discord.ui.button(label="순간이동", style=discord.ButtonStyle.red)
        async def skill_2(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="순간이동", description="공격키", color=0xEC2222)
            embed.set_author(name="scp173 skill",icon_url="https://hub.scpslgame.com/images/thumb/0/0d/173_Icon_new.png/180px-173_Icon_new.png")
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/a/a4/Right_Click.png')
            await interaction.response.edit_message(embed=embed)
        
class scp939_skill(discord.ui.View):
    @discord.ui.button(label="go home",style=discord.ButtonStyle.green)
    async def go_home(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.edit_message(view=scp_classes())

    @discord.ui.button(label="claw",style=discord.ButtonStyle.red)
    async def claw(self,button:discord.ui.Button, interaction:discord.Interaction):
        embed = discord.Embed(title="claw",description="basic attack",color=0xEC2222)
        embed.set_author(name="scp939",icon_url="https://hub.scpslgame.com/images/thumb/3/35/939_Icon.png/180px-939_Icon.png")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/3/3e/939ClawIcon.png/900px-939ClawIcon.png")
        embed.set_footer(text="damage=32~40(아머의 따라 데미지가 다릅니다.)")
        await interaction.response.edit_message(embed=embed,view=scp939_skill())

    @discord.ui.button(label="Amnestic Cloud",style=discord.ButtonStyle.red)
    async def cloud(self,button:discord.ui.Button, interaction:discord.Interaction):
        embed = discord.Embed(title="Amnestic Cloud",description="[F] 를 꾹눌러 사용",color=0xEC2222)
        embed.set_author(name="scp939",icon_url="https://hub.scpslgame.com/images/thumb/3/35/939_Icon.png/180px-939_Icon.png")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/a/a4/939AmnesticIcon.png/900px-939AmnesticIcon.png")
        embed.set_footer(text="가스를 배출해 적군으로부터 자신을 숨깁니다.")
        await interaction.response.edit_message(embed=embed,view=scp939_skill())

class scp096_skill(discord.ui.View):
    @discord.ui.button(label="attack",style=discord.ButtonStyle.red)
    async def scp096_attack(self,button:discord.ui.Button, interaction:discord.Interaction):
        embed = discord.Embed(title="attack",description="Perform a swipe attack with left click that deals high damage to targets.",color=0xEC2222)
        embed.set_author(name="scp096 skill",icon_url="https://hub.scpslgame.com/images/thumb/f/f2/096Plush.png/150px-096Plush.png")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/9/99/096MeleeSprite.png")
        embed.add_field(name="damage:",value="85%")
        await interaction.response.edit_message(embed=embed,view=scp096_skill())
    @discord.ui.button(label="Scopophobia(폭주)",style=discord.ButtonStyle.red)
    async def scopophobia(self,button:discord.ui.Button, interaction:discord.Interaction):
        embed = discord.Embed(title="Scopophobia",description="press [R] Enter enrage mode when looked or shot at. Rage time scales based on targets.",color=0xEC2222)
        embed.set_author(name="scp096 skill",icon_url="https://hub.scpslgame.com/images/thumb/f/f2/096Plush.png/150px-096Plush.png")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/c/c1/096ShieldSprite.png")
        embed.add_field(name="damage:",value="oh f*ck")
        await interaction.response.edit_message(embed=embed,view=scp096_skill())
    @discord.ui.button(label="Charge",style=discord.ButtonStyle.red)
    async def charge(self,button:discord.ui.Button, interaction:discord.Interaction):
        embed = discord.Embed(title="charge",description="Perform a charge attack with right click forcing open any gates you run into.",color=0xEC2222)
        embed.set_author(name="scp096 skill",icon_url="https://hub.scpslgame.com/images/thumb/f/f2/096Plush.png/150px-096Plush.png")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/b/b0/096ChargeSprite.png")
        embed.add_field(name="damage:",value="90%")
        await interaction.response.edit_message(embed=embed,view=scp096_skill())
    @discord.ui.button(label="go home",style=discord.ButtonStyle.red)
    async def go_home(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.edit_message(view=scp_classes())

class scp049_skill(discord.ui.View):
    @discord.ui.button(label="credit arrest",style=discord.ButtonStyle.red)
    async def credit_arrest(self,button:discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="credit arrest",color=0xEC2222)
        embed.set_author(name="SCP Skill",icon_url="https://hub.scpslgame.com/images/thumb/5/5b/049_Icon.png/180px-049_Icon.png")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/b/ba/049Attack.png")
        embed.set_footer(text="공격당할시: 스태미나 소요양x3 + -8hp/s + 40damage ")
        await interaction.response.edit_message(embed=embed,view=scp049_skill())
    @discord.ui.button(label="Good Sense of the Doctor",style=discord.ButtonStyle.red)
    async def gsd(self,button:discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="Good Sense of the Doctor",color=0xEC2222)
        embed.set_author(name="SCP Skill",icon_url="https://hub.scpslgame.com/images/thumb/5/5b/049_Icon.png/180px-049_Icon.png")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/f/fb/049Sense.png")
        embed.set_footer(text="해당 타겟을 선정하면 이동속도가 빨라집니다!!")
        await interaction.response.edit_message(embed=embed,view=scp049_skill())
    @discord.ui.button(label="Waste Not, Want Not",style=discord.ButtonStyle.red)
    async def wson(self,button:discord.ui.Button, interaction: discord.Interaction):
        embed.set_author(name="SCP Skill",icon_url="https://hub.scpslgame.com/images/thumb/b/be/049-2_Icon.png/180px-049-2_Icon.png")
        embed = discord.Embed(title="Waste Not Or Not",description="당신의 선택입니다...좀비로 계속 하실겁니까..?",color=0xEC2222)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/d/d6/049Waste.png")
        await interaction.response.edit_message(embed=embed,view=scp049_skill())
    @discord.ui.button(label="The Doctor's Call",style=discord.ButtonStyle.red)
    async def docor_call(self,button:discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="The Doctor's Call",description="scp049-2 한테 위치공유 + 근처의 있는049-2 한테 HS 제공")
        embed.set_author(name="SCP Skill",icon_url="https://hub.scpslgame.com/images/thumb/b/be/049-2_Icon.png/180px-049-2_Icon.png")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/c/c8/049Call.png")
        await interaction.response.edit_message(embed = embed,view=scp049_skill())
    @discord.ui.button(label="go home",style=discord.ButtonStyle.red)
    async def go_home(self,button:discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.edit_message(view=scp_classes())

class scp106_skill(discord.ui.View):
    @discord.ui.button(label="stalk",style=discord.ButtonStyle.red)
    async def stalk(self,button:discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="STALK",description="I'm F*cking incilable!!!\n(sundowner)",color=0xEC2222)
        embed.set_author(name="SCP106 skill",icon_url="https://hub.scpslgame.com/images/thumb/a/a2/106_Icon.png/180px-106_Icon.png")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/8/88/Pocket_Dimension.png/400px-Pocket_Dimension.png")
        await interaction.response.edit_message(embed=embed,view=scp106_skill())

    @discord.ui.button(label="go home",style=discord.ButtonStyle.red)
    async def go_home(self,button:discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.edit_message(view=scp_classes())

class scp_classes(discord.ui.View):
    @discord.ui.button(label="SCP-173", style=discord.ButtonStyle.red)
    async def scp173(self,button:discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="SCP173",description="Hp:4000\nHS:750~1500\nspeed:7.3m/s",color=0xEC2222)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/1/15/RenderSCP-173.png/353px-RenderSCP-173.png")
        await interaction.response.edit_message(embed=embed,view=Button_173())
    @discord.ui.button(label="SCP-096",style=discord.ButtonStyle.red)
    async def scp096(self,button:discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="Scp096",description="hp:2000\nhs:600~1200\nwalk:3.64m/s\nangry:8m/s",color=0xEC2222)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/f/f2/Docile_096Render.png/90px-Docile_096Render.png")
        embed.set_author(name="scp classed",icon_url="https://hub.scpslgame.com/images/thumb/f/f2/096Plush.png/150px-096Plush.png")
        await interaction.response.edit_message(embed=embed,view=scp096_skill())
    @discord.ui.button(label="SCP939",style=discord.ButtonStyle.red)
    async def scp939(self,button:discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="SCP939",description="HP:2400\nHS:350~700\nspeed:4.3~7.2",color=0xEC2222)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/4/48/RenderSCP-939.png/375px-RenderSCP-939.png")
        await interaction.response.edit_message(embed=embed,view=scp939_skill())
    @discord.ui.button(label="SCP049",style=discord.ButtonStyle.red)
    async def scp049(self,button:discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="SCP049",description="HP:2000\nHS:200~500\nSpeed:3.9~5.4",color=0xEC2222)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/8/8e/RenderSCP-049.png/353px-RenderSCP-049.png")
        embed.set_author(name="SCP classes",icon_url="https://hub.scpslgame.com/images/thumb/5/5b/049_Icon.png/180px-049_Icon.png")
        await interaction.response.edit_message(embed=embed,view=scp049_skill())
    @discord.ui.button(label="SCP079",style=discord.ButtonStyle.red)
    async def scp079(self,button:discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="SCP079",description="OLD AI",color=0xEC2222)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/4/44/RenderSCP-079.png/375px-RenderSCP-079.png")
        embed.set_author(name="Scp class",icon_url="https://hub.scpslgame.com/images/thumb/9/9a/SCPCAT_079.png/120px-SCPCAT_079.png",url="https://en.scpslgame.com/index.php?title=SCPs")
        await interaction.response.edit_message(embed=embed,view=skill_079())
    @discord.ui.button(label="SCP106",style=discord.ButtonStyle.red)
    async def scp106(self,button:discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title="SCP106",description="HP:2000\nHS:300~900\nspeed:4.5~7m/s",color=0xEC2222)
        embed.set_author(name="SCP classes",icon_url="https://hub.scpslgame.com/images/thumb/a/a2/106_Icon.png/180px-106_Icon.png",url="https://en.scpslgame.com/index.php?title=SCPs")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/8/8e/RenderSCP-106.png/450px-RenderSCP-106.png")
        await interaction.response.edit_message(embed=embed,view=scp106_skill())

        

