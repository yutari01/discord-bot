import discord, json
from discord.ext import commands, tasks
from urllib.request import urlopen

class General(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() 
    async def 온라인(self, ctx): 
        await ctx.send(":green_circle: 히나는 온라인이에요!")

    @commands.command() 
    async def 한강(self, ctx): 
        response = urlopen("https://api.hangang.msub.kr/").read().decode('utf-8')
        json_data = json.loads(response)
        temp = json_data['temp']
        time = json_data['time']
        station = json_data['station']
        await ctx.send(f":droplet: `{time}`시`{station}`기준으로 `{temp}`도에요.")

    @commands.command() 
    async def 코로나(self, ctx): 
        response = urlopen("https://capi.msub.kr/").read().decode('utf-8')
        json_data = json.loads(response)
        today_update = json_data['today']['update']
        today_confirmation = json_data['today']['confirmation']
        today_cured = json_data['today']['cured']
        today_isolation = json_data['today']['isolation']
        today_dead = json_data['today']['dead']
        today_suspicion = json_data['today']['suspicion']
        yes_confirmation = json_data['yesterday']['confirmation']
        yes_cured = json_data['yesterday']['cured']
        yes_isolation = json_data['yesterday']['isolation']
        yes_dead = json_data['yesterday']['dead']

        embed=discord.Embed(title="코로나-19 안내", url="http://ncov.mohw.go.kr/", description="오늘 코로나 확진 정보를 알려줘요", color=0x4f4fff)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/e/e2/Symbol_of_KDCA.jpg")
        embed.add_field(name="확진환자", value= today_confirmation+" "+yes_confirmation, inline=True)
        embed.add_field(name="격리해제", value=today_cured+" "+yes_cured, inline=True)
        embed.add_field(name="치료중", value=today_isolation+" "+yes_isolation, inline=True)
        embed.add_field(name="사망", value=today_dead+" "+yes_dead, inline=True)
        embed.add_field(name="검사중", value=today_suspicion, inline=True)
        embed.set_footer(text=today_update)
        await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(General(bot))