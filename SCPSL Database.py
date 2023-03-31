
import discord
from discord import default_permissions
from discord.ext import commands
from discord.commands import Option
from data import token


intents=discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

no_acess = discord.Embed(title="*you have not access from the this data*")
no_acess.set_author(name="접속 거부됨",icon_url='http://pm1.narvii.com/6517/29c28ec05b498ede2172569610a1500e04a61e85_00.jpg')
no_acess.set_thumbnail(url='https://preview.redd.it/e1tgj6hxv5p21.png?width=706&format=png&auto=webp&s=2924b75cb7fe2b9ae2b358bb00b5800dab2f1aff')
no_acess.set_image(url='https://www.pngfind.com/pngs/m/663-6633295_izcje0m-scp-foundation-hd-png-download.png')

@bot.event
async def on_ready():
    print("commands is ready!",bot.user)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="SCP:Secreat Laboratory"))
    
    
    
@bot.slash_command(name='scp079')
async def ping(ctx):
    embed=discord.Embed(title='SCP079',description='OLD AI',color=0x8080FF)
    embed.set_author(name='tear:eculid',icon_url='https://hub.scpslgame.com/images/thumb/8/8c/SZ_CCTV.png/558px-SZ_CCTV.png')
    embed.set_footer(text='SCP',icon_url='https://hub.scpslgame.com/images/thumb/4/44/NEWSCPCAT.png/240px-NEWSCPCAT.png')
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/4/44/RenderSCP-079.png/525px-RenderSCP-079.png')
    class Button(discord.ui.View):
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
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/957968823703719958/1032072591059468410/unknown.png')
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
            await interaction.response.edit_message(embed=embed)
                        
        @discord.ui.button(label="Alpha Warhead Control", style=discord.ButtonStyle.red)
        async def skill_7(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed=discord.Embed(title="Analysis in Progress. ETA: Unknown.",description="ATTENTION! This feature has yet to be added to the beta.",color=0xEC2222)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/d/db/079Death.gif')
            await interaction.response.edit_message(embed=embed)
                                               
    await ctx.respond("red=disable\ngray=tear1\nblurple=high tear\ngreen=new option",embed=embed ,view=Button())
    
@bot.slash_command(name='scp173-skill')
async def button(ctx):
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
        await ctx.respond(view=Button_173())
        
        
@bot.slash_command(name='scp079-skill')
async def button(ctx):
    class Button(discord.ui.View):
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
            embed
            await interaction.response.edit_message(embed=embed)
            
    await ctx.respond("red=disable\ngray=tear1\nblurple=high tear\ngreen=new option", view=Button())

@bot.slash_command(name="scp-2176")
async def ping(ctx):
    embed = discord.Embed(title="SCP2176",description="ghost light",color=0x008000)
    embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/21/2176Icon.png/300px-2176Icon.png")
    embed.add_field(name="기능1.",value="SCP079의 전력을 0으로 만들고 몇초간 전력을 뺍니다.")
    embed.add_field(name="기능2.",value="해당 방은 일시적으로 문을 럭다운및 정전됩니다.")
    await ctx.respond(embed=embed)

@bot.slash_command(name="medical-item")
async def medical_item(ctx):
    class Medic(discord.ui.View):

        @discord.ui.button(label="진통제",style = discord.ButtonStyle.grey)
        async def penikiller(self, button: discord.ui.Button, interaction: discord.Integration):
            embed = discord.Embed(title="Painkillers",url="https://en.scpslgame.com/index.php?title=Painkillers",description="진통제")
            embed.set_author(name="Item",icon_url="https://hub.scpslgame.com/images/thumb/9/95/OldPainkillersIcon.png/383px-OldPainkillersIcon.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/b/bb/NewPainkillersIcon.png/300px-NewPainkillersIcon.png")
            embed.set_image(url="https://hub.scpslgame.com/images/7/71/Painkillers_Use_New.gif")
            embed.add_field(name="기능1",value="15초간 HP가 회복됩니다(1개당 50HP)")
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label="First AID KIT", style=discord.ButtonStyle.blurple)
        async def medikit(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='구급상자',url="https://en.scpslgame.com/index.php?title=First_Aid_Kit")
            embed.set_author(name='Item',icon_url='https://hub.scpslgame.com/images/thumb/7/76/CATSTATUS.png/180px-CATSTATUS.png')
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/7/77/MedkitIcon.png/300px-MedkitIcon.png')
            embed.set_image(url='https://hub.scpslgame.com/images/6/64/Medkit_Use_New.gif')
            embed.set_footer(text="사용시 65hp 회복",icon_url='https://hub.scpslgame.com/images/thumb/7/76/CATSTATUS.png/180px-CATSTATUS.png')
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label="아드레난린", style=discord.ButtonStyle.green)
        async def ad(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='아드레난린',url="https://en.scpslgame.com/index.php?title=Adrenaline",description='의료무기',color=0xffffff)
            embed.set_author(name='Item',icon_url='https://hub.scpslgame.com/images/thumb/5/5c/OldAdrenalineIcon.png/383px-OldAdrenalineIcon.png')
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/0/0d/AdrenalineIcon.png/400px-AdrenalineIcon.png')
            embed.set_image(url='https://hub.scpslgame.com/images/0/07/Adrenaline_Use_New.gif')
            embed.set_footer(text='아드레날린은 의료용아이탬이고 전투에 많이 응용됩니다.')
            embed.add_field(name='기능1.',value='40AHP 제공')
            embed.add_field(name='기능2.',value='심정지 & 뇌진탕 해결')
            embed.set_footer(icon_url='https://hub.scpslgame.com/images/thumb/a/a1/CATSPRINT.png/180px-CATSPRINT.png')
            await interaction.response.edit_message(embed=embed)
            print("ad used by",ctx.user.name)
    await ctx.respond(view=Medic())


@bot.slash_command(name='scp106')
async def ping(ctx):
    embed=discord.Embed(title='SCP106',url="https://en.scpslgame.com/index.php?title=SCP-106",description='X나게 무적인 암살자',color=0xa4542a)
    embed.set_author(name='tear:keter',icon_url="https://static.wikia.nocookie.net/scp-containment-is-magic/images/f/fd/Scp_foundation_keter_symbol_warning_by_lycan_therapy-d4v0vp3.png/revision/latest/scale-to-width-down/183?cb=20130918143544")
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/a/a2/106_Icon.png/180px-106_Icon.png')
    embed.add_field(name="스토킹",value="무적 상태가 되면서 매우 빠른속도랑 HS 복구")
    embed.add_field(name="hunter Atlas",value="본인이 원하는 위치로 순간이동")
    embed.set_footer(text="나는 x나게 무적이다!!!")
    await ctx.respond(embed=embed)
    
@bot.slash_command(name='scp173')
async def ping(ctx):
    embed=discord.Embed(title='SCP173',url="https://en.scpslgame.com/index.php?title=SCP-173",description='SCP173:조각상(The Sculpture)',color=0xa4542a)
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/0/0d/173_Icon_new.png/180px-173_Icon_new.png')
    embed.add_field(name="철근 콘크리트",value="JHP&FMJ 탄 효과적 방어 ",inline=True)
    embed.add_field(name="웅덩이",value="이동속도 늦추는 웅덩이 생성 , 수류탄으로 파괴 가능",inline=True)
    await ctx.respond(embed=embed)
    
    
@bot.slash_command(name='scp049')
async def ping(ctx):
    embed=discord.Embed(title='SCP049',url="https://en.scpslgame.com/index.php?title=SCP-049",description="Cardiac Arrest\nResurrection\nWaste Not Want Not\nGood Sense of The Doctor\nThe Doctor's Call\n\n\nHP:2000\nDamage:160~즉사\nHS:200~500",color=0xEC2222)
    embed.set_author(name='scp tear : Eculid',icon_url='https://www.pngkey.com/maxpic/u2t4q8e6q8i1a9w7/')
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/2/2c/049F1.png/338px-049F1.png')
    await ctx.respond(embed=embed)


@bot.slash_command(title='scp939',description='with many voices')
async def scp939(ctx):
    embed = discord.Embed(title='SCP939',url="https://en.scpslgame.com/index.php?title=SCP-939",description='with many voices')
    embed.set_author(name='scp tear : KETER',icon_url='')
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/3/35/939_Icon.png/240px-939_Icon.png')
    embed.add_field(name='no armor',value='40/d',inline=True)
    embed.add_field(name='light armor',value='36/d',inline=True)
    embed.add_field(name='combat armor',value='34/d',inline=True)
    embed.add_field(name='heavy armor',value='32/d',inline=True)
    embed.set_footer(text="what the Dog Doing??",icon_url='https://hub.scpslgame.com/images/thumb/4/44/NEWSCPCAT.png/240px-NEWSCPCAT.png')
    await ctx.respond(embed=embed)
    
@bot.slash_command(name='scp-018',description='superball')
async def ping(ctx):
    embed = discord.Embed(title='SCP018',description='SuperBall',url="https://en.scpslgame.com/index.php?title=SCP-018")
    embed.set_author(name='scp item [eculid]',icon_url='https://hub.scpslgame.com/images/thumb/4/44/NEWSCPCAT.png/180px-NEWSCPCAT.png',url="https://en.scpslgame.com/index.php?title=SCPs")
    embed.set_image(url='https://hub.scpslgame.com/images/f/fd/018_Equip.gif')
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/b/b3/SCP018Icon.png/300px-SCP018Icon.png')
    embed.set_footer(text='SCP108은 던질시 탄력이 강해지면서 몬을부수거나 사람에게 치명적인 피해를 줍니다.\n그리고 10초간의 예외시간이 있지만 FF 와 관련없이 팀킬이 됩니다.')
    await ctx.respond(embed=embed)

@bot.slash_command(name='scp207',description="cokacola",color=0xff9999)
async def ping(ctx):
    embed = discord.Embed(title="SCP207",url="https://en.scpslgame.com/index.php?title=SCP-207",color=0xff0000)
    embed.set_author(name='SCPitem',icon_url='https://hub.scpslgame.com/images/thumb/8/8b/CATEFFECT.png/61px-CATEFFECT.png')
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/4/4f/NewSCP207Icon.png/300px-NewSCP207Icon.png')
    embed.set_image(url='https://hub.scpslgame.com/images/4/45/207_Use_New.gif')
    embed.add_field(name='LV1',value='>>>207 X1 : 6.48m/sec ,-1HP.s',inline=False)
    embed.add_field(name='LV2',value='>>>207 X2 : 7.45m/sec , -1.5hp.s',inline=True)
    embed.add_field(name='LV3',value='>>>207 X3 : 8.1m/sec ,-2.5HP.s',inline=False)
    embed.add_field(name='LV4',value='>>>207 X4 : 8.42m/sec -4HP.s',inline=True)
    embed.set_footer(icon_url='https://hub.scpslgame.com/images/thumb/4/44/NEWSCPCAT.png/180px-NEWSCPCAT.png')
    await ctx.respond(embed=embed)
    
@bot.slash_command(name='scp-1853',description="scpitem")
async def scp1853(ctx):
    embed = discord.Embed(title="scp1853",url="https://en.scpslgame.com/index.php?title=SCP-1853",color=0x2e8d36)
    embed.set_author(name='Prometheus Labs Inc',icon_url="https://hub.scpslgame.com/images/f/ff/PromLabsLogo.png")
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/d/d8/SCP1853Icon.png/300px-SCP1853Icon.png')
    embed.set_image(url='https://hub.scpslgame.com/images/8/88/1853_Use_Animation.gif')
    embed.set_footer(text='상호작용 속도 +60%.\n조준속도 +30%\n[25%] 반동감소\n[25%] 재장전 시간\nEntering/Exiting ADS is faster by 20%.\n20% reducation in draw & usage time for certain items')
    await ctx.respond(embed=embed)
    
@bot.slash_command(name='scp500',description='the medical scp item',color=0xff1010)
async def scp500(ctx):
    embed = discord.Embed(title='SCP500',url="https://en.scpslgame.com/index.php?title=SCP-500",description='만병통치약')
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/a/ac/SCP500Icon.png/180px-SCP500Icon.png')
    embed.set_image(url='https://hub.scpslgame.com/images/7/78/500_Use.gif')
    embed.add_field(name='option 1',value='~사용자를 완전히 치유됩니다.',inline=False)
    embed.add_field(name='option 2',value='~10초동안 사용자는 최대 200hp 를 회복합니다.',inline=False)
    await ctx.respond(embed=embed)
    
@bot.slash_command(title='scp244',color=0x00ff00)
async def scp244(ctx):
    embed = discord.Embed(title='SCP244',url="https://en.scpslgame.com/index.php?title=SCP-244",description='An ancient vase, freezing to the touch.\nCreates a large cloud of icy fog when placed',color=0x85c2de)
    embed.set_author(name='SCP ITEM',icon_url="https://hub.scpslgame.com/images/thumb/4/44/NEWSCPCAT.png/180px-NEWSCPCAT.png")
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/3/30/SCP244BIcon.png/300px-SCP244BIcon.png')
    embed.set_image(url='https://hub.scpslgame.com/images/7/7e/244B_Equip_Animation.gif')
    embed.set_footer(text='SCP item',icon_url='https://hub.scpslgame.com/images/thumb/3/32/SCP244AIcon.png/300px-SCP244AIcon.png')
    embed.add_field(name="SCP-049-2",value='''**공격속도 쿨다운 + 2** & 공격속도 감소 & 스팩 감소''',inline=True)
    embed.add_field(name="SCP-096",value='''얼굴 못봄 & **공격속도 감소**''',inline=True)
    embed.add_field(name="SCP-106",value="""공격 쿨다온 속도 증가""",inline=True)
    await ctx.respond(embed=embed)

@bot.slash_command(title='scp096',description="shy guy")
async def scp096(ctx):
    embed = discord.Embed(title='SCP096',url="https://en.scpslgame.com/index.php?title=SCP-096",description='분노조절 잘해(?)',color=0xff0000)
    embed.set_author(name="SCP Subject",icon_url="https://hub.scpslgame.com/images/thumb/3/32/096_IconCAT.png/180px-096_IconCAT.png")
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/f/f2/Docile_096Render.png/135px-Docile_096Render.png')
    embed.set_image(url="https://static.wikia.nocookie.net/scp-secret-laboratory-official/images/5/5a/Enraging.gif/revision/latest/scale-to-width-down/250?cb=20200602170935")
    embed.add_field(name='공격',value='85 damage',inline=True)
    embed.add_field(name='돌격',value='90 damage',inline=True)
    embed.add_field(name='try not to cry',value='울음 소리감소 매복 대기',inline=False)
    await ctx.respond(embed=embed)

@bot.slash_command(name='scp049-2')
async def baldy(ctx):
    embed = discord.Embed(title="SCP049-2",url="https://en.scpslgame.com/index.php?title=SCP-049-2",description="zombie",color=0xff0000)
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/b/be/049-2_Icon.png/180px-049-2_Icon.png')
    embed.add_field(name='Melee Swipe',value='40 damage')
    embed.add_field(name='Lobotomized Bloodlus',value='사람을 볼시 피지컬 증가')
    embed.add_field(name='Voracity',value='사람시체를 먹어서 hp100 회복 + ||**취소 불가능**||')
    await ctx.respond(embed=embed)

@bot.slash_command(name='jailbird',description='근접무기')
#@commands.is_owner()
async def Jailbird(ctx):
    embed = discord.Embed(title='Jailbird',url="https://en.scpslgame.com/index.php?title=Jailbird",description=' melee weapon',color=0x2a5098)
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/8/87/JailbirdIcon.png/375px-JailbirdIcon.png')
    embed.set_image(url='https://hub.scpslgame.com/images/thumb/8/88/JailbirdConceptArt.png/375px-JailbirdConceptArt.png')
    embed.set_author(name='Special Weaponry',icon_url='https://hub.scpslgame.com/images/thumb/3/3f/WEAPONCATNEW3.png/180px-WEAPONCATNEW3.png')
    embed.add_field(name="기본대미지", value="대미지:50~200", inline=False)
    embed.add_field(name="SCP049-2 대미지", value="대미지:200~800", inline=False)
    embed.set_footer(text="얻는방법 : SCP914 를 사용\n micro H.I.D 에서 course 로 하면 50% 확률로 나옴\n13.0기준")
    await ctx.respond(embed=embed)

    
@bot.slash_command(name='crossvec', description="구미호 병사의 표준 무기")
async def ping(ctx):
    embed = discord.Embed(title='Crossvec',url="https://en.scpslgame.com/index.php?title=Crossvec",description=str('구미호 병사의 표준 기관단총'),color=0x1700ff)
    embed.set_author(name='Lunae Defence',icon_url='https://hub.scpslgame.com/images/thumb/0/09/LunaeLogo.png/300px-LunaeLogo.png')
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/f/f0/CrossvecIcon.png/375px-CrossvecIcon.png')
    embed.set_image(url='https://hub.scpslgame.com/images/0/09/Crossvec_Equip_Animation.gif')
    embed.set_footer(text='기본피해량=24\n최대피해량=약84',icon_url='https://hub.scpslgame.com/images/thumb/7/7d/MTFPrivateIcon.png/180px-MTFPrivateIcon.png')
    class Button(discord.ui.View):
        @discord.ui.button(label='홀호그램 조준경', style=discord.ButtonStyle.blurple)
        async def hs(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='holograpic sight',color=0x1700ff)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/b/b5/CrossvecHoloSight.png/120px-CrossvecHoloSight.png')
            embed.add_field(name='zoom:',value=str("```fix\n1.05x```"))
            embed.add_field(name='무게:',value=str('```diff\n-무게:17%```'))
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label='야간 조준경', style=discord.ButtonStyle.blurple)
        async def nvs(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='NV sight',color=0x1700ff)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/2/24/CrossvecNightVision.png/120px-CrossvecNightVision.png')
            embed.add_field(name="zoom:",value=str("```yami\n1.85x```"))
            embed.add_field(name='조준속도:',value=str('```diff\n-25%```'))
            embed.add_field(name='준비시간:',value=str('```diff\n- +0.22/s```'))
            embed.add_field(name='무게:',value=str('```diff\n- +47%```'))


            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label='30X철갑탄', style=discord.ButtonStyle.blurple)
        async def ap(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='AP mag',description='''관통력:+200%\n무게:-6%\n데미지:-15%\n탄약:-10''',color=0x1700ff)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/f/fc/30AP.png/75px-30AP.png')
            embed.add_field(name='관통력:',value=str('```fix\n+200%```'))
            embed.add_field(name='무게:',value=str('```fix\n-6%```'))
            embed.add_field(name='탄약 수용양:',value=str('```diff\n-10```'))
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label='수직손잡이', style=discord.ButtonStyle.blurple)
        async def fg(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='Fore Grip',description='''*반동:-40%*\n조준속도:-15%\n무게:+9%\n준비시간:+0.14/s''',color=0x1700ff)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/5/58/CrossvecGrip.png/45px-CrossvecGrip.png')
            embed.add_field(name='반동:',value=str('```fix\n-40%```'))
            embed.add_field(name='조준속도:',value=str('```diff\n-15%```'))
            embed.add_field(name='무게:',value=str('```diff\n- +9%```'))
            embed.add_field(name='준비시간:',value=str('```diff\n- +0.14/s```'))
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label='레이저 사이트', style=discord.ButtonStyle.blurple)
        async def lz(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='lazer sight',description='''지향사격 정확도:+67%\n레이저보임\n무게:+8''',color=0x1700ff)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/5/5f/CrossvecLaser.png/120px-CrossvecLaser.png')
            embed.add_field(name='지향사격 정확도:',value=str("```fix\n+67%```"))
            embed.add_field(name='무게:',value=str("```+8%```"))
            embed.add_field(name="'```warning```'",value='```diff\n- 레이저 보임```')
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label='확장 배럴', style=discord.ButtonStyle.blurple)
        async def eb(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='Extended Barrel',description='''데미지:+5%\n관통력:+10%\n준비시간:0.32/s\n길이:+35%\n무게:+23%''',color=0x1700ff)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/4/4b/CrossvecBarrelLong.png/225px-CrossvecBarrelLong.png')
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label='소음기', style=discord.ButtonStyle.blurple)
        async def sp(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='소음기',description='''총소리:-65%\n총알정확도:+25%\n준비시간:0.32/s\n길이:+35%\n무게:+23%''',color=0x1700ff)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/4/4a/CrossvecBarrelSupp.png/180px-CrossvecBarrelSupp.png')
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label='개머리판 없음', style=discord.ButtonStyle.blurple)
        async def on_stock(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='No Stock',description="준비시간:-0.47/s\n길이:-33%\n조준사격 반동:+100%\n조준사격 정확도:-38%",color=0x1700ff)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/a/a1/CrossvecCollapsedStock.png')
            await interaction.response.edit_message(embed=embed)
            

        @discord.ui.button(label='go back', style=discord.ButtonStyle.gray)
        async def go_back(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='Crossvec',description='구미호 병사의 표준 기관단총',color=0x1700ff)
            embed.set_author(name='Foundation Firearms',icon_url='https://hub.scpslgame.com/images/7/76/CUTCONTENTCAT5.png')
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/f/f0/CrossvecIcon.png/375px-CrossvecIcon.png')
            embed.set_image(url='https://hub.scpslgame.com/images/0/09/Crossvec_Equip_Animation.gif')
            embed.set_footer(text='기본피해량=24\n최대피해량=약84',icon_url='https://hub.scpslgame.com/images/thumb/7/7d/MTFPrivateIcon.png/180px-MTFPrivateIcon.png')
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label='P90', style=discord.ButtonStyle.green)
        async def p90(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='P90',description="removed in 11.0.0",color=0x1700ff)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/2/28/Project90Icon.png')
            await interaction.response.edit_message(embed=embed)
        
    await ctx.respond(embed=embed,view=Button())




@bot.slash_command(name='ebsillon-11-sr', description="구미호 표준 무기")
async def ping(ctx):
    embed = discord.Embed(title='MTF-E11-SR',url="https://en.scpslgame.com/index.php?title=MTF-E11-SR",description='구미호 표준 장비',color=0x1700ff)
    embed.set_author(name='Lunae Defence',icon_url='https://hub.scpslgame.com/images/thumb/0/09/LunaeLogo.png/300px-LunaeLogo.png')
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/9/96/E11SRIcon.png/375px-E11SRIcon.png')
    embed.set_image(url='https://hub.scpslgame.com/images/2/23/E-11_Inspect_Animation.gif')
    embed.set_footer(text='|Fire Rate:570\n|Damage Falloff:100m\n|Equip Time:0.73s\n|Pick-Up Time:0.8s\n|Weight:3.15kg\n|Length:87cm\n|Bullet Accuracy:0.05°\n|Hip Fire Accuracy:2°\n|aming accuracy:0.08°(with Bullet Accuracy)~0.13° (with Bullet Accuracy)',icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
    class Button(discord.ui.View):
        @discord.ui.button(label='go back', style=discord.ButtonStyle.gray)
        async def gb(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='MTF-E11-SR',description='구미호 표준 장비',color=0x1700ff)
            embed.set_author(name='Foundation Firearms',icon_url='https://hub.scpslgame.com/images/thumb/3/3f/WEAPONCATNEW3.png/180px-WEAPONCATNEW3.png')
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/9/96/E11SRIcon.png/375px-E11SRIcon.png')
            embed.set_image(url='https://hub.scpslgame.com/images/2/23/E-11_Inspect_Animation.gif')
            embed.set_footer(text='|Fire Rate:570\n|Damage Falloff:100m\n|Equip Time:0.73s\n|Pick-Up Time:0.8s\n|Weight:3.15kg\n|Length:87cm\n|Bullet Accuracy:0.05°\n|Hip Fire Accuracy:2°\n|aming accuracy:0.08°(with Bullet Accuracy)~0.13° (with Bullet Accuracy)',icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label='Rifle Body', style=discord.ButtonStyle.gray)
        async def sb(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='Rifle Body',description="조준사격 정확도를 올려줍니다.",color=0x1700ff)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/2/28/RifleBody.png/150px-RifleBody.png')
            embed.add_field(name='damage:',value=str("""```fix\n+7.5%```"""))
            embed.add_field(name='관통력:',value=str("""```fix\n+12.5%```"""))
            embed.add_field(name='총알정확도:',value=str("""```fix\n+54%```"""))
            embed.add_field(name='발사속도:',value=str("""```-10%```"""))
            embed.add_field(name='준비시간:',value=str("""```+0.13/s```"""))
            embed.add_field(name='길이:',value=str("""```+20%```"""))
            embed.add_field(name='무게:',value=str("""```+56%```"""))
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label='소음기', style=discord.ButtonStyle.gray)
        async def sp(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='소음기',description='총소리를 감소해줍니다.',color=0x1700ff)
            embed.add_field(name='총소리:',value=str("```fix\n-65%```"))
            embed.add_field(name='총알 정확도:',value=str("```fix\n+11%```"))
            embed.add_field(name='준비시간:',value=str("```+0.08/s```"))
            embed.add_field(name='길이:',value=str("```+20%```"))
            embed.add_field(name='무게:',value=str("```+19%```"))
            await interaction.response.edit_message(embed=embed)
        @discord.ui.button(label='6배율 스코프', style=discord.ButtonStyle.gray)
        async def scope(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='6x scope',color=0x1700ff)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/4/44/Scope_E11.png/150px-Scope_E11.png')
            embed.add_field(name='zoom:',value=str("```fix\nX6```"))
            embed.add_field(name='조준사격 정확도:',value=str("```fix\n+33%```"))
            embed.add_field(name='준비시간:',value=str("```diff\n+0.08/s```"))
            embed.set_footer(text='',icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label='경기관 탄창', style=discord.ButtonStyle.gray)
        async def mag_65(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='65FMJ mag',color=0x1700ff)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/a/a1/Mag65FMJ.png/90px-Mag65FMJ.png')
            embed.add_field(name='탄약수용량:',value="```fix\n+25```")
            embed.add_field(name='재장전 시간:',value="```diff\n- +2/sec```")
            embed.set_footer(text='무게가 늘어난 탄창',icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label='30발 할로포인트 탄창', style=discord.ButtonStyle.gray)
        async def jhp_30(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='30 JHP MAG',color=0x1700ff)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/6/6e/Mag30JHP.png/75px-Mag30JHP.png")
            embed.add_field(name='데미지:',value="```fix\n+30```")
            embed.add_field(name='weight:',value="```fix\n-3```")
            embed.add_field(name='관통력:',value="```-50```")
            embed.set_footer(text='',icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label='30철갑탄', style=discord.ButtonStyle.gray)
        async def AP_30(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='30xAP',color=0x1700ff)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/a/ad/Mag30AP.png/75px-Mag30AP.png')
            embed.add_field(name='관통력:',value="```fix\n+20```")
            embed.add_field(name='무게:',value="```fix\n-3```")
            embed.add_field(name='총알 수용양:',value="```-10```")
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label="Archive : E-11[2017 beta]",style=discord.ButtonStyle.blurple)
        async def beta_e_11(self,button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="old E-11 [2017 Beta]",description="removed in 0.1.0")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/9/9a/OldestE11SRIcon.png")
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label="ARchive : [6.0.0] E-11",style=discord.ButtonStyle.blurple)
        async def beta_e_11(self,button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="first gun rework [E-11]",description="removed in 7.4.3")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/a/a3/OldE11SRIcon.png")
            await interaction.response.edit_message(embed=embed)
            
        @discord.ui.button(label="ARchive : [10.0.0] E-11",style=discord.ButtonStyle.blurple)
        async def beta_e_11(self,button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="Mp1 [E-11]",description="removed in 11.0.0")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/0/03/OldE11Render.png/761px-OldE11Render.png")
            await interaction.response.edit_message(embed=embed)
    await ctx.respond(embed=embed,view=Button())


@bot.slash_command(name='shoutgun', description="혼돈의 반란 습격자들이 사용하는 주무장.")
async def ping(ctx):
    embed = discord.Embed(title='샷건DBS', description="혼돈의 반란 화기", color=0x1a7939)
    embed.set_author(name='Chaos Insurgency Firearms',icon_url='https://hub.scpslgame.com/images/thumb/3/3f/WEAPONCATNEW3.png/180px-WEAPONCATNEW3.png')
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/e/ee/ShotgunIcon.png/250px-ShotgunIcon.png')
    embed.set_image(url='https://hub.scpslgame.com/images/c/c7/Shotgun_Equip_New.gif')
    embed.set_footer(text='기본대미지=20\n최대대미지=70\n',icon_url='https://hub.scpslgame.com/images/thumb/e/ef/ChaosIcon.png/180px-ChaosIcon.png')
    embed.add_field(name="기본 대미지:", value="66.64", inline=False)
    embed.add_field(name="최대 대미지", value="83.3", inline=False)
    await ctx.respond(embed=embed)
    
@bot.slash_command(name='radio')
async def radio(ctx):
    embed = discord.Embed(title='Radio')
    embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/3/34/HykiaLogo.png/375px-HykiaLogo.png")
    embed.set_image(url="https://hub.scpslgame.com/images/thumb/9/97/RadioIcon.png/300px-RadioIcon.png")
    embed.add_field(name="SR",value="108 meter")
    embed.add_field(name="MR",value="180 meter")
    embed.add_field(name="LR",value="1080 meter")
    embed.add_field(name="UR",value="7200 meter")
    embed.set_footer(text="SR = Short Range\nMR = Middle Range\nLR = Large Range\nUR = Ultra Range")
    await ctx.respond(embed=embed)
@radio.error
async def re(ctx,error):
    await ctx.respond(error,embed=no_acess)


@bot.slash_command(name='revolver', description="혼돈의반란 보조무기")
async def ping(ctx):
    embed = discord.Embed(title="리볼버", description="혼돈의 반란 특정 직업군에게 주어지는 보조무기.", color=0x1a7939)
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/b/b5/RevolverIcon.png/375px-RevolverIcon.png')
    embed.set_image(url='https://hub.scpslgame.com/images/e/e3/Revolver_Rare_Equip_Animation.png')
    embed.set_footer(text='normal damage=32 \n maximem damege=*115',icon_url='https://hub.scpslgame.com/images/thumb/e/ef/ChaosIcon.png/180px-ChaosIcon.png')
    class Button(discord.ui.View):
        @discord.ui.button(label='go back', style=discord.ButtonStyle.gray)
        async def gb(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="리볼버", description="혼돈의 반란 특정 직업군에게 주어지는 보조무기.", color=0x1a7939)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/b/b5/RevolverIcon.png/375px-RevolverIcon.png')
            embed.set_image(url='https://hub.scpslgame.com/images/e/e3/Revolver_Rare_Equip_Animation.png')
            embed.set_footer(text='normal damage=32 \n maximem damege=*115',icon_url='https://hub.scpslgame.com/images/thumb/e/ef/ChaosIcon.png/180px-ChaosIcon.png')
            await interaction.response.edit_message(embed=embed)
        @discord.ui.button(label='10.5인치 베럴', style=discord.ButtonStyle.green)
        async def eb(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="확장베럴")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/8/8b/RevolverBarrelLong.png/150px-RevolverBarrelLong.png")
            embed.add_field(name="```damage```",value=str("```diff\n+10%```"))
            embed.add_field(name="```관통력```",value=str("```diff\n+10%```"))
            embed.add_field(name="```총알정확도```",value=str("```diff\n+100%```"))
            embed.add_field(name="```준비시간```",value=str("```+0.08/s```"))
            embed.add_field(name="```길이```",value=str("```+37%```"))
            embed.add_field(name="```무게```",value=str("```+51%```"))
            await interaction.response.edit_message(embed=embed)
    await ctx.respond(embed=embed,view=Button())
    
@bot.slash_command(name='logicer', description="혼돈의 반란 태초무기")
async def ping(ctx):
    embed = discord.Embed(title='Logicer',url="https://en.scpslgame.com/index.php?title=Logicer",description=str('```arm\nHeavy_machin_gun```'),color=0x1a7939)
    embed.set_author(name="Chaos Repressors",url="https://en.scpslgame.com/index.php?title=Chaos_Insurgent#Repressor%20",icon_url="https://hub.scpslgame.com/images/thumb/e/ef/ChaosIcon.png/180px-ChaosIcon.png")
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/d/d4/LogicerIcon.png/375px-LogicerIcon.png')
    embed.set_image(url='https://hub.scpslgame.com/images/2/23/Logicer_Inspect_New.gif')
    embed.set_footer(text='기본피해량=26.9\n최대피해량=94.15',icon_url='https://hub.scpslgame.com/images/thumb/7/75/Icon762x39.png/35px-Icon762x39.png')
    class Button(discord.ui.View):
        @discord.ui.button(label='돌아가기', style=discord.ButtonStyle.green)
        async def gb(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title='Logicer',description=str('```arm\nHeavy_machin_gun```'),color=0x1a7939)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/d/d4/LogicerIcon.png/375px-LogicerIcon.png')
            embed.set_image(url='https://hub.scpslgame.com/images/2/23/Logicer_Inspect_New.gif')
            embed.set_footer(text='기본피해량=26.9\n최대피해량=94.15',icon_url='https://hub.scpslgame.com/images/thumb/e/ef/ChaosIcon.png/180px-ChaosIcon.png')
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label='보정기', style=discord.ButtonStyle.green)
        async def mz(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="Muzzle Brake")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/1/1a/LogicerMuzzleBrake.png/165px-LogicerMuzzleBrake.png")
            embed.add_field(name="반동",value='-30%',inline=False)
            embed.add_field(name="준비시간",value="+0.1/s",inline=False)
            embed.add_field(name="총격음",value="+30%",inline=False)
            embed.add_field(name="길이",value="+7%",inline=False)
            embed.add_field(name="무게",value="+3%",inline=False)
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label='소염기', style=discord.ButtonStyle.green)
        async def fh(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="Flash Hider")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/28/LogicerFlashHider.png/165px-LogicerFlashHider.png")
            embed.add_field(name="섬광 억제 장착",value="기능",inline=False)
            embed.add_field(name="준비시간",value="+0.1/s",inline=False)
            embed.add_field(name="길이",value="+7%",inline=False)
            embed.add_field(name="무게",value="+3%",inline=False)
            await interaction.response.edit_message(embed=embed)
        @discord.ui.button(label='short barre;', style=discord.ButtonStyle.green)
        async def sb(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="Short Barrel")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/1/11/LogicerShortBarrel.png/60px-LogicerShortBarrel.png")
            embed.add_field(name="준비시간",value="-0.35/s",inline=False)
            embed.add_field(name="지향사걱 정확도도",value="+43%",inline=False)
            embed.add_field(name="길이",value="-10%",inline=False)
            embed.add_field(name="무게",value="-10%",inline=False)
            embed.add_field(name="피해량 & 관통력",value="-5%",inline=False)
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label='red dot sight', style=discord.ButtonStyle.green)
        async def rs(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="Red dot")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/4/41/LogicerDotSight.png/60px-LogicerDotSight.png")
            embed.add_field(name="배율",value="1.05x",inline=False)
            embed.add_field(name="무게",value="+2%",inline=False)
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label='nvsight', style=discord.ButtonStyle.green)
        async def nv(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="Red dot")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/29/LogicerScopeNV.png/90px-LogicerScopeNV.png")
            embed.add_field(name="조준속도",value="-25%",inline=False)
            embed.add_field(name="무게",value="+12%",inline=False)
            await interaction.response.edit_message(embed=embed)

        @discord.ui.button(label='수직손잡이', style=discord.ButtonStyle.green)
        async def nv(self, button: discord.ui.Button, interaction: discord.Interaction):
            embed = discord.Embed(title="fore grip")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/d/df/LogicerForegrip.png/25px-LogicerForegrip.png")
            embed.add_field(name="조준속도",value="-25%",inline=False)
            embed.add_field(name="무게",value="+12%",inline=False)
            await interaction.response.edit_message(embed=embed)
    await ctx.respond(embed=embed,view=Button())



@bot.slash_command(name='micro-hid', description="특수무기")
async def ping(ctx):
    embed = discord.Embed(title=str("```MICRO H.I.D```"),url="https://en.scpslgame.com/index.php?title=Micro_H.I.D." ,description="Special Weaponry")
    embed.set_author(name='Special Weaponry',icon_url='https://hub.scpslgame.com/images/thumb/a/ab/AA3.png/75px-AA3.png')
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/d/d1/MicroHIDIcon.png/375px-MicroHIDIcon.png')
    embed.set_image(url='https://hub.scpslgame.com/images/f/fa/Micro_HID_Equip_New.gif')
    embed.add_field(name="ammo:", value="1", inline=False)
    embed.add_field(name="blast damage", value="90~1150", inline=False)
    embed.add_field(name="fire delay", value="2sec", inline=False)
    embed.set_footer(text='how you get: scp914 or micro .H.I.D(aermory tear3)',icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
    await ctx.respond(embed=embed)
    
@bot.slash_command(name='high-explosive-grenade')
async def ping(ctx):
    embed = discord.Embed(title=('```High-Explosive Grenade```'),url="https://en.scpslgame.com/index.php?title=High-Explosive_Grenade",description='Weapon',color=0x0096FF)
    embed.set_author(name='Grenades',icon_url='https://cdn-icons-png.flaticon.com/512/1204/1204537.png')
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/4/44/GrenadeIcon.png/375px-GrenadeIcon.png')
    embed.set_image(url='https://hub.scpslgame.com/images/f/f2/Grenade_Equip_Animation.gif')
    embed.add_field(name="Damage in scp:", value="900", inline=True)
    embed.add_field(name="Damage in human", value="300", inline=True)
    embed.set_footer(text='mtf sergent/captain',icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
    await ctx.respond(embed=embed)
    print('>>bomb is used by:',ctx.user.name)

@bot.slash_command(name='3x-particle-disruptor', description="프로토타입 레이저총")
async def ping(ctx):
    embed = discord.Embed(title=str('```3-X Particle Disruptor```'),url='https://en.scpslgame.com/index.php?title=3-X_Particle_Disruptor', description=str("```fix\nExperimental Fusion Rifle```"), color=0x575757)
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/7/77/IconDisruptor.png/375px-IconDisruptor.png')
    embed.set_image(url='https://hub.scpslgame.com/images/b/b7/3-X_Equip_Animation.gif')
    embed.set_footer(text='normal damage=300\nmax damage=350\n',icon_url="https://hub.scpslgame.com/images/thumb/0/07/UnknownIcon.png/180px-UnknownIcon.png")
    embed.set_author(name='Special Weaponry',icon_url='https://hub.scpslgame.com/images/5/59/OlderE11SRIcon.png')
    await ctx.respond(embed=embed)
    
    
@bot.slash_command(name='com-45',description='게틀링 건 권총')
#@commands.is_owner()
async def ping(ctx):
    embed = discord.Embed(title=str("```COM-45```"),url="https://en.scpslgame.com/index.php?title=COM-45",description='특수무기',color=0xadadad)
    embed.set_author(name='Special Weaponry',icon_url='https://t4.ftcdn.net/jpg/05/38/61/51/360_F_538615190_uf3p4hIKSAjwDmWyIcFVhbC97iciWRU2.jpg')
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/d/d9/IconCom45.png/375px-IconCom45.png')
    embed.set_image(url='https://static.wikia.nocookie.net/guns/images/4/45/Glock_17.jpg/revision/latest/scale-to-width-down/350?cb=20070407141738')
    embed.set_footer(text='Special Weaponry\n획득방법 : SCP914 에서 com-15를 veryfine 으로 하면 15%확률로 나옵니다!',icon_url='https://hub.scpslgame.com/images/thumb/3/3f/WEAPONCATNEW3.png/180px-WEAPONCATNEW3.png')
    embed.add_field(name="**발사속도**:", value="3600", inline=False)
    embed.add_field(name="Damage Falloff:", value="16.5/m", inline=False)
    embed.add_field(name="준비시간:", value="0.5/s", inline=False)
    embed.add_field(name="weight:", value="0.65kg", inline=False)
    embed.add_field(name="length", value="18cm", inline=False)
    embed.add_field(name="accuarcy", value="0.2", inline=False)
    await ctx.respond(embed=embed)
    print('>>com45 is used by:',ctx.user.name)

@bot.slash_command(name="heavy-armor")
async def ping(ctx):
    embed = discord.Embed(title='고강도 방어구',color=0xaf8faa)
    embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/7/77/HeavyArmorIcon.png/300px-HeavyArmorIcon.png")
    embed.add_field(name="body 보호",value="```fix\n80%```")
    embed.add_field(name="head 보호",value="```fix\n80%```")
    embed.set_footer(text="9x19mm : 200\n5.56x45mm : 200\n7.62x39mm : 200\n12/70buckshots : 74\n.44MAG : 68\n4xmedical item \n4x generades\n3x총기")
    await ctx.respond(embed=embed)

@bot.slash_command(name="combat-armor")
async def ping(ctx):
    embed = discord.Embed(title="전투방탄복",url="https://en.scpslgame.com/index.php?title=Combat_Armor",color=0xFF8E00)
    embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/e/e2/CombatArmorIcon.png/300px-CombatArmorIcon.png")
    embed.add_field(name="헤드 보호",value="80%")
    embed.add_field(name="몸통보호",value="60%")
    await ctx.respond(embed=embed)

@bot.slash_command(name="d-계급인원")
async def cd(ctx):
    embed = discord.Embed(title='D 계급 인원',description="enemy = mobile task force\nfriend = Chaous Rebellion",color=0xFF8E00)
    embed.set_thumbnail(url="""https://hub.scpslgame.com/images/thumb/6/69/D-Class_%2812.0%29.png/563px-D-Class_%2812.0%29.png""")
    embed.set_author(name='civilion class',icon_url="https://hub.scpslgame.com/images/thumb/a/a0/ClassDIcon.png/180px-ClassDIcon.png")
    embed.set_footer(text="아이탬 : 없음")
    await ctx.respond(embed=embed)
@cd .error
async def cde(ctx,error):
    await ctx.respond(error)

@bot.slash_command(name="시설경비")
async def fg(ctx):
    embed = discord.Embed(title="시설 경비원",description="적 : 혼돈의반란 & SCP\n아군:MTF & 과학자\n중립 또는 적:D계급인원",color=0x5B6370)
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/7/75/GuardIcon.png/180px-GuardIcon.png')
    file = discord.File("guard inventory.png",filename="image.png")
    embed.set_image(url="attachment://image.png")
    await ctx.respond(embed=embed,file=file)
@fg.error
async def fge(ctx,error):
    await ctx.respond(error)

@bot.slash_command(name="과학자")
async def scientist(ctx):
    embed = discord.Embed(title="과학자",description="중립 또는 적: D계급인원 \n협력 : MTF&시설경비\n적 : SCP",color=0xFFFF7C)
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/9/90/zScientist_%2812.0%29.png/653px-Scientist_%2812.0%29.png')
    file = discord.File("Scientist inventory.png",filename="image.png")
    embed.set_image(url="attachment://image.png")
    await ctx.respond(embed=embed,file=file)
@scientist.error
async def se(ctx,error):
    await ctx.respond(error)

@bot.slash_command(name="mtf_captain")
async def mtfc(ctx):
    embed = discord.Embed(title="MTF 대위",description="적 : 혼돈의반란 & SCP\n아군:MTF & 과학자\n중립 또는 적:D계급인원",url="https://en.scpslgame.com/index.php?title=Mobile_Task_Force",color=0x003DCA)
    embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/5/55/NTF_%2812.0%29.png/653px-NTF_%2812.0%29.png')
    file = discord.File("mtf.png",filename="image.png")
    embed.set_image(url="attachment://image.png")
    await ctx.respond(embed = embed , file=file)

@bot.slash_command(name="chaos-insurgent-rifeman")
async def ci(ctx):
    embed = discord.Embed(title="혼돈의 반란 소총수",description="Chaos Insurgent 의 병사",url="https://en.scpslgame.com/index.php?title=Chaos_Insurgent",color=0x1a7939)
    embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/e/ef/ChaosIcon.png/180px-ChaosIcon.png")
    file = discord.File('chaous inventory.png',filename="image.png")
    embed.set_image(url="attachment://image.png")
    await ctx.respond(embed = embed , file=file)

@bot.slash_command(name="eagle-tactical-solutions",description=" scp제단 무기업체")
async def Eagle_Tactical_Solutions(ctx):
    embed = discord.Embed(title="Eagle Tactical Solutions",description="SCP 제단 무기제조 업체")
    embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/9/91/FBLogo.png/300px-FBLogo.png")
    embed.set_footer(text="제조물품 : 섬광탄")
    await ctx.respond(embed=embed)

@bot.slash_command(name="foundation-gunworks",description="Foundation Gunworks는 미국의 Area-14 근처에 위치한 재단 소유 회사입니다 . 이 회사는 재단이 사용할 무기와 부착물을 제조합니다.")
async def Foundation_Gunworks(ctx):
    embed = discord.Embed(title="Foundation Gunworks")
    embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/29/FoundationGunworksLogo.png/300px-FoundationGunworksLogo.png")
    embed.set_footer(text="제조무기 : COM-18 / E-11-SR / crossvec / FSP-9")
    await ctx.respond(embed=embed)

@bot.slash_command(name="lunae_defence",description="scpsl 파츠재작  업체")
async def lunae_defence(ctx):
    embed = discord.Embed(title="Lunae Defence",url="https://en.scpslgame.com/index.php?title=Lore/Manufacturers",description="SCPSL Manufactor",color=0x945394)
    embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/0/09/LunaeLogo.png/200px-LunaeLogo.png")
    embed.set_footer(text="Comm-18 , Croissvec , E-11-SR , FSP-9의 파츠를 재작합니다.")
    await ctx.respond(embed=embed)

@bot.slash_command(name="chaous-server")
async def chaous_server(ctx):
    embed=discord.Embed(title="카오스서버", url="https://discord.gg/56K7fRbNJr", description="다양한 맵 , 편의성 플러그인 , 친절한 관리자", color=0x008a10)
    embed.set_author(name="scpsl server", url="https://discord.gg/56K7fRbNJr")
    embed.set_image(url="https://cdn.discordapp.com/attachments/1015518345103167508/1075686479487062126/image.png")
    embed.set_thumbnail(url="https://i.pinimg.com/originals/4c/57/ea/4c57ea43169133d32d9c919948fd25f2.jpg")
    embed.add_field(name="편의성 플러그인:", value="있음", inline=False)
    embed.add_field(name="스테미나무제한:", value="예", inline=False)
    embed.add_field(name="자동핵:", value="25분", inline=False)
    embed.add_field(name="DDOS Protection:", value="yes", inline=False)
    embed.set_footer(text="server owner : 하늘#5094")
    await ctx.respond(embed=embed)

@chaous_server.error
async def chaous_error(ctx):
    await ctx.respond(embed=no_acess)

@bot.slash_command(name='candy-list')
async def candy(ctx,
            candy:Option(str,"Candy list",choices=["red","plurple","blue","green","yellow","rainbow","pink","SCP330"])):
    if candy == "pink":
        embed = discord.Embed(title="Pink Candy",color=0xFF0089)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/5/54/IconCandyPink.png/150px-IconCandyPink.png")
        embed.set_image(url="https://hub.scpslgame.com/images/thumb/0/07/UnknownIcon.png/120px-UnknownIcon.png")
        embed.add_field(name="기능1",value="플래이어는 자폭합니다 Xb")
        embed.set_footer(text="확률 : 0%")
        await ctx.respond(embed=embed)
    if candy == "blue":
        embed = discord.Embed(title="Blue Candy",color=0x00FFFF)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/3/35/IconCandyBlue.png/150px-IconCandyBlue.png")
        embed.set_image(url="https://hub.scpslgame.com/images/e/e8/Hume_Shield_Bar.png")
        embed.add_field(name="기능1",value="영구적인 30AHP 를 제공합니다.")
        embed.set_footer(text="확률 : 16.67%")
        await ctx.respond(embed=embed)
    if candy == "rainbow":
        embed = discord.Embed(title="Rainbow candy",color=0x00FFCD)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/c/c2/IconCandyGay.png/150px-IconCandyGay.png")
        embed.add_field(name="기능1",value="HP15 회복")
        embed.add_field(name="기능2",value="H5초 동안 활력 상태 효과를 적용합니다.")
        embed.add_field(name="기능3",value="영구적으로 Bodyshot 감소 상태 효과를 적용합니다.")
        embed.add_field(name="기능4",value="10초 동안 감소하지 않는 20 AHP를 적용합니다")
        await ctx.respond(embed=embed)

    if candy == "yellow":
        embed = discord.Embed(title="yellow candy",color=0xFFD500)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/b/b8/IconCandyYellow.png/100px-IconCandyYellow.png")
        embed.add_field(name="기능1",value="스태미나 25% 회복")
        embed.add_field(name="기능2",value="활렬효과 8초간 부여")
        embed.add_field(name="기능3",value="10%+ 무브먼트 부스트")
        embed.set_footer(text="확률: 16.67%")
        await ctx.respond(emebd=embed)
    if candy == "green":
        embed = discord.Embed(title="green candy",color=0x44FF00)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/21/IconCandyRed.png/100px-IconCandyRed.png")
        embed.add_field(name="HP120 재생 (1초간 1HP)")
        embed.set_footer(text="확률: 16.67%")
        await ctx.respond(embed=embed)

    if candy == "plurple":
        embed = discord.Embed(title="plurple candy",color=0xAB00FF)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/8/8a/IconCandyPurple.png/100px-IconCandyPurple.png")
        embed.add_field(name="기능1",value="손상 감소(4015초 동안) + Hp 15재생")
        embed.set_footer(text="확률: 16.67%")
        await ctx.respond(embed=embed)

    if candy == "red":
        embed = discord.Embed(title="red candy",color=0xFF0000)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/21/IconCandyRed.png/150px-IconCandyRed.png")
        embed.add_field(name="기능1",value="HP45 재생")
        embed.set_footer(text="확률: 16.67%")
        await ctx.respond(embed=embed)

    if candy == "SCP330":
        embed = discord.Embed(title="SCP330",url="https://en.scpslgame.com/index.php?title=SCP-330",color=0x5B146C)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/4/44/330Render.png/450px-330Render.png")
        embed.set_image(url="https://hub.scpslgame.com/images/thumb/a/a9/330Event2021.png/1700px-330Event2021.png")
        embed.set_footer(text="특수 사탕을 받을수 있습니다.\n3개를 가져갈시 손목이 짤립니다.")
        await ctx.respond(embed = embed)
        
@bot.slash_command(name="프로필")
async def profile(ctx):
    embed = discord.Embed(title=ctx.user.name)
    embed.set_footer(url=ctx.author.avatar.url)
    await ctx.respond(embed=embed)

@profile.error
async def error(ctx,error):
    await ctx.respond(error)

@ping.error
async def ping_error(error,ctx):
    await ctx.respond(error)

@bot.slash_command(name="scpsl-update")
async def ping(ctx):
    embed = discord.Embed(title="SCPSL 13.0 update note",description="donate : https://www.patreon.com/HubertMoszka ",url="https://patreon.scpslgame.com/posts/view/fc31dfcb-62db-44c6-9d41-ed33c6b1c50c")
    embed.set_image(url="https://cdn.discordapp.com/attachments/472406978908389376/1090699112481030214/image.png")
    embed.set_footer(text="click the title and check the patreon portal.")
    await ctx.respond("```ansi\n[2;32mscpsl [2;31m13.0 [0m[2;32mpatreon beta [0m[2;33mis open in 4tear(25$)\n[0m[2;32m[2;33m[0m[2;32m[0m[2;41m[2;41m[0m[2;41m[0m[2;34m[0m\n```",embed = embed)

@bot.slash_command(name="scp-1576")
async def ping(ctx):
    embed = discord.Embed(title="SCP1576",description="마법의 소라고동",url="https://en.scpslgame.com/index.php?title=SCP-1576")
    embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/24/SCP1576Icon.png/200px-SCP1576Icon.png")
    embed.set_footer(text="이 아이탬을 사용시 30초간 죽은 사람과 대화를 할수 있습니다.")
    embed.add_field(name="회득 방법 : 없음")
bot.run(token)