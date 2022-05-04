# import Discord packages
import discord
from discord.ext import commands
import music

# client ( bot )
client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    responses= {
        "bye":"huh finally ab shanti miljayegi ||| ja n ab bhi yhi pe pda hua hai",
        "aur kya chl rha hai jindagi me":"apun bot hai yaar bs slave bn ke rh gya hu",
        "tu hai kaun be":":sob: is oneside ka chela",
        "hello":"Hello!",
        "bhai bhai":"behen behen bol","help":"1)bye 2)aur kya chl rha hai jindagi me 3) tu kai kaun be 4)hello" 
    }
    
    if message.content.lower() in responses:
        await message.channel.send(responses[message.content.lower()])


cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)



# run the client on the server
client.run('OTY2MjU4OTQ4NDk3ODcwODY5.Yl_IxQ.b4gxPzJFt9YY-HcogzkH_tHX2RE')