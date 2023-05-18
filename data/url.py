import discord
from discord.ui.item import Item
class SimpleView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=30)  # times out after 30 seconds
        with_go = discord.ui.Button(label='with go', style=discord.ButtonStyle.link, url='https://www.youtube.com/channel/UC1D29Nmf3jWZEH1I-QfHlpA')
        button2 = discord.ui.Button(label='SCPSL Database support link',style=discord.ButtonStyle.link, url="https://discord.gg/nXqhQc6HcH")
        button3 = discord.ui.Button(label="Free_bat",style=discord.ButtonStyle.link,url="https://www.youtube.com/channel/UCFMiAdxy3TZ8K14Lfz-131w/")
        button4 = discord.ui.Button(label="hanbin",style=discord.ButtonStyle.link,url="https://www.youtube.com/channel/UCFGwzNRj1U12cEy9Re65hiA")
        self.add_item(with_go)
        self.add_item(button2)

class Server_Link(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=30)
        luna = discord.ui.Button(label="LUNA Server",style=discord.ButtonStyle.link,disabled=True,url="https://discord.gg/luna-official-1058752179105693716")
        chaous = discord.ui.Button(label="Chaous",style=discord.ButtonStyle.link,url="https://discord.gg/56K7fRbNJr")
        firebird = discord.ui.Button(label="fire bird",style=discord.ButtonStyle.link, url="https://discord.com/invite/tdST7mf5Yd")
        daon = discord.ui.Button(label="DAON",style=discord.ButtonStyle.link, url="https://discord.com/invite/cdhnnS2kVf")
        s79 = discord.ui.Button(label="079 SERVER",style=discord.ButtonStyle.link, url="https://discord.com/invite/msp2XaNka3")
        jdh = discord.ui.Button(label="JDH (자동핵)",style=discord.ButtonStyle.link, url="https://discord.com/invite/8jJrsEB4gP")
        rdg = discord.ui.Button(label="random game mode",style=discord.ButtonStyle.link, url="https://discord.gg/raendeomgeimmodeu-930837847026585600")
        self.add_item(luna)
        self.add_item(chaous)
        self.add_item(firebird)
        self.add_item(daon)
        self.add_item(s79)
        self.add_item(jdh)
        self.add_item(rdg)



#async def on_timeout(self):
#    await self.message.edit(content="Link timed out", view=None)