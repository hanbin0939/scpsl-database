import discord

bot = discord.Bot()

class MyView(discord.ui.View):
    @discord.ui.select( # the decorator that lets you specify the properties of the select menu
        placeholder = "Choose a Class!", # the placeholder text that will be displayed if nothing is selected
        min_values = 1, # the minimum number of values that must be selected by the users
        max_values = 1, # the maximum number of values that can be selected by the users
        options = [ # the list of options from which users can choose, a required field
            discord.SelectOption(
                label="D class",
                emoji="🟧",
                value = "1",
                description="Always dead bol"
            ),
            discord.SelectOption(
                label="Scientist",
                emoji="🟨",
                value = "2",
                description="Foundation reserchier"
            ),
            discord.SelectOption(
                label="facility guard",
                emoji="⚪",
                value = "3",
                description="MTF serculity agent"
            ),
            discord.SelectOption(
                label="MTF Captain",
                emoji="🔵",
                value= "4",
                description="MObile Task Force Captain"
            ),
            discord.SelectOption(
                label="MTF soldier",
                emoji="🔵",
                value="5",
                description="Mobile Task Force soldier"
            ),
            discord.SelectOption(
                label="Chaos Insurgent",
                emoji="🟢",
                value="6",
                description="Chaos Insurgency"
            )
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "1":
            embed = discord.Embed(title="D class personal",description="경계 : 시설 경비 or MTF\n중립 : 과학자\n아군 : 혼돈의반란",color=0xFF8E00)
            embed.set_author(name="civilion class",icon_url="https://hub.scpslgame.com/images/thumb/a/a0/ClassDIcon.png/180px-ClassDIcon.png")
            embed.add_field(name="item",value="None")
            await interaction.response.edit_message(embed=embed)

        if select.values[0] == "2":
            embed = discord.Embed(title="Scientist",description="아군:mtf & 시설경비\n중립 : D계급인원\n",color=0xFFFF7C)
            embed.set_author(name="civilion class",icon_url="https://hub.scpslgame.com/images/thumb/a/a9/ScientistIcon.png/180px-ScientistIcon.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/9/90/Scientist_%2812.0%29.png/653px-Scientist_%2812.0%29.png")
            await interaction.response.edit_message(embed=embed)
            
        if select.values[0] == "3":
            embed = discord.Embed(title="시설 경비원",description="적 : 혼돈의반란 & SCP\n아군:MTF & 과학자\n중립 또는 적:D계급인원",color=0x5B6370)
            embed.set_author(name="Military class",icon_url="https://hub.scpslgame.com/images/thumb/7/75/GuardIcon.png/180px-GuardIcon.png")
            embed.set_thumbnail(url='https://hub.scpslgame.com/images/thumb/3/3e/Facility_Guard_%2812.0%29.png/653px-Facility_Guard_%2812.0%29.png')
            await interaction.response.edit_message(embed=embed)

        if select.values[0] == "4":
            embed = discord.Embed(title="Mobil task force",description="적:혼돈의 반란 & SCP\n아군:과학자\n경계:D 계급인원",color=0x003DCA)
            embed.set_author(name="Military class",icon_url="https://hub.scpslgame.com/images/8/8e/Captain_Keycard.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/5/55/NTF_%2812.0%29.png/653px-NTF_%2812.0%29.png")
            await interaction.response.edit_message(embed=embed)

        if select.values[0] == "5":
            embed = discord.Embed(title="MTF soldier",description="적:혼돈의 반란 & SCP\n아군:과학자\n경계:D 계급인원",color=0x003DCA)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/7/7d/MTFPrivateIcon.png")
            await interaction.response.edit_message(embed=embed)
        
        if select.values[0] == "6":
            embed = discord.Embed(title="Chaos Insurgent",color=0x0D7D35)
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/2/2a/Chaos_Insurgent_%2812.0%29.png/435px-Chaos_Insurgent_%2812.0%29.png")
            await interaction.response.edit_message(embed=embed)
