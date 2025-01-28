import discord
from discord.ext import commands
import aiohttp
import os
import json

black = "\u001b[30m"
red = "\u001b[31m"
green = "\u001b[32m"
yellow = "\u001b[33m"
blue = "\u001b[34m"
magenta = "\u001b[35m"
cyan = "\u001b[36m"
white = "\u001b[37m"
reset = "\u001b[0m"
pink = "\u001b[38;2;255;192;203m"
light_green = "\u001b[92m"
light_yellow = "\u001b[93m"
light_magenta = "\u001b[95m"
light_cyan = "\u001b[96m"
light_red = "\u001b[91m"
light_blue = "\u001b[94m"

class TokenManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    async def validate_token(self, token):
        client = discord.Client(intents=discord.Intents.default())
        token_status = {"active": False, "username": None}

        @client.event
        async def on_ready():
            token_status["username"] = f"{client.user.name}#{client.user.discriminator}"
            token_status["active"] = True
            await client.close()

        try:
            await client.start(token, bot=False)
        except discord.errors.LoginFailure:
            return False, "Invalid token"
        except Exception as e:
            return False, f"Error: {str(e)}"

        if token_status["active"]:
            return True, token_status["username"]
        return False, "Failed to validate token"

    @commands.command(name="addtoken")
    async def add_token(self, ctx, token: str):
        try:
            await ctx.message.delete()
        except:
            pass

        token = token.strip()
        
        is_valid, details = await self.validate_token(token)
        
        if is_valid:
            tokens = []
            if os.path.exists('token.txt'):
                with open('token.txt', 'r') as f:
                    tokens = [t.strip() for t in f.readlines() if t.strip()]
                    
                if token in tokens:
                    await ctx.send(f"```ansi\n{yellow}Token already exists in the file{reset}```", delete_after=5)
                    return

            tokens.append(token)
            
            with open('token.txt', 'w') as f:
                f.write('\n'.join(tokens))
                if tokens: 
                    f.write('\n')
                    
            await ctx.send(f"```ansi\n{green}Token added successfully User: {details}{reset}```", delete_after=5)
        else:
            await ctx.send(f"```ansi\n{red}Invalid token! Error: {details}{reset}```", delete_after=5)

    @commands.command(name="removetoken")
    async def remove_token(self, ctx, token: str):
        try:
            await ctx.message.delete()
        except:
            pass

        token = token.strip()
        
        if os.path.exists('token.txt'):
            with open('token.txt', 'r') as f:
                tokens = [t.strip() for t in f.readlines() if t.strip()]
            
            if token in tokens:
                tokens.remove(token)
                with open('token.txt', 'w') as f:
                    f.write('\n'.join(tokens))
                    if tokens:
                        f.write('\n')
                await ctx.send(f"```ansi\n{green}  Token removed successfully!{reset}```", delete_after=5)
            else:
                await ctx.send(f"```ansi\n{red}  Token not found in the file!{reset}```", delete_after=5)
        else:
            await ctx.send(f"```ansi\n{red}  No token file exists!{reset}```", delete_after=5)

    @commands.command(name="listtokens")
    async def list_tokens(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass

        if os.path.exists('token.txt'):
            with open('token.txt', 'r') as f:
                tokens = [t.strip() for t in f.readlines() if t.strip()]
            
            if tokens:
                tokens_text = f"```ansi\n{cyan}Current tokens:\n" + "\n".join(f"{i+1}. {token}" for i, token in enumerate(tokens)) + f"{reset}```"
                await ctx.send(tokens_text, delete_after=10)
            else:
                await ctx.send(f"```ansi\n{yellow}No tokens found in the file!{reset}```", delete_after=5)
        else:
            await ctx.send(f"```ansi\n{red}  No token file exists!{reset}```", delete_after=5)

    @commands.command(name="cleartoken")
    async def clear_tokens(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass

        if os.path.exists('token.txt'):
            with open('token.txt', 'w') as f:
                f.write('')
            await ctx.send(f"```ansi\n{green}  All tokens have been cleared!{reset}```", delete_after=5)
        else:
            await ctx.send(f"```ansi\n{red}  No token file exists!{reset}```", delete_after=5)

def setup(bot):
    bot.add_cog(TokenManager(bot))
