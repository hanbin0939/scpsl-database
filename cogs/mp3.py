import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

class MusicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @discord.slash_command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @discord.slash_command()
    async def play_custom(self, ctx, *, filename):
        voice = ctx.voice_client
        voice.play(discord.FFmpegPCMAudio(filename))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1

def setup(bot):
    bot.add_cog(MusicCommands(bot))
