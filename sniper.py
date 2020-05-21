# Discord Nitro Sniper
# Made By Syntax
# Twitter: @CockSlime
# Github: https://github.com/cannabispowered

# Tested on Python 3.6.8
# With Discord API Version 1.2.5

import discord
import requests
from colorama import *

client = discord.Client()

# Define 'on_ready' messages
@client.event
async def on_ready():
        print('Logged in as:', client.user.name+"#"+client.user.discriminator)
        print('UID:', client.user.id)
        print('Discord version:', discord.__version__)
        print('Written by Syntax')
        print('Github: https://github.com/cannabispowered')

token = "" # Enter Your Token Here

# Define sniper
@client.event
async def on_message(message):
        if message.content.find("discord.gift") != -1:
                discordmsg = message.content
                nitro = discordmsg.split(".gift/")
                code = nitro[1]
                if len(code) < 16:
                        print(Fore.YELLOW+f"[!] Auto Detected a fake code: {code} in ({message.guild})")
                elif len(code) > 25:
                        print(Fore.YELLOW+f"[!] Auto Detected a fake code: {code} in ({message.guild})")
                else:
                        r = requests.get('https://discord.com/')

                        cookie_payload = {
                                '__cfduid' : r.cookies['__cfduid'],
                        }

                        header_payload = {
                                'Authorization' : token,
                                'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
                        }

                        payload = {
                                'channel_id': str(message.channel.id)
                        }

                        response = requests.post(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', headers=header_payload, cookies=cookie_payload, json=payload)
                        responsedata = response.text

                        if 'This gift has been redeemed already.' in responsedata:
                                print(Fore.RED+f"[!] Sadly this code has been redeemed already. | Code: {code} | Posted In '{message.guild}'")
                        elif 'nitro' in responsedata:
                                print(Fore.GREEN+f"[+] Nitro Sniped Successfully! | Code: {code} | Posted In '{message.guild}'")
                        elif 'Unknown Gift' in responsedata:
                                print(Fore.YELLOW+f"[-] An invalid code was posted | Code: {code} | Posted In '{message.guild}'")
                        else:
                                print(Fore.RED+f"[!] Unhandled Exception! - Try manually forging the request and checking the response!")

client.run(token, bot=False)
