import discord

class weapon_view(discord.ui.View):
    @discord.ui.select(
        placeholder = "Choose a weapon!",
        min_values = 1,
        max_values = 1,
        options=[
            discord.SelectOption(
                label="Com-15",
                value="1",
                description="기본적인 호신용 권총"
            ),
            discord.SelectOption(
                label="Com-18",
                value="2",
                description="기본적인 호신용 권총"
            ),
            discord.SelectOption(
                label="FSP-9",
                value="3",
                description="시설경비의 주무기"
            ),
            discord.SelectOption(
                label="Crossvec",
                value='4',
                description="MTF 이등병의 표준무기"
            ),
            discord.SelectOption(
                label="Ebsillon-11-SR",
                value="5",
                description="assult rife"
            ),
            discord.SelectOption(
                label="Shoutgun",
                value="6",
                description="혼돈의 반란의 산탄총"
            )
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "1":
            embed = discord.Embed(title="com-15", description="기본적인 호신용권총", color=0xadadad)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/22/COM-15Icon.png/375px-COM-15Icon.png")
            embed.set_image(url='https://hub.scpslgame.com/images/0/02/Com15equip.gif')
            embed.add_field(name="데미지",value="25")
            embed.add_field(name="발사속도",value="300")
            embed.add_field(name="사거리",value="22m")
            embed.add_field(name="준비시간",value="0.5/s")
            embed.add_field(name="장전시간",value="1.57/s")
            embed.add_field(name="총알정확도",value="0.2°")
            embed.set_footer(text="스폰장소 : 저위험군 어딘가...",icon_url="https://hub.scpslgame.com/images/thumb/2/22/COM-15Icon.png/250px-COM-15Icon.png")
            await interaction.response.edit_message(embed=embed,view=com_15_attachment())
        if select.values[0] == "2":
            embed = discord.Embed(title='COM-18', description="기본적인 호신용 권총", color=0x575757)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/2/2e/IconCom18.png/250px-IconCom18.png')
            embed.set_image(url="https://hub.scpslgame.com/images/f/f6/Com18equip.gif")
            embed.add_field(name="데미지",value="21.2")
            embed.add_field(name="발사속도",value="420")
            embed.add_field(name="준비시간",value="0.26/s")
            embed.add_field(name="장전시간",value="2.56/s")
            embed.add_field(name="총알정확도",value="0.2°")
            embed.set_footer(text='기본적인 호신용권총',icon_url=('https://hub.scpslgame.com/images/thumb/3/3f/WEAPONCATNEW3.png/180px-WEAPONCATNEW3.png'))
            embed.set_author(name='weapon',icon_url=("https://hub.scpslgame.com/images/thumb/7/72/NEWHUMANCAT.png/120px-NEWHUMANCAT.png"))
            await interaction.response.edit_message(embed=embed,view=com_18_Attachment())
        if select.values[0] == "3":
            embed = discord.Embed(title="fsp-9",description="시설경비의 기본무기",color=0x5B6370)
            embed.set_author(name="weponary",url="https://en.scpslgame.com/index.php?title=Weapons",icon_url="https://hub.scpslgame.com/images/7/76/CUTCONTENTCAT5.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/4/4d/FSP-9Icon.png/250px-FSP-9Icon.png")
            embed.set_footer(text="기본대미지=22.3\n최대대미지=44.6")
            embed.set_image(url="https://hub.scpslgame.com/images/c/c8/FSP-9_Inspect_Animation.gif")
            await interaction.response.edit_message(embed=embed,view=fsp_9_attachment())
        if select.values[0] == "4":
            embed = discord.Embed(title="Crossvec",description="구미호 이등병의 표준무기",color=0x70C3FF)
            embed.set_author(name="weponary",url="https://en.scpslgame.com/index.php?title=Weapons",icon_url="https://hub.scpslgame.com/images/7/76/CUTCONTENTCAT5.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/f/f0/CrossvecIcon.png/250px-CrossvecIcon.png")
            embed.set_image(url="https://hub.scpslgame.com/images/9/95/Crossvecinspect.gif")
            embed.add_field(name="데미지",value="23.5")
            embed.add_field(name="발사속도",value="750")
            embed.add_field(name="사거리",value="30m")
            embed.add_field(name="준비시간",value="1.27/s")
            embed.add_field(name="장전시간",value="3.36/s")
            embed.add_field(name="총알정확도",value="0.17°")
            embed.add_field(name="지향사격 정확도",value="1.7°")
            embed.add_field(name="조준사격 정확도",value="0.2°")
            embed.set_footer(text="Mobile Task Force",icon_url="https://hub.scpslgame.com/index.php?title=File:MTFPrivateIcon.png")
            await interaction.response.edit_message(embed=embed,view=crossvec_attachment())
        if select.values[0] == "5":
            embed = discord.Embed(title="ebsillon-11-SR",description="구미호 상병의 표준무기",color=0x0096FF)
            embed.set_author(name="weponary",icon_url="https://hub.scpslgame.com/images/thumb/3/3f/WEAPONCATNEW3.png/120px-WEAPONCATNEW3.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/9/96/E11SRIcon.png/250px-E11SRIcon.png")
            embed.set_image(url="https://hub.scpslgame.com/images/0/0e/E11inspect.gif")
            embed.add_field(name="데미지",value="25.1")
            embed.add_field(name="발사속도",value="570")
            embed.add_field(name="사거리",value="100m")
            embed.add_field(name="장전시간",value="3.3/s")
            embed.add_field(name="준비시간",value="0.8/s")
            await interaction.response.edit_message(embed=embed,view=weapon_view())
        if select.values[0] == "6":
            embed = discord.Embed(title="Shotgun",color=0x0D7D35)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/e/ee/ShotgunIcon.png/250px-ShotgunIcon.png")
            embed.set_image(url="https://hub.scpslgame.com/images/3/32/Shotguninspect.gif")
            embed.add_field(name="데미지",value="66.64")
            embed.add_field(name="발사속도",value="100")
            embed.add_field(name="준비시간",value="0.58/s")
            await interaction.response.edit_message(embed=embed,view=weapon_view())

class com_15_attachment(discord.ui.View):
    @discord.ui.select(
        placeholder = "Choose a attachment!",
        min_values = 1,
        max_values = 1,
        options=[
            discord.SelectOption(
                label="Suppressor",
                value="1",
                description="총격음을 줄여줍니다."
            ),
            discord.SelectOption(
                label="Extended JHP Magazine",
                value="2",
                description="확장탄창"
            ),
            discord.SelectOption(
                label="Flashlight",
                value="3",
                description="손전등 역할을 합니다."
            ),
            discord.SelectOption(
                label="Go home",
                value="4",
                description="무기 선택 리스트로 돌아갑니다."
            )
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "1":
            embed = discord.Embed(title="소음기",description="총격음을 줄여줍니다.",color=0xadadad)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/c/cd/COM-15Suppressor.png/120px-COM-15Suppressor.png")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "2":
            embed = discord.Embed(title="Extended JHP Magazine",description="탄약수용양을 늘려줍니다.",color=0xadadad)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/5/54/COM-15ExtendedMag.png/60px-COM-15ExtendedMag.png")
            embed.add_field(name="탄약수용양:",value="```ansi\n[2;37m+5[0m\n```")
            embed.add_field(name="준비시간:",value="```ansi\n[2;37m[2;31m+0.06/s[0m[2;37m[0m\n```")
            embed.add_field(name="무게:",value="```ansi\n[2;37m[2;31m+46%[0m[2;37m[0m\n```")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "3":
            embed = discord.Embed(title="Flashlight",description="광원 역할을합니다.",color=0xadadad)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/4/4a/COM-15Flashlight.png/60px-COM-15Flashlight.png")
            embed.add_field(name="준비시간:",value="```ansi\n[2;37m[2;31m+0.03/s[0m[2;37m[0m\n```",)
            embed.add_field(name="무게:",value="```ansi\n[2;37m[2;31m+31%[0m[2;37m[0m\n```")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] =="4":
            await interaction.response.edit_message(view=weapon_view())


class com_18_Attachment(discord.ui.View):
    @discord.ui.select(
        placeholder = "Choose a attachment!",
        min_values = 1,
        max_values = 1,
        options=[
            discord.SelectOption(
                label="Dot Sight",
                value="1",
                description="조준을 편하게 해줍니다!"
            ),
            discord.SelectOption(
                label="Extended Barrel",
                value="2",
                description="총의 명중률과 대미지를 높여줍니다!"
            ),
            discord.SelectOption(
                label="Suppressor",
                value="3",
                description="총소리를 줄여줍니다!"
            ),
            discord.SelectOption(
                label="Go home",
                value="4",
                description="무기 선택 리스트로 돌아갑니다."
            )
        ]
    )
    async def weapon_callback(self, select, interaction):
        if select.values [0] == "1":
            embed = discord.Embed(title="Dot Sight",color=0x5B6370)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/a/a0/COM18DotSight.png")
            embed.add_field(name="zoom",value="1.05x")
            embed.add_field(name="weight",value="+28%")
            await interaction.response.edit_message(embed=embed)

        if select.values[0] == "2":
            embed = discord.Embed(title="Extended Barrel",color=0x5B6370)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/b/ba/COM18Heavy.png")
            embed.add_field(name="데미지:",value="```ansi\n[2;32m[2;36m+15%[0m[2;32m[0m\n```")
            embed.add_field(name="관통력:",value="```ansi\n[2;32m[2;36m+15%[0m[2;32m[0m\n```")
            embed.add_field(name="준비시간:",value="```ansi\n[2;31m+0.09/s[0m\n```")
            embed.add_field(name="조준속도:",value="```ansi\n[2;31m-35%[0m\n```")
            embed.add_field(name="길이:",value="```ansi\n[2;31m+45%[0m\n```")
            embed.add_field(name="무게:",value="```ansi\n[2;31m+69%[0m\n```")
            await interaction.response.edit_message(embed=embed)

        if select.values[0] == "3":
            embed = discord.Embed(title="Suppressor",color=0x5B6370)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/0/06/COM18Suppressor.png/195px-COM18Suppressor.png")
            embed.add_field(name="총알정확도:",value="```ansi\n[2;32m[2;36m+25%[0m[2;32m[0m\n```")
            embed.add_field(name="Gunshot loudness:",value="```ansi\n[2;32m[2;36m-60%[0m[2;32m[0m\n```")
            embed.add_field(name="준비시간:",value="```ansi\n[2;31m+0.09/s[0m\n```")
            embed.add_field(name="길이:",value="```ansi\n[2;31m+92%[0m\n```")
            embed.add_field(name="무게:",value="```ansi\n[2;31m+49%[0m\n```")
            await interaction.response.edit_message(embed=embed)

        if select.values[0] == "4":
            await interaction.response.edit_message(view=weapon_view())

class fsp_9_attachment(discord.ui.View):
    @discord.ui.select(
        placeholder="choose attachment",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(
                label="red dot",
                value="1",
                description="조준경"
            ),
            discord.SelectOption(
                label="Suppressor",
                value="2",
                description="총격음을 줄여줍니다."
            ),
            discord.SelectOption(
                label="확장 개머리판",
                value="3",
                description="조준사격 반동을 줄여줍니다."
            ),
            discord.SelectOption(
                label="수직손잡이",
                value="4",
                description="반동을 줄여줍니다!"
            ),
            discord.SelectOption(
                label="레이저 사이트",
                value="5",
                description="지향사격 정확도를 높여줍니다."
            ),
            discord.SelectOption(
                label="손전등",
                value="6",
                description="광원효과"
            ),
            discord.SelectOption(
                label="go home",
                value="7",
                description="go back"
            )
        ]
    )

    async def fsp_9_callback(self, select, interaction):
        if select.values [0] == "1":
            embed = discord.Embed(title="red dot")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/e/ec/FSP-9Dot.png/98px-FSP-9Dot.png")
            embed.add_field(name="zoom",value="x1")
            embed.add_field(name="weight",value="+16%")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "2":
            embed = discord.Embed(title="Suppressor")
            embed.set_author(name="weponary",url="https://en.scpslgame.com/index.php?title=Weapons",icon_url="https://hub.scpslgame.com/images/7/76/CUTCONTENTCAT5.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/0/0e/FSP-9Suppressor.png/150px-FSP-9Suppressor.png")
            embed.add_field(name="총소리",value="```ansi\n[2;32m-65%[0m\n```")
            embed.add_field(name="총알 정확도",value="```ansi\n[2;32m+18%[0m\n```")
            embed.add_field(name="준비시간",value="```ansi\n[2;31m+0.19s[0m\n```")
            embed.add_field(name="길이",value="```ansi\n[2;31m+41%[0m\n```")
            embed.add_field(name="무게",value="```ansi\n[2;31m+14%[0m\n```")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "3":
            embed = discord.Embed(title="Extended Stock")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/d/d1/FSP-9StockExtended.png/120px-FSP-9StockExtended.png")
            embed.add_field(name="Aiming Accuracy",value="```ansi\n[2;32m+100%[0m\n```")
            embed.add_field(name="Recoil When Aiming",value="```ansi\n[2;32m-40%[0m\n```")
            embed.add_field(name="준비시간",value="```ansi\n[2;31m+1.47s[0m\n```")
            embed.add_field(name="길이",value="```ansi\n[2;31m+51%[0m\n```")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "4":
            embed = discord.Embed(title="수직손잡이")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/1/13/FSP-9GripExtended.png/30px-FSP-9GripExtended.png")
            embed.add_field(name="반동",value="```ansi\n[2;32m-30%[0m\n```")
            embed.add_field(name="준비시간",value="```ansi\n[2;31m+0.93/s[0m\n```")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "5":
            embed = discord.Embed(title="Laser Sight")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/25/FSP-9Laser.png/80px-FSP-9Laser.png")
            embed.add_field(name="지향사격 정확도",value="+100%")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "6":
            embed = discord.Embed(title="Flashlight",description="```ansi\n[2;32mLight Source[0m\n```")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/f/fb/FSP-9Flashlight.png/80px-FSP-9Flashlight.png")
            embed.add_field(name="준비시간",value="```ansi\n[2;31m+0.24s[0m\n```")
            embed.add_field(name="무게",value="```ansi\n[2;31m+16%[0m\n```")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "7":
            await interaction.response.edit_message(view=weapon_view())

class crossvec_attachment(discord.ui.View):
    @discord.ui.select(
        placeholder="choose a attachment",
        max_values=1,
        min_values=1,
        options=[
            discord.SelectOption(
                label="Holographic Sight",
                value="1",
                description="홀로그램 사이트"
            ),
            discord.SelectOption(
                label="Night-Vision Scope",
                value="2",
                description="화질 좋은 야간조준경"
            ),
            discord.SelectOption(
                label="Suppressor",
                value="3",
                description="총격음을 없에줍니다."
            ),
            discord.SelectOption(
                label="Extended Barrel",
                value="4",
                description="데미지를 높여줍니다."
            ),
            discord.SelectOption(
                label="Flash Hider",
                value="5",
                description="소염기"
            ),
            discord.SelectOption(
                label="Foregrip",
                value="6",
                description="반동을 줄여줍니다."
            ),
            discord.SelectOption(
                label="Laser Sight",
                value="7",
                description="지향사격 정확도를 높여줍니다."
            ),
            discord.SelectOption(
                label="Flashlight",
                value="8",
                description="광원효과를 냅니다."
            ),
            discord.SelectOption(
                label="Low-cap AP Mag",
                value="9",
                description="관통력을 매우 높여줍니다."
            ),
            discord.SelectOption(
                label="Go home",
                value="10",
                description="go back"
            )
        ]
    )
    async def crossvec_callback(self, select, interaction):
        if select.values[0] == "1":
            embed = discord.Embed(title="Holographic Sight",color=0x70C3FF)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/b/b5/CrossvecHoloSight.png/80px-CrossvecHoloSight.png")
            embed.add_field(name="zoom",value="x1")
            embed.add_field(name="무게",value="+17%")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "2":
            embed = discord.Embed(title="Night-Vision Scope",color=0x70C3FF)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/24/CrossvecNightVision.png/80px-CrossvecNightVision.png")
            embed.add_field(name="배율",value="```ansi\n[2;34m1.4x[0m\n```")
            embed.add_field(name="조준속도",value="```ansi\n[2;31m-25%[0m[2;31m[2;31m[0m[2;31m[0m\n```")
            embed.add_field(name="준비시간",value="```ansi\n[2;31m+0.22/s[0m\n```")
            embed.add_field(name="무게",value="47%")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "3":
            embed = discord.Embed(title="소음기",color=0x70C3FF)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/4/4a/CrossvecBarrelSupp.png/120px-CrossvecBarrelSupp.png")
            embed.add_field(name="총소리",value="```ansi\n[1;2m[1;34m-65%[0m[0m\n```")
            embed.add_field(name="총알 정확도",value="```ansi\n[1;2m[1;34m+25%[0m[0m\n```")
            embed.add_field(name="준비시간",value="```ansi\n[2;31m+0.14/s[0m\n```")
            embed.add_field(name="길이",value="+29%")
            embed.add_field(name="무게",value="+23%")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "4":
            embed = discord.Embed(title="Extended Barrel",color=0x70C3FF)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/4/4b/CrossvecBarrelLong.png/225px-CrossvecBarrelLong.png")
            embed.add_field(name="Damage",value="```ansi\n[2;34m+5%[0m\n```")
            embed.add_field(name="관통력",value="```ansi\n[2;34m+10%[0m\n```")
            embed.add_field(name="Bullet Accuracy",value="```ansi\n[2;34m+25%[0m\n```")
            embed.add_field(name="준비시간",value="```ansi\n[2;31m+0.32/s[0m\n```")
            embed.add_field(name="길이",value="```ansi\n[2;31m+35%[0m\n```")
            embed.add_field(name="무게",value="```ansi\n[2;31m+23%[0m\n```")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "5":
            embed = discord.Embed(title="Flash Hider",description="```ansi\n[2;34m섬광억제[0m\n```",color=0x70C3FF)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/e/e7/CrossvecBarrelHider.png/120px-CrossvecBarrelHider.png")
            embed.add_field(name="총격음",value="```ansi\n[2;34m-10%[0m\n```")
            embed.add_field(name="준비시간", value="```ansi\n[2;31m+0.14/s[0m\n```")
            embed.add_field(name="길이", value="```ansi\n[2;31m+6%[0m\n```")
            embed.add_field(name="무게", value="```ansi\n[2;31m+8%[0m\n```")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "6":
            embed = discord.Embed(title="수직손잡이",description="반동을 줄여줍니다.",color=0x70C3FF)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/5/58/CrossvecGrip.png/45px-CrossvecGrip.png")
            embed.add_field(name="반동",value="```ansi\n[2;34m-40%[0m\n```")
            embed.add_field(name='조준속도',value="```ansi\n[2;31m-15%[0m\n```")
            embed.add_field(name="준비시간", value="```ansi\n[2;31m+0.14/s[0m\n```")
            embed.add_field(name="무게",value="```ansi\n[2;31m+9%[0m\n```")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "7":
            embed = discord.Embed(title="Laser Sight",color=0x70C3FF)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/5/5f/CrossvecLaser.png/120px-CrossvecLaser.png")
            embed.add_field(name="지향사격 정확도",value="67%")
            embed.add_field(name="무게",value="```ansi\n[2;31m+8%[0m\n```")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "8":
            embed = discord.Embed(title="손전등",color=0x70C3FF)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/9/97/CrossvecFlashlight.png/120px-CrossvecFlashlight.png")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] =="9":
            ...
        if select.values[0] == "10":
            await interaction.response.edit_message(view=weapon_view())
