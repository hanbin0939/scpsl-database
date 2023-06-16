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
            )
        ]
    )

    async def Scp_callback(self, select, interaction):
        if select.values[0] == "1":
            embed = discord.Embed(title="SCP-173",color=0xEC2222)
            embed.set_author(name="SCP Classes",icon_url="https://hub.scpslgame.com/images/thumb/0/0d/173_Icon_new.png/180px-173_Icon_new.png")
            embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/1/15/RenderSCP-173.png/353px-RenderSCP-173.png")
            embed.set_image(url="https://hub.scpslgame.com/images/thumb/2/20/LCZ173CC.png/425px-LCZ173CC.png")
            embed.set_footer(text="Spawn location : LCZ")
            embed.add_field(name="health",value="4000")
            embed.add_field(name="HS",value="750~1500")
            embed.add_field(name="speed",value="7.3~12.4")
            await interaction.response.edit_message(embed=embed,view=SCP_select())