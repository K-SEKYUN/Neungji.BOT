import discord
import os

#Link = https://discord.com/api/oauth2/authorize?client_id=890077622988578868&permissions=2048&scope=bot

prefix = "!"
client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print("System Login!")
    print("==============")
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="!능지표"))

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    
    if message.content == f"{prefix}능지표":
        embed = discord.Embed(title='능지표', description='v1.0.0', color = 0xff0000)
        embed.image(url = "https://cdn.discordapp.com/attachments/890077090383265793/890077103733755914/unknown.png")
        await message.channel.send(embed=embed)

client.run(os.environ['token'])
