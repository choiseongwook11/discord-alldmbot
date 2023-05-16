


import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇실행이 시작되었습니다(24시간 온라인).")
    game = discord.Game('서버 관리')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == 669422575432105984:
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="스카니아 서버")
                        embed.add_field(name="스카니아 전체 알림", value=msg, inline=True)
                        embed.set_footer(text=f"스카니아 서버")
                        await i.send(embed=embed)
                except:
                    pass


client.run('ODA0NDgxNjI4NTg3ODE5MDA4.YBM95g.DUfyoYu4tf7qetEeBH2nO-wjnK4')
