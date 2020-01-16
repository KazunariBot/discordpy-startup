from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

'team1' = 'GG BoyZ:たいじ(シューター),ダイナモン(ラピ/バレ/ナモ/エク),えとな(シューター/バケ凸/キャンプ),Ren〆Zone(L3)'
'team2' = 'Libalent Clamari:くろす(ブラ系/バケ凸),あとばる(シューター),ぴょん(チャー系),2438学園(黒ZAP/黒マニュ)'
'team3' = 'BBV TOKYO:むしきんぐ(シューター),反射神経(クアッド),うどん店長(チャー系),のりすけ(H3D/わかば)'
'team4' = '波乱万丈:ろんつ(スクスロ),はんじょう(スプロラ),ku(マニュコラ),バズ(スピナー)'
'team5' = 'TASO:ゆっきー(ロンブラ),かよたそ(キャンプ/クアッド/青スパ),ガワタ(スシコラ/デュアカス),ぱいなぽ～(ブラ系/チャー系)'
'team6' = 'DetonatioN Gaming:ミリンケーキ(傘/L3),ku(マニュコラ/L3D),れき(ジェット/エク/バレ),けいとぅーん(バケ凸/キャンプ)'
'team7' = '王の運搬クエスト(スプラ1より):もこう(カー凸),たいじ(96凸),りんごもちぃ(96凸),ティラミス(96凸)'

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def abuki(ctx):
    await ctx.send('team1')
    
@bot.command()
async def bbuki(ctx):
    await ctx.send('team2')    
    
@bot.command()
async def cbuki(ctx):
    await ctx.send('team3')  
    
@bot.command()
async def dbuki(ctx):
    await ctx.send('team4')
    
@bot.command()
async def ebuki(ctx):
    await ctx.send('team5')      
    
@bot.command()
async def fbuki(ctx):
    await ctx.send('team6')    

@bot.command()
async def gbuki(ctx):
    await ctx.send('team7')    
    
bot.run(token)
