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


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command(/a)
async def a(ctx):
    await ctx.send('GG Boyz:たいじ,ダイナモン,えとな,レン(Ren〆Zone)')
    
@bot.command(/b)
async def b(ctx):
    await ctx.send('Libalent Clamari:くろす,あとばる,ぴょん,2438学園')    
    

bot.run(token)
