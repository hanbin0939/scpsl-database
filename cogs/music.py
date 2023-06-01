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
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if not member.bot and after.channel is None:
            if not [m for m in before.channel.members if not m.bot]:
                await self.get_player(member.guild).teardown()

def setup(bot):
    bot.add_cog(Music(bot))