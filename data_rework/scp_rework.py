import discord

class SCP_select(discord.ui.View):
    @discord.ui.select(
        placeholder="Choose A SCP",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(
                label="SCP173",
                value="1",
                description="조각상"
            ),
            discord.SelectOption(
                label="SCP096",
                value="2",
                description="햇빛은 쨍쨍 96머리 반짝!",
            ),
            discord.SelectOption(
                label="SCP939",
                value="3",
                description="what the dog doing..?"
            ),
            discord.SelectOption(
                label="SCP-049",
                value="4",
                description="Doctor"
            )
        ]
    )

    async def Scp_callback(self, select, interaction):
        if select.values[0] == "1":
            embed = discord.Embed(title="SCP-173",description="엉첨난 HP 와 속도를 가지고 있는 탱거 + 기동력 SCP 이며 이 SCP 를 계속 봐야합니다...",color=0xEC2222)
            embed.set_author(name="SCP Classes",icon_url="https://hub.scpslgame.com/images/thumb/0/0d/173_Icon_new.png/180px-173_Icon_new.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/1/15/RenderSCP-173.png/353px-RenderSCP-173.png")
            embed.set_footer(text="Spawn location : LCZ")
            embed.add_field(name="health",value="4000")
            embed.add_field(name="HS",value="750~1500")
            embed.add_field(name="speed",value="7.3~12.4")
            await interaction.response.edit_message(embed=embed,view=SCP_select())

        if select.values[0] == "2":
            embed = discord.Embed(title="SCP-096",description="쳐다볼시 096이 폭주합니다.",color=0xEC2222)
            embed.set_author(name="SCP classes",icon_url="https://hub.scpslgame.com/images/thumb/3/32/096_IconCAT.png/180px-096_IconCAT.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/f/f2/Docile_096Render.png/135px-Docile_096Render.png")
            embed.add_field(name="Health",value="2500")
            embed.add_field(name="HS",value="600~1200")
            embed.add_field(name="이동속도 (폭주시)",value="8.0")
            embed.add_field(name="이동속도 (돌진)",value="18.0")
            await interaction.response.edit_message(embed=embed,view=SCP_select())
        
        if select.values[0] == "3":
            embed = discord.Embed(title="SCP-939",color=0xEC2222)
            embed.set_author(name="SCP classes",icon_url="https://hub.scpslgame.com/images/thumb/3/35/939_Icon.png/180px-939_Icon.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/4/48/RenderSCP-939.png/375px-RenderSCP-939.png")
            embed.add_field(name="Hp",value="2400")
            embed.add_field(name="HS",value="350~700")
            embed.add_field(name="이동속도",value="4.3")
            embed.add_field(name="질주시 이동속도",value="7.2")
            await interaction.response.edit_message(embed=embed,view=SCP_select())