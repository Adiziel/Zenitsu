from os
import discord
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_voice_state_update(member, before, after):
  global joined_member
  if before.channel == None:
    joined_member+=[str(member)]

  if after.channel == None:
    joined_member.remove(str(member))
    print('after user left joined members are {}'.format(joined_member))

  if not before.channel and after.channel:
    await spam_join_text()

  if before.channel and not after.channel:
    await spam_exit_text(member)

async def spam_join_text():
  global joined_member
  channel = client.get_channel(1033049227342905455)
  members = channel.members
  members = [('{}#{}'.format(member.name, member.discriminator), member.name, member.bot, member.id) for member in channel.members if member.bot==False]
  if len(members) == len(joined_member):
    print('House Full')
  else:
    for us in members:
      if us[0] in joined_member:
        pass
      else:
        await channel.send('<@{}>, join voice chat mate'.format(us[3]))
  
  print(joined_member)


async def spam_exit_text(member):
  global joined_member
  channel = client.get_channel(1033049227342905455)
  members = channel.members
  members = [('{}#{}'.format(member.name, member.discriminator), member.name, member.bot, member.id) for member in channel.members if member.bot==False]
  if len(joined_member) == 0:
    await channel.send('good talk everybody!!')
  else:
    await channel.send('Hey come back <@{}>, people are still talking'.format(member.id))
  
  print(joined_member)


if __name__ == "__main__":
  keep_alive()
  joined_member = []
  key = os.environ('DISCORD_TOKEN')
