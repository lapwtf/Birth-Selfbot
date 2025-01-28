import os
import webbrowser
import subprocess
import platform
import tempfile
from urllib.parse import quote
import shutil
from discord.ext import commands
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
white = "\033[37m"
blue = "\033[34m"
black = "\033[30m"
light_green = "\033[92m" 
light_yellow = "\033[93m" 
light_magenta = "\033[95m" 
light_cyan = "\033[96m"  
light_red = "\033[91m"  
light_blue = "\033[94m"  
class BrowserCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bsearch(self, ctx, *, query: str):
        if platform.system() == "Windows":
            chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
            if not os.path.exists(chrome_path):
                await ctx.send("```ansi\n Google Chrome is not installed on this system.```")
                return
            url = f"https://www.google.com/search?q={query}"
            webbrowser.get(f'"{chrome_path}" %s').open(url)
            await ctx.send(f"```ansi\n {blue}Searching for {query} using Chrome.```")
        else:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            await ctx.send(f"```ansi\n {blue}Searching for {query} using your default browser.```")

    @commands.command()
    async def opencalc(self, ctx):
        if platform.system() == "Windows":
            try:
                subprocess.run('calc')
                await ctx.send(f"```ansi\n {blue}Opened Windows Calculator.```")
            except Exception as e:
                await ctx.send(f"```ansi\n {red}Error opening calculator: {e}```")
        else:
            await ctx.send(f"```{red}ansi\n Calculator is only available on Windows.```")

    @commands.command()
    async def openpad(self, ctx):
        if platform.system() == "Windows":
            try:
                subprocess.run('notepad')
                await ctx.send(f"```ansi\n {blue}Opened Windows Notepad.```")
            except Exception as e:
                await ctx.send(f"```ansi\n {red}Error opening Notepad: {e}```")
        else:
            await ctx.send(f"```ansi\n{red} Notepad is only available on Windows.```")

    @commands.command()
    async def dfolder(self, ctx, *, name: str):
        desktop_path = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
        folder_path = os.path.join(desktop_path, name)

        if os.path.exists(folder_path):
            await ctx.send(f"```ansi\n {red}The folder {blue}{name} {red}already exists.```")
        else:
            try:
                os.makedirs(folder_path)
                await ctx.send(f"```ansi\n {blue}Folder {name} has been created on your Desktop.```")
            except Exception as e:
                await ctx.send(f"```ansi\n {red}Error creating folder: {e}```")

        
    @commands.command()
    async def cleartemp(self, ctx):
        temp_folder = tempfile.gettempdir()
        
        msg = await ctx.send("```Clearing temp folder...```")

        try:
            files = os.listdir(temp_folder)
            total_files = len(files)
            deleted_files = 0

            update_interval = 5

            for filename in files:
                file_path = os.path.join(temp_folder, filename)
                
                try:
                    if os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                    else:
                        os.remove(file_path)
                    
                    deleted_files += 1
                    progress = (deleted_files / total_files) * 100

                    if deleted_files % update_interval == 0 or deleted_files == total_files:
                        await msg.edit(content=f"```ansi\n {blue}Clearing temp folder...\n {red}{progress:.2f}% completed.\n {blue}Deleting: {red}{filename}```")

                except Exception as e:
                    print("Error")
                    continue

            await msg.edit(content=f"```ansi\n {blue} Temp folder has been cleared successfully!```")

        except Exception as e:
            await msg.edit(content=f"```ansi\n {red}Error clearing temp folder: {e}```")

    @commands.command()
    async def byoutube(self, ctx, *, search: str):
        try:
            search_query = quote(search)

            youtube_url = f"https://www.youtube.com/results?search_query={search_query}"

            webbrowser.open(youtube_url)

            await ctx.send(f"```ansi\n {blue}YouTube search for {red}{search} {blue}has been opened.```")
        except Exception as e:
            await ctx.send(f"```ansi\n {red}An error occurred: {e}```")

    @commands.command()
    async def btiktok(self, ctx, *, search: str):
        try:
            search_query = quote(search)
            tiktok_url = f"https://www.tiktok.com/search?q={search_query}"
            webbrowser.open(tiktok_url)
            await ctx.send(f"```ansi\n {blue} TikTok search for {red}{search}{blue} has been opened.```")
        except Exception as e:
            await ctx.send(f"```ansi\n {red} An error occurred: {e}```")

    @commands.command()
    async def btwitter(self, ctx, *, search: str):
        try:
            search_query = quote(search)
            twitter_url = f"https://twitter.com/search?q={search_query}"
            webbrowser.open(twitter_url)
            await ctx.send(f"```ansi\n {blue} Twitter search for {red}{search}{blue} has been opened.```")
        except Exception as e:
            await ctx.send(f"```ansi\n {red} An error occurred: {e}```")

    @commands.command()
    async def broblox(self, ctx, *, search: str):
        try:
            search_query = quote(search)
            roblox_url = f"https://www.roblox.com/search/users/?keyword={search_query}"
            webbrowser.open(roblox_url)
            await ctx.send(f"```ansi\n {blue} Roblox search for user {red}{search}{blue} has been opened.```")
        except Exception as e:
            await ctx.send(f"```ansi\n {red} An error occurred: {e}```")

def setup(bot):
    bot.add_cog(BrowserCommands(bot))