import discord 
from discord.ext import commands
import youtube_dl
from youtubesearchpython import VideosSearch


class music(commands.Cog):
    def init (self, client):
        self.client = client

    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("Pls join the join channel first")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
    
    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self,ctx,VideoTitle):
        
        print(VideoTitle)
        await self.join(ctx)
        FFMPEG_OPTIONS = {'before_options':'','options':'-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client
        videosSearch = VideosSearch(VideoTitle, limit = 1)
        resultDict = videosSearch.result()
        videoURL = resultDict['result'][0]['link']
        if ctx.voice_client.is_playing():
            print("SONG PLAYING and STOPPING IT")
            ctx.voice_client.stop()
            await self.join(ctx)



        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(videoURL, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2,
            **FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused ⏸️")

    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_channel.resume()
        await ctx.send("resume ▶️")



def setup(client):
    client.add_cog(music(client))