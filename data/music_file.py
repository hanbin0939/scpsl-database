import discord 
Parabellum = discord.File(r'mp3/Parabellum_Theme.mp3')
SCPSL_retro = discord.File(r'mp3/SCP_SL_Main_theme_Famicon.mp3')
The_Final_Flash = discord.File(r'mp3/The_Final_Flash_of_Existence_2.mp3')
The_wating_game = discord.File(r'mp3/The_Waiting_Game.mp3')
class SL_music(discord.ui.View):
    @discord.ui.button(label="parabellum",style=discord.ButtonStyle.blurple)
    async def parabellum(self,buttom: discord.ui.Button, interaction: discord.Integration):
        await interaction.response.edit_message(file=Parabellum,view=SL_music())