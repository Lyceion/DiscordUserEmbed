#                      ____                        #
####################-=|NOTE|=-######################
#U SHOULD INPUT YOUR E-MAIL AND PASSWORD TO LINE-22#
#THIS IS FOR NORMAL DISCORD USERS...               #
#Programmed By Cylops. (Lyceion)                   #
####################################################
#Licensed By MIT's Casual License...



import asyncio
import discord
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print("Cylops' Core Is Online \[T]/")
    print("\n Name: %s || ID: %s"%(client.user.name, client.user.id))
    channelID = input("Please Input A Channel ID: ")
    Break_Varaible = "ext-msg"
    while True:
        msg = input("\nMessage To Send Server:")
        aaa = discord.Embed(color=0xff8000)
        aaa.add_field(name="Sent From Cylops' Core", value=msg, inline=False)
		aaa.set_footer(text="-|- Programmed By Cylops -|-")
        aaa.set_thumbnail(url="https://i.hizliresim.com/nlYg1M.jpg")
        main_channel = channelID
        await client.send_message(discord.Object(id=main_channel), embed=aaa)
        print("Message Has Been Sent!")

client.run('E-MAIL', 'PASS', bot=False)