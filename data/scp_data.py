import discord

class skill_079(discord.ui.View):
    @discord.ui.button(label="Open/Close Doors (Active)", style=discord.ButtonStyle.grey)
    async def skill_1(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed=discord.Embed(title="open or close the door",color=0x8080FF)
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/6/64/682CCDoorIcon.png/75px-682CCDoorIcon.png')
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="Lockdown (Active)", style=discord.ButtonStyle.grey)
    async def skill_2(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed=discord.Embed(title="Lockdown (Active)",description="Lockdown a room and turn off its lights, allowing SCP-173 to move freely.",color=0x8080FF)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/957968823703719958/1032072439527645254/unknown.png')
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="Tesla Overcharge (Active)", style=discord.ButtonStyle.blurple)
    async def skill_3(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed=discord.Embed(title="Tesla Overcharge (Active)",description="Activate Tesla Gates on anyone who walks through.",color=0x8080FF)
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/e/e4/079tesla2.png')
        await interaction.response.edit_message(embed=embed)
                        
                        
    @discord.ui.button(label="Zone Blackout", style=discord.ButtonStyle.success)
    async def skill_4(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed=discord.Embed(title="Zone Blackout",description="At tire5 079 can black out the one zone to uses 200AP 60sec and cooldown 90sec",color=0x8080FF)
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/7/74/ChaosCarIsLowOnGas.png/75px-ChaosCarIsLowOnGas.png')
        await interaction.response.edit_message(embed=embed)
                        
      
    @discord.ui.button(label="Target Counter", style=discord.ButtonStyle.red)
    async def skill_5(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed=discord.Embed(title="Analysis in Progress. ETA: Unknown.",description="ATTENTION! This feature has yet to be added to the beta.",color=0xEC2222)
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/d/db/079Death.gif')
        await interaction.response.edit_message(embed=embed)
                        
    @discord.ui.button(label="Breach Scanner", style=discord.ButtonStyle.red)
    async def skill_6(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed=discord.Embed(title="작업 진행중... ETA: Unknown.",description="주목! 이기능은 아직 추가되지 않았습니다..",color=0xEC2222)
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/d/db/079Death.gif')
        embed2 = discord.Embed(title="new data detected",description="새로운 자료가 제시되었습니다",url="https://twitter.com/scpslofficial/status/1629936604059156480")
        await interaction.response.edit_message(embeds=[embed,embed2])
                        
    @discord.ui.button(label="Alpha Warhead Control", style=discord.ButtonStyle.gray,disabled=True)
    async def skill_7(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed=discord.Embed(title="alpha warhead overdrive",description="ATTENTION! This feature has yet to be added to the beta.",color=0xEC2222)
        embed.set_author(name="tear5",icon_url="https://hub.scpslgame.com/images/thumb/9/9a/SCPCAT_079.png/180px-SCPCAT_079.png")
        embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/f/fe/NEWWarheadCAT.png/180px-NEWWarheadCAT.png')
        await interaction.response.edit_message(embed=embed)

class Button_173(discord.ui.View):
        @discord.ui.button(label="철근 콘크리트", style=discord.ButtonStyle.blurple)
        async def skill_1(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="철근 콘크리트[활성화]", description="총알저항 보호막 제공(HS)", color=0xff0000)
            embed.set_author(name='hs',icon_url='https://hub.scpslgame.com/images/e/e8/Hume_Shield_Bar.png')
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/f/fd/CATSHIELD.png/160px-CATSHIELD.png')
            await interaction.response.edit_message(embed=embed)
        @discord.ui.button(label="웅덩이", style=discord.ButtonStyle.blurple)
        async def skill_2(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="웅덩이", description="이동속도 감소하는 진흑 생성", color=0xff0000)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/a/a1/CATSPRINT.png/180px-CATSPRINT.png')
            await interaction.response.edit_message(embed=embed)
        @discord.ui.button(label="목꺽기", style=discord.ButtonStyle.blurple)
        async def skill_2(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="목꺽기", description="공격키", color=0xff0000)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/b/b7/Left_Click.png')
            await interaction.response.edit_message(embed=embed)
        @discord.ui.button(label="순간이동", style=discord.ButtonStyle.blurple)
        async def skill_2(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="순간이동", description="공격키", color=0xff0000)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/a/a4/Right_Click.png')
            await interaction.response.edit_message(embed=embed)
        @discord.ui.button(label="go home",style=discord.ButtonStyle.blurple)
        async def go_home(self, button: discord.ui.Button, interaction: discord.Interaction):
            await interaction.response.edit_message(view=scp_classes())

class scp096_skill(discord.ui.View):
    @discord.ui.button(label="attack",style=discord.ButtonStyle.red)
    async def scp096_attack(self,button:discord.ui.Button, interaction:discord.Interaction):
        embed = discord.Embed(title="try not to cry",description="Perform a swipe attack with left click that deals high damage to targets.",color="0xEC2222")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/9/99/096MeleeSprite.png")
        embed.add_field(name="damage:",value="85%")
        await interaction.response.edit_message(embed=embed)
    @discord.ui.button(label="Scopophobia(폭주)",style=discord.ButtonStyle.red)
    async def scopophobia(self,button:discord.ui.Button, interaction:discord.Interaction):
        embed = discord.Embed(title="Scopophobia",description="press [R] Enter enrage mode when looked or shot at. Rage time scales based on targets.",color="0xEC2222")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/c/c1/096ShieldSprite.png")
        embed.add_field(name="damage:",value="oh f*ck")
        await interaction.response.edit_message(embed=embed)
    @discord.ui.button(label="Charge",style=discord.ButtonStyle.red)
    async def charge(self,button:discord.ui.Button, interaction:discord.Interaction):
        embed = discord.Embed(title="charge",description="Perform a charge attack with right click forcing open any gates you run into.",color="0xEC2222")
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/b/b0/096ChargeSprite.png")
        embed.add_field(name="damage:",value="90%")
        await interaction.response.edit_message(embed=embed)


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
