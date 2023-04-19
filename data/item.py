import discord

class item(discord.ui.View):
    @discord.ui.button(label="radio",style=discord.ButtonStyle.green)
    async def radio(self,buttom: discord.ui.Button, interaction: discord.Integration):
        embed = discord.Embed(title="radio",color=0x008000)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/9/97/RadioIcon.png/300px-RadioIcon.png")
        embed.set_author(name="Hykia",icon_url="https://hub.scpslgame.com/images/thumb/e/e9/HykiaLogoNew.png/675px-HykiaLogoNew.png")
        embed.add_field(name="SR",value="108 meter")
        embed.add_field(name="MR",value="180 meter")
        embed.add_field(name="LR",value="1080 meter")
        embed.add_field(name="UR",value="7200 meter")
        await interaction.response.edit_message(embed=embed)
    
    