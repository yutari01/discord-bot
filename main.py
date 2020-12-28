# YUTARI DISCORD MUSIC BOT
# https://github.com/Yutari/Discord-Music-Bot
# Contact me on Discord!

#import dependencies
import discord, json, asyncio, os, traceback
from discord.ext import commands, tasks


#config import
with open('config.json', 'r') as f:
    json_data = json.load(f)
    TOKEN = json_data['TOKEN']
    PREFIX = json_data['PREFIX']
    VERSION = json_data['VERSION']

bot = commands.Bot(command_prefix=PREFIX)

#import music
#for filename in os.listdir("Cogs"):

    #if filename.endswith(".py"):
    #    bot.load_extension(f"Cogs.{filename[:-3]}")

bot.load_extension("general")

@bot.event
async def on_ready():
    print(f"Logged in to {bot.user}")
    print(f"Version : {VERSION}")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"{PREFIX}도움 | {VERSION}"))
'''
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(":warning: 저에게 더 많은 정보를 주세요...")
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.send(":warning: 제가 알수 없는 명령어에요...")
'''

#run
bot.run(TOKEN)