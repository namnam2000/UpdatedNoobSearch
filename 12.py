import discord
from discord.ext.commands import Bot
from discord.ext import commands
import requests
client = commands.Bot(command_prefix = "#")
token = "NTU4MzI4NzIzNjM2NzQ4MzA2.D3VPvQ.mXauhV-aAVnIi0MW0lvYE8KnDqc"


@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    if message.content.startswith("#"):
        final = str(message.content)[1:]
        final = final.replace(' ', '+')
        url = f"https://www.google.com/search?q={final}&oq={final}aqs=chrome.0.69i59j0l5.1427j0j7&sourceid=chrome&ie=UTF-8"
        webpage = requests.get(url)
        with open ('C:\\Users\Omri\Desktop\\text.txt', 'w') as file:
            file.write(webpage.text)
        hello = "yes no banana dudee= fdggdfg"
        start = (webpage.text).split('"ltr" href="/url?q=')
        end = start[1].split('&amp')
        end[0] = end[0].replace('<b>', '')
        end[0] = end[0].replace('</b>', '')
        await client.send_message(message.channel, end[0])

client.run(token)
