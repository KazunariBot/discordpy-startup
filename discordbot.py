from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@client.event
async def omikuzi(ctx):
    
import random

omikuzi = [
            "大吉"   if i < 2 else
            "中吉"   if 2 <= i < 10 else
            "小吉"   if 10 <= i < 20 else
            "吉"     if 20 <= i < 40 else
            "末吉"   if 40 <= i < 50 else
            "凶"     if 50 <= i < 55 else
            "中凶"   if 55 <= i < 59 else
            "大凶"   for i in range(61)]

print(omikuzi[random.randrange(len(omikuzi))])

await ctx.send(omikuzi[random.randrange(len(omikuzi))])
    
bot.run(token)
