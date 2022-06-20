import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is ready.')


@client.command(aliases=['purge', 'delete'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 1000000):
    await ctx.channel.purge(limit=amount)

client.run('OTg4NDg0MzA1NTQ0MTgzODg4.GFsVQQ.GAfB8MRtEKQSbdxIugp8bsKPkTkd4BqKRw82N4')
