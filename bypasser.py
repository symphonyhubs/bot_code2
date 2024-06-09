import discord
from discord.ext import commands
import requests
import time
from discord.ui import Button, View

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command()
async def fluxus(ctx, link):
    if link.startswith("https://flux.li/android/external/start.php?HWID="):
        waiting_embed = discord.Embed(title="⏳ WAIT", description="Try again if it doesn't send key 👀", color=0x00ff00)
        await ctx.reply(embed=waiting_embed)
        api_url = f"http://134.255.218.3:1206/fluxus/?url={link}&api_key=X"
        # Start the time
        start_time = time.time()
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            key = data.get("key")
            credits = data.get("Credits")
            embed = discord.Embed(title="Bypassed ✅", color=0x00ff00)
            embed.add_field(name="Key", value=f"```{key}```", inline=True)
            embed.add_field(name="Hold to copy [Mobile]", value=f"{key}", inline=True)
            embed.add_field(name="Time taken", value=f"{time.time() - start_time:.2f} seconds", inline=True)
            embed.set_footer(icon_url=ctx.author.avatar.url, text=f"Requested by {ctx.author.name} | Api - Jado0066 | Code - Faisal")
            await ctx.reply(embed=embed)

bot.run("MTI0NTM1ODE5NDIyNjg4ODg2Ng.GkDcL-.3VZf9yIewcG1zq9Hz-ea1RXZapiXgz_jyNwycM")
