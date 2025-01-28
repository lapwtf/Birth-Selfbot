import discord
from discord.ext import commands
import json
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"
reset = "\033[0m"
pink = "\033[38;2;255;192;203m"
light_green = "\033[92m"
light_yellow = "\033[93m"
light_magenta = "\033[95m"
light_cyan = "\033[96m"
light_red = "\033[91m"
light_blue = "\033[94m"

ronmessage_data = {}
sendonmessage_data = {}
eonmessage_data = {}

def load_data():
    global ronmessage_data, sendonmessage_data, eonmessage_data
    try:
        with open("ronmessage_data.json", "r") as f:
            ronmessage_data = json.load(f)
    except FileNotFoundError:
        ronmessage_data = {}
    
    try:
        with open("sendonmessage_data.json", "r") as f:
            sendonmessage_data = json.load(f)
    except FileNotFoundError:
        sendonmessage_data = {}
    
    try:
        with open("eonmessage_data.json", "r") as f:
            eonmessage_data = json.load(f)
    except FileNotFoundError:
        eonmessage_data = {}

def save_data():
    with open("ronmessage_data.json", "w") as f:
        json.dump(ronmessage_data, f, indent=4)
    with open("sendonmessage_data.json", "w") as f:
        json.dump(sendonmessage_data, f, indent=4)
    with open("eonmessage_data.json", "w") as f:
        json.dump(eonmessage_data, f, indent=4)
class RonMessageCog(commands.Cog, name="RonMessage"):
    def __init__(self, bot):
        self.bot = bot
        load_data()

    @commands.group(name="ronmessage", invoke_without_command=True)
    async def ronmessage(self, ctx):
        await ctx.send(f"""```ansi\n
[ {blue}ronmessage{reset} ] automatic reactions to messages.
    {red}Usage:{reset}
        {green}[ {blue}^{green} ] {black}ronmessage add <message> <reaction>{reset} - {black}Add a reaction to a specific message.{reset}
        {green}[ {blue}^{green} ] {black}ronmessage list{reset} - {black}List all messages with their reactions.{reset}
        {green}[ {blue}^{green} ] {black}ronmessage remove <message>{reset} - {black}Remove the reaction from a specific message.{reset}
        {green}[ {blue}^{green} ] {black}ronmessage clear{reset} - {black}Clear all message to reaction.{reset}
        {green}[ {blue}^{green} ] {black}ronmessage on <message>{reset} - {black}Enable reaction for a specific message.{reset}
        {green}[ {blue}^{green} ] {black}ronmessage off <message>{reset} - {black}Disable reaction for a specific message.{reset}```""")

    @ronmessage.command(name="add")
    async def ronmessage_add(self, ctx, message: str, reaction: str):
        if message in ronmessage_data:
            await ctx.send(f"```{message} already has a reaction set.```")
        else:
            ronmessage_data[message] = {'reaction': reaction, 'enabled': True}
            save_data()
            await ctx.send(f"```added reaction {reaction} to the message {message}.```")

    @ronmessage.command(name="list")
    async def ronmessage_list(self, ctx):
        if not ronmessage_data:
            await ctx.send("```No ronmessage found.```")
            return
        response = "```Current ronmessage:\n```"
        for message, data in ronmessage_data.items():
            status = "Enabled" if data.get('enabled', False) else "Disabled"
            response += f"```ansi\n{blue}Message: {white}{message}\n``` | Reaction: {data.get('reaction', 'None')} \n ```ansi\n {blue}Status: {red}{status}\n```"
        await ctx.send(response)

    @ronmessage.command(name="remove")
    async def ronmessage_remove(self, ctx, message: str):
        if message in ronmessage_data:
            del ronmessage_data[message]
            save_data()
            await ctx.send(f"```Removed the reaction for the message: {message}.```")
        else:
            await ctx.send(f"```No reaction found for the message: {message}.```")

    @ronmessage.command(name="clear")
    async def ronmessage_clear(self, ctx):
        ronmessage_data.clear()
        save_data()
        await ctx.send("```Cleared all ronmessage bindings.```")

    @ronmessage.command(name="on")
    async def ronmessage_on(self, ctx):
        if ronmessage_data:
            for message in ronmessage_data:
                ronmessage_data[message]['enabled'] = True
            save_data() 
            await ctx.send("```Enabled all reaction messages.```")
        else:
            await ctx.send("```No reaction messages found to enable.```")

    @ronmessage.command(name="off")
    async def ronmessage_off(self, ctx):
        if ronmessage_data:
            for message in ronmessage_data:
                ronmessage_data[message]['enabled'] = False
            save_data()
            await ctx.send("```Disabled all reaction messages.```")
        else:
            await ctx.send("```No reaction messages found to disable.```")

    @commands.group(name="sonmessage", invoke_without_command=True)
    async def sonmessage(self, ctx):
        await ctx.send(f"""```ansi\n
    [ {blue}sonmessage{reset} ] Automatic responses to messages.
        {red}Usage:{reset}
        {green}[ {blue}^{green} ] {black}sonmessage add <message> <response>{reset} - {black}Add a custom response to a specific message.{reset}
        {green}[ {blue}^{green} ] {black}sonmessage list{reset} - {black}List all messages with their responses.{reset}
        {green}[ {blue}^{green} ] {black}sonmessage remove <message>{reset} - {black}Remove the response from a specific message.{reset}
        {green}[ {blue}^{green} ] {black}sonmessage clear{reset} - {black}Clear all message-to-response bindings.{reset}
        {green}[ {blue}^{green} ] {black}sonmessage on <message>{reset} - {black}Enable response for a specific message.{reset}
        {green}[ {blue}^{green} ] {black}sonmessage off <message>{reset} - {black}Disable response for a specific message.{reset}
```""")

    @sonmessage.command(name="add")
    async def sonmessage_add(self, ctx, message: str, *, response: str):
        if message in sendonmessage_data:
            await ctx.send(f"```'{message}' already has a response set.```")
        else:
            sendonmessage_data[message] = {'response': response, 'enabled': True}
            save_data()
            await ctx.send(f"```Added response {response} to the message {message}.```")

    @sonmessage.command(name="list")
    async def sonmessage_list(self, ctx):
        if not sendonmessage_data:
            await ctx.send("```No sendonmessage bindings found.```")
            return
        response = "```Current sendonmessage:\n```"
        for message, data in sendonmessage_data.items():
            status = "Enabled" if data['enabled'] else "Disabled"
            response += f"```ansi\n{blue}Message: {white}{message}\n{blue}Response: {white}{data.get('response', 'None')}\n{blue}Status: {white}{status}\n```"
        await ctx.send(response)

    @sonmessage.command(name="remove")
    async def sonmessage_remove(self, ctx, message: str):
        if message in sendonmessage_data:
            del sendonmessage_data[message]
            save_data()
            await ctx.send(f"```Removed the response for the message: {message}.```")
        else:
            await ctx.send(f"```No response found for the message: {message}.```")

    @sonmessage.command(name="clear")
    async def sonmessage_clear(self, ctx):
        sendonmessage_data.clear()
        save_data()
        await ctx.send("```Cleared all sendonmessage.```")

    @sonmessage.command(name="on")
    async def sonmessage_on(self, ctx):
        if sendonmessage_data:
            for message in sendonmessage_data:
                sendonmessage_data[message]['enabled'] = True
            save_data() 
            await ctx.send("```Enabled all response messages.```")
        else:
            await ctx.send("```No response messages found to enable.```")

    @sonmessage.command(name="off")
    async def sonmessage_off(self, ctx):
        if sendonmessage_data:
            for message in sendonmessage_data:
                sendonmessage_data[message]['enabled'] = False
            save_data() 
            await ctx.send("```Disabled all response messages.```")
        else:
            await ctx.send("```No response messages found to disable.```")


    @commands.group(name="eonmessage", invoke_without_command=True)
    async def eonmessage(self, ctx):
        await ctx.send(f"""```ansi\n
[ {blue}eonmessage{reset} ] automatic message editing.
    {red}Usage:{reset}
    {green}[ {blue}^{green} ] {black}eonmessage add <message> <edited_message>{reset} - {black}Edit a specific message to a new message.{reset}
    {green}[ {blue}^{green} ] {black}eonmessage list{reset} - {black}List all messages with their edited versions.{reset}
    {green}[ {blue}^{green} ] {black}eonmessage remove <message>{reset} - {black}Remove the edited message from a specific message.{reset}
    {green}[ {blue}^{green} ] {black}eonmessage clear{reset} - {black}Clear all message-to-edited bindings.{reset}
    {green}[ {blue}^{green} ] {black}eonmessage on <message>{reset} - {black}Enable auto-edit for a specific message.{reset}
    {green}[ {blue}^{green} ] {black}eonmessage off <message>{reset} - {black}Disable auto-edit for a specific message.{reset}
```""")

    @eonmessage.command(name="add")
    async def eonmessage_add(self, ctx, message: str, *, edited_message: str):
        if message in eonmessage_data:
            await ctx.send(f"```'{message}' already has an edited message set.```")
        else:
            eonmessage_data[message] = {'edited_message': edited_message, 'enabled': True}
            save_data()
            await ctx.send(f"```Added edited message: {edited_message} to the message {message}.```")

    @eonmessage.command(name="list")
    async def eonmessage_list(self, ctx):
        if not eonmessage_data:
            await ctx.send("```No eonmessage bindings found.```")
            return
        response = "```Current eonmessage:\n```"
        for message, data in eonmessage_data.items():
            status = "Enabled" if data['enabled'] else "Disabled"
            response += f"```ansi\n{blue}Message: {white}{message}\n{blue}Edited Message: {white}{data.get('edited_message', 'None')}\n{blue}Status: {white}{status}\n```"
        await ctx.send(response)

    @eonmessage.command(name="remove")
    async def eonmessage_remove(self, ctx, message: str):
        if message in eonmessage_data:
            del eonmessage_data[message]
            save_data()
            await ctx.send(f"```Removed the edited message for the message: {message}.```")
        else:
            await ctx.send(f"```No edited message found for the message: {message}.```")

    @eonmessage.command(name="clear")
    async def eonmessage_clear(self, ctx):
        eonmessage_data.clear()
        save_data()
        await ctx.send("```Cleared all eonmessage bindings.```")

    @eonmessage.command(name="on")
    async def eonmessage_on(self, ctx):
        if eonmessage_data:
            for message in eonmessage_data:
                eonmessage_data[message]['enabled'] = True
            save_data() 
            await ctx.send("```Enabled all eonmessage edits.```")
        else:
            await ctx.send("```No eonmessage bindings found to enable.```")

    @eonmessage.command(name="off")
    async def eonmessage_off(self, ctx):
        if eonmessage_data:
            for message in eonmessage_data:
                eonmessage_data[message]['enabled'] = False
            save_data()  
            await ctx.send("```Disabled all eonmessage edits.```")
        else:
            await ctx.send("```No eonmessage bindings found to disable.```")
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content in ronmessage_data:
            if ronmessage_data[message.content].get('enabled', True): 
                reaction = ronmessage_data[message.content]['reaction']
                await message.add_reaction(reaction)

        if message.content in sendonmessage_data:
            if sendonmessage_data[message.content].get('enabled', True): 
                response = sendonmessage_data[message.content]['response']
                await message.channel.send(response)

        if message.content in eonmessage_data:
            if eonmessage_data[message.content].get('enabled', True):  
                edited_message = eonmessage_data[message.content]['edited_message']
                await message.edit(content=edited_message)


def setup(bot):
    load_data()  
    bot.add_cog(RonMessageCog(bot))