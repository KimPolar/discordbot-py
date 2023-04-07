import discord, datetime, random
from discord_webhook import DiscordWebhook
from discord.commands import Option
from math import *
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
from discord import File
from numpy import *
import os

bot = discord.Bot()
token = os.environ['token']

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
def telenum(callnum):
    callnum = int(callnum.replace("-","")[3:7])
    if callnum < 2180 or 3099 < callnum < 3200 or 3499 < callnum < 3900 or 3999 < callnum < 4200 or \
    4499 < callnum < 5100 or 5199 < callnum < 5500 or 5899 < callnum < 5970 or 6199 < callnum < 6500 or 7099 < callnum < 7200 or 8499 < callnum < 9500: #SKT인 경우
        return "SKT"
    if 2199 < callnum < 2500 or 3899 < callnum < 4000 or 5499 < callnum < 5900 or 7499 < callnum < 7800 or 7899 < callnum < 8500:
        return "LG U+"
    if 2179 < callnum < 2200 or 2499 < callnum < 3100 or 3199 < callnum < 3500 or 4199 < callnum < 4500 or 5099 < callnum < 5200 or 6499 < callnum < 6900 or 7199 < callnum < 7500 or 9499 < callnum:
        return "KT"
    else:
        return "미배정"

@bot.slash_command(description="Pong!")
async def ping(ctx):
    val = round(float(bot.latency)*1000,0)
    embed = discord.Embed(title = "😀" if val <= 200 else "😐" if val <= 500 else "☹️" if val <= 1000 else "🤬" if val > 1000 else "😅", color= 0x2aef65 if val <= 200 else 0xf0e853 if val <= 500 else 0xf0a92b if val <= 1000 else 0xef583f if val > 1000 else 0xa6f0ab)
    embed.add_field(name="Latency",value=str(val)+"ms")
    await ctx.respond(embed=embed)

@bot.slash_command(description="Rock! Scissors! Paper!")
async def 가위바위보(ctx,
             선택: Option(str, "가위바위보", choices=["가위","바위", "보"]),):
    h_ch = 선택
    b_ch = random.choice(["가위","바위","보"])
    rsp = {"가위":"✌️","바위":"✊","보":"🖐"}
    if b_ch == h_ch:
        embed = discord.Embed(title = "사람 " + rsp[h_ch] + " vs " + rsp[b_ch] + " 봇",description = "비겼습니다!", color = 0xEDEDDF)
    if (b_ch == "가위" and h_ch == "보") or (b_ch == "바위" and h_ch == "가위") or (b_ch == "보" and h_ch == "바위"):
        embed = discord.Embed(title = "사람 " + rsp[h_ch] + " vs " + rsp[b_ch] + " 봇",description = "졌습니다!", color = 0xEF7B78)
    if (h_ch == "가위" and b_ch == "보") or (h_ch == "바위" and b_ch == "가위") or (h_ch == "보" and b_ch == "바위"):
        embed = discord.Embed(title = "사람 " + rsp[h_ch] + " vs " + rsp[b_ch] + " 봇",description = "이겼습니다!", color = 0x87F0B1)
    await ctx.respond(embed=embed)
        
@bot.slash_command(description="방정식")
async def 인수분해(ctx,
              fx: Option(str, "방정식"),):
    x = symbols('x')
    await ctx.respond("입력한 식 : `" + str(fx) + "`\n인수분해한 식 : `" + str(factor(fx)) + "`\n방정식의 해 : `" + str(solve(fx)) + "`")

@bot.slash_command(description="계산기")
async def 계산(ctx,
             fx: Option(str, "계산식"),):
    await ctx.respond("입력한 식 : `" + str(fx) + "`\n답 : `" + str(float(eval(fx))) + "`")

@bot.slash_command(description="그래프")
async def 그래프(ctx,
             fx: Option(str, "함수"),
             범위: Option(int, "범위"),):
    plt.clf()
    x = np.arange(-1*범위, 범위)
    y = eval(fx)
    plt.figure(figsize=(20,10))
    plt.plot(x, y)
    plt.savefig('plot.png')
    await ctx.respond(file=File('./plot.png'))
    
@bot.slash_command(description="통신사별 원배정 국번")
async def 원국번(ctx,
              번호: Option(str, "전화번호"),):
    await ctx.respond(telenum(번호))
    
bot.run(token)
