from discord.ext import commands
from help_func import EmbedHelp, msgf
from random import choice
from discord import Embed


class Init(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flip(self, ctx):
        """Flips The Coin"""
        await ctx.send(
            embed=Embed(
                title="Flipping the coin",
                description=msgf(f"[B]{choice(['Head', 'Tail'])}[B] wins"),
            )
        )

    @commands.command(aliases=["format"])
    async def fmt(self, ctx, *msg):
        """Formats The String"""
        args = " ".join(msg)
        if args.strip() == "":
            help = EmbedHelp(self.fmt, accepted_args=['message'])
            await ctx.send(
                embed=await(help())
            )
        else:
            await ctx.message.delete()
            await ctx.send(msgf(args))


def setup(bot) -> dict:
    return {
        "Object": Init(bot),
        "name": "Formatter",
        "description": "Adds Ability to Format Messages"
    }
