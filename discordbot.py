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
    
   teama = ['GG BoyZ:たいじ(短シューター),ダイナモン(ラピ/バレ/ナモ/エク),えとな(中シューター/バケ凸/キャンプ),Ren〆Zone(L3)', 
            'Libalent Clamari:くろす(ブラ系/バケ凸),あとばる(中シューター),ぴょん(チャー系),2438学園(黒ZAP/黒マニュ)', 
            'BBV TOKYO:むしきんぐ(短シューター),反射神経(クア),うどん店長(チャー系),のりすけ(H3D/わかば)', 
            'DetonatioN Gaming:ミリンケーキ(傘/L3),ku(マニュコラ/L3D),れき(ジェッカス/エク),けいとぅーん(バケ凸/キャンプ)',
            'Pixio Monster:ぼむα(短シューター),るす(ナモ),ちかし(キャンプ),ごっどちゃそ(シマネ/わかば)',
            '波乱万丈:ろんつ(スクスロ),はんじょう(スプロラ),ku(マニュコラ),バズ(スピナー)', 
            'TASO:ゆっきー(ロンブラ),かよたそ(キャンプ/クア/青スパ),ガワタ(スシコラ/デュアカス),ぱいなぽ～(ブラ系/チャー系)', 
            'たいじ軍団:たいじ(スシコラ),りんごもちぃ(96凸),りょぼ(スプロラ),とリバード(ハイカス)',
            '王の運搬クエスト(スプラ1より):もこう(カー凸),たいじ(96凸),りんごもちぃ(96凸),ティラミス(96凸)',
            'ALWAYS:ナイツ(クゲヒュー/ハイカス),ここねのパパ(パブロ),しゅー(デュアカス),ほるもん(フロデコ/わかば)',
            'SOMETIMES:うま(スロッシャー系/わかば),にゃむら(リッター/ハイドラ),りつ(プラベチュ),なり(ラピベチュ)']

   teamb = ['GG BoyZ:たいじ(短シューター),ダイナモン(ラピ/バレ/ナモ/エク),えとな(中シューター/バケ凸/キャンプ),Ren〆Zone(L3)', 
            'Libalent Clamari:くろす(ブラ系/バケ凸),あとばる(中シューター),ぴょん(チャー系),2438学園(黒ZAP/黒マニュ)', 
            'BBV TOKYO:むしきんぐ(短シューター),反射神経(クア),うどん店長(チャー系),のりすけ(H3D/わかば)', 
            'DetonatioN Gaming:ミリンケーキ(傘/L3),ku(マニュコラ/L3D),れき(ジェッカス/エク),けいとぅーん(バケ凸/キャンプ)', 
            'Pixio Monster:ぼむα(短シューター),るす(ナモ),ちかし(キャンプ),ごっどちゃそ(シマネ/わかば)',
            '波乱万丈:ろんつ(スクスロ),はんじょう(スプロラ),ku(マニュコラ),バズ(スピナー)', 
            'TASO:ゆっきー(ロンブラ),かよたそ(キャンプ/クア/青スパ),ガワタ(スシコラ/デュアカス),ぱいなぽ～(ブラ系/チャー系)', 
            'たいじ軍団:たいじ(スシコラ),りんごもちぃ(96凸),りょぼ(スプロラ),とリバード(ハイカス)',
            '王の運搬クエスト(スプラ1より):もこう(カー凸),たいじ(96凸),りんごもちぃ(96凸),ティラミス(96凸)',
            'ALWAYS:ナイツ(クゲヒュー/ハイカス),ここねのパパ(パブロ),しゅー(デュアカス),ほるもん(フロデコ/わかば)',
            'SOMETIMES:うま(スロッシャー系/わかば),にゃむら(リッター/ハイドラ),りつ(プラベチュ),なり(ラピベチュ)']

   choicea = random.choice(teama)
   choiceb = random.choice(teamb)
    
   await ctx.send(choicea)
   await ctx.send(choiceb)
    
bot.run(token)
