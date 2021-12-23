from discord.ext import commands
from help_func import EmbedHelp, msgf
from asyncio import sleep


class Init(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def repeat(self, ctx, num=2, delay=0.8, *message):
        """Repeats|Spam a message"""
        message = " ".join(message)
       
        if message.strip() == "" or num == 0 or delay == 0:
            help = EmbedHelp(self.repeat, accepted_args=["num", "message"])
            await ctx.send(embed=await(help()))
            return
        else:
            for _ in range(num):
                await sleep(delay)
                await ctx.send(msgf(message))


def setup(bot) -> dict:
    return {
        "Object": Init(bot),
        "name": "Repeat it!",
        "description": "Adds Ability to Repeat|Spam a Message"
    }
