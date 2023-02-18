import discord

intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'The bot is online')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower() == 'hello':
        await message.channel.send(f'Hello')
    if message.content.lower() == 'hi':
        await message.add_reaction('\U0001F44B')

@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} react with {reaction.emoji}')

@client.event
async def on_message_edit(before, after):
    await before.channel.send(f'{before.author} edited a message.\nBefore: {before.content}\nAfter: {after.content}')

client.run('MTA3NTc5ODU3MjkxOTk2NzgwNA.GKliNg.D8OR1-9DjytwFWi8RWXfGobZRL6Se0t3OoXufI')
