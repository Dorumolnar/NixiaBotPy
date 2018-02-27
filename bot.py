import os
import discord
import asyncio
from discord.ext import commands


startup_extensions = ["General"]
bot = commands.Bot("nb!")

@bot.event
async def on_ready():
    print('NixiaBot is on')

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot

@bot.command(pass_context=True)
async def gdpsdownload(ctx):
    await bot.say("For PC: http://www.mediafire.com/file/z41c0vgndpcxpwf/NixiaGDPS+2.11.zip")
    await asyncio.sleep(0.5)
    await bot.say("For android: http://www.mediafire.com/file/hfgfhgo5ac015z0/NixiaGDPS+2.11.apk")

@bot.command(pass_context=True)
async def gdpstextures(ctx):
    await bot.say("Texture for gdps: http://www.mediafire.com/file/psg48o4fg733z5q/NixiaGDPS+2.11+Resources.zip")

@bot.command(pass_context=True)
async def gdpsmodapp(ctx):
    await bot.say("Mod app: https://goo.gl/forms/xGIJGTc3QNvbLQt72")

@bot.command(pass_context=True)
async def discordmodapp(ctx):
    await bot.say("Discord mod app: https://goo.gl/forms/Eg8iTMerpuMG5aJj1")

@bot.command(pass_context=True)
async def gdpsmodcmds(ctx):
    await bot.say("Here are the gdps commands!")
    await asyncio.sleep(0.0)
    await bot.say(":fire:!rate na 0 0 0 to un-rate a level!")
    await asyncio.sleep(0.0)
    await bot.say(":fire:!rate (Diff) (Stars 1-10) (Verifycoins 0=no 1=yes) (Feature 0=no 1=yes")
    await asyncio.sleep(0.0)
    await bot.say(":fire:!feature (feature a level")
    await asyncio.sleep(0.0)
    await bot.say(":fire:!epic (epic feature a level)")
    await asyncio.sleep(0.0)
    await bot.say(":fire:!unepic (remove a level's epic feature)")
    await asyncio.sleep(0.0)
    await bot.say(":fire:!verifycoins (verify a level's coins)")
    await asyncio.sleep(0.0)
    await bot.say(":fire:!daily (make a level daily)")
    await asyncio.sleep(0.0)
    await bot.say(":fire:!weekly ([make a level weekly (weekly demon)]")
    await asyncio.sleep(0.0)
    await bot.say(":fire:!rename [name]")
    await asyncio.sleep(0.0)
    await bot.say(":fire:!description [description]")
    await asyncio.sleep(0.0)
    await bot.say(":fire:!pass (change the password of a level)")
    await asyncio.sleep(0.0)
    await bot.say(":fire:!public (make a level public)")
    await asyncio.sleep(0.0)
    await bot.say(":fire:!unlist (unlist a level)")
    await asyncio.sleep(0.0)
    await bot.say(":fire:!sharecp (all creators will get cp if it's a collab)")
    await asyncio.sleep(0.0)
    await bot.say(":fire:!delete")
    await asyncio.sleep(0.0)
    await bot.say(":fire:!setacc [name]")

@bot.command(pass_context=True, hidden=True)
async def secretcode123(ctx, message : str):
    team_list = ["awsomepeeeps"]
    entered_team = message.content[6:].lower()
    role = discord.utils.get(message.server.roles, name=entered_team)
    roles = [
        "413413408461815828",
    ]
    if role in message.author.roles:
        await bot.say("You already have awsome peeps!")
    else:
        try:
            await bot.add_roles(message.author, role)
            await bot.say("Succesfully added role Awsome Peeps.")
        except discord.Forbidden:
            await bot.say("I dont have perms to add roles!")

bot.run(os.getenv('TOKEN'))
