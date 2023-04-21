import discord
class SimpleView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=30)  # times out after 30 seconds
        with_go = discord.ui.Button(label='with go', style=discord.ButtonStyle.link, url='https://www.youtube.com/channel/UC1D29Nmf3jWZEH1I-QfHlpA')
        button2 = discord.ui.Button(label='SCPSL Database support link',style=discord.ButtonStyle.link, url="https://discord.gg/nXqhQc6HcH")
        button3 = discord.ui.Button(label="Free_bat",style=discord.ButtonStyle.link,url="https://www.youtube.com/channel/UCFMiAdxy3TZ8K14Lfz-131w/")
        button4 = discord.ui.Button(label="hanbin",style=discord.ButtonStyle.link,url="https://www.youtube.com/channel/UCFGwzNRj1U12cEy9Re65hiA")
        self.add_item(with_go)
        self.add_item(button2)