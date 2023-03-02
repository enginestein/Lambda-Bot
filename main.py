from urllib.request import urlopen
from arrays import burns
from arrays import hug_links
import os
import random
import json
import randfacts
import aiohttp
import logging
import asyncio
from colorama import Fore, Style
import datetime
import traceback
import disnake
from disnake.ext import commands
from topgg import Forbidden
from easy_pil import *


# https://discord.com/api/oauth2/authorize?client_id=1017975608942268416&permissions=4398046511095&scope=bot

intents = disnake.Intents.all()
print(Style.BRIGHT + "")
print(Fore.GREEN + "--------------------------------------------------------")
dictionary_check = True
timer_check = True 
content_check = True 
history_check = True
lev = ["Level-5+", "Level-10+", "Level-15+"]
level_num = [5, 10, 15]
_bot = commands.Bot(command_prefix='!', intents=intents)
_bot.remove_command('help')
amount_del = 0
rand = 0
logging.basicConfig(level=logging.INFO)
intents.members = True
voice_clients = {}
yt_dl_opts = {'format': 'bestaudio/best'}
song_played=[]
song_url=[]
chvc=[]
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'} #locking options for ffmpeg
time_window_milliseconds = 5000
max_msg_per_window = 5
author_msg_times = {}
sent_color = 0xE3E5E8
changed_color = 0xFAA61A
deleted_color = 0xF04747
colors = [1752220, 1146986, 3066993, 2067276, 3447003, 2123412, 10181046, 7419530, 15277667,15844367, 11342935, 12745742, 15105570, 11027200, 15158332, 10038562, 9807270, 9936031, 8359053, 12370112, 3426654, 2899536, 16776960]

@_bot.event
async def on_member_join(member: disnake.Member):
    with open('setup.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    channel = _bot.get_channel(int(data[str(member.guild.id)]['hello_byebye'][0]))
    embed = disnake.Embed(color=random.choice(colors))
    embed.add_field(name="Welcome to our server! I am bot, but accept this welcome", value=member.mention)
    await channel.send(embed=embed)

@_bot.event
async def on_member_remove(member: disnake.Member):
    with open('setup.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    channel = _bot.get_channel(int(data[str(member.guild.id)]['hello_byebye'][0]))
    embed = disnake.Embed(color=random.choice(colors))
    embed.add_field(name="One of our members have left", valiue=member.mention)
    await channel.send(embed=embed)

@_bot.event
async def on_ready(): 
    print(Style.BRIGHT  + ''' 
Made by-                   
          _>   `'-.  .--'/
     .--'` ._      `/   <_
      >,-' ._'.. ..__ . ' '-.
   .-'   .'`         `'.     '.
    >   / >`-.     .-'< \ , '._\'
   /    ; '-._>   <_.-' ;  '._>
   `>  ,/  /___\ /___\  \_  /
   `.-|(|  \o_/  \o_/   |)|`
       \;        \      ;/
         \  .-,   )-.  /   
          /`  .'-'.  `\'
         ;_.-`.___.'-.;
           
           Enginestein
              ''')
    print(f"Bot logged in as {_bot.user}")
    print("--------------------------------------------------------")


class Help(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Fun commands", style=disnake.ButtonStyle.green)
    async def fun(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(color=random.choice(colors))
        embed.set_author(name="Games an fun commands")

        commands = [("/hug <user>", "`Hug someone`", False),
              ("/meme", "`Get an meme`", False),
              ("/pmeme", "`Get an programming meme`", False),
              ("/fact", "`Get an fact`", False),
              ("/web_scrape", "`Scrape HTML of any web page`", False),
              ("/serverinfo", "`Get server info`", False),
              ("/advice <context>", "`Get an advice`", False),
              ("/userinfo <user>", "`Get some information about an user`", False),
              ("/roast <user>", "`Roasting?`", False),
              ("/pic", "`Get an cool picture`", False),
              ("/truth", "`Get an random truth question`", False),
              ("/compliment", "`Get an compliment`", False),
              ("/dadjokes", "`Get an dad joke`", False),
              ("/topic", "`Get an topic to chat on`", False)]

        for name, value, inline in commands:
            embed.add_field(name=name, value=value, inline=inline)
    
        await interaction.response.send_message(embed=embed)
    
    @disnake.ui.button(label="Economy commands", style=disnake.ButtonStyle.green)
    async def eco(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = disnake.Embed(color=random.choice(colors))
        embed.set_author(name="Economy commands")

        commands = [("/bal", "`Get your account balance`", False),
              ("/inv", "`Check your inventory`", False),
              ("/shop", "`Open shop`", False),
              ("/buy <item code>", "`Buy some items`", False),
              ("/crypto", "`Mine some crypto currency if you have an laptop`", False),
              ("/redeem <amount>", "`Redeem all of your crypto currency`", False),
              ("/jobs", "`See the job board`", False),
              ("/job <job code>", "`Get an job`", False),
              ("/subjects", "`Subjects to study`", False),
              ("/learn <subject>", "`Learn any subject`", False),
              ("/learnpoints", "`Get your points in every subject`", False),
              ("/top", "`Get global leaderboard of richest person`", False),
              ("/level", "`See your level`", False),
              ("/software", "`Make softwares if you have software engineer job`", False),
              ("/assemble", "`Assemble an computer if you have enough requirements`", False),
              ("/computer", "`Open your computer, see your programs and os`", False),
              ("/attack <member>", "`Use your spyware, malware or ransomware to earn money and items`", False),
              ("/run", "`Run your disnake bot, app or website`", False),
              ("/daily", "`Get your daily coins`", False),
              ("/retire", "`Retire from your current job`", False),
              ("/delete <program name>", "`Delete an program from your computer`", False),
              ("/loan <amount>", "`Get a loan`", False),
              ("/pay <amount>", "`Pay for loan`", False),
              ("/business", "`Start and navigate your business`", False),
              ("/lend", "`Check how much loan is left`", False),
              ("/send <member> <amount>", "`Send money to someone`", False) ]
        
        for name, value, inline in commands:
            embed.add_field(name=name, value=value, inline=inline)
    
        await interaction.response.send_message(embed=embed)

@_bot.slash_command(description='Get help for commands')
async def help(ctx):
    await ctx.send(view=Help())

@_bot.slash_command(description='Get an topic to chat on')
async def topic(ctx):
    lines = open("topics.txt").read().splitlines()
    embed = disnake.Embed(color=random.choice(colors))
    embed.add_field(name='Topic', value=random.choice(lines))
    await ctx.send(embed=embed)

@_bot.slash_command(description="Get user information")
async def userinfo(ctx, user: disnake.Member):
        if user is None:
            color = disnake.Color(value=random.choice(colors))
            em = disnake.Embed(color=color, title=f'User Info: {ctx.author.name}')
            em.add_field(name='Status', value=f'{ctx.author.status}')       
            em.add_field(name='Account Created', value=ctx.message.author.created_at)
            em.add_field(name='ID', value=f'{ctx.author.id}')
            em.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=em)
        else:
            color = disnake.Color(value=random.choice(colors))
            em = disnake.Embed(color=color, title=f'User Info: {user.name}')
            em.add_field(name='Status', value=f'{user.status}')       
            em.add_field(name='Account Created', value=user.created_at)
            em.add_field(name='ID', value=f'{user.id}')
            em.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=em)        

async def learnp(ctx):
    await learning_points(ctx)
    await open_account(ctx)
    with open('learning_points.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    p = data[str(ctx.author.id)]['Physics']
    c = data[str(ctx.author.id)]['Chemistry']
    b = data[str(ctx.author.id)]['Biology']     
    cs =  data[str(ctx.author.id)]['Computer science']
    m = data[str(ctx.author.id)]['Maths']
     
    with open('account.json', 'r', encoding='utf-8') as file:
        data2 = json.load(file)

    if p == 15:
        await ctx.send("You have gained an Physics science degree")
        data2[str(ctx.author.id)]['Inventory'].append("Computer science degree")
        with open('account.json', 'w') as file:
            json.dump(data2, file)

def akinator_embed(question: str = None, counter: int = None, guess=None) -> disnake.Embed:
    if guess and not (question and counter):
        embed = disnake.Embed(title=f"My Guess", color=random.choice(colors))
        embed.add_field("Name", guess["name"], inline=False)
        embed.add_field("Description", guess["description"], inline=False)
        embed.set_thumbnail(guess["absolute_picture_path"])
    else:
        embed = disnake.Embed(
            title=f"Question no. {counter}: {question}", color=random.choice(colors)
        )

    return embed

async def log_in(user):
    with open('login.json', 'r', encoding='utf-8') as file:
        data = json.load(file)  

    if str(user.author.id) in data:
        return False
    else:
        data[str(user.author.id)] = {}
        data[str(user.author.id)]['OS'] = ["Windows XP"]
        data[str(user.author.id)]['Programs'] = ["System files"]
    
    with open('login.json', 'w') as f:
        json.dump(data, f)
    
    return True

class Attack(disnake.ui.View):
    def __init__(self, member: disnake.Member):
        super().__init__(timeout=None)

        self.member = member

    @disnake.ui.button(label="Ransomware", style=disnake.ButtonStyle.red)
    async def ransomware(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):

        computers = ["Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954>💾", "Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555>💾", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️💾", "Computer🖱️🖥️⌨️<:disnakeFloppy:987628788256997377>"]
        with open('account.json', 'r', encoding='utf-8') as f:
            file = json.load(f)
        
        if any(computer in file[str(interaction.user.id)]["Inventory"] for computer in computers):
            with open("login.json", 'r', encoding='utf-8') as r:
                f = json.load(r)
            
            if "Ransomware" in f[str(interaction.user.id)]["Programs"]:
                possiblities = ["pc_locked", "pc_locked_not", "reverse_shelled"]
                crypto_amt = random.randrange(file[str(self.member.id)]['Crypto'])

                inv = file[str(interaction.user.id)]['Inventory']
                inv2 = file[str(self.member.id)]['Inventory']
                c = random.choice(possiblities)
                if c == "pc_locked":
                    if crypto_amt != 0:
                        file[str(interaction.user.id)]['Crypto'] += crypto_amt
                        file[str(self.member.id)]['Inventory'] -= crypto_amt
                        embed = disnake.Embed(color=random.choice(colors))
                        embed.add_field(name="Ransomware worked and you have gained", value=f"{crypto_amt} Crypto")
                        await interaction.response.send_message(embed=embed)
                        with open('account.json', 'w') as f:
                            json.dump(file, f)
                    else:
                        embed = disnake.Embed(color=random.choice(colors))
                        embed.add_field(name="Failed", value="Victim doesnt have any crypto")
                        await interaction.response.send_message(embed=embed)

                elif c == "pc_locked_not":
                    embed = disnake.Embed(color=random.choice(colors))
                    embed.add_field(name="Failed", value="Ransomware was not able to lock programs")
                    await interaction.response.send_message(embed=embed)

                elif "Antivirus <:blurple_shield:1001104190875107429>" in inv2:
                    embed = disnake.Embed(color=random.choice(colors))
                    embed.add_field(name="Failed", value="Victim had antivirus")
                    await interaction.response.send_message(embed=embed)

                elif c == 'reverse_shelled':
                    if "Antivirus <:blurple_shield:1001104190875107429>" in inv:
                        embed = disnake.Embed(color=random.choice(colors))
                        embed.add_field(name="Failed", value="The victim reverse shelled on your but glad you had antivirus")
                        await interaction.response.send_message(embed=embed)
                    else:
                        embed = disnake.Embed(color=random.choice(colors))
                        embed.add_field(name="Failed", value="victim wasn't a victim, now you are a victim, he reverse shelled on you, you paid him 5000 <:nerd_coin:992265892756979735>")
                        await interaction.response.send_message(embed=embed)
                        file[str(interaction.user.id)]['Bank'] -= 5000
                        with open('account.json', 'w') as f:
                            json.dump(file, f)
                
            else:
                embed = disnake.Embed(color=random.choice(colors))
                embed.add_field(name="Failed", value="You don't have an ransomware, create it using /software")
                await interaction.response.send_message(embed=embed)
        else:
            embed = disnake.Embed(color=random.choice(colors))
            embed.add_field(name="Failed", value="You think you are gonna use an software without an computer? make one with /assemble if you have enough items")
            await interaction.response.send_message(embed=embed)
            
    
    @disnake.ui.button(label="Spyware", style=disnake.ButtonStyle.red)
    async def spyware(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        with open('account.json', 'r', encoding='utf-8') as f:
            data2 = json.load(f)
        
        computers = ["Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954>💾", "Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555>💾", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️💾", "Computer🖱️🖥️⌨️<:disnakeFloppy:987628788256997377>"]

        if any(computer in data2[str(interaction.user.id)]['Inventory'] for computer in computers):
            if "Coin Booster <:DigitalTwo:1003623866272329748>" in data2[str(interaction.user.id)]["Inventory"]:
                with open("login.json", 'r', encoding='utf-8') as r:
                    f = json.load(r)
            
                if "Spyware" in f[str(interaction.user.id)]["Programs"]:
                    if "Antivirus <:blurple_shield:1001104190875107429>" not in data2[str(self.member.id)]["Inventory"]:
                        ps = ['yes', 'no']
                        choice = random.choice(ps)
                        if choice == 'yes':
                            amt = random.randrange(data2[str(self.member.id)]["Bank"])

                            if data2[str(self.member.id)]["Bank"] != 0:
                                data2[str(interaction.user.id)]['Bank'] += (amt * 2)
                                data2[str(self.member.id)]["Bank"] -= amt
                                with open('account.json', 'w') as f:
                                    json.dump(data2, f)
                                
                                embed = disnake.Embed(color=random.choice(colors))
                                embed.add_field(name="Sucess, You gain", value=f"{amt * 2} <:nerd_coin:992265892756979735>'")
                                await interaction.response.send_message(embed=embed)
                            else:
                                embed = disnake.Embed(color=random.choice(colors))
                                embed.add_field(name="Failed", value='Victim has no money')
                                await interaction.response.send_message(embed=embed)

                        else:
                            embed = disnake.Embed(color=random.choice(colors))
                            embed.add_field(name="Failed", value="You got none of victim data")
                            await interaction.response.send_message(embed=embed)
                    else:
                        embed = disnake.Embed(color=random.choice(colors))
                        embed.add_field(name="Failed", value="Victim had an antivirus")
                        await interaction.response.send_message(embed=embed)
                else:
                    embed = disnake.Embed(color=random.choice(colors))
                    embed.add_field(name="Failed", value="You don't have an spyware, create it using /software")
                    interaction.response.send_message(embed=embed)
            else:
                with open("login.json", 'r', encoding='utf-8') as r:
                    f = json.load(r)
            
                if "Spyware" in f[str(interaction.user.id)]["Programs"]:
                    if "Antivirus <:blurple_shield:1001104190875107429>" not in data2[str(self.member.id)]["Inventory"]:
                        ps = ['yes', 'no']
                        choice = random.choice(ps)
                        if choice == 'yes':
                            amt = random.randrange(data2[str(self.member.id)]["Bank"])

                            if data2[str(self.member.id)]["Bank"] != 0:
                                data2[str(interaction.user.id)]['Bank'] += amt
                                data2[str(self.member.id)]["Bank"] -= amt
                                with open('account.json', 'w') as f:
                                    json.dump(data2, f)
                                
                                embed = disnake.Embed(color=random.choice(colors))
                                embed.add_field(name="Sucess, You gain", value=f"{amt} <:nerd_coin:992265892756979735>'")
                                await interaction.response.send_message(embed=embed)
                            else:
                                embed = disnake.Embed(color=random.choice(colors))
                                embed.add_field(name="Failed", value='Victim has no money')
                                await interaction.response.send_message(embed=embed)

                        else:
                            embed = disnake.Embed(color=random.choice(colors))
                            embed.add_field(name="Failed", value="You got none of victim data")
                            await interaction.response.send_message(embed=embed)
                    else:
                        embed = disnake.Embed(color=random.choice(colors))
                        embed.add_field(name="Failed", value="Victim had an antivirus")
                        await interaction.response.send_message(embed=embed)
                else:
                    embed = disnake.Embed(color=random.choice(colors))
                    embed.add_field(name="Failed", value="You don't have an spyware, create it using /software")
                    interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("You don't have a computer, assemble one, make an program then run it")
                
    
    @disnake.ui.button(label="Malware", style=disnake.ButtonStyle.red)
    async def malware(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction): 
        computers = ["Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954>💾", "Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555>💾", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️💾", "Computer🖱️🖥️⌨️<:disnakeFloppy:987628788256997377>"]
        with open('account.json', 'r', encoding='utf-8') as f:
            file = json.load(f)
        
        if any(computer in file[str(interaction.user.id)]["Inventory"] for computer in computers):
            with open("login.json", 'r', encoding='utf-8') as r:
                f = json.load(r)
            
            if "Malware" in f[str(interaction.user.id)]["Programs"]:
                if "Antivirus <:blurple_shield:1001104190875107429>" in file[str(self.member.id)]["Inventory"]:
                    embed = disnake.Embed(color=random.choice(colors))
                    embed.add_field(name="Failed", value="Victim has an antivirus")
                    await interaction.response.send_message(embed=embed)
                
                else:

                    tem = ["Antivirus <:blurple_shield:1001104190875107429>", "AI Software <:galaxy_brain:1003621546050474034>", "Coin Booster <:DigitalTwo:1003623866272329748>", "Windows 10 <:windows_10:1003626037713842228>", "Kali linux <:kali:1003630422560886905>", 'no tem']
                    if any(item in file[str(self.member.id)]["Inventory"] for item in tem):
                        cc = random.choice(tem)
                        file[str(interaction.user.id)]['Inventory'].append(cc)
                        file[str(self.member.id)]["Inventory"].remove(cc)
                        embed = disnake.Embed(color=random.choice(colors))
                        embed.add_field(name="Success, your malware brought you", value=cc)
                        await interaction.response.send_message(embed=embed)
                        with open('account.json', 'w') as f:
                            json.dump(file, f)
                
                    else:
                        embed = disnake.Embed(color=random.choice(colors))
                        embed.add_field(name="Failed", value="Victim has nothing")
                        await interaction.response.send_message(embed=embed)
        else:
            embed = disnake.Embed(color=random.choice(colors))
            embed.add_field(name="Failed", value="You don't have a computer, assemble one, make an program then run it")
            await interaction.response.send_message(embed=embed)

class Software(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Ransomware", style=disnake.ButtonStyle.blurple)
    async def ransomware(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        computers = ["Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954>💾", "Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555>💾", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️💾", "Computer🖱️🖥️⌨️<:disnakeFloppy:987628788256997377>"]
        with open('account.json', 'r', encoding='utf-8') as f:
            file = json.load(f)
        
        if any(computer in file[str(interaction.user.id)]["Inventory"] for computer in computers):
            await interaction.response.send_message("You have made an Ransomware, it is now in your programs")
            with open('login.json', 'r', encoding='utf-8') as login:
                d = json.load(login)
            
            d[str(interaction.user.id)]["Programs"].append("Ransomware")
            with open('login.json', 'w') as login:
                json.dump(d, login)
        else:
            embed = disnake.Embed(color=random.choice(colors))
            embed.add_field(name="Failed", value="You don't have a computer, assemble one.")
            await interaction.response.send_message(embed=embed)
    
    @disnake.ui.button(label="Spyware", style=disnake.ButtonStyle.blurple)
    async def spyware(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        computers = ["Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954>💾", "Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555>💾", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️💾", "Computer🖱️🖥️⌨️<:disnakeFloppy:987628788256997377>"]
        with open('account.json', 'r', encoding='utf-8') as f:
            file = json.load(f)
        
        if any(computer in file[str(interaction.user.id)]['Inventory'] for computer in computers):
            embed = disnake.Embed(color=random.choice(colors))
            embed.add_field(name="Success", value="You have made an Spyware, it is now in your programs")
            await interaction.response.send_message(embed=embed)
            with open('login.json', 'r', encoding='utf-8') as login:
                d = json.load(login)
            
            d[str(interaction.user.id)]["Programs"].append("Spyware")
            with open('login.json', 'w') as login:
                json.dump(d, login)
        else:
            embed = disnake.Embed(color=random.choice(colors))
            embed.add_field(name="Failed", value="You don't have a computer, assemble one.")
            await interaction.response.send_message(embed=embed)
    
    @disnake.ui.button(label="Malware", style=disnake.ButtonStyle.blurple)
    async def malware(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        computers = ["Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954>💾", "Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555>💾", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️💾", "Computer🖱️🖥️⌨️<:disnakeFloppy:987628788256997377>"]
        with open('account.json', 'r', encoding='utf-8') as f:
            file = json.load(f)
        
        if any(computer in file[str(interaction.user.id)]['Inventory'] for computer in computers):
            embed = disnake.Embed(color=random.choice(colors))
            embed.add_field(name="Success", value="You have made an Malware, it is now in your programs")
            await interaction.response.send_message(embed=embed)
            with open('login.json', 'r', encoding='utf-8') as login:
                d = json.load(login)
            
            d[str(interaction.user.id)]["Programs"].append("Malware")
            with open('login.json', 'w') as login:
                json.dump(d, login)
        else:
            embed = disnake.Embed(color=random.choice(colors))
            embed.add_field(name="Failed", value="You don't have a computer, assemble one.")
            await interaction.response.send_message(embed=embed)
    
    @disnake.ui.button(label="disnake bot", style=disnake.ButtonStyle.blurple)
    async def disordbot(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        computers = ["Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954>💾", "Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555>💾", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️💾", "Computer🖱️🖥️⌨️<:disnakeFloppy:987628788256997377>"]
        with open('account.json', 'r', encoding='utf-8') as f:
            file = json.load(f)
        
        if any(computer in file[str(interaction.user.id)]['Inventory'] for computer in computers):
            embed = disnake.Embed(color=random.choice(colors))
            embed.add_field(name="Success", value="You have made an disnake bot, it is now in your programs")
            await interaction.response.send_message(embed=embed)
            with open('login.json', 'r', encoding='utf-8') as login:
                d = json.load(login)
            
            await disnakebot(interaction)

            d[str(interaction.user.id)]["Programs"].append("disnake bot")
            with open('login.json', 'w') as login:
                json.dump(d, login)
        else:
            embed = disnake.Embed(color=random.choice(colors))
            embed.add_field(name="Failed", value="You don't have a computer, assemble one.")
            await interaction.response.send_message(embed=embed)

    @disnake.ui.button(label="App", style=disnake.ButtonStyle.blurple)
    async def app(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        computers = ["Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954>💾", "Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555>💾", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️💾", "Computer🖱️🖥️⌨️<:disnakeFloppy:987628788256997377>"]
        with open('account.json', 'r', encoding='utf-8') as f:
            file = json.load(f)
        
        if any(computer in file[str(interaction.user.id)]['Inventory'] for computer in computers):
            embed = disnake.Embed(color=random.choice(colors))
            embed.add_field(name="Success", value="You have made an App, it is now in your programs")
            await interaction.response.send_message(embed=embed)
            with open('login.json', 'r', encoding='utf-8') as login:
                d = json.load(login)
            
            await app(interaction)

            d[str(interaction.user.id)]["Programs"].append("App")
            with open('login.json', 'w') as login:
                json.dump(d, login)
        else:
            embed = disnake.Embed(color=random.choice(colors))
            embed.add_field(name="Failed", value="You don't have a computer, assemble one.")
            await interaction.response.send_message(embed=embed)
    
    @disnake.ui.button(label="Website", style=disnake.ButtonStyle.blurple)
    async def web(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        computers = ["Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954>💾", "Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555>💾", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️💾", "Computer🖱️🖥️⌨️<:disnakeFloppy:987628788256997377>"]
        with open('account.json', 'r', encoding='utf-8') as f:
            file = json.load(f)
        
        if any(computer in file[str(interaction.user.id)]['Inventory'] for computer in computers):
            embed = disnake.Embed(color=random.choice(colors))
            embed.add_field(name="Success", value="You have made an Website, it is now in your programs")
            await interaction.response.send_message(embed=embed)
            with open('login.json', 'r', encoding='utf-8') as login:
                d = json.load(login)
            
            await website(interaction)


            d[str(interaction.user.id)]["Programs"].append("Website")
            with open('login.json', 'w') as login:
                json.dump(d, login)
        else:
            embed = disnake.Embed(color=random.choice(colors))
            embed.add_field(name="Failed", value="You don't have a computer, assemble one.")
            await interaction.response.send_message(embed=embed)

#CoolPreTeensAlt#9914   

async def disnakebot(user):
    with open('dbot.json', 'r', encoding='utf-8') as file:
        data = json.load(file)  

    if str(user.author.id) in data:
        return False
    else:
        data[str(user.author.id)] = {}
        data[str(user.author.id)]['Servers'] = 1
        data[str(user.author.id)]['Commands'] = 1       
    
    with open('dbot.json', 'w') as f:
        json.dump(data, f)
    
    return True

async def website(user):
    with open('web.json', 'r', encoding='utf-8') as file:
        data = json.load(file)  

    if str(user.author.id) in data:
        return False
    else:
        data[str(user.author.id)] = {}
        data[str(user.author.id)]['Signed in people'] = 1      
    
    with open('web.json', 'w') as f:
        json.dump(data, f)
    
    return True

async def app(user):
    with open('app.json', 'r', encoding='utf-8') as file:
        data = json.load(file)  

    if str(user.author.id) in data:
        return False
    else:
        data[str(user.author.id)] = {}
        data[str(user.author.id)]['Downloads'] = 1          
    
    with open('app.json', 'w') as f:
        json.dump(data, f)
    
    return True

class Web(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @disnake.ui.button(label="Advertise", style=disnake.ButtonStyle.blurple)
    async def ad(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        with open("account.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        if data[str(interaction.user.id)]["Bank"] >= 10000:
            with open('web.json') as file2:
                data2 = json.load(file2)
            
            data2[str(interaction.user.id)]["Signed in people"] += random.randrange(10)
            data[str(interaction.user.id)]["Bank"] -= 10000

            with open("account.json", 'w') as file:
                json.dump(data, file)

            with open("web.json", 'w') as file2:
                json.dump(data2, file2)

            await interaction.response.send_message("You advertised your bot, number of people who have signed in have increased")
        
        else:
            await interaction.response.send_message("You need to have at least 10000 <:nerd_coin:992265892756979735> to advertise")
    
    @disnake.ui.button(label="Sell email datas", style=disnake.ButtonStyle.blurple)
    async def sell(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        with open('web.json') as file2:
            data2 = json.load(file2)
        
        amt = data2[str(interaction.user.id)]["Signed in people"] * 20

        with open("account.json", 'r', encoding='utf-8') as file:
            data = json.load(file)

        data[str(interaction.user.id)]["Bank"] += amt

        with open("account.json", 'w') as file:
            json.dump(data, file)
        
        await interaction.response.send_message(f"You have sold all of email data you had for {amt} <:nerd_coin:992265892756979735>")
    
    @disnake.ui.button(label="Delete website", style=disnake.ButtonStyle.blurple)
    async def deletee(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        with open('login.json', 'r', encoding='utf-8') as frik:
            drik = json.load(frik)
        
        drik[str(interaction.user.id)]["Programs"].remove("Website")
        
        with open('login.json', 'w') as frik:
            json.dump(drik, frik)
        
        await interaction.response.send_message("You have deleted your website")    

class App(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @disnake.ui.button(label="Advertise", style=disnake.ButtonStyle.blurple)
    async def ad(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        with open("account.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        if data[str(interaction.user.id)]["Bank"] >= 1000:
            with open('app.json') as file2:
                data2 = json.load(file2)
            
            data2[str(interaction.user.id)]["Downloads"] += random.randrange(50)
            data[str(interaction.user.id)]["Bank"] -= 1000

            with open("account.json", 'w') as file:
                json.dump(data, file)

            with open("app.json", 'w') as file2:
                json.dump(data2, file2)

            await interaction.response.send_message("You advertised your bot, your downloads have increased")
        
        else: 
            await interaction.response.send_message("You need to have at least 1000 <:nerd_coin:992265892756979735> to advertise")
    
    @disnake.ui.button(label="Show ads", style=disnake.ButtonStyle.blurple)
    async def show(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        with open('app.json') as file2:
            data2 = json.load(file2)

        if data2[str(interaction.user.id)]["Downloads"] >= 1000:
            with open("account.json", 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            data[str(interaction.user.id)]["Bank"] += 10000
            
            with open("account.json", 'w') as file:
                json.dump(data, file)
            
            await interaction.response.send_message("You have shown ads in your app and have earned 10000 <:nerd_coin:992265892756979735>!")

        else:
            await interaction.response.send_message("You need at least 1000 downloads to show ads")

    @disnake.ui.button(label="Delete website", style=disnake.ButtonStyle.blurple)
    async def deletee(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        with open('login.json', 'r', encoding='utf-8') as frik:
            drik = json.load(frik)
        
        drik[str(interaction.user.id)]["Programs"].remove("App")
        
        with open('login.json', 'w') as frik:
            json.dump(drik, frik)
        
        await interaction.response.send_message("You have deleted your website")    

class Dbot(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Advertise", style=disnake.ButtonStyle.blurple)
    async def ad(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        with open("account.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        if data[str(interaction.user.id)]["Bank"] >= 7000:
            with open('dbot.json') as file2:
                data2 = json.load(file2)
            
            data2[str(interaction.user.id)]["Servers"] += random.randrange(10)
            data[str(interaction.user.id)]["Bank"] -= 7000
            
            with open("account.json", 'w') as file:
                json.dump(data, file)

            with open("dbot.json", 'w') as file2:
                json.dump(data2, file2)

            await interaction.response.send_message("You advertised your bot, servers have increased")
        
        else:
            await interaction.response.send_message("You need to have at least 7000 <:nerd_coin:992265892756979735> to advertise")
    
    @disnake.ui.button(label="Add command", style=disnake.ButtonStyle.blurple)
    async def cmd(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        with open('dbot.json', 'r', encoding='utf-8') as file2:
            data2 = json.load(file2)
        
        data2[str(interaction.user.id)]["Commands"] += 1
        with open("dbot.json", 'w') as file2:
            json.dump(data2, file2)

        await interaction.response.send_message("You have added another command in your bot")
    
    @disnake.ui.button(label="Earn money", style=disnake.ButtonStyle.blurple)
    async def earn(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        with open('dbot.json', 'r', encoding='utf-8') as file2:
            data2 = json.load(file2)
        
        if data2[str(interaction.user.id)]["Servers"] >= 100:
            with open("account.json", 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            data[str(interaction.user.id)]["Bank"] += 100

            with open("account.json", 'w') as file:
                json.dump(data, file)

            await interaction.response.send_message("You have earned 100 <:nerd_coin:992265892756979735>")
        
        else:
            await interaction.response.send_message("You need to reach 100 servers in order to earn money")
    
    @disnake.ui.button(label="Delete bot", style=disnake.ButtonStyle.red)
    async def dele(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        with open('login.json', 'r', encoding='utf-8') as frik:
            drik = json.load(frik)
        
        drik[str(interaction.user.id)]["Programs"].remove("disnake bot")
        
        with open('login.json', 'w') as frik:
            json.dump(drik, frik)
        
        await interaction.response.send_message("You have deleted your disnake bot")

@_bot.slash_command(description="Delete an program from your computer")
async def delete(ctx, program_name):
    with open("login.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    deletembed = disnake.Embed(color=random.choice(colors))
    failembed = disnake.Embed(color=random.choice(colors))
    howcandelte = disnake.Embed(color=random.choice(colors))
    failembed.add_field(name="Deletion failed", value="Can't remove system file")
    howcandelte.add_field(name='Deletion failed', value="How can you delete an file that doesnt exist?")
    deletembed.add_field(name='Deletion successful', value='Program has been removed')
    
    if program_name == "system file":
        await ctx.send(embed=failembed)
    
    elif program_name == "system files":
        await ctx.send(embed=failembed)
    
    elif program_name == "System file":
        await ctx.send(embed=failembed)
    
    elif program_name == "System files":
        await ctx.send(embed=failembed)
    
    elif program_name == "systemfile":
        await ctx.send(embed=failembed)
    
    elif program_name == "systemfiles":
        await ctx.send(embed=failembed)
    
    elif program_name == "Systemfiles":
        await ctx.send(embed=failembed)
    
    elif program_name == "Systemfiles":
        await ctx.send(embed=failembed)
    
    elif program_name == "Ransomware":
        if "Ransomware" in data[str(ctx.author.id)]["Programs"]:
            data[str(ctx.author.id)]["Programs"].remove("Ransomware")
            await ctx.send(embed=deletembed)

            with open('login.json', 'w') as file:
                json.dump(data, file)
        else:
            ctx.send(embed=howcandelte)
    
    elif program_name == "ransomware":
        if "Ransomware" in data[str(ctx.author.id)]["Programs"]:
            data[str(ctx.author.id)]["Programs"].remove("Ransomware")
            await ctx.send(embed=deletembed)

            with open('login.json', 'w') as file:
                json.dump(data, file)
        else:
            ctx.send(embed=howcandelte)
    
    elif program_name == "Ransom ware":
        if "Ransomware" in data[str(ctx.author.id)]["Programs"]:
            data[str(ctx.author.id)]["Programs"].remove("Ransomware")
            await ctx.send(embed=deletembed)

            with open('login.json', 'w') as file:
                json.dump(data, file)
        else:
            ctx.send(embed=howcandelte)
    
    elif program_name == "ransom ware":
        if "Ransomware" in data[str(ctx.author.id)]["Programs"]:
            data[str(ctx.author.id)]["Programs"].remove("Ransomware")
            await ctx.send(embed=deletembed)

            with open('login.json', 'w') as file:
                json.dump(data, file)
        else:
            ctx.send(embed=howcandelte)
    
    elif program_name == "Spyware":
        if "Spyware" in data[str(ctx.author.id)]["Programs"]:
            data[str(ctx.author.id)]["Programs"].remove("Spyware")
            await ctx.send(embed=deletembed)

            with open('login.json', 'w') as file:
                json.dump(data, file)
        
        else:
            await ctx.send(embed=howcandelte)

    elif program_name == "Spy ware":
        if "Spyware" in data[str(ctx.author.id)]["Programs"]:
            data[str(ctx.author.id)]["Programs"].remove("Spyware")
            await ctx.send(embed=deletembed)

            with open('login.json', 'w') as file:
                json.dump(data, file)
        
        else:
            await ctx.send(embed=howcandelte)
    
    elif program_name == "spyware":
        if "Spyware" in data[str(ctx.author.id)]["Programs"]:
            data[str(ctx.author.id)]["Programs"].remove("Spyware")
            await ctx.send(embed=deletembed)

            with open('login.json', 'w') as file:
                json.dump(data, file)
        
        else:
            await ctx.send(embed=howcandelte)
    
    elif program_name == "spy ware":
        if "Spyware" in data[str(ctx.author.id)]["Programs"]:
            data[str(ctx.author.id)]["Programs"].remove("Spyware")
            await ctx.send(embed=deletembed)

            with open('login.json', 'w') as file:
                json.dump(data, file)
        
        else:
            await ctx.send(embed=howcandelte)
    
    elif program_name == "Malware":
        if "Malware" in data[str(ctx.author.id)]["Programs"]:
            data[str(ctx.author.id)]["Programs"].remove("Malware")
            await ctx.send(embed=deletembed)

            with open('login.json', 'w') as file:
                json.dump(data, file)
        
        else:
            await ctx.send(embed=howcandelte)
    
    elif program_name == "malware":
        if "Malware" in data[str(ctx.author.id)]["Programs"]:
            data[str(ctx.author.id)]["Programs"].remove("Malware")
            await ctx.send(embed=deletembed)

            with open('login.json', 'w') as file:
                json.dump(data, file)
        
        else:
            await ctx.send(embed=howcandelte)
    
    elif program_name == "Mal ware":
        if "Malware" in data[str(ctx.author.id)]["Programs"]:
            data[str(ctx.author.id)]["Programs"].remove("Malware")
            await ctx.send(embed=deletembed)

            with open('login.json', 'w') as file:
                json.dump(data, file)
        
        else:
            await ctx.send(embed=howcandelte)
    
    elif program_name == "mal ware":
        if "Malware" in data[str(ctx.author.id)]["Programs"]:
            data[str(ctx.author.id)]["Programs"].remove("Malware")
            await ctx.send(embed=deletembed)

            with open('login.json', 'w') as file:
                json.dump(data, file)
        
        else:
            await ctx.send(embed=howcandelte)
    
    elif program_name == 'App':
        if "App" in data[str(ctx.author.id)]["Programs"]:
            data[str(ctx.author.id)]["Programs"].remove("App")
            await ctx.send(embed=deletembed)

            with open('login.json', 'w') as file:
                json.dump(data, file)
        
        else:
            await ctx.send(embed=howcandelte)
    
    elif program_name == 'app':
        if "App" in data[str(ctx.author.id)]["Programs"]:
            data[str(ctx.author.id)]["Programs"].remove("App")
            await ctx.send(embed=deletembed)

            with open('login.json', 'w') as file:
                json.dump(data, file)
        
        else:
            await ctx.send(embed=howcandelte)
    
    elif program_name == 'disnake bot':
        if "disnake bot" in data[str(ctx.author.id)]["Programs"]:
            data[str(ctx.author.id)]["Programs"].remove("disnake bot")
            await ctx.send(embed=deletembed)

            with open('login.json', 'w') as file:
                json.dump(data, file)
        
        else:
            await ctx.send(embed=howcandelte)
    
    elif program_name == 'disnakebot':
        if "disnake bot" in data[str(ctx.author.id)]["Programs"]:
            data[str(ctx.author.id)]["Programs"].remove("disnake bot")
            await ctx.send(embed=deletembed)

            with open('login.json', 'w') as file:
                json.dump(data, file)
        
        else:
            await ctx.send(embed=howcandelte)
    
    elif program_name == 'disnake bot':
        if "disnake bot" in data[str(ctx.author.id)]["Programs"]:
            data[str(ctx.author.id)]["Programs"].remove("disnake bot")
            await ctx.send(embed=deletembed)

            with open('login.json', 'w') as file:
                json.dump(data, file)
        
        else:
            await ctx.send(embed=howcandelte)
    
    elif program_name == 'disnakebot':
        if "disnake bot" in data[str(ctx.author.id)]["Programs"]:
            data[str(ctx.author.id)]["Programs"].remove("disnake bot")
            await ctx.send(embed=deletembed)

            with open('login.json', 'w') as file:
                json.dump(data, file)
        
        else:
            await ctx.send(embed=howcandelte)
    
    elif program_name == 'website':
        if "Website" in data[str(ctx.author.id)]["Programs"]:
            data[str(ctx.author.id)]["Programs"].remove("Website")
            await ctx.send(embed=deletembed)

            with open('login.json', 'w') as file:
                json.dump(data, file)
        
        else:
            await ctx.send(embed=howcandelte)
    
    elif program_name == 'Website':
        if "Website" in data[str(ctx.author.id)]["Programs"]:
            data[str(ctx.author.id)]["Programs"].remove("Website")
            await ctx.send(embed=deletembed)

            with open('login.json', 'w') as file:
                json.dump(data, file)
        
        else:
            await ctx.send(embed=howcandelte)
    
    else:
        embed = disnake.Embed(color=random.choice(colors))
        embed.add_field(title="Deletion failed", value="Not an valid program")
        await ctx.send(embed=embed)
    
class Run(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
 
    @disnake.ui.button(label="disnake bot", style=disnake.ButtonStyle.blurple)
    async def dc(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        computers = ["Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954>💾", "Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555>💾", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️💾", "Computer🖱️🖥️⌨️<:disnakeFloppy:987628788256997377>"]
        with open('account.json', 'r', encoding='utf-8') as f:
            file = json.load(f)
        
        if any(computer in file[str(interaction.user.id)]["Inventory"] for computer in computers):
            with open('login.json', 'r', encoding='utf-8') as f2:
                file2 = json.load(f2)
            
            with open('dbot.json', 'r', encoding='utf-8') as fri:
                dat = json.load(fri)
            
            if "disnake bot" in file2[str(interaction.user.id)]['Programs']:
                color = disnake.Color(value=random.choice(colors))
                embed = disnake.Embed(title="disnake bot", color=color)
                a = dat[str(interaction.user.id)]["Servers"]
                e = dat[str(interaction.user.id)]["Commands"]

                embed.add_field(name='Servers', value=a)
                embed.add_field(name='Commands', value=e)

                await interaction.response.send_message(embed=embed, view=Dbot())
            
            else:
                embed = disnake.Embed(color=random.choice(colors))
                embed.add_field(name='Running failed', value="You don't have this program in your computer")
                await interaction.response.send_message(embed=embed)
        else:
            embed = disnake.Embed(color=random.choice(colors))
            embed.add_field(name='Running failed', value="You don't have a computer")
            await interaction.response.send_message(embed=embed)
    
    @disnake.ui.button(label="Website", style=disnake.ButtonStyle.blurple)
    async def webbo(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        computers = ["Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954>💾", "Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555>💾", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️💾", "Computer🖱️🖥️⌨️<:disnakeFloppy:987628788256997377>"]
        with open('account.json', 'r', encoding='utf-8') as f:
            file = json.load(f)
        
        if any(computer in file[str(interaction.user.id)]["Inventory"] for computer in computers):
            with open('login.json', 'r', encoding='utf-8') as f2:
                file2 = json.load(f2)
            
            with open('web.json', 'r', encoding='utf-8') as fri:
                dat = json.load(fri)
            
            if "Website" in file2[str(interaction.user.id)]['Programs']:
                color = disnake.Color(value=random.choice(colors))
                embed = disnake.Embed(title="disnake bot", color=color)
                a = dat[str(interaction.user.id)]['Signed in people']
                embed.add_field(name='Signed in people', value=a)
                await interaction.response.send_message(embed=embed, view=Web())
            else:
                embed = disnake.Embed(color=random.choice(colors))
                embed.add_field(name='Running failed', value="You don't have this program in your computer")
                await interaction.response.send_message(embed=embed)
        else:
            embed = disnake.Embed(color=random.choice(colors))
            embed.add_field(name='Running failed', value="You don't have a computer")
            await interaction.response.send_message(embed=embed)

@_bot.slash_command(description='With this command you can run your disnake bot, app and website if you have it in your computer')
async def run(ctx):
    await ctx.send("Program selection", view=Run())

@_bot.event
async def coin_boost(message):
    await open_account(message)
    with open('account.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    if "Coin Booster <:DigitalTwo:1003623866272329748>" in data[str(message.author.id)]["Inventory"]:
        await asyncio.sleep(7200)  
        data[str(message.author.id)]["Inventory"].remove("Coin Booster <:DigitalTwo:1003623866272329748>")
        with open('account.json', 'w') as file:
            json.dump(data, file)
    else:
        pass

@_bot.event
async def xp_boost(message):
    await open_account(message)
    with open('account.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    if "AI Software <:galaxy_brain:1003621546050474034>" in data[str(message.author.id)]["Inventory"]:
        await asyncio.sleep(7200)  
        data[str(message.author.id)]["Inventory"].remove("AI Software <:galaxy_brain:1003621546050474034>")
        with open('account.json', 'w') as file:
            json.dump(data, file)
    else:
        pass

@_bot.event
async def xp_boost(message):
    await open_account(message)
    with open('account.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    if "AI Software <:galaxy_brain:1003621546050474034>" in data[str(message.author.id)]["Inventory"]:
        await asyncio.sleep(7200)  
        data[str(message.author.id)]["Inventory"].remove("AI Software <:galaxy_brain:1003621546050474034>")
        with open('account.json', 'w') as file:
            json.dump(data, file)
    else:
        pass

@_bot.slash_command(description="Make softwares which will be added")
async def software(ctx):
    await ctx.send(view=Software())

@_bot.slash_command(description="Use your spyware, ransomware and malware to gain items and earn money")
@commands.cooldown(1, 60 , commands.BucketType.user)
async def attack(ctx, member: disnake.Member):
    await ctx.send(view=Attack(member=member))

@attack.error
async def attack_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        tim = datetime.timedelta(seconds = error.retry_after)
        await ctx.send(f"Wait for **{tim}** before running this command again") 

@_bot.slash_command(description="Assemble your computer!")
async def assemble(ctx):
    await open_account(ctx)
    with open('account.json', 'r', encoding='utf-8') as data:
        f = json.load(data)
    
    inv = f[str(ctx.author.id)]["Inventory"]
    
    keys = ['Membrane Keyboard ⌨️', "Mehcanical Keyboard <:RGBKeyboard:986490410849423441>", "Mehcanical Gaming Keyboard <:gamer_keyboard:987622731614945330>"]
    monitor = ["Wide Montior <:gaming_keyboard:987619238204305438>", "Ultra Wide Montior with Ipad <:programmershit:987628014722514984>", "Monitor 🖥️"]
     
    embed = disnake.Embed(color=random.choice(colors))
    if 'Mouse 🖱️' in inv:
        if any(k in inv for k in keys):
            if any(m in inv for m in monitor):
                if "10 gb ram 💾" in inv:
                        inv.append("Computer🖱️🖥️⌨️💾")
                elif "16 gb ram <:disnakeFloppy:987628788256997377>" in inv:
                        inv.append("Computer🖱️🖥️⌨️<:disnakeFloppy:987628788256997377>")
                else:
                    embed.add_field(name="Error occured", value="You don't have any ram")
                    await ctx.send(embed=embed)
            else:
                embed.add_field(name="Error occured", value="You don't have any monitor")
                await ctx.send(embed=embed)
        else:
            embed.add_field(name="Error occured", value="You don't have any keyboard")
            await ctx.send(embed=embed)
    else:
        embed.add_field(name="Error occured", value="You don't have mouse")
        await ctx.send(embed=embed)
   
    with open('account.json', 'w') as data:
        json.dump(f, data)
 
@_bot.slash_command(description="Log in to your computer and see your programs and os")
async def computer(ctx):
    await open_account(ctx)
    with open('account.json', 'r', encoding='utf-8') as data:
        f = json.load(data)
    
    inv = f[str(ctx.author.id)]["Inventory"]
    computers = ["Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954>💾", "Computer🖱️🖥️⌨️<:AMD_Radeon_RX_6900_XT_GPU:987622463431122954><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555>💾", "Computer🖱️🖥️⌨️<:Nvidia_3090_GPU:987623191159660555><:disnakeFloppy:987628788256997377>", "Computer🖱️🖥️⌨️💾", "Computer🖱️🖥️⌨️<:disnakeFloppy:987628788256997377>"]
    if any(comp in inv for comp in computers):
        await log_in(ctx)
        with open('login.json', 'r', encoding='utf-8') as file:
            data = json.load(file) 
        
    
        os = data[str(ctx.author.id)]['OS']
        programs = data[str(ctx.author.id)]['Programs']
        embed = disnake.Embed(title=f"{ctx.author}'s Programs")
        o = '\n'.join(os)
        embed.add_field(name="Operating system", value=o)
        pro = '\n'.join(programs)
        embed.add_field(name="Programs", value=pro)
        await ctx.send(embed=embed)     

    else:
        
        await ctx.send("You don't have an computer")

@_bot.slash_command(description="Get the nerd's advice")
async def advice(ctx, *, message:str):
        try:
            choices = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes, definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', ' Outlook good:', 'Yes', 'Signs point to yes', 'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Do not count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful.']
            color = disnake.Color(value=random.choice(colors))
            em = disnake.Embed(color=color, title=f"{message}")
            em.description = random.choice(choices) 
            em.set_author(name="Nerd's advice", icon_url="")
            em.set_footer(text=f"Sent by {ctx.author}")
            await ctx.send(embed=em)
        except Forbidden:
            color = disnake.Color(value=random.choice(colors))
            em = disnake.Embed(color=color, title='Error ')
            em.description = 'Error code **{e.code}**: {e.error}'
            return await ctx.send(embed=em)

@_bot.slash_command(description='Earn some money')
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
    await open_account(ctx)
    with open("account.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    nc = random.randrange(5000)
    embed = disnake.Embed(color=random.choice(colors))
    embed.add_field(name="Daily transaction successful", value=f"You got {nc} daily <:nerd_coin:992265892756979735>")
    await ctx.send(embed=embed)

    data[str(ctx.author.id)]['Bank'] += nc
    
    with open('account.json', 'w') as file:
        json.dump(data, file)

@daily.error
async def daily_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        tim = datetime.timedelta(seconds = error.retry_after)
        embed = disnake.Embed(color=random.choice(colors))
        embed.add_field(name='Command on cooldown', value=f"Wait for **{tim}** before running this command again")
        await ctx.send(embed=embed) 



@_bot.event
async def on_error(event, *args, **kwargs):
    print(traceback.format_exc())
    print(event)

@_bot.slash_command(description="Get server information")
async def serverinfo(ctx):
        guild = ctx.guild
        roles = [x.name for x in guild.roles]
        role_length = len(roles)
        roles = ', '.join(roles)
        channels = len(guild.channels)
        time = str(guild.created_at.strftime("%b %m, %Y, %A, %I:%M %p"))         
        em = disnake.Embed(description= "-", title='Server Info', colour=0x00ff00)
        em.set_thumbnail(url=guild.icon.url)
        em.add_field(name='__Server __', value=str(guild.name))
        em.add_field(name='__Server ID__', value=str(guild.id))
        em.add_field(name='__Owner__', value=str(guild.owner))
        em.add_field(name='__Owner ID__', value=guild.owner_id) 
        em.add_field(name='__Member Count__', value=str(guild.member_count))
        em.add_field(name='__Text/Voice Channels__', value=str(channels))
        em.add_field(name='__Server Region__', value='%s' % str(guild.region))
        em.add_field(name='__ Total Roles__', value='%s' % str(role_length))
        em.add_field(name='__Roles__', value='%s' % str(roles))
        em.set_footer(text='Created - %s' % time)        
        await ctx.send(embed=em)

@_bot.slash_command(description="Get an job")
async def job(ctx,*, jobname):
    await learning_points(ctx)
    with open('learning_points.json', 'r', encoding='utf-8') as r:
        file = json.load(r)
    
    p = file[str(ctx.author.id)]['Physics']
    c = file[str(ctx.author.id)]['Chemistry']
    b = file[str(ctx.author.id)]['Biology']
    cs =  file[str(ctx.author.id)]['Computer science']
    m = file[str(ctx.author.id)]['Maths']

    await open_account(ctx)
    with open('account.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    jb = data[str(ctx.author.id)]['Job']
    inv = data[str(ctx.author.id)]['Inventory']

    with open('jobs.json', 'r', encoding='utf-8') as file:
        jobs = json.load(file)
    
    if p >= jobs[jobname]["Physics points"]:
        if c >= jobs[jobname]["Chemistry points"]:
            if b >= jobs[jobname]["Biology points"]:
                if cs >= jobs[jobname]["Computer science points"]:
                    if m >= jobs[jobname]["Maths points"]:
                        if len(jobs[jobname]["Required jobs"]) == 0:
                            await ctx.send(f"You can now do job as {jobname}")
                            jb.clear()
                            jb.append(jobname)
                            with open('account.json', 'w') as file:
                                json.dump(data, file) 

                        elif len(jobs[jobname]["Required jobs"][0]) != 0:
                            if jobs[jobname]["Required jobs"][0] in inv:
                                await ctx.send(f"You can now do job as {jobname}")
                                jb.clear()
                                jb.append(jobname)
                                with open('account.json', 'w') as file:
                                    json.dump(data, file) 
                            else:
                                await ctx.send(f"You need job of {jobs[jobname]['Required jobs']} to get this job")
                    else:
                        await ctx.send("You don't have enough maths points")
                else:
                    await ctx.send("You don't have enough computer science points")
            else:
                await ctx.send("You don't have enough biology points")
        else:
            await ctx.send("You don't have enough chemistry points")
    else:
        await ctx.send("You don't have enough physics points")

@_bot.slash_command(description="Leave your current job")
async def retire(ctx):
    await open_account(ctx)
    with open('account.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    if len(data[str(ctx.author.id)]['Job']) == 0:
        await ctx.send("Get a job first then think of retire")

    else:
        await ctx.send("You have retired from your job")
        data[str(ctx.author.id)]['Job'].clear()
        with open('account.json', 'w') as file:
            json.dump(data, file)

@_bot.slash_command(description="Do some work in your job")
@commands.cooldown(1, 3600, commands.BucketType.user)
async def work(ctx):
    await open_account(ctx)
    with open('account.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    job = data[str(ctx.author.id)]['Job']
    
    if "Coin Booster <:DigitalTwo:1003623866272329748>" in data[str(ctx.author.id)]["Inventory"]:
        if len(job) != 0:
            jb = job[0]

            with open('jobs.json', 'r', encoding='utf-8') as file:
                jobs = json.load(file)

            sal = jobs[jb]['salary']
            new = sal + 5000
            data[str(ctx.author.id)]['Bank'] += new

            with open('account.json', 'w') as file:
                json.dump(data, file)
    
            await ctx.send(f"You have earned {new} <:nerd_coin:992265892756979735>")

        else:
            await ctx.send("You don't have a job") 
    else:
        if len(job) != 0:
            jb = job[0]

            with open('jobs.json', 'r', encoding='utf-8') as file:
                jobs = json.load(file)

            sal = jobs[jb]['salary']
            data[str(ctx.author.id)]['Bank'] += sal

            with open('account.json', 'w') as file:
                json.dump(data, file)
    
            await ctx.send(f"You have earned {sal} <:nerd_coin:992265892756979735>")

        else:
            await ctx.send("You don't have a job") 

@work.error
async def work_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        tim = datetime.timedelta(seconds = error.retry_after)
        await ctx.send(f"Wait for **{tim}** seconds before running this command again") 
 
@_bot.slash_command(description="Check your balance")
async def bal(ctx):
    await open_account(ctx)
    with open('account.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    bank = data[str(ctx.author.id)]['Bank']
    crpt = data[str(ctx.author.id)]['Crypto']
    jb = data[str(ctx.author.id)]['Job']

    embed = disnake.Embed(title=f"{ctx.author.name}'s stats")
    embed.add_field(name="Bank", value=bank)
    embed.add_field(name="Crypto", value=crpt) 
    embed.add_field(name="Job", value=jb)

    await ctx.send(embed=embed)

async def open_account(user):
    with open('account.json', 'r', encoding='utf-8') as file:
        data = json.load(file)  

    if str(user.author.id) in data:
        return False
    else:
        data[str(user.author.id)] = {}
        data[str(user.author.id)]['Bank'] = 0
        data[str(user.author.id)]['Job'] = []
        data[str(user.author.id)]['XP'] = 0
        data[str(user.author.id)]['Level'] = 0
        data[str(user.author.id)]['Inventory'] = ["🎒"]
        data[str(user.author.id)]['Crypto'] = 0
    
    with open('account.json', 'w') as f:
        json.dump(data, f)
    
    return True

@_bot.slash_command(description="Roasting?")
async def roast(message, member: disnake.Member):
    try:
        rand_roast = random.choice(burns)
        await message.send(f'{message.author.mention}, {rand_roast}')
    except:
        pass

@_bot.slash_command(description="Hug someone!")
async def hug(ctx, member: disnake.Member):
    try:
        rand_hugs = random.choice(hug_links)
        await ctx.send(f'{rand_hugs}')
        await ctx.send(f'{member.mention} gets a hug.')
    except:
        pass


@_bot.slash_command(description="Get HTML of any web page")
async def web_scrape(ctx, *, url):
    try:
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")

        with open("html.txt", "w", encoding="utf-8") as file:
            file.write(html)

        await ctx.send(file=disnake.File("html.txt"))
        await ctx.send('Code has been sent...')
        os.remove("html.txt")

    except:
        await ctx.send("Invalid URL...")

@_bot.slash_command(description="See the job board")
async def jobs(ctx):
    with open('jobs.json', 'r', encoding='utf-8') as file:
        jobs = json.load(file)

    embed = disnake.Embed(title="Jobs")

    for job in jobs:
        jbb = '\n'.join(jobs[job]['Required jobs'])
        embed.add_field(name=f"{job.title()}:", value=f"{jobs[job]['description']}\n**Salary** - {jobs[job]['salary']}\n**Computer science points** - {jobs[job]['Computer science points']}\n**Physics points** - {jobs[job]['Physics points']}\n**Biology points** - {jobs[job]['Biology points']}\n**Chemistry points** - {jobs[job]['Chemistry points']}\n**Maths points** - {jobs[job]['Maths points']}\n**Required jobs** - {jbb}")

    await ctx.send(embed=embed)

@_bot.slash_command(description="Mine crypto currency if you have an laptop")
@commands.cooldown(1, 30, commands.BucketType.user)
async def crypto(ctx):
    try:
        with open('account.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    
        await open_account(ctx)
        inv = data[str(ctx.author.id)]['Inventory']
        if "Laptop 💻" in inv: 
            crypto = random.randrange(2000)
            if crypto <= 1000:
                await ctx.send("Damn, you cannot find any crypto currency")
            else:
                await ctx.send(f"You got {crypto} crypto currency!")
                data[str(ctx.author.id)]['Crypto'] += crypto
            
                with open('account.json', 'w') as file:
                    json.dump(data, file)
    
        elif "MacBook <:MacBook:987624574202044447>" in inv:
            crpt = data[str(ctx.author.id)]['Crypto']
            crypto = random.randrange(2000)
            if crypto <= 900:
                await ctx.send("Damn, you cannot find any crypto currency")
            else:
                await ctx.send(f"You got {crypto} crypto currency!")
                data[str(ctx.author.id)]['Crypto'] += crypto
        
                with open('account.json', 'w') as file:
                    json.dump(data, file)

        else:
            await ctx.send("You don't have any laptop, buy an laptop")
    
    except commands.CommandOnCooldown:
        await ctx.send("Your command is on ann 30 second cooldown, wait for 30 seconds and try again")

@crypto.error
async def crypto_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
            tim = datetime.timedelta(seconds = error.retry_after)
            await ctx.send(f"Wait for **{tim}** before running this command again") 

@_bot.slash_command(description="Redeem an amount of crypto currency you have")
async def redeem(ctx, amount):
    with open('account.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    await open_account(ctx)
    crpt = data[str(ctx.author.id)]['Crypto']
    
    if int(amount) > crpt:
        await ctx.send(f"You don't have {amount} crypto")
    elif int(amount) < 0:
        await ctx.send("Invalid amount")
    else:
        money = crpt * 2
        data[str(ctx.author.id)]['Bank'] += money
        data[str(ctx.author.id)]['Crypto'] -= int(amount)
        await ctx.send(f"You have redeemed {amount} crypto currency and have increased {money} <:nerd_coin:992265892756979735>")
        

        with open('account.json', 'w') as file:
            json.dump(data, file)

@_bot.slash_command(description="Open the shop")
async def shop(ctx):
    with open('shop.json', 'r', encoding='utf-8') as file:
        items = json.load(file)

    embed = disnake.Embed(title="Shop")

    for item in items:
        embed.add_field(name=f"{item.title()}:", value=f"{items[item]['description']}\n**Price** - {items[item]['price']}\n**code** - {items[item]['code']}")

    await ctx.send(embed=embed)

@_bot.slash_command(description="Buy an item from the shop")
async def buy(ctx, code):
    await open_account(ctx)
    
    with open('account.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open('shop.json', 'r', encoding='utf-8') as file:
        items = json.load(file)
    
    for item in items:
        if item not in data[str(ctx.author.id)]['Inventory']:
            if code == items[item]['code']:
                if data[str(ctx.author.id)]['Bank'] <= items[item]['price']:
                    embed=disnake.Embed(color=random.choice(colors))
                    embed.add_field(name="Error", value=f"You don't have enough money to buy {item}")
                    await ctx.send(embed=embed)
                else:
                    embed=disnake.Embed(color=random.choice(colors))
                    embed.add_field(name="Success", value=f"You have bought {item}!")
                    await ctx.send(embed=embed)
            
                    inv = data[str(ctx.author.id)]['Inventory']
                    data[str(ctx.author.id)]['Bank'] -= items[item]['price']

                    inv.append(item)

                    with open('account.json', 'w') as file:
                        json.dump(data, file)
        else:
            pass

async def kali_installed(ctx):
    with open('account.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    if "Kali linux <:kali:1003630422560886905>" in data[str(ctx.author.id)]["Inventory"]:
        print("KALI IN")
        with open("login.json", 'r', encoding='utf-8') as file2:
            data2 = json.load(file2)
        data2[str(ctx.author.id)]["OS"].clear()
        data2[str(ctx.author.id)]["OS"].append("Kali linux <:kali:1003630422560886905>")
        with open("login.json", 'w') as file2:
            json.dump(data2, file2)
        print("PROCESS 1 DONE")
        data[str(ctx.author.id)]["Inventory"].remove("Kali linux <:kali:1003630422560886905>")

        with open("account.json", 'w') as file:
            json.dump(data, file)
    
    else:
        pass

@_bot.event 
async def win10_installed(ctx):
    with open('account.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    if "Windows 10 <:windows_10:1003626037713842228>" in data[str(ctx.author.id)]["Inventory"]:
        with open("login.json", 'r', encoding='utf-8') as file2:
            data2 = json.load(file2)
        data2[str(ctx.author.id)]["OS"].clear()
        data2[str(ctx.author.id)]["OS"].append("Windows 10 <:windows_10:1003626037713842228>")
        with open("login.json", 'w') as file2:
            json.dump(data2, file2)
        data[str(ctx.author.id)]["Inventory"].remove("Windows 10 <:windows_10:1003626037713842228>")

        with open("account.json", 'w') as file:
            json.dump(data, file)
    
    else:
        pass

@_bot.slash_command(description="Check your inventory")
async def inv(ctx):
    with open('account.json') as file:
        data = json.load(file)

    embed = disnake.Embed(title=f"{ctx.author.name}'s Inventory")
    iv = '\n'.join(data[str(ctx.author.id)]['Inventory'])
    embed.add_field(name=f"----------", value=iv)
    await ctx.send(embed=embed)

@_bot.slash_command(description="See what subjects to learn")
async def subjects(ctx):
    embed = disnake.Embed(color=random.choice(colors))
    embed.set_author(name="Subjects")

    subjects = [("Physics (p)", "`This would help to get jobs related to physics`", False),
              ("Chemistry (c)", "`You can get jobs related to chemistry with this`", False),
              ("Biology (b)", "`You can get biology jobs with this`", False),
              ("Computer science (cs)", "`All jobs related to programmming might be opened`", False),
              ("Maths (m)", "`This subject's degree is necessary for many jobs`", False)]
        
    for name, value, inline in subjects:
        embed.add_field(name=name, value=value, inline=inline)
    
    await ctx.send(embed=embed)

async def learning_points(user):
    with open('learning_points.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    if str(user.author.id) in data:
        return False
    else:
        data[str(user.author.id)] = {}
        data[str(user.author.id)]['Physics'] = 0
        data[str(user.author.id)]['Chemistry'] = 0
        data[str(user.author.id)]['Biology'] = 0
        data[str(user.author.id)]['Computer science'] = 0   
        data[str(user.author.id)]['Maths'] = 0

    with open('learning_points.json', 'w') as f:
        json.dump(data, f)
    
    return True

@_bot.slash_command(description="Learn an subject")
@commands.cooldown(1, 3600, commands.BucketType.user)
async def learn(ctx, subject):
    await learning_points(ctx)
    with open('learning_points.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    if subject == "Physics":
        data[str(ctx.author.id)]['Physics'] += 5
        await ctx.send("You have learned Physics for an hour and have gained 5 points in Physics")

    elif subject == "Chemistry":
        data[str(ctx.author.id)]['Chemistry'] += 5
        await ctx.send("You have learned Chemistry for an hour and have gained 5 points in Chemistry")
    
    elif subject == "Biology":
        data[str(ctx.author.id)]['Biology'] += 5
        await ctx.send("You have learned Biology for an hour and have gained 5 points in Biology")
    
    elif subject == "cs":
        data[str(ctx.author.id)]['Computer science'] += 5
        await ctx.send("You have learned Computer science for an hour and have gained 5 points in Computer science")
    
    elif subject == "Maths":
        data[str(ctx.author.id)]['Maths'] += 5
        await ctx.send("You have learned Maths for an hour and have gained 5 points in Maths")
    
    elif subject == "chemistry":
        data[str(ctx.author.id)]['Chemistry'] += 5
        await ctx.send("You have learned Chemistry for an hour and have gained 5 points in Chemistry")
    
    elif subject == "biology":
        data[str(ctx.author.id)]['Biology'] += 5
        await ctx.send("You have learned Biology for an hour and have gained 5 points in Biology")
    
    elif subject == "maths":
        data[str(ctx.author.id)]['Maths'] += 5
        await ctx.send("You have learned Maths for an hour and have gained 5 points in Maths")
    
    elif subject == "p":
        data[str(ctx.author.id)]['Physics'] += 5
        await ctx.send("You have learned Physics for an hour and have gained 5 points in Physics")
         
    elif subject == "c":
        data[str(ctx.author.id)]['Chemistry'] += 5
        await ctx.send("You have learned Chemistry for an hour and have gained 5 points in Chemistry")
    
    elif subject == "b":
        data[str(ctx.author.id)]['Biology'] += 5
        await ctx.send("You have learned Biology for an hour and have gained 5 points in Biology")
    
    elif subject == "m":
        data[str(ctx.author.id)]['Maths'] += 5
        await ctx.send("You have learned Maths for an hour and have gained 5 points in Maths")
    
    else:
        await ctx.send("Invalid subject")
    
    with open('learning_points.json', 'w') as file:
        json.dump(data, file)

@learn.error
async def learn_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
            tim = datetime.timedelta(seconds = error.retry_after)
            await ctx.send(f"Wait for **{tim}** before running this command again") 

@_bot.slash_command(description="Get top 3 richest people")
async def top(ctx,x=3):
    await open_account(ctx)
    with open('account.json', 'r', encoding='utf-8') as file:
        users = json.load(file)

    leader_board = {}
    total = []

    for user in users:
        name = int(user)    
        total_amtt = users[user]['Bank']
        leader_board[total_amtt] = name 
        total.append(total_amtt)

    total = sorted(total,reverse=True)

    embed = disnake.Embed(title=f'Top {x} Leaderboard', description='Top Rich People')
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        print(id_)
        member = await _bot.fetch_user(id_)
        embed.add_field(name=f'{index}. {member}', value=f'{amt} <:nerd_coin:992265892756979735>', inline=False)
        if index == x:
            break
        else:
            index +=1
    await ctx.send(embed=embed)

@_bot.slash_command(description="Check how much learning points you got in every subject")
async def learnpoints(ctx):
    await learning_points(ctx)
    with open('learning_points.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    p = data[str(ctx.author.id)]['Physics']
    c = data[str(ctx.author.id)]['Chemistry']
    b = data[str(ctx.author.id)]['Biology']
    cs =  data[str(ctx.author.id)]['Computer science']
    m = data[str(ctx.author.id)]['Maths']

    embed = disnake.Embed(title=f"{ctx.author.name}'s Subjects Points")
    embed.add_field(name="Physics points", value=p)
    embed.add_field(name="Chemistry points", value=c)
    embed.add_field(name="Biology points", value=b)
    embed.add_field(name="Computer science points", value=cs)
    embed.add_field(name="Maths points", value=m)

    await ctx.send(embed=embed)

@_bot.slash_command(description="See your level card")
async def level(ctx):
    userr = ctx.author
    
    await open_account(ctx)
    with open("account.json", "r") as f:
      data = json.load(f)

    xp = data[str(userr.id)]["XP"]
    lvl = data[str(userr.id)]["Level"]

    next_level_xp = (lvl+1) * 100
    xp_need = next_level_xp
    xp_have = data[str(userr.id)]["XP"]

    percentage = int(((xp_have * 100)/ xp_need))

    if percentage < 1:
      percentage = 0
    
    background = Editor(f"zIMAGE.png")
    profile = await load_image_async(str(userr.avatar.url))

    profile = Editor(profile).resize((150, 150)).circle_image()
    
    poppins = Font.poppins(size=40)
    poppins_small = Font.poppins(size=30)

    ima = Editor("zBLACK.png")
    background.blend(image=ima, alpha=.5, on_top=False)

    background.paste(profile.image, (30, 30))

    background.rectangle((30, 220), width=650, height=40, fill="#fff", radius=20)
    background.bar(
        (30, 220),
        max_width=650,
        height=40,
        percentage=percentage,
        fill="#ff9933",
        radius=20,
    )
    background.text((200, 40), str(userr.name), font=poppins, color="#ff9933")

    background.rectangle((200, 100), width=350, height=2, fill="#ff9933")
    background.text(
        (200, 130),
        f"Level : {lvl}"
        + f" XP : {xp} / {(lvl+1) * 100}",
        font=poppins_small,
        color=random.choice(colors)
    )

    card = disnake.File(fp=background.image_bytes, filename="zCARD.png")
    await ctx.send(file=card)
            

async def xp(ctx, amt):
    await open_account(ctx)
    with open('account.json', 'r', encoding='utf-8') as file:
        data = json.load(file)  
    
    if ctx.author != _bot.user:
        data[str(ctx.author.id)]["XP"] += amt 
    else:
        pass

    with open('account.json', 'w') as file:
        json.dump(data, file)

async def lvl(message):
    if not message.author.bot:
        with open("account.json", "r") as f:
            data = json.load(f)
    
        if "AI Software <:galaxy_brain:1003621546050474034>" in data[str(message.author.id)]["Inventory"]:
            if str(message.author.id) in data:
                xp = data[str(message.author.id)]['XP']
                lvl = data[str(message.author.id)]['Level']

                increased_xp = xp+35
                new_level = int(increased_xp/100)

                data[str(message.author.id)]['XP']=increased_xp

                with open("account.json", "w") as f:
                    json.dump(data, f)

                if new_level > lvl:
                    await message.reply(f"{message.author.mention} Just Leveled Up to Level {new_level}!!!")

                    data[str(message.author.id)]['Level']=new_level
                    data[str(message.author.id)]['XP']=0

                    with open("account.json", "w") as f:
                        json.dump(data, f)
            
                    for i in range(len(lev)):
                        if new_level == level_num[i]:
                            await message.author.add_roles(disnake.utils.get(message.author.guild.roles, name=level[i]))

                            mbed = disnake.Embed(title=f"{message.author} You Have Gotten role **{level[i]}**!", color = message.author.colour)
                            mbed.set_thumbnail(url=message.author.avatar_url)
                            with open('setup.json', 'r', encoding='utf-8') as file:
                                dddd = json.load(file)
                            c = _bot.get_channel(dddd[str(message.guild.id)]['level'])
                            await c.send(embed=mbed)
        else:
            if str(message.author.id) in data:
                xp = data[str(message.author.id)]['XP']
                lvl = data[str(message.author.id)]['Level']

                increased_xp = xp+25
                new_level = int(increased_xp/100)

                data[str(message.author.id)]['XP']=increased_xp

                with open("account.json", "w") as f:
                    json.dump(data, f)

                if new_level > lvl:
                    await message.reply(f"{message.author.mention} Just Leveled Up to Level {new_level}!!!")

                    data[str(message.author.id)]['Level']=new_level
                    data[str(message.author.id)]['XP']=0

                    with open("account.json", "w") as f:
                        json.dump(data, f)
            
                    for i in range(len(lev)):
                        if new_level == level_num[i]:
                            await message.author.add_roles(disnake.utils.get(message.author.guild.roles, name=level[i]))

                            mbed = disnake.Embed(title=f"{message.author} You Have Gotten role **{level[i]}**!", color = message.author.colour)
                            mbed.set_thumbnail(url=message.author.avatar_url)
                            with open('setup.json', 'r', encoding='utf-8') as file:
                                dddd = json.load(file)
                            c = _bot.get_channel(dddd[str(message.guild.id)]['level'])
                            await c.send(embed=mbed)
                    

'''async def lvldetect(ctx):
    if not ctx.author.bot:
        await open_account(ctx)
        with open('account.json', 'r', encoding='utf-8') as file:
            data = json.load(file) 
    
        xp = data[str(ctx.author.id)]["XP"]
        lev = data[str(ctx.author.id)]["Level"]

        if lev == 5 and xp == 30: 
            await ctx.send("You got an degree")
        else:
            pass''' 

@_bot.slash_command(description="Get an programming meme")
async def pmeme(ctx):
    images = os.path.join(os.getcwd(), "memes")
    fil = os.path.join(images, random.choice(os.listdir(images)))
    await ctx.send(file=disnake.File(fil))

@_bot.slash_command(description='Get an meme')
async def meme(ctx):
    embed = disnake.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@_bot.slash_command(description="Get an fact")
async def fact(ctx):
    f = randfacts.get_fact()
    embed=disnake.Embed(color=random.choice(colors))
    embed.add_field(name="Fact", value=f)
    await ctx.send(embed=embed)

@_bot.slash_command(description="Get an cool image")
async def pic(ctx):
    images = os.path.join(os.getcwd(), "scifi")
    fil = os.path.join(images, random.choice(os.listdir(images)))
    await ctx.send(file=disnake.File(fil))

@_bot.slash_command(description="Get an random truth question")
async def truth(ctx):
    lines = open("truth.txt", encoding='utf-8').read().splitlines()
    embed = disnake.Embed(color=random.choice(colors))
    embed.add_field(name='Truth question', value=random.choice(lines))
    await ctx.send(embed=embed)

@_bot.slash_command(description="Get an compliment")
async def compliment(ctx):
    lines = open("compliments.txt",  encoding='utf-8').read().splitlines()
    embed = disnake.Embed(color=random.choice(colors))
    embed.add_field(name='Compliment', value=random.choice(lines))
    await ctx.send(embed=embed)

async def loan_payment(user):
    with open('loan.json', 'r', encoding='utf-8') as file:
        data = json.load(file)  

    if str(user.author.id) in data:
        return False
    else:
        data[str(user.author.id)] = {}
        data[str(user.author.id)]['Loan'] = 0
    with open('loan.json', 'w') as f:
        json.dump(data, f)
    
    return True

@_bot.event
async def loan_payment_process(ctx):
    with open('loan.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    if data[str(ctx.author.id)]['Loan'] == 0:
        pass
    
    else:
        await asyncio.sleep(259200)
        
        with open("account.json", 'r', encoding='utf-8') as data2:
            file2 = json.load(data2)
        
        if file2[str(ctx.author.id)]["Crypto"] != 0:
            file2[str(ctx.author.id)]["Crypto"] *= 0
            with open("account.json", 'w') as data2:
                json.dump(file2, data2)
        else:
            if len(file2[str(ctx.author.id)]["Inventory"]) != 0:
                file2[str(ctx.author.id)]["Inventory"].clear()
                with open("account.json", 'w') as data2:
                    json.dump(file2, data2)
            else:
                if file2[str(ctx.author.id)]["XP"] >= 500:
                    file2[str(ctx.author.id)]["XP"] -= 500
                    with open("account.json", 'w') as data2:
                        json.dump(file2, data2)
                else:
                    file2[str(ctx.author.id)]["XP"] *= 0
                    with open("account.json", 'w') as data2:
                        json.dump(file2, data2)
                
@_bot.slash_command(description="Pay amount for your loan")
async def pay(ctx, amount: int):
    with open("account.json", 'r', encoding='utf-8') as file2:
        data2 = json.load(file2)
    
    if data2[str(ctx.author.id)]['Bank'] >= 10000:
        with open("loan.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        if amount <= data2[str(ctx.author.id)]['Bank'] :
            if amount <= data[str(ctx.author.id)]['Loan']:

                data[str(ctx.author.id)]['Loan'] -= amount

                with open("loan.json", 'w') as file:
                    json.dump(data, file)  
    
                data2[str(ctx.author.id)]['Bank'] -= amount

                with open("account.json", 'w') as file2:
                    json.dump(data2, file2)

                await ctx.send(f"You have paid {amount} <:nerd_coin:992265892756979735> for your loan")  
            
            else:
                await ctx.send("You cant pay money more than the loan")
        
        else:
            await ctx.send("You don't have enough money to pay your loan")
    
    else:
        await ctx.send("Have at least 10k <:nerd_coin:992265892756979735> to pay for loan")

@_bot.slash_command(description="Get some dad jokes")
async def dadjokes(ctx):
    lines = open("dadjokes.txt", encoding='utf-8').read().splitlines()
    embed = disnake.Embed(color=random.choice(colors))
    embed.add_field(name='Dad joke', value=random.choice(lines))
    await ctx.send(embed=embed)

@_bot.slash_command(description="Check how much of your loan is left")
async def lend(ctx):
    with open("loan.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    embed = disnake.Embed(title='Your loan', color=random.choice(colors))
    embed.add_field(name='------', value=data[str(ctx.author.id)]["Loan"])
    await ctx.send(embed=embed)

@_bot.slash_command(description="Take loan from bank")
async def loan(ctx, amount: int):
    with open('account.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    with open('loan.json', 'r', encoding='utf-8') as file2:
        data2 = json.load(file2)
    
    if data[str(ctx.author.id)]["Bank"] <= 10000:
        await ctx.send("You need to have at least 10000 <:nerd_coin:992265892756979735> in your bank because you have to pay 10000 per 2 hours")
    
    elif amount <= 100000:
        await ctx.send("You can't buy a loan less than 100000 <:nerd_coin:992265892756979735>")
    
    elif amount % 10 != 0:
        await ctx.send("You can have loan only in 0s for example, 100000/1000000/10000000 etc.")
    
    elif data2[str(ctx.author.id)]['Loan'] != 0:
        await ctx.send(f"You have a loan left of {data2[str(ctx.author.id)]['Loan']} <:nerd_coin:992265892756979735>")

    else:
        await ctx.send(f"You took loan of {amount} <:nerd_coin:992265892756979735>, you need to pay 10k <:nerd_coin:992265892756979735> {amount / 10000} times to finish your loan. You have 3 days to remaining to pay your loan")
        data[str(ctx.author.id)]["Bank"] += amount
        data2[str(ctx.author.id)]["Loan"] += amount

        with open("account.json", 'w') as file:
            json.dump(data, file)
        
        with open("loan.json", 'w') as file2:
            json.dump(data2, file2)

async def busines(user):
    with open('business.json', 'r',encoding='utf-8') as file:
        data = json.load(file)  

    if str(user.author.id) in data:
        return False
    else:
        data[str(user.author.id)] = {}
        data[str(user.author.id)]['Income'] = 100
        data[str(user.author.id)]['Facilities'] = []
    
    with open('business.json', 'w') as f: 
        json.dump(data, f)
    
class Spacelab(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Self destruction", style=disnake.ButtonStyle.blurple)
    async def dest(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        with open('business.json', 'r', encoding='utf-8') as file:
            data = json.load(file) 
        
        data[str(interaction.user.id)]['Facilities'].remove("Space research sector 🔭")

        with open("business.json", 'w') as file:
            json.dump(data, file)

        await interaction.response.send_message("You have destroyed radiation lab")

class Radlab(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Self destruction", style=disnake.ButtonStyle.blurple)
    async def dest(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        with open('business.json', 'r', encoding='utf-8') as file:
            data = json.load(file) 
        
        data[str(interaction.user.id)]['Facilities'].remove("Radiation sector ☣")

        with open("business.json", 'w') as file:
            json.dump(data, file)

        await interaction.response.send_message("You have destroyed radiation lab")

class Biolab(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Self destruction", style=disnake.ButtonStyle.blurple)
    async def dest(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        with open('business.json', 'r', encoding='utf-8') as file:
            data = json.load(file) 
        
        data[str(interaction.user.id)]['Facilities'].remove("Bio-Lab sector 🦠")

        with open("business.json", 'w') as file:
            json.dump(data, file)

        await interaction.response.send_message("You have destroyed bio lab")

class Business(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Get money", style=disnake.ButtonStyle.blurple)
    async def money(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        with open('business.json', 'r', encoding='utf-8') as file:
            data = json.load(file)  
        
        with open("account.json", 'r', encoding='utf-8') as file2:
            data2 = json.load(file2)
        
        data2[str(interaction.user.id)]["Bank"] += data[str(interaction.user.id)]["Income"]

        with open("account.json", 'w') as file2:
            json.dump(data2, file2)
        
        await interaction.response.send_message(f"You have earned {data[str(interaction.user.id)]['Income']} <:nerd_coin:992265892756979735>")
    
    @disnake.ui.button(label="Bio-Lab sector 🦠", style=disnake.ButtonStyle.blurple)
    async def bio_lab(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        with open('business.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        if "Bio-Lab sector 🦠" not in data[str(interaction.user.id)]["Facilities"]:
        
            with open("account.json", 'r', encoding='utf-8') as file2:
                data2 = json.load(file2)
        
            if data2[str(interaction.user.id)]["Bank"] >= 500000:
                data[str(interaction.user.id)]["Income"] += 1000
                data[str(interaction.user.id)]["Facilities"].append("Bio-Lab sector 🦠") 

                with open("account.json", 'w') as file2:
                    json.dump(data2, file2)

                with open("business.json", 'w') as file:
                    json.dump(data, file)

                await interaction.response.send_message("You have increased your income by 1000 <:nerd_coin:992265892756979735> and Bio-Lab sector 🦠 have been added in facilites.")
            
            else:
                await interaction.response.send_message("You need to have 500000 <:nerd_coin:992265892756979735>")

        else:          
            with open('business.json', 'r', encoding='utf-8') as file:
                data = json.load(file)  
            
            embed = disnake.Embed(title="Bio-Lab sector 🦠", color=random.choice(colors))
            await interaction.response.send_message(embed=embed, view=Biolab(), file=disnake.File('biolab.jpeg'))
    
    @disnake.ui.button(label="Radiation sector ☣", style=disnake.ButtonStyle.blurple)
    async def rad(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        with open('business.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        if "Radiation sector ☣" not in data[str(interaction.user.id)]["Facilities"]:
        
            with open("account.json", 'r', encoding='utf-8') as file2:
                data2 = json.load(file2)
        
            if data2[str(interaction.user.id)]["Bank"] >= 600000:
                data[str(interaction.user.id)]["Income"] += 2000
                data[str(interaction.user.id)]["Facilities"].append("Radiation sector ☣") 

                with open("account.json", 'w') as file2:
                    json.dump(data2, file2)

                with open("business.json", 'w') as file:
                    json.dump(data, file)

                await interaction.response.send_message("You have increased your income by 2000 <:nerd_coin:992265892756979735> and Radiation sector ☣ have been added in facilites.")
            
            else:
                await interaction.response.send_message("You need to have 600000 <:nerd_coin:992265892756979735>")

        else:          
            with open('business.json', 'r', encoding='utf-8') as file:
                data = json.load(file)  
            
            embed = disnake.Embed(title="Radiation sector ☣", color=random.choice(colors))
            await interaction.response.send_message(embed=embed, view=Radlab(), file=disnake.File('radlab.jpeg'))
    
    @disnake.ui.button(label="Space research sector 🔭", style=disnake.ButtonStyle.blurple)
    async def sp(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        with open('business.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        if "Space research sector 🔭" not in data[str(interaction.user.id)]["Facilities"]:
        
            with open("account.json", 'r', encoding='utf-8') as file2:
                data2 = json.load(file2)
        
            if data2[str(interaction.user.id)]["Bank"] >= 700000:
                data[str(interaction.user.id)]["Income"] += 3000
                data[str(interaction.user.id)]["Facilities"].append("Space research sector 🔭") 

                with open("account.json", 'w') as file2:
                    json.dump(data2, file2)

                with open("business.json", 'w') as file:
                    json.dump(data, file)

                await interaction.response.send_message("You have increased your income by 3000 <:nerd_coin:992265892756979735> and Radiation sector ☣ have been added in facilites.")
            
            else:
                await interaction.response.send_message("You need to have 700000 <:nerd_coin:992265892756979735>")

        else:          
            with open('business.json', 'r', encoding='utf-8') as file:
                data = json.load(file)  
            
            embed = disnake.Embed(title="Space research sector 🔭", color=random.choice(colors))
            await interaction.response.send_message(embed=embed, view=Spacelab(), file=disnake.File('spacelab.jpeg'))

@_bot.slash_command(description='Start your own business')
async def business(ctx):
    with open("account.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    with open("business.json", 'r', encoding='utf-8') as file2:
        data2 = json.load(file2)
    
    if data[str(ctx.author.id)]["Bank"] >= 10000000:
        if str(ctx.author.id) in data2:
            color = disnake.Color(value=random.choice(colors))
            embed = disnake.Embed(title=f"{ctx.author}'s Company", color=color)
            embed.add_field(name="Income", value=data2[str(ctx.author.id)]["Income"])
            await ctx.send(embed=embed, view=Business())
        
        else:
            await busines(ctx)
            data[str(ctx.author.id)]["Bank"] -= 10000000
            with open("account.json", 'w') as file:
                json.dump(data, file)
            await ctx.send("You have started a business now, check your business using the same command.")
    
    else:
        await ctx.send("You need to have at least 10 millions of <:nerd_coin:992265892756979735> to start your own business")

async def spem(user):
    with open('spam.json', 'r', encoding='utf-8') as file:
        data = json.load(file)  

    if str(user.guild.id) in data:
        return False                    
    else:
        data[str(user.guild.id)] = {}
        data[str(user.guild.id)]['Spam'] = [1]
        data[str(user.guild.id)]['Dis'] = []
    
    with open('spam.json', 'w') as file:
        json.dump(data, file)  

@_bot.slash_command(description="Set the level messages channel")
async def levlog(ctx, channel_id):
    with open("setup.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    if len(data[str(ctx.guild.id)]["level"]) == 0:
        data[str(ctx.guild.id)]["level"].append(channel_id)
        await ctx.send(f"You have set up leveling logs in {_bot.get_channel(channel_id)}")
        with open("setup.json", 'w') as file:
            json.dump(data, file)
    else:
        data[str(ctx.guild.id)]["level"].clear()
        with open("setup.json", 'w') as file:
            json.dump(data, file)
        data[str(ctx.guild.id)]["level"].append(channel_id)
        with open("setup.json", 'w') as file:
            json.dump(data, file)
        await ctx.send(f"You have set up new leveling logs in {_bot.get_channel(channel_id)}")

@_bot.slash_command(description="Enable or disable spam protection")
@commands.has_permissions(administrator = True)
async def spam(ctx):   
    await spem(ctx)
    
    with open('spam.json', 'r', encoding='utf-8') as file:
        data = json.load(file)  
    if 1 in data[str(ctx.guild.id)]['Spam']:
        data[str(ctx.guild.id)]['Spam'][0] += 1
        color = disnake.Color(value=random.choice(colors))
        em = disnake.Embed(color=color, title="Spam protection")
        em.add_field(name='Enabled', value=data[str(ctx.guild.id)]['Spam'])
        await ctx.send(embed=em)
        await ctx.send("Spam protection is now disabled")
        with open('spam.json', 'w') as file:
            json.dump(data, file)  

    else:
        data[str(ctx.guild.id)]['Spam'][0] -= 1
        color = disnake.Color(value=random.choice(colors))
        em = disnake.Embed(color=color, title="Spam protection")
        em.add_field(name='Enabled', value=data[str(ctx.guild.id)]['Spam'])
        await ctx.send(embed=em)
        await ctx.send("Spam protection is now enabled")
    
        with open('spam.json', 'w') as file:
            json.dump(data, file)  

@_bot.slash_command(description="Send money to someone")
async def send(ctx, member: disnake.Member, amount: int):
    with open("account.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    if amount >= data[str(ctx.author.id)]['Bank']:
        await ctx.send(f"You don't have that much money, how would you give it to {member}?")
    else:

        data[str(member.id)]['Bank'] += amount
        data[str(ctx.author.id)]['Bank'] -= amount
        with open("account.json", 'w') as file:
            json.dump(data, file)

        await ctx.send("Transaction done")

@_bot.event
async def on_message(message):
        with open('spam.json', 'r', encoding='utf-8') as file:
            data = json.load(file)  
    
        await spem(message)

        if 1 in data[str(message.guild.id)]['Spam']:

                global author_msg_counts

                author_id = message.author.id
                curr_time = datetime.datetime.now().timestamp() * 1000

                if not author_msg_times.get(author_id, False):
                    author_msg_times[author_id] = []

                author_msg_times[author_id].append(curr_time)
                expr_time = curr_time - time_window_milliseconds
                expired_msgs = [
                    msg_time for msg_time in author_msg_times[author_id]
                    if msg_time < expr_time
                ]

                for msg_time in expired_msgs:
                    author_msg_times[author_id].remove(msg_time)

                if len(author_msg_times[author_id]) > max_msg_per_window:
                    color = disnake.Color(value=random.choice(colors))
                    em = disnake.Embed(color=color, title=f"WARNING: by The Nerd from **{message.guild.name}**.",   description="You need to stop spamming")
                    await message.author.send(embed=em)
                    try:
                        await message.channel.send(f"{message.author.mention} has been kicked")
                        await message.author.kick()
                    except disnake.Forbidden:
                        await message.channel.send("I don't have banning permissions")
                    except disnake.ext.commands.MissingPermissions:
                        await message.channel.send("Sorry, you don't have permission to run this command")
                
                if not message.author.bot:
                    await open_account(message)
                    await xp(message, 5)
                    await lvl(message)
                    await coin_boost(message)
                    await xp_boost(message)
                    await kali_installed(message)
                    await win10_installed(message)
                    await loan_payment(message)
                    await loan_payment_process(message)
        
        else:   
            if not message.author.bot:
                await open_account(message)
                await xp(message, 5)
                await lvl(message)
                await coin_boost(message)
                await xp_boost(message)
                await kali_installed(message)
                await win10_installed(message)
                await loan_payment(message)
                await loan_payment_process(message)

            else:
                pass

        await _bot.process_commands(message)

_bot.run(Your token")      
