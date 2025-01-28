import discord
from discord.ext import commands
import threading
import random
import string
import os
import tls_client
import asyncio
from colorama import Fore, Style

class TokenJoiner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.joined_tokens_lock = threading.Lock()
        self.client = tls_client.Session(
            client_identifier="chrome112",
            random_tls_extension_order=True
        )
        self.tokens = []
        self.proxies = []
        self.joined_count = 0
        self.not_joined_count = 0
        self.done_event = threading.Event()

    def headers(self, token: str):
        return {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': token,
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjExMDQzNzg1NDMwNzg2Mzc1OTEiLCJsb2NhdGlvbl9jaGFubmVsX2lkIjoiMTEwNzI4NDk3MTkwMDYzMzIzMCIsImxvY2F0aW9uX2NoYW5uZWxfdHlwZSI6MH0=',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-GB',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6Iml0LUlUIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEyLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE5MzkwNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='
        }

    def get_cookies(self):
        cookies = {}
        try:
            response = self.client.get('https://discord.com')
            for cookie in response.cookies:
                if cookie.name.startswith('__') and cookie.name.endswith('uid'):
                    cookies[cookie.name] = cookie.value
            return cookies
        except Exception as e:
            print(f'Failed to obtain cookies ({e})')
            return cookies

    async def accept_invite(self, token: str, invite: str, proxy_: str, status_message):
        try:
            payload = {
                'session_id': ''.join(random.choice(string.ascii_lowercase) + random.choice(string.digits) for _ in range(16))
            }

            proxy = {
                "http": f"http://{proxy_}",
                "https": f"https://{proxy_}"
            } if proxy_ else None

            response = self.client.post(
                url=f'https://discord.com/api/v10/invites/{invite}',
                headers=self.headers(token=token),
                json=payload,
                cookies=self.get_cookies(),
                proxy=proxy
            )
            
            response_json = response.json()
            status_text = ""

            if response.status_code == 200:
                self.joined_count += 1
                status_text = f"Token {token[:10]}... joined successfully"
            else:
                self.not_joined_count += 1
                status_text = f"Token {token[:10]}... failed to join ({response.status_code})"

            await status_message.edit(content=f"```\nJoining progress:\nSuccessful: {self.joined_count}\nFailed: {self.not_joined_count}\nLast action: {status_text}```")

        except Exception as e:
            self.not_joined_count += 1
            await status_message.edit(content=f"```\nError with token {token[:20]}...: {str(e)}```")

        if self.joined_count + self.not_joined_count >= len(self.tokens):
            self.done_event.set()

    def load_tokens(self):
        with open("tokens.txt", "r") as file:
            return [line.strip() for line in file if line.strip()]

    def load_proxies(self):
        try:
            with open("proxies.txt", "r") as file:
                return [line.strip() for line in file if line.strip()]
        except:
            return []

    @commands.command()
    async def tjoin(self, ctx, invite_link: str, token_count: int):

        self.joined_count = 0
        self.not_joined_count = 0
        self.done_event.clear()
        

        invite_code = invite_link.split('/')[-1]
        
        self.tokens = self.load_tokens()[:token_count]
        self.proxies = self.load_proxies()
        
        if not self.tokens:
            await ctx.send("```No tokens found in input/tokens.txt```")
            return

        status_message = await ctx.send("```Starting join process...```")
        
        proxy_iter = iter(self.proxies) if self.proxies else iter([None] * len(self.tokens))
        
        tasks = []
        for token in self.tokens:
            proxy = next(proxy_iter, None)
            task = asyncio.create_task(self.accept_invite(token, invite_code, proxy, status_message))
            tasks.append(task)
            await asyncio.sleep(0.5)
        
        await asyncio.gather(*tasks)
        

        await status_message.edit(content=f"```Join process completed:\nSuccessful joins: {self.joined_count}\nFailed joins: {self.not_joined_count}```")

def setup(bot):
    bot.add_cog(TokenJoiner(bot))