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
            )
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "1":
            embed = discord.Embed(title="com-15", description="기본적인 호신용권총", color=0xadadad)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/22/COM-15Icon.png/375px-COM-15Icon.png")
            embed.set_image(url='https://hub.scpslgame.com/images/e/e8/COM-15_Inspect_Animation.gif')
            embed.set_footer(text='| 기본대미지=25\n| 해드샷대미지=50')
            await interaction.response.edit_message(embed=embed,view=com_15_attachment())
        if select.values[0] == "2":
            embed = discord.Embed(title='COM-18', description="기본적인 호신용 권총", color=0x575757)
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/2/2e/IconCom18.png/250px-IconCom18.png')
            embed.set_footer(text='기본대미지=20\n최대대미지=70\n',icon_url=('https://hub.scpslgame.com/images/thumb/3/3f/WEAPONCATNEW3.png/180px-WEAPONCATNEW3.png'))
            embed.set_author(name='weapon',icon_url=("https://hub.scpslgame.com/images/thumb/7/72/NEWHUMANCAT.png/120px-NEWHUMANCAT.png"))
            await interaction.response.edit_message(embed=embed,view=com_18_Attachment())
        if select.values[0] == "3":
            embed = discord.Embed(title="fsp-9",description="시설경비의 기본무기",color=0x5B6370)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/4/4d/FSP-9Icon.png/250px-FSP-9Icon.png")
            embed.set_footer(text="기본대미지=22.3\n최대대미지=44.6")
            embed.set_image(url="https://hub.scpslgame.com/images/c/c8/FSP-9_Inspect_Animation.gif")
            await interaction.response.edit_message(embed=embed)


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

class Fsp9_attachment(discord.ui.View):
    @discord.ui.select(
        placeholder="choose a attachment",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(
                label="Holographic Sight",
                value="1",
                description="조준시아를 깔끔하게 해줍니다."
            ),
            discord.SelectOption(
                label="Flash Hider",
                value="2",
                description="Flash Suppression"
            ),
            discord.SelectOption(
                label="Suppressor",
                value="2",
                description="소음기"
            )
        ]
    )

    async def fsp_9_Callback(self,select,interaction):
        ...