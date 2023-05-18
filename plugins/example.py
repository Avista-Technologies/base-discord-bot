from discord.ext import commands

class MyPlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello from MyPlugin!")

def setup(bot):
    bot.add_cog(MyPlugin(bot))
