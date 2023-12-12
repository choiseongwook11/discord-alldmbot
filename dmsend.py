import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇실행이 시작되었습니다.")
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
                    if message.author.id == 디스코드ID를 적기!!:
                        if message.author.id == 669422575432105984:
                            embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="서버")
                            embed.add_field(name="서버 전체 알림", value=msg, inline=True)
                            embed.set_footer(text=f"서버")


            async def on_message(message):
                pass

            client.run('봇의 토큰을 넣어주세요')
