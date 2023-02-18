import discord

intents = discord.Intents().all()

client = discord.Client(intents=intents)

@client.event
async def on_raw_reaction_add(payload):
    guild_id = payload.guild_id
    guild = client.get_guild(guild_id)
    if payload.emoji.name == "😃":
        role = discord.utils.get(guild.roles, name="Happy")
        await payload.member.add_roles(role)
    elif payload.emoji.name == "😭":
        role = discord.utils.get(guild.roles, name="Sad")
        await payload.member.add_roles(role)
    elif payload.emoji.name == "😎":
        role = discord.utils.get(guild.roles, name="Cool")
        await payload.member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
    guild_id = payload.guild_id
    guild = client.get_guild(guild_id)
    member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
    if payload.emoji.name == "😃":
        role = discord.utils.get(guild.roles, name="Happy")
        await member.remove_roles(role)
    elif payload.emoji.name == "😭":
        role = discord.utils.get(guild.roles, name="Sad")
        await member.remove_roles(role)
    elif payload.emoji.name == "😎":
        role = discord.utils.get(guild.roles, name="Cool")
        await member.remove_roles(role)

client.run('MTA3NTc5ODU3MjkxOTk2NzgwNA.GntXhK.tkRt_6mBfLmooi1Oq1JRXTvroESVmGesq4mcIw')
