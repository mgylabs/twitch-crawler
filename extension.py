from discord.ext import commands


def setup(bot):
    @commands.command()
    @bot.MGCert.verify(2)
    async def twitch(ctx):
        await ctx.send('Hello {0.display_name}.'.format(ctx.author))
    bot.add_command(twitch)


def teardown(bot):
    print('I am being unloaded!')
