from os import environ
import discord
from datetime import datetime 

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_voice_state_update(member, before, after):
  if not before.channel and after.channel and member.id == 614062460256911364:
    channel = client.get_channel(1033079903647694858)
    await channel.send('USER IS IN VOICE')


if __name__ == "__main__":
  key = environ.get('DISCORD_TOKEN')
