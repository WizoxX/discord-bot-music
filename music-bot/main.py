import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))
TEXT_CHANNEL_ID = int(os.getenv("TEXT_CHANNEL_ID"))

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot connecté en tant que {bot.user}')

@bot.event
async def on_voice_state_update(member, before, after):
    if member.bot:
        return
    if after.channel:
        channel = bot.get_channel(TEXT_CHANNEL_ID)
        if channel:
            await channel.send(f"🎵 Hi {member.mention}! Type the name of a song or paste a link to play music!")

bot.run(TOKEN)
