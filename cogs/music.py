import discord
from discord.ext import commands
import wavelink

async def connect_nodes(self):
        await self.bot.wait_until_ready() # wait until the bot is ready

        await wavelink.NodePool.create_node(
        bot=self.bot,
        host="fsn.lavalink.alexanderof.xyz",
        port=2333,
        password = "lavalink",
        )

class Music(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.queue = []

    @commands.Cog.listener()
    async def on_ready(self):
        await connect_nodes(self)

    @commands.Cog.listener()
    async def on_wavelink_node_ready(self,node: wavelink.Node):
        print(f"{node.identifier} is ready.") # print a message
    
    @discord.slash_command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.respond("성공적으로 연결되었습니다!")
    
    @discord.slash_command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.respond("성공적으로 연결되었습니다!")

    @discord.slash_command()
    async def play(self,ctx, search: str):
        vc = ctx.voice_client
        if not vc:
            vc = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        if ctx.author.voice.channel.id != vc.channel.id:
            return await ctx.respond("You must be in the same voice channel as the bot.")
        song = await wavelink.YouTubeTrack.search(query=search, return_first=True)

        if not song:
            return await ctx.respond("No song found.")
        await vc.play(song)
        await ctx.respond(f"Now playing: `{vc.source.title}`")
        
    @discord.slash_command()
    async def stop(self,ctx):
        vc = ctx.voice_client
        await vc.stop()
        await ctx.respond(f"Sucessfully stoped")
    
    @discord.slash_command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.respond("disconnected :|")

def setup(bot):
    bot.add_cog(Music(bot))