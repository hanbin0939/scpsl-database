import discord

class itemlist(discord.ui.View):
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
    @discord.ui.button(label="light_armor",style=discord.ButtonStyle.gray)
    async def light_armor(self,buttom: discord.ui.Button, interaction: discord.Integration):
        embed = discord.Embed(title="light armor",description="so __weak__ armor")
        embed.set(url="https://hub.scpslgame.com/images/thumb/8/8d/LightArmorIcon.png/300px-LightArmorIcon.png")
        embed.add_field(name="body protection",value="40%",inline=False)
        await interaction.response.edit_message(embed=embed)
    @discord.ui.button(label="Combat Armor",style=discord.ButtonStyle.blurple)
    async def combat_armor(self,buttom: discord.ui.Button, interaction: discord.Integration):
        embed = discord.Embed(title="Combat_Armor",description="Reduces damage from bullets and grenades",color=0x003DCA)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/e/e2/CombatArmorIcon.png/300px-CombatArmorIcon.png")
        embed.add_field(name="body protection",value="60%",inline=False)
        embed.add_field(name="head protection",value="80%",inline=False)
        await interaction.response.edit_message(embed=embed)
    @discord.ui.button(label="heavy Armor",style=discord.ButtonStyle.blurple)
    async def heavy_armor(self,buttom: discord.ui.Button, interaction: discord.Integration):
        embed = discord.Embed(title="heavy_armor",description="Reduces damage from bullets and grenades",color=0xff0000)
        embed.set_thumbnail(url="https://hub.scpslgame.com/images/thumb/7/77/HeavyArmorIcon.png/300px-HeavyArmorIcon.png")
        embed.add_field(name="body protection",value="80%",inline=False)
        embed.add_field(name="head protection",value="80%",inline=False)
        await interaction.response.edit_message(embed=embed)
    