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
async def abuki(ctx):
    await ctx.send('GG Boyz:たいじ(シューター),ダイナモン(ラピ/バレ/ナモ/エク),えとな(シューター/バケ凸/キャンプ),Ren〆Zone(バケ凸/L3)')
    
@bot.command()
async def bbuki(ctx):
    await ctx.send('Libalent Clamari:くろす(ブラ系/バケ凸),あとばる(シューター),ぴょん(チャー系),2438学園(黒ZAP/黒マニュ)')    
    
@bot.command()
async def cbuki(ctx):
    await ctx.send('Cool&Cool:むしきんぐ(シューター),反射神経(クアッド),うどん店長(チャー系),のりすけ(H3D/わかば)')  
    
@bot.command()
async def dbuki(ctx):
    await ctx.send('波乱万丈:ろんつ(スクスロ),はんじょう(スプロラ),ku(マニュコラ),バズ(スピナー)')
    
@bot.command()
async def ebuki(ctx):
    await ctx.send('TASO:ゆっきー(ロンブラ),かよたそ(キャンプ/クアッド/青スパ),ガワタ(スシコラ/デュアカス),ぱいなぽ～(ブラ系/チャー系)')      
    
@bot.command()
async def fbuki(ctx):
    await ctx.send('DetonatioN Gaming:ミリンケーキ(傘/L3),ku(マニュコラ/L3D),れき(ジェット/エク/バレ),けいとぅーん(バケ凸)')    

@bot.command()
async def gbuki(ctx):
    await ctx.send('王の運搬クエスト:もこう(カー凸),たいじ(96凸),りんごもちぃ(96凸),ティラミス(96凸)')    
    
bot.run(token)
