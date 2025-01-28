import discord
from discord.ext import commands
from plyer import notification
import json
import os
import aiohttp

class PingNotification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.notifications_enabled = {}
        self.dm_notifications = {}
        self.dm_notifications_enabled = {}
        self.reaction_notifications_enabled = {}

        self.load_data()
        self.loadd_data()
        self.load_reaction_data()

    def loadd_data(self):
        try:
            with open("nondm_settings.json", "r") as f:
                self.dm_notifications = json.load(f)
        except FileNotFoundError:
            self.dm_notifications = {}

    def saves_data(self):
        with open("nondm_settings.json", "w") as f:
            json.dump(self.dm_notifications, f, indent=4)

    def load_data(self):
        try:
            with open("nonping_settings.json", "r") as f:
                self.notifications_enabled = json.load(f)
        except FileNotFoundError:
            self.notifications_enabled = {}

    def save_data(self):
        with open("nonping_settings.json", "w") as f:
            json.dump(self.notifications_enabled, f, indent=4)


    def load_reaction_data(self):
        try:
            with open("nonreaction_settings.json", "r") as f:
                self.reaction_notifications_enabled = json.load(f)
        except FileNotFoundError:
            self.reaction_notifications_enabled = {}

    def save_reaction_data(self):
        with open("nonreaction_settings.json", "w") as f:
            json.dump(self.reaction_notifications_enabled, f, indent=4)




    @commands.group(name="nonping", invoke_without_command=True)
    async def nonping(self, ctx):
        await ctx.send("""```ansi
[ nonping ] Notification system when you are pinged.
    Usage:
        nonping on  - Enable ping notifications.
        nonping off - Disable ping notifications.
        nonping status - Check your notification status.
```""")

    @nonping.command(name="on")
    async def nonping_on(self, ctx):
        user_id = str(ctx.author.id)
        self.notifications_enabled[user_id] = True
        self.save_data()
        await ctx.send(f"```Ping notifications enabled for.```")

    @nonping.command(name="off")
    async def nonping_off(self, ctx):
        user_id = str(ctx.author.id)
        self.notifications_enabled[user_id] = False
        self.save_data()
        await ctx.send(f"```Ping notifications disabled for.```")

    @nonping.command(name="status")
    async def nonping_status(self, ctx):
        user_id = str(ctx.author.id)
        status = self.notifications_enabled.get(user_id, False)
        await ctx.send(
            f"```Ping notifications are {'enabled' if status else 'disabled'}.```"
        )
    @commands.group(name="nondm", invoke_without_command=True)
    async def nondm(self, ctx):
        await ctx.send("""```ansi
[ nondm ] Notification system for direct messages.
    Usage:
        nondm on  - Enable DM notifications.
        nondm off - Disable DM notifications.
        nondm status - Check your DM notification status.
```""")

    @nondm.command(name="on")
    async def nondm_on(self, ctx):
        self.dm_notifications_enabled = True
        await ctx.send(f"```DM notifications enabled globally.```")

    @nondm.command(name="off")
    async def nondm_off(self, ctx):
        self.dm_notifications_enabled = False
        await ctx.send(f"```DM notifications disabled globally.```")

    @nondm.command(name="status")
    async def nondm_status(self, ctx):
        status = "enabled" if self.dm_notifications_enabled else "disabled"
        await ctx.send(f"```DM notifications are currently {status}.```")

    @commands.group(name="nonreaction", invoke_without_command=True)
    async def nonreaction(self, ctx):
        await ctx.send("""```ansi
[ nonreaction ] Notification system for reactions to your messages.
    Usage:
        nonreaction on  - Enable reaction notifications.
        nonreaction off - Disable reaction notifications.
        nonreaction status - Check your reaction notification status.
```""")

    @nonreaction.command(name="on")
    async def nonreaction_on(self, ctx):
        user_id = str(ctx.author.id)
        self.reaction_notifications_enabled[user_id] = True
        self.save_reaction_data()
        await ctx.send(f"```Reaction notifications enabled.```")

    @nonreaction.command(name="off")
    async def nonreaction_off(self, ctx):
        user_id = str(ctx.author.id)
        self.reaction_notifications_enabled[user_id] = False
        self.save_reaction_data()
        await ctx.send(f"```Reaction notifications disabled.```")

    @nonreaction.command(name="status")
    async def nonreaction_status(self, ctx):
        user_id = str(ctx.author.id)
        status = self.reaction_notifications_enabled.get(user_id, False)
        await ctx.send(f"```Reaction notifications are {'enabled' if status else 'disabled'}.```")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return 

        for mentioned_user in message.mentions:
            user_id = str(mentioned_user.id)
            if self.notifications_enabled.get(user_id, False):
                content = message.content or "You were mentioned."
                author_name = message.author.name

                try:
                    notification.notify(
                        title=f"pinged by @{author_name} >.<!",
                        message=content,
                        app_name="Birth Selfbot",
                        timeout=5,
                        app_icon="695eb4bbf96291ef0813969a32fd4776.ico",  
                    )
                except Exception as e:
                    print(f"Failed to send notification: {e}")

        if message.guild is None: 
            if self.dm_notifications_enabled: 
                if message.author.id == self.bot.user.id:
                    return 

                content = message.content or "No content"
                author_name = message.author.name
                try:
                    print(f"Sending DM notification for {author_name}")
                    notification.notify(
                        title=f"@{author_name} dmed you >.< !",
                        message=content,
                        app_name="Birth Selfbot",
                        timeout=5,
                        app_icon="695eb4bbf96291ef0813969a32fd4776.ico"
                    )
                except Exception as e:
                    print(f"Failed to send DM notification: {e}")



    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.id == self.bot.user.id:  
            return
            
        if reaction.message.author.id == self.bot.user.id:
            user_id = str(reaction.message.author.id)
            if not self.reaction_notifications_enabled.get(user_id, False):
                return
                
            content = f"Your message got a reaction from {user.name}!"
            message_author = reaction.message.author.name
            
            try:
                notification.notify(
                    title=f"Reaction from @{message_author} >.<!",
                    message=content,
                    app_name="Birth Selfbot",
                    timeout=5,
                    app_icon="695eb4bbf96291ef0813969a32fd4776.ico"
                )
            except Exception as e:
                print(f"Failed to send notification: {e}")
def setup(bot):
    bot.add_cog(PingNotification(bot))