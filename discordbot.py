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
    
    
async def team(ctx):
    
    team = [
    
    'GG BoyZ:たいじ(シューター),ダイナモン(ラピ/バレ/ナモ/エク),えとな(シューター/バケ凸/キャンプ),Ren〆Zone(L3)' if i < 2 else
    
    'Libalent Clamari:くろす(ブラ系/バケ凸),あとばる(シューター),ぴょん(チャー系),2438学園(黒ZAP/黒マニュ)' if 2 <= i < 10 else
    
    'BBV TOKYO:むしきんぐ(シューター),反射神経(クアッド),うどん店長(チャー系),のりすけ(H3D/わかば)' if 10 <= i < 20 else
    
    '波乱万丈:ろんつ(スクスロ),はんじょう(スプロラ),ku(マニュコラ),バズ(スピナー)' if 20 <= i < 40 else
    
    'TASO:ゆっきー(ロンブラ),かよたそ(キャンプ/クアッド/青スパ),ガワタ(スシコラ/デュアカス),ぱいなぽ～(ブラ系/チャー系)' if 40 <= i < 50 else
    
    'DetonatioN Gaming:ミリンケーキ(傘/L3),ku(マニュコラ/L3D),れき(ジェット/エク/バレ),けいとぅーん(バケ凸/キャンプ)' if 50 <= i < 59 else  

    '王の運搬クエスト(スプラ1より):もこう(カー凸),たいじ(96凸),りんごもちぃ(96凸),ティラミス(96凸)' for i in range(61)] 

    print(random.choice(team))
    
await ctx.send(random.choice(team))

    
bot.run(token)
