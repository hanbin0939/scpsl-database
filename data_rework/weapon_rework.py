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
            ),
            discord.SelectOption(
                label="Logicer",
                value="7",
                description="혼돈의 반란의 기관총"
            ),
            discord.SelectOption(
                label="AK",
                value="8",
                description="혼돈의 반란 소총수의 기본무기"
            ),
            discord.SelectOption(
                label="리볼버",
                value="9",
                description="현존 최강 권총"
            ),
            discord.SelectOption(
                label="jailbird",
                value="10",
                description="melle wepon"
            ),
            discord.SelectOption(
                label="COM-45",
                value="11",
                description="glock-18"
            ),
            discord.SelectOption(
                label="3-X Particle Disruptor",
                value="12",
                description="Micro.H.I.D v2"
            ),
            discord.SelectOption(
                label="Micro .H.I.D",
                value="13",
                description="Experimental Energy Weapon"
            )
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "1":
            embed = discord.Embed(title="com-15", description="기본적인 호신용권총", color=0xadadad)
            embed.set_author(name='weapon',icon_url=("https://hub.scpslgame.com/images/thumb/7/72/NEWHUMANCAT.png/120px-NEWHUMANCAT.png"))
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/22/COM-15Icon.png/375px-COM-15Icon.png")
            embed.set_image(url='https://hub.scpslgame.com/images/0/02/Com15equip.gif')
            embed.add_field(name="데미지",value="25")
            embed.add_field(name="발사속도",value="300")
            embed.add_field(name="사거리",value="22m")
            embed.add_field(name="준비시간",value="0.5/s")
            embed.add_field(name="장전시간",value="1.57/s")
            embed.add_field(name="총알정확도",value="0.2°")
            embed.set_footer(text="9x19mm",icon_url="https://hub.scpslgame.com/images/thumb/4/46/Icon9x19mm.png/53px-Icon9x19mm.png")
            await interaction.response.edit_message(embed=embed,view=com_15_attachment())
        if select.values[0] == "2":
            embed = discord.Embed(title='COM-18', description="기본적인 호신용 권총", color=0x575757)
            embed.set_author(name="weponary",icon_url="https://hub.scpslgame.com/images/thumb/7/75/GuardIcon.png/180px-GuardIcon.png")
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/2/2e/IconCom18.png/250px-IconCom18.png')
            embed.set_image(url="https://hub.scpslgame.com/images/f/f6/Com18equip.gif")
            embed.add_field(name="데미지",value="21.2")
            embed.add_field(name="발사속도",value="420")
            embed.add_field(name="준비시간",value="0.26/s")
            embed.add_field(name="장전시간",value="2.56/s")
            embed.add_field(name="총알정확도",value="0.2°")
            embed.set_footer(text="9x19mm",icon_url="https://hub.scpslgame.com/images/thumb/4/46/Icon9x19mm.png/53px-Icon9x19mm.png")
            embed.set_author(name='weapon',icon_url=("https://hub.scpslgame.com/images/thumb/7/72/NEWHUMANCAT.png/120px-NEWHUMANCAT.png"))
            await interaction.response.edit_message(embed=embed,view=com_18_Attachment())
        if select.values[0] == "3":
            embed = discord.Embed(title="fsp-9",description="시설경비의 기본무기",color=0x5B6370)
            embed.set_author(name="Mobile Tack Force",icon_url="https://hub.scpslgame.com/images/thumb/7/75/GuardIcon.png/180px-GuardIcon.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/4/4d/FSP-9Icon.png/250px-FSP-9Icon.png")
            embed.set_footer(text="기본대미지=22.3\n최대대미지=44.6")
            embed.set_image(url="https://hub.scpslgame.com/images/c/c8/FSP-9_Inspect_Animation.gif")
            await interaction.response.edit_message(embed=embed,view=fsp_9_attachment())
        if select.values[0] == "4":
            embed = discord.Embed(title="Crossvec",description="구미호 이등병의 표준무기",color=0x70C3FF)
            embed.set_author(name="Mobile Task Force",icon_url="https://hub.scpslgame.com/images/7/7d/MTFPrivateIcon.png")
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
            embed.set_footer(text="9x19mm",icon_url="https://hub.scpslgame.com/images/thumb/4/46/Icon9x19mm.png/53px-Icon9x19mm.png")
            await interaction.response.edit_message(embed=embed,view=crossvec_attachment())
        if select.values[0] == "5":
            embed = discord.Embed(title="ebsillon-11-SR",description="구미호 상병의 표준무기",color=0x0096FF)
            embed.set_author(name="Mobile Tack Force",icon_url="https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/9/96/E11SRIcon.png/250px-E11SRIcon.png")
            embed.set_image(url="https://hub.scpslgame.com/images/0/0e/E11inspect.gif")
            embed.add_field(name="데미지",value="25.1")
            embed.add_field(name="발사속도",value="570")
            embed.add_field(name="사거리",value="100m")
            embed.add_field(name="장전시간",value="3.3/s")
            embed.add_field(name="준비시간",value="0.8/s")
            embed.set_footer(text="5.56x45mm",icon_url="https://hub.scpslgame.com/images/thumb/d/d7/Icon556x45.png/53px-Icon556x45.png")
            await interaction.response.edit_message(embed=embed,view=ebsillon_11_Attachment())
        if select.values[0] == "6":
            embed = discord.Embed(title="Shotgun",description="혼돈의 반한의 산탄총",color=0x0D7D35)
            embed.set_author(name="Chaous insergencuy",icon_url="https://hub.scpslgame.com/images/thumb/e/ef/ChaosIcon.png/180px-ChaosIcon.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/e/ee/ShotgunIcon.png/250px-ShotgunIcon.png")
            embed.set_image(url="https://hub.scpslgame.com/images/3/32/Shotguninspect.gif")
            embed.add_field(name="데미지",value="66.64")
            embed.add_field(name="발사속도",value="100")
            embed.add_field(name="준비시간",value="0.58/s")
            embed.add_field(name="사거리",value="18m")
            embed.set_footer(text="12/70 Buckshot",icon_url="https://hub.scpslgame.com/images/thumb/f/f4/Icon12ga.png/53px-Icon12ga.png")
            await interaction.response.edit_message(embed=embed,view=shoutgun_Attachment())
        if select.values[0] =="7":
            embed = discord.Embed(title="Logicer",description="혼돈의 반란의 기관총",color=0x006826)
            embed.set_author(name="Chaos Insurgent",icon_url="https://hub.scpslgame.com/images/thumb/e/ef/ChaosIcon.png/180px-ChaosIcon.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/d/d4/LogicerIcon.png/375px-LogicerIcon.png")
            embed.set_image(url="https://hub.scpslgame.com/images/2/2f/Logicerinspect.gif")
            embed.add_field(name="Damage",value="26.9")
            embed.add_field(name="Fire Rate",value="660")
            embed.add_field(name="사거리",value="150m")
            embed.add_field(name="준비시간",value="0.93/s")
            embed.add_field(name="장전시간",value="5.3/s")
            embed.add_field(name="총알정확도",value="0.035°")
            embed.add_field(name="지향사격 정확도",value="3.5°")
            embed.add_field(name="조준사격정확도",value="0.15°")
            embed.set_footer(text="7.62x39mm",icon_url="https://hub.scpslgame.com/images/thumb/7/75/Icon762x39.png/53px-Icon762x39.png")
            await interaction.response.edit_message(embed=embed,view=weapon_view())
        if select.values[0] == "8":
            embed = discord.Embed(title="AK",description="혼돈의 반란의 주무기",color=0x008F1C)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/3/33/NewAKIcon.png/250px-NewAKIcon.png")
            embed.set_image(url="https://hub.scpslgame.com/images/a/a3/AKinspect.gif")
            embed.set_author(name="Chaous insergencuy",icon_url="https://hub.scpslgame.com/images/thumb/e/ef/ChaosIcon.png/180px-ChaosIcon.png")
            embed.add_field(name="damage",value="26.2")
            embed.add_field(name="발사속도",value="498")
            embed.add_field(name="사거리",value="100m")
            embed.add_field(name="준비시간",value="0.54/s")
            embed.add_field(name="장전시간",value="3/s")
            embed.add_field(name="총알 정확도",value="0.07°")
            embed.add_field(name="지향사격 정확도",value="2.5°")
            embed.add_field(name="조준사격 정확도",value="0.08°")
            embed.set_footer(text="7.62x39mm",icon_url="https://hub.scpslgame.com/images/thumb/7/75/Icon762x39.png/53px-Icon762x39.png")
            await interaction.response.edit_message(embed=embed,view=weapon_view())
        if select.values[0] == "9":
            embed = discord.Embed(title=".44 Revolver",description="현존 최강 권총",color=0x0D7D35)
            embed.set_author(name="Chaous insergencuy",icon_url="https://hub.scpslgame.com/images/thumb/e/ef/ChaosIcon.png/180px-ChaosIcon.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/b/b5/RevolverIcon.png/375px-RevolverIcon.png")
            embed.set_image(url="https://hub.scpslgame.com/images/7/76/Revolverrarequip.gif")
            embed.add_field(name="데미지",value="57.7")
            embed.add_field(name="발사속도",value="240")
            embed.add_field(name="준비시간",value="0.45/s")
            embed.add_field(name="총알정확도",value="0.15°")
            embed.add_field(name="지향사격 정확도",value="2°")
            embed.add_field(name="조준사격 정확도",value="0.75°")
            embed.set_footer(text=".44 Mag",icon_url="https://hub.scpslgame.com/images/thumb/f/ff/Icon44cal.png/53px-Icon44cal.png")
            await interaction.response.edit_message(embed=embed,view=weapon_view())
        if select.values[0] == "10":
            embed = discord.Embed(title="jailbird",description="First melle weapon",color=0x33338c)
            embed.set_author(name="Special weapon",icon_url="https://hub.scpslgame.com/images/thumb/8/87/JailbirdIcon.png/250px-JailbirdIcon.png")
            embed.set_image(url="https://hub.scpslgame.com/images/1/1d/Jbnormalinspect.gif")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/8/87/JailbirdIcon.png/250px-JailbirdIcon.png")
            embed.add_field(name="damage",value="50")
            embed.add_field(name="damage(charged)",value="200")
            embed.add_field(name="zombie",value="damage * 4")
            await interaction.response.edit_message(embed=embed,view=weapon_view())
        if select.values[0] == "11":
            embed = discord.Embed(title="COM-45",description="RPM=3600",color=0x33338c)
            embed.set_author(name="Special Weapon",icon_url="https://hub.scpslgame.com/images/thumb/d/d9/IconCom45.png/120px-IconCom45.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/d/d9/IconCom45.png/250px-IconCom45.png")
            embed.set_image(url="https://hub.scpslgame.com/images/1/10/Com45inspect.gif")
            embed.add_field(name="damage",value="25")
            embed.add_field(name="Fire Rate",value="3600")
            embed.add_field(name="준비시간",value="0.5/s")
            embed.add_field(name="장전시간",value="2.14/s")
            await interaction.response.edit_message(embed=embed,view=weapon_view())
        if select.values[0] == "12":
            embed = discord.Embed(title="3-X Particle Disruptor",description="Tatical Lazer Blaster",color=0x33338c)
            embed.set_author(name="Speial Weapon",icon_url="https://hub.scpslgame.com/images/thumb/7/77/IconDisruptor.png/250px-IconDisruptor.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/7/77/IconDisruptor.png/250px-IconDisruptor.png")
            embed.set_image(url="https://hub.scpslgame.com/images/5/58/3xinspect.gif")
            embed.add_field(name="ammo",value="5")
            embed.add_field(name="발사속도",value="9")
            embed.add_field(name="damage",value="250")
            embed.add_field(name="장전시간",value="5.55/s")
            await interaction.response.edit_message(embed=embed,view=weapon_view())
        if select.values[0] == "13":
            embed = discord.Embed(title="Micro H.I.D.",description="Micro High-Intensity Electrical Discharge Thrower",color=0x33338c)
            embed.set_author(name="Special Weapon",icon_url="https://hub.scpslgame.com/images/thumb/d/d1/UpdatedMicroHIDIcon.png/120px-UpdatedMicroHIDIcon.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/d/d1/UpdatedMicroHIDIcon.png/250px-UpdatedMicroHIDIcon.png")
            embed.set_image(url="https://hub.scpslgame.com/images/0/09/Microequip.gif")
            embed.add_field(name="데미지",value="143.75")
            embed.add_field(name="데미지(DPS)",value="1150")
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
            embed = discord.Embed(title="x30 AP mag",description="관통력을 매우 높여줍니다.",color=0x70C3FF)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/f/fc/30AP.png/50px-30AP.png")
            embed.add_field(name="탄약 수용량",value="```ansi\n[2;31m-10[0m\n```")
            embed.add_field(name="데미지",value="```ansi\n[2;31m-15%[0m\n```")
            embed.add_field(name="관통력",value="```ansi\n[2;34m+200%[0m\n```")
            embed.add_field(name="무게",value="```ansi\n[2;34m-6%[0m\n```")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "10":
            await interaction.response.edit_message(view=weapon_view())

class ebsillon_11_Attachment(discord.ui.View):
    @discord.ui.select(
        placeholder="choose a attachment",
        max_values=1,
        min_values=1,
        options=[
            discord.SelectOption(
                label="홀로그램 조준경",
                value="1",
                description="조준경"
            ),
            discord.SelectOption(
                label="NV 조준경",
                value="2",
                description="화질이 좋은 야간 조준경"
            ),
            discord.SelectOption(
                label="망원 조준경",
                value="3",
                description="저격 스코프"
            ),
            discord.SelectOption(
                label="소총총신",
                value="4",
                description="조준사격의 최적화된 배럴"
            ),
            discord.SelectOption(
                label="Suppressor",
                value="5",
                description="총격음을 줄여줍니다."
            ),
            discord.SelectOption(
                label="Flash Hider",
                value="6",
                description="섬광 제거"
            ),
            discord.SelectOption(
                label="머즐부스터",
                value="7",
                description="화력이 올라가지만, 명중율 이 줄어듭니다."
            ),
            discord.SelectOption(
                label="보정기",
                value="8",
                description="반동을 줄여줍니다."
            ),
            discord.SelectOption(
                label="Lightweight Stock",
                value="9",
                description="기동성이 매우 좋은 개머리판"
            ),
            discord.SelectOption(
                label="Recoil-Reducing Stock",
                value="10",
                description="조준사격 반동을 줄여줍니다."
            ),
            discord.SelectOption(
                label="수직손잡이",
                value="11",
                description="반동을 줄여줍니다."
            ),
            discord.SelectOption(
                label="레이저 사이트",
                value="12",
                description="지향사격 정확도를 높여줍니다"
            ),
            discord.SelectOption(
                label="드럼탄창",
                value="13",
                description="경기관탄창"
            ),
            discord.SelectOption(
                label="30 발 AP탄",
                value="14",
                description="관통력을 높여줍니다."
            ),
            discord.SelectOption(
                label="30 발 JHP 탄",
                value="15",
                description="데미지를 높이는대신 관통력을 줄어듭니다."
            ),
            discord.SelectOption(
                label="go home",
                value="16",
                description="검색 리스트로 돌아갑니다."
            )
        ]
    )
    async def e_callback(self, select, interaction):
        if select.values[0] == "1":
            embed = discord.Embed(title="Holographic Sight",color=0x0096FF)
            embed.set_author(name="attachment : Sight",icon_url="https://hub.scpslgame.com/images/thumb/d/d3/IronSights_E11.png/75px-IronSights_E11.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/7/7b/Holo_E11.png/75px-Holo_E11.png")
            embed.add_field(name="zoom",value="```ansi\n[2;34mx1[0m\n```")
            embed.add_field(name="준비시간",value="```ansi\n[2;31m+0.14/s[0m```")
            embed.add_field(name="무게",value="```ansi\n[2;31m+13%[0m\n```")
            embed.set_footer(text="Mobile Task Force",icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "2":
            embed = discord.Embed(title="야간 조준경",description="```ansi\n[2;34mNight Vision[0m\n```",color=0x0096FF)
            embed.set_author(name="attachment : Sight",icon_url="https://hub.scpslgame.com/images/thumb/d/d3/IronSights_E11.png/75px-IronSights_E11.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/b/bc/NV_E11.png/100px-NV_E11.png")
            embed.add_field(name="배율",value="```ansi\n[2;34m1.4x\n[0m```")
            embed.add_field(name="조준시간",value="```ansi\n[2;31m+25%[0m\n```")
            embed.add_field(name="준비시간",value="```ansi\n[2;31m+0.08/s[0m\n```")
            embed.add_field(name="무게",value="```ansi\n[2;31m+35%[0m\n```")
            embed.set_footer(text="Mobile Task Force",icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "3":
            embed = discord.Embed(title="Telescopic Sight",description="고배율 스코프",color=0x0096FF)
            embed.set_author(name="attachment : Sight",icon_url="https://hub.scpslgame.com/images/thumb/d/d3/IronSights_E11.png/75px-IronSights_E11.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/4/44/Scope_E11.png/100px-Scope_E11.png")
            embed.add_field(name="배율",value="```ansi\n[2;34m7.25x\n[0m```")
            embed.add_field(name="조준사격 정확도",value="```ansi\n[2;34m+33%n[0m```")
            embed.add_field(name="준비시간",value="```ansi\n[2;31m+0.08/s[0m\n```")
            embed.add_field(name="무게",value="```ansi\n[2;31m+32%[0m\n```")
            embed.add_field(name="조준시간",value="```ansi\n[2;31m+30%[0m\n```")
            embed.set_footer(text="Mobile Task Force",icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "4":
            embed = discord.Embed(title="Rifle Body",description="조준사격의 최적화된 배럴",color=0x003DCA)
            embed.set_author(name="attachment : Body",icon_url="https://hub.scpslgame.com/images/thumb/0/0f/ShortBody.png/90px-ShortBody.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/28/RifleBody.png/100px-RifleBody.png")
            embed.add_field(name="데미지",value="```ansi\n[2;34m+7.5%[0m\n```")
            embed.add_field(name="관통력",value="```ansi\n[2;34m+12.5%[0m\n```")
            embed.add_field(name="총알정확도",value="```ansi\n[2;34m+54%[0m\n```")
            embed.add_field(name="발사속도",value="```ansi\n[2;31m-10%[0m\n```")
            embed.add_field(name="준비속도",value="```ansi\n[2;31m+0.13/s[0m\n```")
            embed.add_field(name="지향사격 정확도",value="```ansi\n[2;31m-26%[0m\n```")
            embed.add_field(name="무게",value="```ansi\n[2;31m+20%[0m\n```")
            embed.add_field(name="길이",value="```ansi\n[2;31m+46%[0m\n```")
            embed.set_footer(text="Mobile Task Force",icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "5":
            embed = discord.Embed(title="Suppressor",description="총격음을 줄여줍니다.",color=0x0096FF)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/c/c4/SuppressorE11.png/100px-SuppressorE11.png")
            embed.add_field(name="총알정확도",value="```ansi\n[2;34m-65%[0m\n```")
            embed.add_field(name="총알정확도",value="```ansi\n[2;34m+11%[0m\n```")
            embed.add_field(name="준비속도",value="```ansi\n[2;31m+0.08/s[0m\n```")
            embed.add_field(name="무게",value="```ansi\n[2;31m+19%[0m\n```")
            embed.add_field(name="길이",value="```ansi\n[2;31m+20%[0m\n```")
            embed.set_footer(text="Mobile Task Force",icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "6":
            embed = discord.Embed(title="Flash Hider",description="섬광을 없에줍니다.",color=0x0096FF)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/b/b4/FlashHiderE11.png/90px-FlashHiderE11.png")
            embed.add_field(name="준비속도",value="```ansi\n[2;31m+0.04/s[0m\n```")
            embed.add_field(name="무게",value="```ansi\n[2;31m+1%[0m\n```")
            embed.add_field(name="길이",value="```ansi\n[2;31m+2%[0m\n```")
            embed.set_footer(text="Mobile Task Force",icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "7":
            embed = discord.Embed(title="Muzzle Booster",color=0x0096FF)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/0/00/MuzzleBoosterE11.png/60px-MuzzleBoosterE11.png")
            embed.add_field(name="발사속도",value="```ansi\n[2;34m[1;34m+10%[0m[2;34m[0m\n```")
            embed.add_field(name="반동",value="```ansi\n[2;31m+30%[0m\n```")
            embed.add_field(name="총알정확도",value="```ansi\n[2;31m-17%[0m\n```")
            embed.add_field(name="준비속도",value="```ansi\n[2;31m+0.04/s[0m\n```")
            embed.add_field(name="무게",value="```ansi\n[2;31m+6%[0m\n```")
            embed.add_field(name="길이",value="```ansi\n[2;31m+1%[0m\n```")
            embed.set_footer(text="Mobile Task Force",icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "8":
            embed = discord.Embed(title="Muzzle Brake",description="반동을 줄여줍니다.",color=0x003DCA)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/b/b3/MuzzleBrake_0.png/60px-MuzzleBrake_0.png")
            embed.add_field(name="반동",value="```ansi\n[2;34m[1;34m-10%[0m[2;34m[0m\n```")
            embed.add_field(name="총격음",value="```ansi\n[2;31m+20%[0m\n```")
            embed.add_field(name="준비속도",value="```ansi\n[2;31m+0.04/s[0m\n```")
            embed.add_field(name="무게",value="```ansi\n[2;31m+2%[0m\n```")
            embed.add_field(name="길이",value="```ansi\n[2;31m+1%[0m\n```")
            embed.set_footer(text="Mobile Task Force",icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "9":
            embed = discord.Embed(title="Lightweight Stock",description="기동성이 뛰어난 개머리판",color=0x0096FF)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/e/ee/LightStock_0.png/100px-LightStock_0.png")
            embed.add_field(name="지향사격 정확도",value="```ansi\n[2;34m+18%[0m\n```")
            embed.add_field(name="준비시간",value="```ansi\n[2;34m-0.12s[0m\n```")
            embed.add_field(name="길이",value="```ansi\n[2;34m-1%[0m\n```")
            embed.add_field(name="무게",value="```ansi\n[2;34m-13%[0m\n```")
            embed.add_field(name="조준사격 반동",value="```ansi\n[2;31m+25%[0m\n```")
            embed.set_footer(text="Mobile Task Force",icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "10":
            embed = discord.Embed(title="Recoil-Reducing Stock",description="저격용 개머리판",color=0x003DCA)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/3/36/ShockStock.png/100px-ShockStock.png")
            embed.add_field(name="조준사격 반동",value="```ansi\n[1;2m[1;34m-33.3%[0m[0m\n```")
            embed.add_field(name="길이",value="```ansi\n[2;34m-1%[0m\n```")
            embed.add_field(name="준비시간",value="```ansi\n[2;31m+0.08/s[0m\n```")
            embed.add_field(name="무게",value="```ansi\n[2;31m+22%[0m\n```")
            embed.set_footer(text="Mobile Task Force",icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "11":
            embed = discord.Embed(title="Foregrip",description="반동을 줄여줍니다.",color=0x0096FF)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/c/c8/GripE11.png/60px-GripE11.png")
            embed.add_field(name="조준사격 반동",value="```ansi\n[1;2m[1;34m-15%[0m[0m\n```")
            embed.add_field(name="조준속도",value="```ansi\n[2;34m-15%[0m\n```")
            embed.add_field(name="무게",value="```ansi\n[2;31m+8%[0m\n```")
            embed.set_footer(text="Mobile Task Force",icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "12":
            embed = discord.Embed(title="Laser Sight",description="지향사격 정확도를 높여줍니다.",color=0x003DCA)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/a/ac/LaserE11.png/60px-LaserE11.png")
            embed.add_field(name="Hip-Firing Accuracy",value="```ansi\n[2;34m[1;34m+100%[0m[2;34m[0m\n```")
            embed.add_field(name="무게",value="```ansi\n[2;31m+11%[0m\n```")
            embed.set_footer(text="Mobile Task Force",icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "13":
            embed = discord.Embed(title="경기관 탄창",description="LMG MAG",color=0x003DCA)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/a/a1/Mag65FMJ.png/60px-Mag65FMJ.png")
            embed.add_field(name="Magazine Capacity",value="```ansi\n[2;34m[1;34m+25[0m[2;34m[0m\n```")
            embed.add_field(name="무게",value="```ansi\n[2;31m+79%[0m\n```")
            embed.add_field(name="장전시간",value="```ansi\n[2;31m[1;31m+2/s[0m[2;31m[0m\n```")
            embed.set_footer(text="Mobile Task Force",icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "14":
            embed = discord.Embed(title="30 x AP mag",description="관통력을 늘려줍니다.",color=0x003DCA)
            embed.set_author(name="attachment : Megazine",icon_url="https://hub.scpslgame.com/images/thumb/5/5e/Mag40FMJ.png/75px-Mag40FMJ.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/a/ad/Mag30AP.png/75px-Mag30AP.png")
            embed.add_field(name="관통력",value="```ansi\n[2;34m[1;34m+20%[0m[2;34m[0m\n```")
            embed.add_field(name="weight",value="```ansi\n[2;34m[1;34m-3%[0m[2;34m[0m```")
            embed.add_field(name="Magazine Capacity",value="```ansi\n[2;31m[1;31m-10[0m[2;31m[0m\n```")
            embed.set_footer(text="Mobile Task Force",icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "15":
            embed = discord.Embed(title="Low-Cap JHP Magazine",description="관통력을 줄이는대신 데미지가 늘어납니다.",color=0x003DCA)
            embed.set_author(name="attachment : Megazine",icon_url="https://hub.scpslgame.com/images/thumb/5/5e/Mag40FMJ.png/75px-Mag40FMJ.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/6/6e/Mag30JHP.png/75px-Mag30JHP.png")
            embed.add_field(name="데미지",value="```ansi\n[2;34m[1;34m+30%[0m[2;34m[0m\n```")
            embed.add_field(name="관통력",value="```ansi\n[2;31m[1;31m-50%[0m[2;31m[0m\n```")
            embed.add_field(name="weight",value="```ansi\n[2;34m[1;34m-3%[0m[2;34m[0m```")
            embed.add_field(name="Magazine Capacity",value="```ansi\n[2;31m[1;31m-10[0m[2;31m[0m\n```")
            embed.set_footer(text="Mobile Task Force",icon_url='https://hub.scpslgame.com/images/thumb/1/19/MTFCaptainIcon.png/180px-MTFCaptainIcon.png')
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "16":
            await interaction.response.edit_message(view=weapon_view())

class shoutgun_Attachment(discord.ui.View):
    @discord.ui.select(
        placeholder="choose a attachment",
        max_values=1,
        min_values=1,
        options=[
            discord.SelectOption(
                label="Double-shot system",
                value="1",
                description="Super Shoutgun"
            ),
            discord.SelectOption(
                label="Ammo Counter",
                value="2",
                description="탄약수를 알려줍니다."
            ),
            discord.SelectOption(
                label="Laser Sight",
                value="3",
                description="지향사격 정확도를 매우 높여줍니다."
            ),
            discord.SelectOption(
                label="Choke",
                value="4",
                description="패턴이 일정해집니다."
            )
        ]
    )
    async def shoutgun_callback(self, select, interaction):
        if select.values[0] == "1":
            embed = discord.Embed(title="Double-shot system",description="발사체 x 2",color=0x006826)
            embed.set_author(name="Attachment : trigger",icon_url="https://hub.scpslgame.com/images/thumb/9/9e/TriggerSingle.png/120px-TriggerSingle.png",url="https://en.scpslgame.com/index.php?title=Shotgun#Trigger")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/a/af/TriggerDouble.png/80px-TriggerDouble.png")
            embed.add_field(name="Projectiles Number",value="```ansi\n[2;32m[1;32m+100%[0m[2;32m[0m\n```")
            embed.add_field(name="발사속도",value="```ansi\n[2;31m-40%[0m\n```")
            embed.add_field(name="패턴 일관성",value="```ansi\n[2;31m-35%[0m\n```")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "2":
            embed = discord.Embed(title="Ammo Counter",description="남은 탄약수를 새워줍니다.",color=0x006826)
            embed.set_author(name="Attachment : Side",icon_url="https://hub.scpslgame.com/images/thumb/3/3a/ShotgunNoRail.png/120px-ShotgunNoRail.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/0/0e/FSP-9AmmoCounter.png")
            embed.add_field(name="weight",value="```ansi\n[2;31m+20%[0m\n```")
            await interaction.response.edit_message(embed=embed)
        if select.values[0] == "3":
            embed = discord.Embed(title="Lazer Sight",description="지향사격 정확도를 높여줍니다.")
            embed.add_field(name="지향사격 정확도",value="```ansi\n[2;32m[1;32m+100%[0m[2;32m[0m\n```")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/25/FSP-9Laser.png/120px-FSP-9Laser.png")
            embed.add_field(name="weight",value="```ansi\n[2;31m+5%[0m\n```")
            await interaction.response.edit_message(embed=embed)

class revolver_attachment(discord.ui.View):
    @discord.ui.select(
        placeholder="Select the attachment",
        max_values=1,
        min_values=1,
        options=[
            discord.SelectOption(
                label="6배율 조준경",
                description="저격총(?)",
                value="1"
            ),
            discord.SelectOption(
                label="10 인치 베럴",
                description="엄청난 파괴력",
                value="2"
            ),
            discord.SelectOption(
                label="숏 베럴",
                description="기동성 사기적 베럴",
                value="3"
            ),
            discord.SelectOption(
                label="Stock",
                description="조준사격 정확도",
                value="4"
            ),
            discord.SelectOption(
                label="4발 실린더",
                description="관통력이 엄청난 탄",
                value="5"
            ),
            discord.SelectOption(
                label="stock",
                description="조준사격의 최적화된 개머리판(?)",
                value="6"
            )
        ]
    )
    async def reveolver_callback(self, select, interaction):
        if select.values[0] == "1":
            embed = discord.Embed(title="Telescopic Sight",description="고배율 스코프",color=0x006826)
            embed.set_author(name="Attachment | Sight",icon_url="https://hub.scpslgame.com/images/b/b0/RevolverIronSight.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/c/c0/RevolverScope.png/150px-RevolverScope.png")
            embed.add_field(name="ADS zoom",value="```ansi\n[2;32m[1;32m6.15x[0m[2;32m[0m\n```")
            embed.add_field(name="준비시간",value="```ansi\n[2;31m+0.05/s[0m\n```")
            embed.add_field(name="무게",value="```ansi\n[2;31m+33%[0m\n```")
            embed.set_footer(text="Chaos Insurgent",icon_url="https://hub.scpslgame.com/images/thumb/e/ef/ChaosIcon.png/180px-ChaosIcon.png")
        if select.values[0] == "2":
            embed = discord.Embed(title="Long Barrel")