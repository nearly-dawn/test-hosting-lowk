import discord
import os

intents = discord.Intents.default()
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.slash_command(name="ping", description="Check the bot's latency")
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.respond(f"🏓 Pong! `{latency}ms`")

bot.run("MTQ5NTYyNjM1NzA4MDg1MDQzMg.GjcuPk.wRgzoreh35_jkM8K3nlG8-DnfNt7ehSM04CQcU")
