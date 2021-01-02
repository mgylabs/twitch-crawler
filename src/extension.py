from discord.ext import commands
from src import highlight

def setup(bot):
    @commands.command()
    @bot.MGCert.verify(2)

    async def twitchHL(ctx, link):
        """
        Twitch Highlights 기능을 사용할 수 있습니다.
        """
        await ctx.send("트위치 하이라이트...")
    bot.add_command(twitch)

    async def twitchClip(ctx, amount):
        """
        오늘의 재밌는 클립을 추려서 보여줍니다
        """
        await ctx.send("오늘의 하이라이트:")

def teardown(bot):
    print('I am being unloaded!')
