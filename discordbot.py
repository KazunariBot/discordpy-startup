from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    

@bot.command()    
async def team(ctx): 
    
   teama = ['GG BoyZ', 
           'Libalent Clamari', 
           'BBV TOKYO', 
           '波乱万丈', 
           'TASO', 
           'DetonatioN Gaming', 
           '王の運搬クエスト(スプラ1より)']

   teamb = ['GG BoyZ', 
           'Libalent Clamari', 
           'BBV TOKYO', 
           '波乱万丈', 
           'TASO', 
           'DetonatioN Gaming', 
           '王の運搬クエスト(スプラ1より)']

   choicea = random.choice(teama)
   choiceb = random.choice(teamb)
    
   await ctx.send(choicea)
   await ctx.send(choiceb)
    
bot.run(token)
