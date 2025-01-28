import discord
import asyncio
from discord.ext import commands
import json
import os
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
TIMEOUT = 60  


kitty_frames = [
    f"{white}⠀⠀⠀⠀⢀⡠⠤⠔⢲⢶⡖⠒⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⣠⡚⠁⢀⠀⠀⢄⢻⣿⠀⠀⠀⡙⣷⢤⡀⠀⠀⠀⠀⠀⠀",
    f"{white}⠀⡜⢱⣇⠀⣧⢣⡀⠀⡀⢻⡇⠀⡄⢰⣿⣷⡌⣢⡀⠀⠀⠀⠀\n⠸⡇⡎⡿⣆⠹⣷⡹⣄⠙⣽⣿⢸⣧⣼⣿⣿⣿⣶⣼⣆⠀⠀⠀",
    f"{white}⣷⡇⣷⡇⢹⢳⡽⣿⡽⣷⡜⣿⣾⢸⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀\n⣿⡇⡿⣿⠀⠣⠹⣾⣿⣮⠿⣞⣿⢸⣿⣛⢿⣿⡟⠯⠉⠙⠛⠓",
    f"{white}⣿⣇⣷⠙⡇⠀⠁⠀{red}⠉⣽⣷⣾{white}⢿⢸⣿⠀⢸⣿⢿⠀⠀⠀⠀⠀\n⡟⢿⣿⣷{red}⣾⣆{white}⠀⠀{red}⠘⠘⠿⠛{white}⢸⣼⣿⢖⣼⣿⠘⡆⠀⠀⠀⠀",
    f"{white}⠃⢸⣿⣿{red}⡘⠋{white}⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⡆⠇⠀⠀⠀⠀\n⠀⢸⡿⣿⣇⠀⠈⠀⠤⠀⠀⢀⣿⣿⣿⣿⣿⣿⣧⢸⠀⠀⠀⠀",
    f"{white}⠀⠈⡇⣿⣿⣷⣤⣀⠀⣀⠔⠋⣿⣿⣿⣿⣿⡟⣿⡞⡄⠀⠀⠀\n⠀⠀⢿⢸⣿⣿⣿⣿⣿⡇⠀⢠⣿⡏⢿⣿⣿⡇⢸⣇⠇⠀⠀⠀",
    f"{white}⠀⠀⢸⡏⣿⣿⣿⠟⠋⣀⠠⣾⣿⠡⠀⢉⢟⠷⢼⣿⣿⠀⠀⠀\n⠀⠀⠈⣷⡏⡱⠁⠀⠊⠀⠀⣿⣏⣀⡠⢣⠃⠀⠀⢹⣿⡄⠀⠀",
    f"{white}⠀⠀⠘⢼⣿⠀⢠⣤⣀⠉⣹⡿⠀⠁⠀⡸⠀⠀⠀⠈⣿⡇⠀⠀\n{red}    social and lap runs you"
]


async def get_page_count(pages):
    return len(pages) 
pages = {
    1: f"""
    {magenta}Multi Token Management{reset}
    [ {blue}1{reset} ] outlast <@user>          - Outlast @user in channel
    [ {blue}2{reset} ] stopoutlast              - Stop outlast command
    [ {blue}3{reset} ] multilast <@user>        - Multiple token outlast
    [ {blue}4{reset} ] stopmultilast            - Stop multilast command
    [ {blue}5{reset} ] tok                      - Showcases all tokens
    [ {blue}6{reset} ] multivc                  - Connects all tokens to VC

    {magenta}Auto Response{reset}
    [ {blue}7{reset} ] ar <@user>               - Autoresponds to @user
    [ {blue}8{reset} ] arend                    - Stop autoresponse
    [ {blue}9{reset} ] arm <@user>              - Autoreply multi token
    [ {blue}10{reset} ] armend                  - Stop multi token autoreply

    {magenta}Spam & Control{reset}
    [ {blue}11{reset} ] kill <@user>            - Spams @user until rate limit
    [ {blue}12{reset} ] killend                 - Stop kill command
    [ {blue}13{reset} ] gcfill                  - Fills gc with tokens
    [ {blue}14{reset} ] gc                      - Changes gc with tokens
    [ {blue}15{reset} ] gcend                   - Stop gc command
    [ {blue}16{reset} ] mping                   - Mass ping the server with tokens
    [ {blue}17{reset} ] mpingoff                - Turns off mass ping
    [ {blue}18{reset} ] invis                   - Mass spam invis text
    [ {blue}19{reset} ] invisoff                - Turns off invis spam
    [ {blue}20{reset} ] popout                  - Auto Press

    {magenta}Message Formatting{reset}
    [ {blue}21{reset} ] bold                    - Turns all messages bold
    [ {blue}22{reset} ] unbold                  - Turns off bold messages
    [ {blue}23{reset} ] cord                    - Pings user while making message bold
    [ {blue}24{reset} ] cordoff                 - Turns off cord command
    [ {blue}25{reset} ] translate <language>    - Translates your message
    [ {blue}26{reset} ] translateoff            - Turns off translate

    {magenta}Reactions & Status{reset}
    [ {blue}27{reset} ] mreact                  - Mass reacts with specific emoji
    [ {blue}28{reset} ] reactoff                - Turns off mass react
    [ {blue}29{reset} ] autoreact               - Auto react to messages globally
    [ {blue}30{reset} ] autoreactoff            - Turns off autoreact
    [ {blue}31{reset} ] rpcall                  - Custom status for all tokens
    [ {blue}32{reset} ] stoprpc                 - Stop custom status

    {magenta}Server & User Info{reset}
    [ {blue}33{reset} ] inviteinfo <code>       - Displays invite information
    [ {blue}34{reset} ] serverinfo              - Get server information
    [ {blue}35{reset} ] userinfo                - Get info off a user

    {magenta}Utility{reset}
    [ {blue}36{reset} ] nickname                - Change your server nickname
    [ {blue}37{reset} ] mimic                   - Mimic a user
    [ {blue}38{reset} ] mimicoff                - Stop the mimic
    [ {blue}39{reset} ] emojisteal              - Steal emoji and add to server
    [ {blue}40{reset} ] reload                  - Reload the selfbot
    [ {blue}41{reset} ] say #optional <num>     - Send specific message with tokens

    {magenta}╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                      we been rich since birth          {red}@mwpv        {red}@intertwinedthoughts            ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝{reset}
""",
    2: f"""
    {magenta}User Interaction{reset}
    [ {blue}42{reset} ] pfpscrape <num>          - Scrapes server for <number> of members pfp
    [ {blue}43{reset} ] triggertyping <duration> - Set user typing for specific duration
    [ {blue}44{reset} ] triggertypingoff         - Turn off trigger typing
    [ {blue}45{reset} ] ghostping <@user>        - Double Ghost ping a user
    [ {blue}46{reset} ] antigcspam               - Toggle autogroupchat leaver
    [ {blue}47{reset} ] token                    - Get a users token ( HAHA U THOUGHT )
    [ {blue}48{reset} ] forcedc                  - Force disconnect a user from vcs

    {magenta}Message & Reaction{reset}
    [ {blue}49{reset} ] dreact                   - Auto react to messages with alternating emojis
    [ {blue}50{reset} ] mspam                    - Spam a message with all your tokens
    [ {blue}51{reset} ] webhookcopy              - Send messages as a webhook
    [ {blue}52{reset} ] webhookcopyoff           - Turn off Webhook copying
    [ {blue}53{reset} ] avatar                   - Get avatar of user or yourself

    {magenta}Server Management{reset}
    [ {blue}54{reset} ] tempchannel <name>       - Create a temp text channel
    [ {blue}55{reset} ] tempvc <name>            - Create a temp voice channel
    [ {blue}56{reset} ] roblox <username>        - Get info from a roblox user
    [ {blue}57{reset} ] servername <name>        - Change the guild's name
    [ {blue}58{reset} ] pin                      - Pin the most recent message
    [ {blue}59{reset} ] createchannel            - Create a channel
    [ {blue}60{reset} ] createvc                 - Create a Voice Channel
    [ {blue}61{reset} ] createrole               - Create a role
    [ {blue}62{reset} ] servername               - Rename the current server

    {magenta}Utility & Backup{reset}
    [ {blue}63{reset} ] cls                      - Clear cmd prompt ui
    [ {blue}64{reset} ] backupserver             - Backup your server and save to json
    [ {blue}65{reset} ] pasteserver              - Paste your backup json into your new server
    [ {blue}66{reset} ] clearbackup              - Clear ALL backup jsons
    [ {blue}67{reset} ] clearchannels            - Clear all channels and categories

    {magenta}╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                      we been rich since birth          {red}@mwpv        {red}@intertwinedthoughts            ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝{reset}
    """,
    3: f"""
    {magenta}Friendly Actions{reset}
    [ {blue}68{reset} ] kiss <@user>            - Kiss a user
    [ {blue}69{reset} ] pat <@user>             - Pat a user
    [ {blue}70{reset} ] hug <@user>             - Hug a user
    [ {blue}71{reset} ] wave <@user>            - Wave at a user
    [ {blue}72{reset} ] cuddle <@user>          - Cuddle a user
    [ {blue}73{reset} ] handhold <@user>        - Hold hands with a user
    [ {blue}74{reset} ] highfive <@user>        - High-five a user
    [ {blue}75{reset} ] poke <@user>            - Poke a user

    {magenta}Playful Actions{reset}
    [ {blue}76{reset} ] nom <@user>             - Nom on a user
    [ {blue}77{reset} ] wink                    - Wink i guess
    [ {blue}78{reset} ] dance                   - Dance
    [ {blue}79{reset} ] smug                    - Show a smug expression
    [ {blue}80{reset} ] cry                     - :( aww cry baby

    {magenta}Aggressive Actions{reset}
    [ {blue}81{reset} ] slap <@user>            - Slap a user
    [ {blue}82{reset} ] bite <@user>            - Bite a user
    [ {blue}83{reset} ] lick <@user>            - Lick a user
    [ {blue}84{reset} ] bully <@user>           - Bully a user
    [ {blue}85{reset} ] hurt <@user>            - Kill a user
    [ {blue}86{reset} ] bonk <@user>            - Bonk a user
    [ {blue}87{reset} ] yeet <@user>            - Yeet a user

    {magenta}╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                      we been rich since birth          {red}@mwpv        {red}@intertwinedthoughts            ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝{reset}
    """,
    4: f"""
    {magenta}Emoji Management{reset}
    [ {blue}88{reset} ] emojiexport                                                        - Download all emojis from server
    [ {blue}89{reset} ] pastemoji                                                          - Add all your exported emojis
    [ {blue}90{reset} ] wipemojis                                                          - Clear all exported emojis

    {magenta}Server & Group Actions{reset}
    [ {blue}91{reset} ] leavegroups                                                        - Leave all of your groups
    [ {blue}92{reset} ] firstmessage <channel>                                             - See the first message in the channel
    [ {blue}93{reset} ] fakeactive                                                         - Use your tokens to make server active
    [ {blue}94{reset} ] fakeactiveoff                                                      - Turn off fake activity
    [ {blue}95{reset} ] info                                                               - Show Cmd Prmpt Info but in chat

    {magenta}Ping Response System{reset}
    [ {blue}96{reset} ] pingresponse                                                       - Reply to pings with a custom response
    {magenta}Usage:{reset}
    {green}[ {blue}^{reset} {green}]{reset} {black}pingresponse {green}toggle{reset} {black}"your a skid!"{reset}
    {green}[ {blue}^{reset} {green}]{reset} {black}pingresponse {green}list{reset}         - {black}Show current ping responses.{reset}
    {green}[ {blue}^{reset} {green}]{reset} {black}pingresponse {green}clear{reset}        - {black}Clear all ping responses.{reset}

    [ {blue}97{reset} ] pinginsult                                                         - Reply to pings by insulting the user
    {magenta}Usage:{reset}
    {green}[ {blue}^{reset} {green}]{reset} {black}pinginsult {green}toggle{reset}         - {black}Toggle ping insults on or off.{reset}
    {green}[ {blue}^{reset} {green}]{reset} {black}pinginsult {green}list{reset}           - {black}Show current ping insults.{reset}
    {green}[ {blue}^{reset} {green}]{reset} {black}pinginsult {green}clear{reset}          -{black} Clear all ping insults.{reset}

    [ {blue}98{reset} ] pingreact                                                          - Reply to pings by adding a reaction
    {magenta}Usage:{reset}
    {green}[ {blue}^{reset} {green}]{reset} {black}pingreact {green}toggle reaction{reset} - {black}Toggle ping reactions on or off.{reset}
    {green}[ {blue}^{reset} {green}]{reset} {black}pingreact {green}list{reset}            - {black}Show current ping reactions.{reset}
    {green}[ {blue}^{reset} {green}]{reset} {black}pingreact {green}clear{reset}           - {black}Clear all ping reactions.{reset}

    {magenta}╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                      we been rich since birth          {red}@mwpv        {red}@intertwinedthoughts            ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝{reset}
    """,
    5: f"""
    {magenta}AFK Check Systems{reset}
    [ {blue}99{reset} ]  mcountdown <@user> <num>                                     - Afk check someone with tokens
    [ {blue}100{reset} ] mcountdownoff                                                - Stop Multi countdown
    [ {blue}101{reset} ] countdown <@user> <num>                                      - Afk Check someone
    [ {blue}102{reset} ] countdownoff                                                 - Stop Countdown

    {magenta}User Control Systems{reset}
    [ {blue}103{reset} ] autotrap                                                     - Manage users who cannot leave the group chat
    {magenta}Usage:{reset}
    {green}[ {blue}^ {green}] {black}autotrap {green}toggle <user>{reset}             - {black}Toggle no-leave status for the specified user{reset}
    {green}[ {blue}^ {green}] {black}autotrap {green}list{reset}                      - {black}Show users prevented from leaving the group chat{reset}
    {green}[ {blue}^ {green}] {black}autotrap {green}clear{reset}                     - {black}Allow all users to leave the group chat{reset}
    [ {blue}104{reset} ] autonick                                                     - Force change a user's nickname
    {magenta}Usage:{reset}
    {green}[ {blue}^ {green}] {black}autonick {green}toggle <@user> <nickname>{reset} - {black}Toggle forcing the specified user's nickname{reset}
    {green}[ {blue}^ {green}] {black}autonick {green}list{reset}                      - {black}Show users with forced nicknames{reset}
    {green}[ {blue}^ {green}] {black}autonick {green}clear{reset}                     - {black}Clear forced nicknames for all users{reset}
    [ {blue}105{reset} ] forcepurge                                                   - Force delete a user's messages
    {magenta}Usage:{reset}
    {green}[ {blue}^ {green}] {black}forcepurge {green}toggle <@user>{reset}          - {black}Toggle force-deleting messages{reset}
    {green}[ {blue}^ {green}] {black}forcepurge {green}list{reset}                    - {black}Show users with auto-deleted messages{reset}
    {green}[ {blue}^ {green}] {black}forcepurge {green}clear{reset}                   - {black}Clear auto-delete settings{reset}
    [ {blue}106{reset} ] autokick                                                     - Automatically kick users
    {magenta}Usage:{reset}
    {green}[ {blue}^ {green}] {black}autokick {green}toggle <@user>{reset}            - {black}Toggle auto-kicking for the user{reset}
    {green}[ {blue}^ {green}] {black}autokick {green}list{reset}                      - {black}Show users with auto-kick enabled{reset}
    {green}[ {blue}^ {green}] {black}autokick {green}clear{reset}                     - {black}Clear auto-kick settings{reset}
    [ {blue}107{reset} ] autovclock                                                   - Auto lock a voice channel when you join

    {magenta}╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                      we been rich since birth          {red}@mwpv        {red}@intertwinedthoughts            ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝{reset}
    """,
    6: f"""
    {magenta}Nuke Configuration{reset}
    [ {blue}108{reset} ] destroy                      - Perform destructive actions on the server
    [ {blue}109{reset} ] nukehook                    - Change the webhook message for the nuke process
    [ {blue}110{reset} ] nukename                    - Change the Discord server name for the nuke process
    [ {blue}111{reset} ] nukedelay                   - Change the delay between webhook messages
    [ {blue}112{reset} ] nukechannel                 - Change the channel name used for the webhook
    [ {blue}113{reset} ] nukeconfig                  - Show the current configuration for the nuke process
    [ {blue}114{reset} ] nukeconfigwipe              - Delete the nuke config file and reset all data

    {magenta}Mass Server Actions{reset}
    [ {blue}115{reset} ] massrole <name>             - Creates mass roles with the given name
    [ {blue}116{reset} ] massroledel                 - Deletes all roles except the default ones
    [ {blue}117{reset} ] masschannel <name> <number> - Creates mass channels
    [ {blue}118{reset} ] massban                     - Bans everyone from the server
    [ {blue}119{reset} ] masskick                    - Kicks everyone from the server
    [ {blue}120{reset} ] massdelemoji                - Delete all emojis from server

    {magenta}╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                      we been rich since birth          {red}@mwpv        {red}@intertwinedthoughts            ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝{reset}
    """,
    7: f"""
    {magenta}Spotify Control System{reset}
    {magenta}Spotify Control System{reset}
    [ {blue}121{reset} ] spotify                - Control your Spotify playback

        {magenta}Playback Controls{reset}
        {green}[ {blue}^{green} ] {black}spotify {green}unpause{reset}              - {black}Resume playback if paused{reset}
        {green}[ {blue}^{green} ] {black}spotify {green}pause{reset}                - {black}Pause the current playback{reset}
        {green}[ {blue}^{green} ] {black}spotify {green}next{reset}                 - {black}Skip to the next track{reset}
        {green}[ {blue}^{green} ] {black}spotify {green}prev{reset}                 - {black}Revert to the previous track{reset}
        
        {magenta}Track Management{reset}
        {green}[ {blue}^{green} ] {black}spotify {green}play <song>{reset}          - {black}Search for and play a specific song{reset}
        {green}[ {blue}^{green} ] {black}spotify {green}current{reset}              - {black}Show current track info{reset}
        {green}[ {blue}^{green} ] {black}spotify {green}addqueue <song>{reset}      - {black}Add a song to the queue{reset}
        
        {magenta}Settings{reset}
        {green}[ {blue}^{green} ] {black}spotify {green}volume <0-100>{reset}       - {black}Set volume level (0-100){reset}
        {green}[ {blue}^{green} ] {black}spotify {green}shuffle <on/off>{reset}     - {black}Toggle shuffle mode{reset}
        {green}[ {blue}^{green} ] {black}spotify {green}repeat <mode>{reset}        - {black}Set repeat mode (track/context/off){reset}

    {magenta}╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                      we been rich since birth          {red}@mwpv        {red}@intertwinedthoughts            ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝{reset}
    """,
    8: f"""
    {magenta}Profile Customization{reset}
    [ {blue}122{reset} ] rotatepfp <hours>      - Starts profile picture rotation
    [ {blue}123{reset} ] stoprandomizepfp       - Stops profile picture rotation
    [ {blue}124{reset} ] setpfp <url>           - Set avatar with url
    [ {blue}125{reset} ] setbanner <url>        - Set banner with url
    [ {blue}126{reset} ] stealpfp <user>        - Steal a user's avatar
    [ {blue}127{reset} ] stealbanner <user>     - Steal user's banner

    {magenta}Bio & Status Management{reset}
    [ {blue}128{reset} ] rotatebio <text>       - Rotate your bio each hour
    [ {blue}129{reset} ] stoprotatebio          - Stop bio rotation
    [ {blue}130{reset} ] setbio <custom>        - Set your bio
    [ {blue}131{reset} ] stealbio <user>        - Snatch a user's About Me
    [ {blue}132{reset} ] rstatus                - Rotate your custom status
    [ {blue}133{reset} ] rstatusend             - Cancel your rotate status

    {magenta}Name & Pronouns{reset}
    [ {blue}134{reset} ] nickloop <nicknames>   - Rotates through nicknames
    [ {blue}135{reset} ] stopnickloop           - Stops nickname rotation
    [ {blue}136{reset} ] setpronoun <custom>    - Set a custom pronoun
    [ {blue}137{reset} ] rotatepronoun <custom> - Rotate your pronouns
    [ {blue}138{reset} ] stoprotatepronoun      - Stop pronoun rotate
    [ {blue}139{reset} ] setname <custom>       - Set a custom display name
    [ {blue}140{reset} ] stealpronoun <user>    - Snatch a user's pronoun
    [ {blue}141{reset} ] stealname <user>       - Steal user's display name

    {magenta}Server Information{reset}
    [ {blue}142{reset} ] channelinfo <id>       - Display channel information
    [ {blue}143{reset} ] channels <serverid>    - Shows all channels
    [ {blue}144{reset} ] roles <serverid>       - Shows all roles
    [ {blue}145{reset} ] mutualinfo             - Shows Mutual info between users
    
    {magenta}Voice Channel Management{reset}
    [ {blue}146{reset} ] spamregion <channel>   - Changes voice channel region
    [ {blue}147{reset} ] stopspamregion         - Stops region spam

    {magenta}╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                      we been rich since birth          {red}@mwpv        {red}@intertwinedthoughts            ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝{reset}

    """,
    9: f"""
    {magenta}Message Reaction System{reset}
    [ {blue}148{reset} ] ronmessage                               - Automatic reactions to messages
    [ {blue}^{reset} ] {black}ronmessage add <message> <reaction>{reset} - Add reaction to message
    [ {blue}^{reset} ] {black}ronmessage list{reset}                     - List message reactions
    [ {blue}^{reset} ] {black}ronmessage remove <message>{reset}         - Remove message reaction
    [ {blue}^{reset} ] {black}ronmessage clear{reset}                    - Clear all reactions
    [ {blue}^{reset} ] {black}ronmessage on/off <message>{reset}         - Toggle reaction

    {magenta}Message Response System{reset}
    [ {blue}149{reset} ] sonmessage                               - Automatic responses to messages
    [ {blue}^{reset} ] {black}sendonmessage add <msg> <response>{reset}  - Add custom response
    [ {blue}^{reset} ] {black}sendonmessage list{reset}                  - List responses
    [ {blue}^{reset} ] {black}sendonmessage remove <message>{reset}      - Remove response
    [ {blue}^{reset} ] {black}sendonmessage clear{reset}                 - Clear responses
    [ {blue}^{reset} ] {black}sonmessage on/off <message>{reset}         - Toggle response

    {magenta}Message Edit System{reset}
    [ {blue}150{reset} ] eonmessage                               - Automatic message editing
    [ {blue}^{reset} ] {black}eonmessage add <msg> <edit>{reset}         - Add auto-edit
    [ {blue}^{reset} ] {black}eonmessage list{reset}                     - List edits
    [ {blue}^{reset} ] {black}eonmessage remove <message>{reset}         - Remove edit
    [ {blue}^{reset} ] {black}eonmessage clear{reset}                    - Clear edits
    [ {blue}^{reset} ] {black}eonmessage on/off <message>{reset}         - Toggle edit
    
    {magenta}Notification Systems{reset}
    [ {blue}151{reset} ] nonping                               - Get notifications when pinged
    [ {blue}^{reset} ] {black}nonping on/off{reset}                      - Toggle notifications
    [ {blue}^{reset} ] {black}nonping status{reset}                      - Check status
    [ {blue}152{reset} ] nondm                               - Get DM notifications
    [ {blue}^{reset} ] {black}nondm on/off{reset}                        - Toggle DM alerts
    [ {blue}^{reset} ] {black}nondm status{reset}                        - Check status
    [ {blue}153{reset} ] nonreaction                               - Get reaction notifications
    [ {blue}^{reset} ] {black}nonreaction on/off{reset}                  - Toggle alerts
    [ {blue}^{reset} ] {black}nonreaction status{reset}                  - Check status

    {magenta}╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                      we been rich since birth          {red}@mwpv        {red}@intertwinedthoughts            ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝{reset}
    """,
    10: f"""
    {magenta}Screenshot Management{reset}
    [ {blue}154{reset} ] wscreenshot             - Takes a full screen screenshot
    [ {blue}155{reset} ] pscreenshot             - Takes a screenshot of active window
    [ {blue}156{reset} ] sendss                  - Sends the most recent screenshot
    [ {blue}157{reset} ] openss                  - Opens the most recent screenshot

    {magenta}Windows Utilities{reset}
    [ {blue}158{reset} ] bsearch <name>          - Search using default browser
    [ {blue}159{reset} ] opencalc                - Opens Windows Calculator
    [ {blue}160{reset} ] openpad                 - Opens Windows Notepad
    [ {blue}161{reset} ] dfolder <name>          - Creates Desktop folder
    [ {blue}162{reset} ] cleartemp               - Clear %temp% folder

    {magenta}Social Media Search{reset}
    [ {blue}163{reset} ] byoutube <name>         - Search YouTube
    [ {blue}164{reset} ] btwitter <name>         - Search Twitter
    [ {blue}165{reset} ] btiktok <name>          - Search TikTok
    [ {blue}166{reset} ] broblox <name>          - Search Roblox

    {magenta}╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                      we been rich since birth          {red}@mwpv        {red}@intertwinedthoughts            ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝{reset}
    """,
    11: f"""
    {magenta}General NSFW{reset}
    [ {blue}167{reset} ] hentai                  - Get hentai content
    [ {blue}168{reset} ] uniform                 - Get uniform content
    [ {blue}169{reset} ] maid                    - Get maid content
    [ {blue}170{reset} ] oppai                   - Get oppai content
    [ {blue}171{reset} ] selfies                 - Get selfie content

    {magenta}Character Specific{reset}
    [ {blue}172{reset} ] raiden                  - Get Raiden Shogun content
    [ {blue}173{reset} ] marin                   - Get Marin Kitagawa content

    {magenta}╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                      we been rich since birth          {red}@mwpv        {red}@intertwinedthoughts            ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝{reset}
    """,
    12: f"""
    {magenta}Main Commands{reset}
    [ {blue}174{reset} ] mdm < num > < message > - Mass DMs a number of friends
    [ {blue}175{reset} ] theme                   - Change theme colors
    [ {blue}176{reset} ] info                    - Shows bot info

    {magenta}Utility Commands{reset}
    [ {blue}177{reset} ] clear                   - Clear console
    [ {blue}178{reset} ] reload                  - Restart the bot
    [ {blue}179{reset} ] shutdown                - Shutdown the bot
    [ {blue}179{reset} ] clearconfigs            - Clear all configs
    [ {blue}180{reset} ] autobump                - Auto Bump your server every 2hrs
    [ {blue}181{reset} ] autobumpoff             - Disable autobump
    [ {blue}182{reset} ] blocked                 - Show blocked users
    [ {blue}183{reset} ] pending                 - Show pending friend users
    [ {blue}184{reset} ] outgoing                - Show outgoing friend requests

    {magenta}Token Utility{reset}
    [ {blue}186{reset} ] tnickname < server id > - Change token's server nickname
    [ {blue}187{reset} ] tpronoun < name >       - Change token's pronoun
    [ {blue}188{reset} ] tbio < custom >         - Change token's bio
    [ {blue}189{reset} ] tstatus < status >      - Change token's online status
    [ {blue}190{reset} ] tstatusoff              - Turn off token's custom status
    [ {blue}191{reset} ] tinfo                   - Get token account info
    [ {blue}192{reset} ] tjoin < invite >        - Join server with token
    [ {blue}193{reset} ] tleave < server id >    - Leave server with token

    {magenta}Friend & Block Utility{reset}
    [ {blue}194{reset} ] unfriend < user >       - Send friend request to user
    [ {blue}195{reset} ] block < user >          - Block user
    [ {blue}196{reset} ] unblock < user >        - Unblock user  
    [ {blue}197{reset} ] friend < user id >      - Send friend request to user
    [ {blue}198{reset} ] fnote < user id >       - Send friend note to user
    [ {blue}199{reset} ] fnick < user id >       - Change friend nickname

    {magenta}╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                      we been rich since birth          {red}@mwpv        {red}@intertwinedthoughts            ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝{reset}
    """,
    13: f"""
    {magenta}Auto Press Commands{reset}
    [ {blue}201{reset} ] autopress < user >           - Auto press messages in channel
    [ {blue}202{reset} ] autopress stop               - Turn off autopress
    [ {blue}203{reset} ] autopress list               - List all autopress channels
    [ {blue}204{reset} ] autopress add < message >    - Add a message to autopress
    [ {blue}205{reset} ] autopress remove < message > - Remove a message from autopress
    [ {blue}206{reset} ] autopress clear              - Clear all autopress messages

    {magenta}Auto Kill Commands{reset}
    [ {blue}207{reset} ] autokill < user >            - Auto kill user in all channels
    [ {blue}208{reset} ] autokill stop                - Turn off autokill
    [ {blue}209{reset} ] autokill list                - List all autokill users
    [ {blue}210{reset} ] autokill clear               - Clear all autokill users
    [ {blue}211{reset} ] autokill add < word >        - Add a word to autokill
    [ {blue}212{reset} ] autokill remove < word >     - Remove a word from autokill

    {magenta}Manual Mode Commands{reset}
    [ {blue}213{reset} ] manual < user >              - Enable manual mode
    [ {blue}214{reset} ] manual stop                  - Turn off manual mode
    [ {blue}215{reset} ] manual list                  - List all manual msgs
    [ {blue}216{reset} ] manual clear                 - Clear all manual msgs
    [ {blue}217{reset} ] manual add < message >       - Add a message to manual mode
    [ {blue}218{reset} ] manual remove < message >    - Remove a message from manual mode

    {magenta}Multi Press Commands{reset}
    [ {blue}219{reset} ] testimony < user > < user >  - Send testimony to user
    [ {blue}220{reset} ] testimonyoff                 - Turn off testimony

    {magenta}Random Beef Commands{reset}
    [ {blue}219{reset} ] dripcheck < user >           - Check user's drip level
    [ {blue}220{reset} ] discordreport < user >       - Generate a report card for user
    [ {blue}221{reset} ] relationship < user >        - Check user's relationship potential
    [ {blue}222{reset} ] stats < user >               - Get user's stats

    {magenta}Multi/Vc Commands{reset}
    [ {blue}223{reset} ] gcleave < user >             - Leave group chat with your tokens
    [ {blue}224{reset} ] gcleaveall                   - Leave all group chats with your tokens
    [ {blue}225{reset} ] vcjoin r < channel id >      - Rotate join a voice channel
    [ {blue}226{reset} ] vcjoin s < channel id >      - Join a voice channel
    [ {blue}227{reset} ] vcjoin status                - Shows the current voice channel status
    [ {blue}228{reset} ] vcjoin list                  - List all available voice channels
    [ {blue}229{reset} ] vcjoin leave                 - Leave voice channel

    {magenta}╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                      we been rich since birth          {red}@mwpv        {red}@intertwinedthoughts            ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝{reset}
    """,
    14: f"""
    {magenta}Auto Multi Commands{reset}
    [ {blue}230{reset} ] autogc                      - Auto add tokens to any group chat your added to
    [ {blue}231{reset} ] autogcstop                  - Turn off autogc
    [ {blue}232{reset} ] autogc whitelist            - Whitelist a user to auto add to gc ( if they add you, it wont add tokens )
    [ {blue}233{reset} ] autogc whitelist remove     - Remove a user from the whitelist
    [ {blue}234{reset} ] autogc list                 - List all whitelisted users

    {magenta}Auto Gc Leave Commands{reset}
    [ {blue}235{reset} ] autogcleave                  - Auto leave any group chat you leave
    [ {blue}236{reset} ] autogcleave stop             - Turn off autogcleave

    {magenta}Auto Server Leave Commands{reset}
    [ {blue}237{reset} ] autoserverleave              - Auto leave any server you leave
    [ {blue}240{reset} ] autoserverleave stop         - Turn off autoserverleave

    {magenta}Auto Repeat Commands{reset}
    [ {blue}241{reset} ] repeat start                 - Start auto repeat
    [ {blue}242{reset} ] repeat stop                  - Turn off auto repeat
    [ {blue}243{reset} ] repeat delay < seconds >     - Set the delay between repeats
    [ {blue}244{reset} ] repeat status                - Check auto repeat status

    {magenta}Auto Ladder Commands{reset}
    [ {blue}245{reset} ] ladder                       - Start auto ladder
    [ {blue}246{reset} ] ladder stop                  - Turn off auto ladder
    [ {blue}247{reset} ] ladder delay < seconds >     - Set the delay between ladders
    [ {blue}248{reset} ] ladder add < message >       - Add a message to auto ladder
    [ {blue}249{reset} ] ladder remove < msg >        - Remove a message from auto ladder
    [ {blue}250{reset} ] ladder clear                 - Clear all auto ladder messages
    [ {blue}251{reset} ] ladder list                  - List all auto ladder messages
    [ {blue}252{reset} ] ladder reset                 - Reset auto ladder
    [ {blue}253{reset} ] ladder status                - Show all ladder messages

    {magenta}╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                      we been rich since birth          {red}@mwpv        {red}@intertwinedthoughts            ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝{reset}
    """,


15: f"""
    {magenta}Anti Gc Spam{reset}
    [ {blue}254{reset} ] antigcspam                       - Toggle protection & show status
    [ {blue}255{reset} ] antigcspam whitelist @user       - Add user to whitelist
    [ {blue}256{reset} ] antigcspam unwhitelist @user     - Remove user from whitelist
    [ {blue}257{reset} ] antigcspam blacklist @user       - Add user to blacklist
    [ {blue}258{reset} ] antigcspam unblacklist @user     - Remove user from blacklist
    [ {blue}259{reset} ] antigcspam silent true/false     - Toggle silent mode
    [ {blue}260{reset} ] antigcspam message <text>        - Set leave message
    [ {blue}261{reset} ] antigcspam autoremove true/false - Toggle auto-remove of blacklisted
    [ {blue}262{reset} ] antigcspam webhook <url>         - Set webhook for logging
    [ {blue}263{reset} ] antigcspam autoblock true/false  - Toggle auto-block feature
    [ {blue}264{reset} ] antigcspam list                  - Show white/blacklisted users

    {magenta}Rotate Guild{reset}
    [ {blue}265{reset} ] rotateguild                      - Start rotating guild badges
    [ {blue}266{reset} ] rotateguild stop                 - Stop rotating guild badges
    [ {blue}267{reset} ] rotateguild delay <delay>        - Set the delay between guild badge rotations
    [ {blue}268{reset} ] rotateguild status               - Show current guild rotation status

    {magenta}GC Protection Spam{reset}
    [ {blue}269{reset} ] protection start                 - Start protection
    [ {blue}270{reset} ] protection stop                  - Stop protection
    [ {blue}271{reset} ] protection message <message>     - Set protection message
    [ {blue}272{reset} ] protection status                - Show protection status

    {magenta}Message Sniper System{reset}
    [ {blue}273{reset} ] dmsnipe log <webhook>            - Set webhook for logging deleted messages
    [ {blue}274{reset} ] dmsnipe toggle <on/off>          - Toggle message sniping
    [ {blue}275{reset} ] dmsnipe edit <on/off>            - Toggle edit sniping
    [ {blue}276{reset} ] dmsnipe ignore <@user>           - Toggle ignoring a user
    [ {blue}277{reset} ] dmsnipe status                   - Show current settings
    [ {blue}278{reset} ] dmsnipe clear                    - Clear all ignore lists

    {magenta}╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                      we been rich since birth          {red}@mwpv        {red}@intertwinedthoughts            ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝{reset}
    """,
    16: f"""
    {magenta}Anti LastWord{reset}
    [ {blue}279{reset} ] antilast toggle <on/off>    - Toggle anti last word system
    [ {blue}280{reset} ] antilast whitelist <id>     - Add user to whitelist
    [ {blue}281{reset} ] antilast channel <id>       - Add channel to whitelist
    [ {blue}282{reset} ] antilast webhook <url>      - Set webhook for logging
    [ {blue}283{reset} ] antilast config             - Show current config

    {magenta}Random{reset}
    [ {blue}284{reset} ] laz <user> <user 2>         - Send a message to a user
    [ {blue}285{reset} ] endlaz                      - Turn off laz
    [ {blue}286{reset} ] hypesquad <house>           - Change your HypeSquad house
    [ {blue}287{reset} ] hypesquad off               - Remove your HypeSquad house

    {magenta}Server Edit{reset}
    [ {blue}288{reset} ] setspfp <url>               - Set server-specific profile picture 
    [ {blue}289{reset} ] setsbanner <url>            - Set server-specific banner
    [ {blue}290{reset} ] setsbio <text>              - Set server-specific bio
    [ {blue}291{reset} ] setspronoun <text>          - Set server-specific pronouns
    [ {blue}292{reset} ] srotate pfp <urls>          - Start rotating server profile pictures
    [ {blue}293{reset} ] srotate banner <urls>       - Start rotating server banners
    [ {blue}294{reset} ] srotate bio <bios>          - Start rotating server bios
    [ {blue}295{reset} ] srotate pronouns <pronouns> - Start rotating server pronouns
    [ {blue}296{reset} ] srotate delay <cmd> <time>  - Set delay for specific feature
    [ {blue}297{reset} ] srotate stop [cmd]          - Stop rotation (all or specific feature)
    [ {blue}298{reset} ] srotate status              - Show current rotation status

    {magenta}Image Dumping{reset}
    [ {blue}299{reset} ] imgdump                     - Dump a user's image
    [ {blue}300{reset} ] gifdump                     - Dump a user's gif
    [ {blue}301{reset} ] movdump                     - Dump a user's video
    [ {blue}302{reset} ] mp4dump                     - Dump all videos in a channel
    
    {magenta}Guild Rotation{reset}
    [ {blue}303{reset} ] guildrotate start           - Start automatic rotation
    [ {blue}304{reset} ] guildrotate stop            - Stop rotation
    [ {blue}305{reset} ] guildrotate delay <seconds> - Set rotation delay

    {magenta}Token Management{reset}
    [ {blue}306{reset} ] token add <token>           - Add a token to the list
    [ {blue}307{reset} ] token remove <token>        - Remove a token from the list
    [ {blue}308{reset} ] token list                  - Show the list of tokens
    [ {blue}309{reset} ] token clear                 - Clear the list of tokens

    {magenta}╔═════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                      we been rich since birth          {red}@mwpv        {red}@intertwinedthoughts            ║
    ╚═════════════════════════════════════════════════════════════════════════════════════════════════════╝{reset}
    """
}

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active_help_messages = {}
        self.auto_snipe_settings = {}
        self.auto_csnipe_settings = {}
        self.user_themes = self.load_themes()
        self.default_colors = {
            "text": blue,
            "highlight": magenta,
            "accent": red
        }
        self.command_help = {
        "outlast": {
        "usage": "outlast <@user>",
        "description": "Outlast @user in channel",
        "example": ".outlast @user",
        "category": "Multi Token Management"
    },
    "stopoutlast": {
        "usage": "stopoutlast",
        "description": "Stop outlast command",
        "example": ".stopoutlast",
        "category": "Multi Token Management"
    },
    "multilast": {
        "usage": "multilast <@user>",
        "description": "Multiple token outlast",
        "example": ".multilast @user",
        "category": "Multi Token Management"
    },
    "stopmultilast": {
        "usage": "stopmultilast",
        "description": "Stop multilast command",
        "example": ".stopmultilast",
        "category": "Multi Token Management"
    },
    "tok": {
        "usage": "tok",
        "description": "Showcases all tokens",
        "example": ".tok",
        "category": "Multi Token Management"
    },
    "multivc": {
        "usage": "multivc",
        "description": "Connects all tokens to VC",
        "example": ".multivc",
        "category": "Multi Token Management"
    },
    "ar": {
        "usage": "ar <@user>",
        "description": "Autoresponds to @user",
        "example": ".ar @user",
        "category": "Auto Response"
    },
    "arend": {
        "usage": "arend",
        "description": "Stop autoresponse",
        "example": ".arend",
        "category": "Auto Response"
    },
    "arm": {
        "usage": "arm <@user>",
        "description": "Autoreply multi token",
        "example": ".arm @user",
        "category": "Auto Response"
    },
    "armend": {
        "usage": "armend",
        "description": "Stop multi token autoreply",
        "example": ".armend",
        "category": "Auto Response"
    },
    "kill": {
        "usage": "kill <@user>",
        "description": "Spams @user until rate limit",
        "example": ".kill @user",
        "category": "Spam & Control"
    },
    "killend": {
        "usage": "killend",
        "description": "Stop kill command",
        "example": ".killend",
        "category": "Spam & Control"
    },
    "gcfill": {
        "usage": "gcfill",
        "description": "Fills gc with tokens",
        "example": ".gcfill",
        "category": "Spam & Control"
    },
    "gc": {
        "usage": "gc",
        "description": "Changes gc with tokens",
        "example": ".gc",
        "category": "Spam & Control"
    },
    "gcend": {
        "usage": "gcend",
        "description": "Stop gc command",
        "example": ".gcend",
        "category": "Spam & Control"
    },
    "mping": {
        "usage": "mping",
        "description": "Mass ping the server with tokens",
        "example": ".mping",
        "category": "Spam & Control"
    },
    "mpingoff": {
        "usage": "mpingoff",
        "description": "Turns off mass ping",
        "example": ".mpingoff",
        "category": "Spam & Control"
    },
    "invis": {
        "usage": "invis",
        "description": "Mass spam invis text",
        "example": ".invis",
        "category": "Spam & Control"
    },
    "invisoff": {
        "usage": "invisoff",
        "description": "Turns off invis spam",
        "example": ".invisoff",
        "category": "Spam & Control"
    },
    "popout": {
        "usage": "popout",
        "description": "Auto Press",
        "example": ".popout",
        "category": "Spam & Control"
    },
    "bold": {
        "usage": "bold",
        "description": "Turns all messages bold",
        "example": ".bold",
        "category": "Message Formatting"
    },
    "unbold": {
        "usage": "unbold",
        "description": "Turns off bold messages",
        "example": ".unbold",
        "category": "Message Formatting"
    },
    "cord": {
        "usage": "cord",
        "description": "Pings user while making message bold",
        "example": ".cord",
        "category": "Message Formatting"
    },
    "cordoff": {
        "usage": "cordoff",
        "description": "Turns off cord command",
        "example": ".cordoff",
        "category": "Message Formatting"
    },
    "translate": {
        "usage": "translate <language>",
        "description": "Translates your message",
        "example": ".translate spanish",
        "category": "Message Formatting"
    },
    "translateoff": {
        "usage": "translateoff",
        "description": "Turns off translate",
        "example": ".translateoff",
        "category": "Message Formatting"
    },
    "mreact": {
        "usage": "mreact",
        "description": "Mass reacts with specific emoji",
        "example": ".mreact",
        "category": "Reactions & Status"
    },
    "reactoff": {
        "usage": "reactoff",
        "description": "Turns off mass react",
        "example": ".reactoff",
        "category": "Reactions & Status"
    },
    "autoreact": {
        "usage": "autoreact",
        "description": "Auto react to messages globally",
        "example": ".autoreact",
        "category": "Reactions & Status"
    },
    "autoreactoff": {
        "usage": "autoreactoff",
        "description": "Turns off autoreact",
        "example": ".autoreactoff",
        "category": "Reactions & Status"
    },
    "rpcall": {
        "usage": "rpcall",
        "description": "Custom status for all tokens",
        "example": ".rpcall",
        "category": "Reactions & Status"
    },
    "stoprpc": {
        "usage": "stoprpc",
        "description": "Stop custom status",
        "example": ".stoprpc",
        "category": "Reactions & Status"
    },
    "inviteinfo": {
        "usage": "inviteinfo <code>",
        "description": "Displays invite information",
        "example": ".inviteinfo abc123",
        "category": "Server & User Info"
    },
    "serverinfo": {
        "usage": "serverinfo",
        "description": "Get server information",
        "example": ".serverinfo",
        "category": "Server & User Info"
    },
    "userinfo": {
        "usage": "userinfo",
        "description": "Get info off a user",
        "example": ".userinfo",
        "category": "Server & User Info"
    },
    "nickname": {
        "usage": "nickname",
        "description": "Change your server nickname",
        "example": ".nickname",
        "category": "Utility"
    },
    "mimic": {
        "usage": "mimic",
        "description": "Mimic a user",
        "example": ".mimic",
        "category": "Utility"
    },
    "mimicoff": {
        "usage": "mimicoff",
        "description": "Stop the mimic",
        "example": ".mimicoff",
        "category": "Utility"
    },
    "emojisteal": {
        "usage": "emojisteal",
        "description": "Steal emoji and add to server",
        "example": ".emojisteal",
        "category": "Utility"
    },
    "reload": {
        "usage": "reload",
        "description": "Reload the selfbot",
        "example": ".reload",
        "category": "Utility"
    },
    "say": {
        "usage": "say #optional <num>",
        "description": "Send specific message with tokens",
        "example": ".say #general 5",
        "category": "Utility"
    },
    "pfpscrape": {
        "usage": "pfpscrape <num>",
        "description": "Scrapes server for <number> of members pfp",
        "example": ".pfpscrape 10",
        "category": "User Interaction"
    },
    "triggertyping": {
        "usage": "triggertyping <duration>",
        "description": "Set user typing for specific duration",
        "example": ".triggertyping 30",
        "category": "User Interaction"
    },
    "triggertypingoff": {
        "usage": "triggertypingoff",
        "description": "Turn off trigger typing",
        "example": ".triggertypingoff",
        "category": "User Interaction"
    },
    "ghostping": {
        "usage": "ghostping <@user>",
        "description": "Double Ghost ping a user",
        "example": ".ghostping @user",
        "category": "User Interaction"
    },
    "antigcspam": {
        "usage": "antigcspam",
        "description": "Toggle autogroupchat leaver",
        "example": ".antigcspam",
        "category": "User Interaction"
    },
    "token": {
        "usage": "token",
        "description": "Get a users token ( HAHA U THOUGHT )",
        "example": ".token",
        "category": "User Interaction"
    },
    "forcedc": {
        "usage": "forcedc",
        "description": "Force disconnect a user from vcs",
        "example": ".forcedc",
        "category": "User Interaction"
    },
    "dreact": {
        "usage": "dreact",
        "description": "Auto react to messages with alternating emojis",
        "example": ".dreact",
        "category": "Message & Reaction"
    },
    "mspam": {
        "usage": "mspam",
        "description": "Spam a message with all your tokens",
        "example": ".mspam",
        "category": "Message & Reaction"
    },
    "webhookcopy": {
        "usage": "webhookcopy",
        "description": "Send messages as a webhook",
        "example": ".webhookcopy",
        "category": "Message & Reaction"
    },
    "webhookcopyoff": {
        "usage": "webhookcopyoff",
        "description": "Turn off Webhook copying",
        "example": ".webhookcopyoff",
        "category": "Message & Reaction"
    },
    "avatar": {
        "usage": "avatar",
        "description": "Get avatar of user or yourself",
        "example": ".avatar",
        "category": "Message & Reaction"
    },
    "tempchannel": {
        "usage": "tempchannel <name>",
        "description": "Create a temp text channel",
        "example": ".tempchannel general",
        "category": "Server Management"
    },
    "tempvc": {
        "usage": "tempvc <name>",
        "description": "Create a temp voice channel",
        "example": ".tempvc voice",
        "category": "Server Management"
    },
    "roblox": {
        "usage": "roblox <username>",
        "description": "Get info from a roblox user",
        "example": ".roblox username",
        "category": "Server Management"
    },
    "servername": {
        "usage": "servername <name>",
        "description": "Change the guild's name",
        "example": ".servername New Server",
        "category": "Server Management"
    },
    "pin": {
        "usage": "pin",
        "description": "Pin the most recent message",
        "example": ".pin",
        "category": "Server Management"
    },
    "createchannel": {
        "usage": "createchannel",
        "description": "Create a channel",
        "example": ".createchannel",
        "category": "Server Management"
    },
    "createvc": {
        "usage": "createvc",
        "description": "Create a Voice Channel",
        "example": ".createvc",
        "category": "Server Management"
    },
    "createrole": {
        "usage": "createrole",
        "description": "Create a role",
        "example": ".createrole",
        "category": "Server Management"
    },
    "cls": {
        "usage": "cls",
        "description": "Clear cmd prompt ui",
        "example": ".cls",
        "category": "Utility & Backup"
    },
    "backupserver": {
        "usage": "backupserver",
        "description": "Backup your server and save to json",
        "example": ".backupserver",
        "category": "Utility & Backup"
    },
    "pasteserver": {
        "usage": "pasteserver",
        "description": "Paste your backup json into your new server",
        "example": ".pasteserver",
        "category": "Utility & Backup"
    },
    "clearbackup": {
        "usage": "clearbackup",
        "description": "Clear ALL backup jsons",
        "example": ".clearbackup",
        "category": "Utility & Backup"
    },
    "clearchannels": {
        "usage": "clearchannels",
        "description": "Clear all channels and categories",
        "example": ".clearchannels",
        "category": "Utility & Backup"
    },
    "kiss": {
        "usage": "kiss <@user>",
        "description": "Kiss a user",
        "example": ".kiss @user",
        "category": "Friendly Actions"
    },
    "pat": {
        "usage": "pat <@user>",
        "description": "Pat a user",
        "example": ".pat @user",
        "category": "Friendly Actions"
    },
    "hug": {
        "usage": "hug <@user>",
        "description": "Hug a user",
        "example": ".hug @user",
        "category": "Friendly Actions"
    },
    "wave": {
        "usage": "wave <@user>",
        "description": "Wave at a user",
        "example": ".wave @user",
        "category": "Friendly Actions"
    },
    "cuddle": {
        "usage": "cuddle <@user>",
        "description": "Cuddle a user",
        "example": ".cuddle @user",
        "category": "Friendly Actions"
    },
    "handhold": {
        "usage": "handhold <@user>",
        "description": "Hold hands with a user",
        "example": ".handhold @user",
        "category": "Friendly Actions"
    },
    "highfive": {
        "usage": "highfive <@user>",
        "description": "High-five a user",
        "example": ".highfive @user",
        "category": "Friendly Actions"
    },
    "poke": {
        "usage": "poke <@user>",
        "description": "Poke a user",
        "example": ".poke @user",
        "category": "Friendly Actions"
    },
    "nom": {
        "usage": "nom <@user>",
        "description": "Nom on a user",
        "example": ".nom @user",
        "category": "Playful Actions"
    },
    "wink": {
        "usage": "wink",
        "description": "Wink i guess",
        "example": ".wink",
        "category": "Playful Actions"
    },
    "dance": {
        "usage": "dance",
        "description": "Dance",
        "example": ".dance",
        "category": "Playful Actions"
    },
    "smug": {
        "usage": "smug",
        "description": "Show a smug expression",
        "example": ".smug",
        "category": "Playful Actions"
    },
    "cry": {
        "usage": "cry",
        "description": ":( aww cry baby",
        "example": ".cry",
        "category": "Playful Actions"
    },
    "slap": {
        "usage": "slap <@user>",
        "description": "Slap a user",
        "example": ".slap @user",
        "category": "Aggressive Actions"
    },
    "bite": {
        "usage": "bite <@user>",
        "description": "Bite a user",
        "example": ".bite @user",
        "category": "Aggressive Actions"
    },
    "lick": {
        "usage": "lick <@user>",
        "description": "Lick a user",
        "example": ".lick @user",
        "category": "Aggressive Actions"
    },
    "bully": {
        "usage": "bully <@user>",
        "description": "Bully a user",
        "example": ".bully @user",
        "category": "Aggressive Actions"
    },
    "hurt": {
        "usage": "hurt <@user>",
        "description": "Kill a user",
        "example": ".hurt @user",
        "category": "Aggressive Actions"
    },
    "bonk": {
        "usage": "bonk <@user>",
        "description": "Bonk a user",
        "example": ".bonk @user",
        "category": "Aggressive Actions"
    },
    "yeet": {
        "usage": "yeet <@user>",
        "description": "Yeet a user",
        "example": ".yeet @user",
        "category": "Aggressive Actions"
    },
    "emojiexport": {
        "usage": "emojiexport",
        "description": "Download all emojis from server",
        "example": ".emojiexport",
        "category": "Emoji Management"
    },
    "pastemoji": {
        "usage": "pastemoji",
        "description": "Add all your exported emojis",
        "example": ".pastemoji",
        "category": "Emoji Management"
    },
    "wipemojis": {
        "usage": "wipemojis",
        "description": "Clear all exported emojis",
        "example": ".wipemojis",
        "category": "Emoji Management"
    },
    "leavegroups": {
        "usage": "leavegroups",
        "description": "Leave all of your groups",
        "example": ".leavegroups",
        "category": "Server & Group Actions"
    },
    "firstmessage": {
        "usage": "firstmessage <channel>",
        "description": "See the first message in the channel",
        "example": ".firstmessage #general",
        "category": "Server & Group Actions"
    },
    "fakeactive": {
        "usage": "fakeactive",
        "description": "Use your tokens to make server active",
        "example": ".fakeactive",
        "category": "Server & Group Actions"
    },
    "fakeactiveoff": {
        "usage": "fakeactiveoff",
        "description": "Turn off fake activity",
        "example": ".fakeactiveoff",
        "category": "Server & Group Actions"
    },
    "info": {
        "usage": "info",
        "description": "Show Cmd Prmpt Info but in chat",
        "example": ".info",
        "category": "Server & Group Actions"
    },

    "pingresponse": {
        "usage": "pingresponse [toggle/list/clear] [response]",
        "description": "Reply to pings with a custom response",
        "example": ".pingresponse toggle \"your a skid!\"",
        "category": "Ping Response System"
    },
    "pinginsult": {
        "usage": "pinginsult [toggle/list/clear]",
        "description": "Reply to pings by insulting the user",
        "example": ".pinginsult toggle",
        "category": "Ping Response System"
    },
    "pingreact": {
        "usage": "pingreact [toggle reaction/list/clear]",
        "description": "Reply to pings by adding a reaction",
        "example": ".pingreact toggle 👋",
        "category": "Ping Response System"
    },
    "mcountdown": {
        "usage": "mcountdown <@user> <num>",
        "description": "Afk check someone with tokens",
        "example": ".mcountdown @user 60",
        "category": "AFK Check Systems"
    },
    "mcountdownoff": {
        "usage": "mcountdownoff",
        "description": "Stop Multi countdown",
        "example": ".mcountdownoff",
        "category": "AFK Check Systems"
    },
    "countdown": {
        "usage": "countdown <@user> <num>",
        "description": "Afk Check someone",
        "example": ".countdown @user 30",
        "category": "AFK Check Systems"
    },
    "countdownoff": {
        "usage": "countdownoff",
        "description": "Stop Countdown",
        "example": ".countdownoff",
        "category": "AFK Check Systems"
    },
    "autotrap": {
        "usage": "autotrap [toggle <user>/list/clear]",
        "description": "Manage users who cannot leave the group chat",
        "example": ".autotrap toggle @user",
        "category": "User Control Systems"
    },
    "autonick": {
        "usage": "autonick [toggle <@user> <nickname>/list/clear]",
        "description": "Force change a user's nickname",
        "example": ".autonick toggle @user NewNick",
        "category": "User Control Systems"
    },
    "forcepurge": {
        "usage": "forcepurge [toggle <@user>/list/clear]",
        "description": "Force delete a user's messages",
        "example": ".forcepurge toggle @user",
        "category": "User Control Systems"
    },
    "autokick": {
        "usage": "autokick [toggle <@user>/list/clear]",
        "description": "Automatically kick users",
        "example": ".autokick toggle @user",
        "category": "User Control Systems"
    },
    "autovclock": {
        "usage": "autovclock",
        "description": "Auto lock a voice channel when you join",
        "example": ".autovclock",
        "category": "User Control Systems"
    },
    "destroy": {
        "usage": "destroy",
        "description": "Perform destructive actions on the server",
        "example": ".destroy",
        "category": "Nuke Configuration"
    },
    "nukehook": {
        "usage": "nukehook",
        "description": "Change the webhook message for the nuke process",
        "example": ".nukehook",
        "category": "Nuke Configuration"
    },
    "nukename": {
        "usage": "nukename",
        "description": "Change the Discord server name for the nuke process",
        "example": ".nukename",
        "category": "Nuke Configuration"
    },
    "nukedelay": {
        "usage": "nukedelay",
        "description": "Change the delay between webhook messages",
        "example": ".nukedelay",
        "category": "Nuke Configuration"
    },
    "nukechannel": {
        "usage": "nukechannel",
        "description": "Change the channel name used for the webhook",
        "example": ".nukechannel",
        "category": "Nuke Configuration"
    },
    "nukeconfig": {
        "usage": "nukeconfig",
        "description": "Show the current configuration for the nuke process",
        "example": ".nukeconfig",
        "category": "Nuke Configuration"
    },
    "nukeconfigwipe": {
        "usage": "nukeconfigwipe",
        "description": "Delete the nuke config file and reset all data",
        "example": ".nukeconfigwipe",
        "category": "Nuke Configuration"
    },
    "massrole": {
        "usage": "massrole <name>",
        "description": "Creates mass roles with the given name",
        "example": ".massrole NewRole",
        "category": "Mass Server Actions"
    },
    "massroledel": {
        "usage": "massroledel",
        "description": "Deletes all roles except the default ones",
        "example": ".massroledel",
        "category": "Mass Server Actions"
    },
    "masschannel": {
        "usage": "masschannel <name> <number>",
        "description": "Creates mass channels",
        "example": ".masschannel general 5",
        "category": "Mass Server Actions"
    },
    "massban": {
        "usage": "massban",
        "description": "Bans everyone from the server",
        "example": ".massban",
        "category": "Mass Server Actions"
    },
    "masskick": {
        "usage": "masskick",
        "description": "Kicks everyone from the server",
        "example": ".masskick",
        "category": "Mass Server Actions"
    },
    "massdelemoji": {
        "usage": "massdelemoji",
        "description": "Delete all emojis from server",
        "example": ".massdelemoji",
        "category": "Mass Server Actions"
    },
    "spotify": {
        "usage": "spotify [command] [options]",
        "description": "Control your Spotify playback",
        "example": ".spotify play songname",
        "category": "Spotify Control System",
        "subcommands": {
            "unpause": "Resume playback if paused",
            "pause": "Pause the current playback",
            "next": "Skip to the next track",
            "prev": "Revert to the previous track",
            "play": "Search for and play a specific song",
            "current": "Show current track info",
            "addqueue": "Add a song to the queue",
            "volume": "Set volume level (0-100)",
            "shuffle": "Toggle shuffle mode",
            "repeat": "Set repeat mode (track/context/off)"
        }
    },
    "rotatepfp": {
        "usage": "rotatepfp <hours>",
        "description": "Starts profile picture rotation",
        "example": ".rotatepfp 24",
        "category": "Profile Customization"
    },
    "stoprandomizepfp": {
        "usage": "stoprandomizepfp",
        "description": "Stops profile picture rotation",
        "example": ".stoprandomizepfp",
        "category": "Profile Customization"
    },
    "setpfp": {
        "usage": "setpfp <url>",
        "description": "Set avatar with url",
        "example": ".setpfp https://example.com/image.png",
        "category": "Profile Customization"
    },
    "setbanner": {
        "usage": "setbanner <url>",
        "description": "Set banner with url",
        "example": ".setbanner https://example.com/banner.png",
        "category": "Profile Customization"
    },
    "stealpfp": {
        "usage": "stealpfp <user>",
        "description": "Steal a user's avatar",
        "example": ".stealpfp @user",
        "category": "Profile Customization"
    },
    "stealbanner": {
        "usage": "stealbanner <user>",
        "description": "Steal user's banner",
        "example": ".stealbanner @user",
        "category": "Profile Customization"
    },
    "rotatebio": {
        "usage": "rotatebio <text>",
        "description": "Rotate your bio each hour",
        "example": ".rotatebio Hello World",
        "category": "Bio & Status Management"
    },
    "stoprotatebio": {
        "usage": "stoprotatebio",
        "description": "Stop bio rotation",
        "example": ".stoprotatebio",
        "category": "Bio & Status Management"
    },
    "setbio": {
        "usage": "setbio <custom>",
        "description": "Set your bio",
        "example": ".setbio My Custom Bio",
        "category": "Bio & Status Management"
    },
    "stealbio": {
        "usage": "stealbio <user>",
        "description": "Snatch a user's About Me",
        "example": ".stealbio @user",
        "category": "Bio & Status Management"
    },
    "rstatus": {
        "usage": "rstatus",
        "description": "Rotate your custom status",
        "example": ".rstatus",
        "category": "Bio & Status Management"
    },
    "rstatusend": {
        "usage": "rstatusend",
        "description": "Cancel your rotate status",
        "example": ".rstatusend",
        "category": "Bio & Status Management"
    },
    "nickloop": {
        "usage": "nickloop <nicknames>",
        "description": "Rotates through nicknames",
        "example": ".nickloop Nick1 Nick2 Nick3",
        "category": "Name & Pronouns"
    },
    "stopnickloop": {
        "usage": "stopnickloop",
        "description": "Stops nickname rotation",
        "example": ".stopnickloop",
        "category": "Name & Pronouns"
    },
    "setpronoun": {
        "usage": "setpronoun <custom>",
        "description": "Set a custom pronoun",
        "example": ".setpronoun they/them",
        "category": "Name & Pronouns"
    },
    "rotatepronoun": {
        "usage": "rotatepronoun <custom>",
        "description": "Rotate your pronouns",
        "example": ".rotatepronoun he/him they/them",
        "category": "Name & Pronouns"
    },
    "stoprotatepronoun": {
        "usage": "stoprotatepronoun",
        "description": "Stop pronoun rotate",
        "example": ".stoprotatepronoun",
        "category": "Name & Pronouns"
    },
    "setname": {
        "usage": "setname <custom>",
        "description": "Set a custom display name",
        "example": ".setname NewName",
        "category": "Name & Pronouns"
    },
    "stealpronoun": {
        "usage": "stealpronoun <user>",
        "description": "Snatch a user's pronoun",
        "example": ".stealpronoun @user",
        "category": "Name & Pronouns"
    },
    "stealname": {
        "usage": "stealname <user>",
        "description": "Steal user's display name",
        "example": ".stealname @user",
        "category": "Name & Pronouns"
    },
    "channelinfo": {
        "usage": "channelinfo <id>",
        "description": "Display channel information",
        "example": ".channelinfo 123456789",
        "category": "Server Information"
    },
    "channels": {
        "usage": "channels <serverid>",
        "description": "Shows all channels",
        "example": ".channels 123456789",
        "category": "Server Information"
    },
    "roles": {
        "usage": "roles <serverid>",
        "description": "Shows all roles",
        "example": ".roles 123456789",
        "category": "Server Information"
    },
    "mutualinfo": {
        "usage": "mutualinfo",
        "description": "Shows Mutual info between users",
        "example": ".mutualinfo",
        "category": "Server Information"
    },
    "spamregion": {
        "usage": "spamregion <channel>",
        "description": "Changes voice channel region",
        "example": ".spamregion General",
        "category": "Voice Channel Management"
    },
    "stopspamregion": {
        "usage": "stopspamregion",
        "description": "Stops region spam",
        "example": ".stopspamregion",
        "category": "Voice Channel Management"
    },
    "ronmessage": {
        "usage": "ronmessage [add/list/remove/clear/on/off] [message] [reaction]",
        "description": "Automatic reactions to messages",
        "example": ".ronmessage add \"hello\" 👋",
        "category": "Message Reaction System",
        "subcommands": {
            "add": "Add reaction to message",
            "list": "List message reactions",
            "remove": "Remove message reaction",
            "clear": "Clear all reactions",
            "on/off": "Toggle reaction"
        }
    },
    "sonmessage": {
        "usage": "sonmessage [add/list/remove/clear/on/off] [message] [response]",
        "description": "Automatic responses to messages",
        "example": ".sonmessage add \"hi\" \"hello!\"",
        "category": "Message Response System",
        "subcommands": {
            "add": "Add custom response",
            "list": "List responses",
            "remove": "Remove response",
            "clear": "Clear responses",
            "on/off": "Toggle response"
        }
    },
    "eonmessage": {
        "usage": "eonmessage [add/list/remove/clear/on/off] [message] [edit]",
        "description": "Automatic message editing",
        "example": ".eonmessage add \"original\" \"edited\"",
        "category": "Message Edit System",
        "subcommands": {
            "add": "Add auto-edit",
            "list": "List edits",
            "remove": "Remove edit",
            "clear": "Clear edits",
            "on/off": "Toggle edit"
        }
    },
    "nonping": {
        "usage": "nonping [on/off/status]",
        "description": "Get notifications when pinged",
        "example": ".nonping on",
        "category": "Notification Systems",
        "subcommands": {
            "on/off": "Toggle notifications",
            "status": "Check status"
        }
    },
    "nondm": {
        "usage": "nondm [on/off/status]",
        "description": "Get DM notifications",
        "example": ".nondm on",
        "category": "Notification Systems",
        "subcommands": {
            "on/off": "Toggle DM alerts",
            "status": "Check status"
        }
    },
    "nonreaction": {
        "usage": "nonreaction [on/off/status]",
        "description": "Get reaction notifications",
        "example": ".nonreaction on",
        "category": "Notification Systems",
        "subcommands": {
            "on/off": "Toggle alerts",
            "status": "Check status"
        }
    },
    "wscreenshot": {
        "usage": "wscreenshot",
        "description": "Takes a full screen screenshot",
        "example": ".wscreenshot",
        "category": "Screenshot Management"
    },
    "pscreenshot": {
        "usage": "pscreenshot",
        "description": "Takes a screenshot of active window",
        "example": ".pscreenshot",
        "category": "Screenshot Management"
    },
    "sendss": {
        "usage": "sendss",
        "description": "Sends the most recent screenshot",
        "example": ".sendss",
        "category": "Screenshot Management"
    },
    "openss": {
        "usage": "openss",
        "description": "Opens the most recent screenshot",
        "example": ".openss",
        "category": "Screenshot Management"
    },
    "bsearch": {
        "usage": "bsearch <name>",
        "description": "Search using default browser",
        "example": ".bsearch discord",
        "category": "Windows Utilities"
    },
    "opencalc": {
        "usage": "opencalc",
        "description": "Opens Windows Calculator",
        "example": ".opencalc",
        "category": "Windows Utilities"
    },
    "openpad": {
        "usage": "openpad",
        "description": "Opens Windows Notepad",
        "example": ".openpad",
        "category": "Windows Utilities"
    },
    "dfolder": {
        "usage": "dfolder <name>",
        "description": "Creates Desktop folder",
        "example": ".dfolder NewFolder",
        "category": "Windows Utilities"
    },
    "cleartemp": {
        "usage": "cleartemp",
        "description": "Clear %temp% folder",
        "example": ".cleartemp",
        "category": "Windows Utilities"
    },
    "byoutube": {
        "usage": "byoutube <name>",
        "description": "Search YouTube",
        "example": ".byoutube music",
        "category": "Social Media Search"
    },
    "btwitter": {
        "usage": "btwitter <name>",
        "description": "Search Twitter",
        "example": ".btwitter username",
        "category": "Social Media Search"
    },
    "btiktok": {
        "usage": "btiktok <name>",
        "description": "Search TikTok",
        "example": ".btiktok username",
        "category": "Social Media Search"
    },
    "broblox": {
        "usage": "broblox <name>",
        "description": "Search Roblox",
        "example": ".broblox username",
        "category": "Social Media Search"
    },
    "hentai": {
        "usage": "hentai",
        "description": "Get hentai content",
        "example": ".hentai",
        "category": "General NSFW"
    },
    "uniform": {
        "usage": "uniform",
        "description": "Get uniform content",
        "example": ".uniform",
        "category": "General NSFW"
    },
    "maid": {
        "usage": "maid",
        "description": "Get maid content",
        "example": ".maid",
        "category": "General NSFW"
    },
    "oppai": {
        "usage": "oppai",
        "description": "Get oppai content",
        "example": ".oppai",
        "category": "General NSFW"
    },
    "selfies": {
        "usage": "selfies",
        "description": "Get selfie content",
        "example": ".selfies",
        "category": "General NSFW"
    },
    "raiden": {
        "usage": "raiden",
        "description": "Get Raiden Shogun content",
        "example": ".raiden",
        "category": "Character Specific"
    },
    "marin": {
        "usage": "marin",
        "description": "Get Marin Kitagawa content",
        "example": ".marin",
        "category": "Character Specific"
    },
    "mdm": {
        "usage": "mdm <num> <message>",
        "description": "Mass DMs a number of friends",
        "example": ".mdm 5 Hello!",
        "category": "Main Commands"
    },
    "theme": {
        "usage": "theme",
        "description": "Change theme colors",
        "example": ".theme",
        "category": "Main Commands"
    },
    "info": {
        "usage": "info",
        "description": "Shows bot info",
        "example": ".info",
        "category": "Main Commands"
    },
    "clear": {
        "usage": "clear",
        "description": "Clear console",
        "example": ".clear",
        "category": "Utility Commands"
    },
    "reload": {
        "usage": "reload",
        "description": "Restart the bot",
        "example": ".reload",
        "category": "Utility Commands"
    },
    "shutdown": {
        "usage": "shutdown",
        "description": "Shutdown the bot",
        "example": ".shutdown",
        "category": "Utility Commands"
    },
    "clearconfigs": {
        "usage": "clearconfigs",
        "description": "Clear all configs",
        "example": ".clearconfigs",
        "category": "Utility Commands"
    },
    "autobump": {
        "usage": "autobump",
        "description": "Auto Bump your server every 2hrs",
        "example": ".autobump",
        "category": "Utility Commands"
    },
    "autobumpoff": {
        "usage": "autobumpoff",
        "description": "Disable autobump",
        "example": ".autobumpoff",
        "category": "Utility Commands"
    },
    "blocked": {
        "usage": "blocked",
        "description": "Show blocked users",
        "example": ".blocked",
        "category": "Utility Commands"
    },
    "pending": {
        "usage": "pending",
        "description": "Show pending friend users",
        "example": ".pending",
        "category": "Utility Commands"
    },
    "outgoing": {
        "usage": "outgoing",
        "description": "Show outgoing friend requests",
        "example": ".outgoing",
        "category": "Utility Commands"
    },
    "tnickname": {
        "usage": "tnickname <server id>",
        "description": "Change token's server nickname",
        "example": ".tnickname 123456789",
        "category": "Token Utility"
    },
    "tpronoun": {
        "usage": "tpronoun <name>",
        "description": "Change token's pronoun",
        "example": ".tpronoun they/them",
        "category": "Token Utility"
    },
    "tbio": {
        "usage": "tbio <custom>",
        "description": "Change token's bio",
        "example": ".tbio New Bio Text",
        "category": "Token Utility"
    },
    "tstatus": {
        "usage": "tstatus <status>",
        "description": "Change token's online status",
        "example": ".tstatus playing games",
        "category": "Token Utility"
    },
    "tstatusoff": {
        "usage": "tstatusoff",
        "description": "Turn off token's custom status",
        "example": ".tstatusoff",
        "category": "Token Utility"
    },
    "tinfo": {
        "usage": "tinfo",
        "description": "Get token account info",
        "example": ".tinfo",
        "category": "Token Utility"
    },
    "tjoin": {
        "usage": "tjoin <invite>",
        "description": "Join server with token",
        "example": ".tjoin discord.gg/invite",
        "category": "Token Utility"
    },
    "tleave": {
        "usage": "tleave <server id>",
        "description": "Leave server with token",
        "example": ".tleave 123456789",
        "category": "Token Utility"
    },
    "autopress": {
        "usage": "autopress [command] [options]",
        "description": "Auto press messages in channel",
        "example": ".autopress add \"Hello\"",
        "category": "Auto Press Commands",
        "subcommands": {
            "user": "Auto press messages in channel",
            "stop": "Turn off autopress",
            "list": "List all autopress channels",
            "add": "Add a message to autopress",
            "remove": "Remove a message from autopress",
            "clear": "Clear all autopress messages"
        }
    },

    "autokill": {
        "usage": "autokill [command] [options]",
        "description": "Auto kill user in all channels",
        "example": ".autokill @user",
        "category": "Auto Kill Commands",
        "subcommands": {
            "user": "Auto kill user in all channels",
            "stop": "Turn off autokill",
            "list": "List all autokill users",
            "clear": "Clear all autokill users",
            "add": "Add a word to autokill",
            "remove": "Remove a word from autokill"
        }
    },
    "manual": {
        "usage": "manual [command] [options]",
        "description": "Enable manual mode",
        "example": ".manual @user",
        "category": "Manual Mode Commands",
        "subcommands": {
            "user": "Enable manual mode",
            "stop": "Turn off manual mode",
            "list": "List all manual msgs",
            "clear": "Clear all manual msgs",
            "add": "Add a message to manual mode",
            "remove": "Remove a message from manual mode"
        }
    },
    "vcjoin": {
        "usage": "vcjoin [command] [options]",
        "description": "Voice channel join commands",
        "example": ".vcjoin r 123456789",
        "category": "Multi/Vc Commands",
        "subcommands": {
            "r": "Rotate join a voice channel",
            "s": "Join a voice channel",
            "status": "Shows the current voice channel status",
            "list": "List all available voice channels",
            "leave": "Leave voice channel"
        }
    },
    "dripcheck": {
        "usage": "dripcheck <user>",
        "description": "Check user's drip level",
        "example": ".dripcheck @user",
        "category": "Random Beef Commands"
    },
    "discordreport": {
        "usage": "discordreport <user>",
        "description": "Generate a report card for user",
        "example": ".discordreport @user",
        "category": "Random Beef Commands"
    },
    "relationship": {
        "usage": "relationship <user>",
        "description": "Check user's relationship potential",
        "example": ".relationship @user",
        "category": "Random Beef Commands"
    },
    "stats": {
        "usage": "stats <user>",
        "description": "Get user's stats",
        "example": ".stats @user",
        "category": "Random Beef Commands"
    },
    "unfriend": {
        "usage": "unfriend <user>",
        "description": "Send friend request to user",
        "example": ".unfriend @user",
        "category": "Friend & Block Utility"
    },
    "block": {
        "usage": "block <user>",
        "description": "Block user",
        "example": ".block @user",
        "category": "Friend & Block Utility"
    },
    "unblock": {
        "usage": "unblock <user>",
        "description": "Unblock user",
        "example": ".unblock @user",
        "category": "Friend & Block Utility"
    },
    "friend": {
        "usage": "friend <user id>",
        "description": "Send friend request to user",
        "example": ".friend 123456789",
        "category": "Friend & Block Utility"
    },
    "fnote": {
        "usage": "fnote <user id>",
        "description": "Send friend note to user",
        "example": ".fnote 123456789",
        "category": "Friend & Block Utility"
    },
    "fnick": {
        "usage": "fnick <user id>",
        "description": "Change friend nickname",
        "example": ".fnick 123456789",
        "category": "Friend & Block Utility"
    },
    "autogc": {
        "usage": "autogc [command] [options]",
        "description": "Auto add tokens to any group chat your added to",
        "example": ".autogc whitelist @user",
        "category": "Auto Multi Commands",
        "subcommands": {
            "whitelist": "Whitelist a user to auto add to gc",
            "whitelist remove": "Remove a user from the whitelist",
            "list": "List all whitelisted users"
        }
    },
    "autogcstop": {
        "usage": "autogcstop",
        "description": "Turn off autogc",
        "example": ".autogcstop",
        "category": "Auto Multi Commands"
    },
    "autogcleave": {
        "usage": "autogcleave [stop]",
        "description": "Auto leave any group chat you leave",
        "example": ".autogcleave",
        "category": "Auto Gc Leave Commands",
        "subcommands": {
            "stop": "Turn off autogcleave"
        }
    },
    "autoserverleave": {
        "usage": "autoserverleave [stop]",
        "description": "Auto leave any server you leave",
        "example": ".autoserverleave",
        "category": "Auto Server Leave Commands",
        "subcommands": {
            "stop": "Turn off autoserverleave"
        }
    },
    "repeat": {
        "usage": "repeat [command] [options]",
        "description": "Auto repeat commands",
        "example": ".repeat start",
        "category": "Auto Repeat Commands",
        "subcommands": {
            "start": "Start auto repeat",
            "stop": "Turn off auto repeat",
            "delay": "Set the delay between repeats",
            "status": "Check auto repeat status"
        }
    },
    "ladder": {
        "usage": "ladder [command] [options]",
        "description": "Auto ladder system",
        "example": ".ladder start",
        "category": "Auto Ladder Commands",
        "subcommands": {
            "start": "Start auto ladder",
            "stop": "Turn off auto ladder",
            "delay": "Set the delay between ladders",
            "add": "Add a message to auto ladder",
            "remove": "Remove a message from auto ladder",
            "clear": "Clear all auto ladder messages",
            "list": "List all auto ladder messages",
            "reset": "Reset auto ladder",
            "status": "Show all ladder messages"
        }
    },
    "antigcspam": {
        "usage": "antigcspam [command] [options]",
        "description": "Anti group chat spam protection",
        "example": ".antigcspam whitelist @user",
        "category": "Anti Gc Spam",
        "subcommands": {
            "toggle": "Toggle protection & show status",
            "whitelist": "Add user to whitelist",
            "unwhitelist": "Remove user from whitelist",
            "blacklist": "Add user to blacklist",
            "unblacklist": "Remove user from blacklist",
            "silent": "Toggle silent mode",
            "message": "Set leave message",
            "autoremove": "Toggle auto-remove of blacklisted",
            "webhook": "Set webhook for logging",
            "autoblock": "Toggle auto-block feature",
            "list": "Show white/blacklisted users"
        }
    },
    "rotateguild": {
        "usage": "rotateguild [command] [options]",
        "description": "Guild badge rotation system",
        "example": ".rotateguild start",
        "category": "Rotate Guild",
        "subcommands": {
            "start": "Start rotating guild badges",
            "stop": "Stop rotating guild badges",
            "delay": "Set the delay between guild badge rotations",
            "status": "Show current guild rotation status"
        }
    },
    "protection": {
        "usage": "protection [command] [options]",
        "description": "GC Protection Spam",
        "example": ".protection start",
        "category": "GC Protection Spam",
        "subcommands": {
            "start": "Start protection",
            "stop": "Stop protection",
            "message": "Set protection message",
            "status": "Show protection status"
        }
    },
    "dmsnipe": {
        "usage": "dmsnipe [command] [options]",
        "description": "Message sniper system",
        "example": ".dmsnipe start",
        "category": "Message Sniper System",
        "subcommands": {
            "toggle": "Toggle message sniping",
            "edit": "Toggle edit sniping",
            "ignore": "Toggle ignoring a user",
            "ignore": "Toggle ignoring a channel",
            "status": "Show current settings",
            "clear": "Clear all ignore lists"
        }
    },
    "antilast": {
        "usage": "antilast [command] [options]",
        "description": "Anti last word system",
        "example": ".antilast toggle",
        "category": "Anti Last Word",
        "subcommands": {
            "toggle": "Toggle anti last word system",
            "whitelist": "Add user to whitelist",
            "channel": "Add channel to whitelist",
            "webhook": "Set webhook for logging",
            "config": "Show current config"
        }
    },
    "spam": {
        "usage": "spam [user] [user 2]",
        "description": "Send a message to a user",
        "example": ".spam @user @user2",
        "category": "Spam Commands"
    },
    "hypesquad": {
        "usage": "hypesquad [house]",
        "description": "Change your HypeSquad house",
        "example": ".hypesquad bravery",
        "category": "HypeSquad Commands"
    },
    "setspfp": {
        "usage": "setspfp <url>",
        "description": "Set server-specific profile picture",
        "example": ".setspfp https://example.com/image.png",
        "category": "Server Edit Commands"
    },
    "setsbanner": {
        "usage": "setsbanner <url>",
        "description": "Set server-specific banner",
        "example": ".setsbanner https://example.com/image.png",
        "category": "Server Edit Commands"
    },
    "setsbio": {
        "usage": "setsbio <text>",
        "description": "Set server-specific bio",
        "example": ".setsbio Hello, world!",
        "category": "Server Edit Commands"
    },
    "setspronoun": {
        "usage": "setspronoun <text>",
        "description": "Set server-specific pronouns",
        "example": ".setspronoun He/Him",
        "category": "Server Edit Commands"
    },
    "srotate": {
        "usage": "srotate [command] [options]",
        "description": "Server rotation system",
        "example": ".srotate start",
        "category": "Server Rotate Commands",
        "subcommands": {
            "pfp": "Start rotating server profile pictures",
            "banner": "Start rotating server banners",
            "bio": "Start rotating server bios",
            "pronouns": "Start rotating server pronouns",
            "delay": "Set the delay between rotations",
            "stop": "Stop rotation",
            "status": "Show current rotation status"
        }
    },
    "imgdump": {
        "usage": "imgdump",
        "description": "Dump a user's image",
        "example": ".imgdump",
        "category": "Image Dumping"
    },
    "gifdump": {
        "usage": "gifdump",
        "description": "Dump a user's gif",
        "example": ".gifdump",
        "category": "Image Dumping"
    },
    "movdump": {
        "usage": "movdump",
        "description": "Dump a user's video",
        "example": ".movdump",
        "category": "Image Dumping"
    },
    "mp4dump": {
        "usage": "mp4dump",
        "description": "Dump all videos in a channel",
        "example": ".mp4dump",
        "category": "Image Dumping"
    }       
        }
    def load_themes(self):
        try:
            with open('themes.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_themes(self):
        with open('themes.json', 'w') as f:
            json.dump(self.user_themes, f, indent=4)

    @commands.command()
    async def theme(self, ctx, color=None):
        if color and not color.startswith('t'):
            color = color.lower()
            valid_colors = {
                "red": red,
                "blue": blue, 
                "cyan": cyan,
                "green": green,
                "yellow": yellow,
                "magenta": magenta
            }
            
            if color not in valid_colors:
                await ctx.send("```ansi\nInvalid theme color. Use .theme to see available options```")
                return
                
            self.user_themes[str(ctx.author.id)] = color
            self.save_themes()
            
            self.default_colors = {
                "text": valid_colors[color],
                "highlight": valid_colors[color], 
                "accent": valid_colors[color]
            }
            
            await ctx.send(f"```ansi\nTheme set to {color}```")
            return

        pages = {
            "t1": f"""```ansi
    Current theme: {self.user_themes.get(str(ctx.author.id), 'default')}
{blue}─────────────────────────────────────────────────────────────────────────────────────────────────────────────{reset}
    {blue}Blue Theme Example{reset}
    [ {blue}1{reset} ] Lappy was here >.< 
    [ {blue}2{reset} ] Are you a skid ?
    [ {blue}3{reset} ] HAHA BIRTH SB IS BETTER
{blue}─────────────────────────────────────────────────────────────────────────────────────────────────────────────{reset}

    Use {blue}tselect blue{reset} to select this theme
    Page 1/6 - Use t1-t7```""",

            "t2": f"""```ansi
    Current theme: {self.user_themes.get(str(ctx.author.id), 'default')}
{red}─────────────────────────────────────────────────────────────────────────────────────────────────────────────{reset}
    {red}Red Theme Example{reset}
    [ {red}1{reset} ] Lappy was here >.< 
    [ {red}2{reset} ] Are you a skid ?
    [ {red}3{reset} ] HAHA BIRTH SB IS BETTER
{red}─────────────────────────────────────────────────────────────────────────────────────────────────────────────{reset}
    Use {red}tselect red{reset} to select this theme
    Page 2/6 - Use t1-t7```""",

            "t3": f"""```ansi
    Current theme: {self.user_themes.get(str(ctx.author.id), 'default')}
{magenta}─────────────────────────────────────────────────────────────────────────────────────────────────────────────{reset}
    {magenta}Magenta Theme Example{reset}
    [ {magenta}1{reset} ] Lappy was here >.< 
    [ {magenta}2{reset} ] Are you a skid ?
    [ {magenta}3{reset} ] HAHA BIRTH SB IS BETTER
{magenta}─────────────────────────────────────────────────────────────────────────────────────────────────────────────{reset}
    Use {magenta}tselect magenta{reset} to select this theme
    Page 3/6 - Use t1-t7```""",

            "t4": f"""```ansi
    Current theme: {self.user_themes.get(str(ctx.author.id), 'default')}
{cyan}─────────────────────────────────────────────────────────────────────────────────────────────────────────────{reset}
    {cyan}Cyan Theme Example{reset}
    [ {cyan}1{reset} ] Lappy was here >.< 
    [ {cyan}2{reset} ] Are you a skid ?
    [ {cyan}3{reset} ] HAHA BIRTH SB IS BETTER
{cyan}─────────────────────────────────────────────────────────────────────────────────────────────────────────────{reset}
    Use {cyan}tselect cyan{reset} to select this theme
    Page 4/6 - Use t1-t7```""",

            "t5": f"""```ansi
    Current theme: {self.user_themes.get(str(ctx.author.id), 'default')}
{green}─────────────────────────────────────────────────────────────────────────────────────────────────────────────{reset}
    {green}Green Theme Example{reset}
    [ {green}1{reset} ] Lappy was here >.< 
    [ {green}2{reset} ] Are you a skid ?
    [ {green}3{reset} ] HAHA BIRTH SB IS BETTER
{green}─────────────────────────────────────────────────────────────────────────────────────────────────────────────{reset}
    Use {green}tselect green{reset} to select this theme
    Page 5/6 - Use t1-t7```""",

            "t6": f"""```ansi
    Current theme: {self.user_themes.get(str(ctx.author.id), 'default')}
{yellow}─────────────────────────────────────────────────────────────────────────────────────────────────────────────{reset}
    {yellow}Yellow Theme Example{reset}
    [ {yellow}1{reset} ] Lappy was here >.< 
    [ {yellow}2{reset} ] Are you a skid ?
    [ {yellow}3{reset} ] HAHA BIRTH SB IS BETTER
{yellow}─────────────────────────────────────────────────────────────────────────────────────────────────────────────{reset}
    Use {yellow}tselect yellow{reset} to select this theme
    Page 6/6 - Use t1-t7```""",
            "t7": f"""```ansi
    Current theme: {self.user_themes.get(str(ctx.author.id), 'default')}
    \u001b[35;1m─────────────────────────────────────────────────────────────────────────────────────────────────────────────{reset}
    \u001b[35;1mPurple Theme Example{reset}
    [ \u001b[35;1m1{reset} ] Lappy was here >.< 
    [ \u001b[35;1m2{reset} ] Are you a skid ?
    [ \u001b[35;1m3{reset} ] HAHA BIRTH SB IS BETTER
    \u001b[35;1m─────────────────────────────────────────────────────────────────────────────────────────────────────────────{reset}
    Use \u001b[35;1mtselect purple{reset} to select this theme
    Page 7/10 - Use t1-t10```"""
    }
        msg = await ctx.send(pages["t1"])
        self.theme_message = msg

        def check(m):
            return (m.author == ctx.author and 
                    (m.content.startswith('t') and m.content[1:].isdigit() and 
                    1 <= int(m.content[1:]) <= 10) or 
                    m.content.startswith('tselect'))

        while True:
            try:
                user_msg = await ctx.bot.wait_for('message', timeout=20.0, check=check)
                await user_msg.delete() 

                if user_msg.content.startswith('tselect'):
                    parts = user_msg.content.split()
                    if len(parts) < 2: 
                        continue  
                        
                    selected_color = parts[1].lower()
                    if selected_color in ["red", "blue", "magenta", "cyan", "green", "yellow"]:
                        self.user_themes[str(ctx.author.id)] = selected_color
                        self.save_themes()
                        confirm = await ctx.send(f"```ansi\nTheme set to {selected_color}```")
                        await asyncio.sleep(3)
                        await confirm.delete()
                        await self.theme_message.delete()
                        break

                elif user_msg.content.startswith('t'):
                    page_num = f"t{user_msg.content[1]}"
                    if page_num in pages:
                        await self.theme_message.edit(content=pages[page_num])

            except asyncio.TimeoutError:
                print(" Timed out")
                break
    @commands.command()
    async def help(self, ctx, command_name: str = None):
        if command_name:
            theme = self.user_themes.get(str(ctx.author.id), None)
            if theme:
                text_color = highlight_color = accent_color = globals()[theme]
            else:
                text_color = self.default_colors["text"]
                highlight_color = self.default_colors["highlight"]
                accent_color = self.default_colors["accent"]

            command_info = self.command_help.get(command_name.lower())
            BOX_WIDTH = 78 
            PADDING_START = len("║ Command: ") 

            def format_line(content, prefix_len):
                spaces_needed = BOX_WIDTH - prefix_len - len(content) - 1  
                return content + " " * spaces_needed + f"{text_color}║"
            if command_info:
                help_text = f"""```ansi
{text_color}╔══════════════════════════════════════════════════════════════════════════════╗{reset}
{text_color}║ {blue}Command:{white} {format_line(command_info['usage'], 9)}
{text_color}║ {blue}Category:{white} {format_line(command_info['category'], 10)}
{text_color}║ {blue}Description:{white} {format_line(command_info['description'], 13)}
{text_color}║ {blue}Example:{white} {format_line(command_info['example'], 9)}
{text_color}╚══════════════════════════════════════════════════════════════════════════════╝{reset}
```"""
                await ctx.send(help_text)
                return

        theme = self.user_themes.get(str(ctx.author.id), None)
        if theme:
            text_color = highlight_color = accent_color = globals()[theme]
        else:
            text_color = self.default_colors["text"]
            highlight_color = self.default_colors["highlight"]
            accent_color = self.default_colors["accent"]

        themed_pages = {}
        for page_num, content in pages.items():
            themed_content = content.replace(blue, text_color)
            themed_content = themed_content.replace(magenta, highlight_color)
            themed_content = themed_content.replace(red, accent_color)
            themed_pages[page_num] = themed_content

        msg = await ctx.send("Loading.")
        help_message_id = msg.id
        self.active_help_messages[help_message_id] = {"current_page": 1, "user_id": ctx.author.id}
        
        full_art = ""
        for frame in kitty_frames:
            full_art += frame + "\n"
            await msg.edit(content=f"```ansi\n{full_art}```")
            await asyncio.sleep(0.3)
        
        total_pages = await get_page_count(themed_pages)
        await msg.edit(content=f"```ansi\n{themed_pages[1]}\n{accent_color}Page 1/{total_pages}                                    {accent_color}type {highlight_color}'p[Page #]'{accent_color} To see pages. ```")

        def check(message):
            return (
                message.author == ctx.author and
                message.content.startswith("p") and
                message.content[1:].isdigit()
            )

        try:
            while True:
                user_message = await self.bot.wait_for("message", timeout=TIMEOUT, check=check)
                new_page = int(user_message.content[1:])

                if new_page not in themed_pages:
                    await ctx.send(
                        f"```Page {new_page} does not exist. Please choose a valid page number between 1 and {total_pages}.```",
                        delete_after=5
                    )
                    continue

                current_page_content = f"```ansi\n{themed_pages[new_page]}\n{accent_color}Page {new_page}/{total_pages}                                    type {highlight_color}'p[Page #]'{accent_color} To see pages.```"
                await msg.edit(content=current_page_content)
                self.active_help_messages[help_message_id]["current_page"] = new_page

                await user_message.delete()

        except asyncio.TimeoutError:
            if help_message_id in self.active_help_messages:
                del self.active_help_messages[help_message_id]
                await msg.edit(content=f"```ansi\n{themed_pages[1]}```")



    @commands.group()
    async def autosnipe(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(f"```ansi\n{blue}Invalid autosnipe command. Use {red}.autosnipe toggle on/off, .autosnipe custom <message>, .autosnipe clear, or .autosnipe list.```")

    @autosnipe.command()
    async def toggle(self, ctx, option: str):
        channel_id = ctx.channel.id
        if option.lower() not in ["on", "off"]:
            await ctx.send(f"```ansi\n{blue}Invalid Use {red}.autosnipe toggle on or .autosnipe toggle off.")
            return

        if channel_id not in self.auto_snipe_settings:
            self.auto_snipe_settings[channel_id] = {"enabled": False, "custom_message": None}

        self.auto_snipe_settings[channel_id]["enabled"] = option.lower() == "on"
        status = "enabled" if option.lower() == "on" else "disabled"
        await ctx.send(f"```auto snipe is now {status} in this channel.```")

    @autosnipe.command()
    async def custom(self, ctx, *, message: str):
        channel_id = ctx.channel.id
        if channel_id not in self.auto_snipe_settings:
            self.auto_snipe_settings[channel_id] = {"enabled": False, "custom_message": None}

        self.auto_snipe_settings[channel_id]["custom_message"] = message
        await ctx.send(f"```ansi\nauto snipe message set to: {red}{message}```")

    @autosnipe.command()
    async def clear(self, ctx):
        channel_id = ctx.channel.id
        if channel_id in self.auto_snipe_settings:
            self.auto_snipe_settings[channel_id]["custom_message"] = None
            await ctx.send("Custom auto-snipe message cleared.")
        else:
            await ctx.send("```Auto snipe is not set up in this channel.```")

    @autosnipe.command()
    async def list(self, ctx):
        channel_id = ctx.channel.id
        if channel_id in self.auto_snipe_settings:
            settings = self.auto_snipe_settings[channel_id]
            custom_message = settings["custom_message"] or "Default: `,s`"
            status = "enabled" if settings["enabled"] else "disabled"
            await ctx.send(f"```ansi\nAuto snipe status: {red}{status}\n{white}Custom message: {red}{custom_message}```")
        else:
            await ctx.send("```No auto snipe settings found for this channel.```")


    @commands.command()
    async def autocsnipe(self, ctx, action: str, *, content=None):
        guild_id = ctx.guild.id
        channel_id = ctx.channel.id

        if guild_id not in self.auto_csnipe_settings:
            self.auto_csnipe_settings[guild_id] = {}

        if channel_id not in self.auto_csnipe_settings[guild_id]:
            self.auto_csnipe_settings[guild_id][channel_id] = {
                "enabled": False,
                "custom_message": ",cs",
                "user_id": ctx.author.id 
            }

        if action == "toggle":
            if content == "on":
                self.auto_csnipe_settings[guild_id][channel_id]["enabled"] = True
                await ctx.send("```auto cs enabled for this channel.```")
            elif content == "off":
                self.auto_csnipe_settings[guild_id][channel_id]["enabled"] = False
                await ctx.send("```auto cs disabled for this channel.```")
            else:
                await ctx.send("```Usage: .autocsnipe toggle on/off```")

        elif action == "custom":
            if content:
                self.auto_csnipe_settings[guild_id][channel_id]["custom_message"] = content
                await ctx.send(f"```auto cs message set to: {content}```")
            else:
                await ctx.send("```Please provide a custom message. Usage: .autocsnipe custom <message>```")

        elif action == "clear":
            self.auto_csnipe_settings[guild_id][channel_id]["custom_message"] = "cs"
            await ctx.send("```auto cs message cleared. Reverted to default: 'cs'```")

        elif action == "list":
            current_settings = self.auto_csnipe_settings[guild_id][channel_id]
            status = "Enabled" if current_settings["enabled"] else "Disabled"
            message = current_settings["custom_message"]
            await ctx.send(f"```auto cs Status: {status}\nCustom Message: {message}```")

        else:
            await ctx.send("```Invalid action. Use toggle, custom, clear, or list.```")


    @commands.command()
    async def clearconfigs(self, ctx):
        confirmation_msg = await ctx.send("```ansi\n Are you sure you want to clear all config files?```")
        await confirmation_msg.add_reaction("✅")
        await confirmation_msg.add_reaction("❌")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["✅", "❌"] and reaction.message == confirmation_msg

        try:
            reaction, user = await self.bot.wait_for('reaction_remove', timeout=10.0, check=check)
            
            if str(reaction.emoji) == "✅":
                config_dir = "configs"
                for filename in os.listdir(config_dir):
                    if filename.endswith('.json') and filename != "config.json":
                        filepath = os.path.join(config_dir, filename)
                        with open(filepath, 'w') as f:
                            f.write('{}')
                
                main_config = os.path.join(config_dir, "config.json")
                if os.path.exists(main_config):
                    with open(main_config, 'r') as f:
                        existing_config = json.load(f)
                        
                    cleared_config = {key: "" for key in existing_config.keys()}
                    
                    with open(main_config, 'w') as f:
                        json.dump(cleared_config, f, indent=4)
                        
                await ctx.send("```ansi\n All config files have been cleared.```")
            else:
                await ctx.send("```ansi\n Config clear operation cancelled```")

        except TimeoutError:
            await ctx.send("```ansi\n Config clear operation timed out```")

    @commands.command()
    async def shutdown(self, ctx):
        await ctx.send("```ansi\n Shutting down the bot...```")
        await self.bot.close()

    """@commands.Cog.listener()
    async def on_message_delete(self, message):
        channel_id = message.channel.id
        guild_id = message.guild.id
        if channel_id in self.auto_snipe_settings and self.auto_snipe_settings[channel_id]["enabled"]:
            custom_message = self.auto_snipe_settings[channel_id]["custom_message"] or ",s"
            await message.channel.send(custom_message)


        if guild_id in self.auto_csnipe_settings and channel_id in self.auto_csnipe_settings[guild_id]:
            settings = self.auto_csnipe_settings[guild_id][channel_id]


            if settings["enabled"] and message.author.id == settings["user_id"]:
                custom_message = settings["custom_message"]
                await message.channel.send(custom_message)"""



def setup(bot):
    bot.add_cog(HelpCog(bot))


"""
    [ {highlight_color}146{reset} ] autosnipe - Manage automatic responses to deleted messages.
        {accent_color}Usage:
        {green}[ {text_color}^{green} ] {black}autosnipe {green}toggle on{reset} - {black}Enable auto snipe in the current channel.{reset}
        {green}[ {text_color}^{green} ] {black}autosnipe {green}toggle off{reset} - {black}Disable auto snipe in the current channel.{reset}
        {green}[ {text_color}^{green} ] {black}autosnipe {green}custom <message>{reset} - {black}Set a custom auto-snipe message for the current channel.{reset}
        {green}[ {text_color}^{green} ] {black}autosnipe {green}clear{reset} - {black}Clear the custom auto snipe message.{reset}
        {green}[ {text_color}^{green} ] {black}autosnipe {green}list{reset} - {black}Show the current auto snipe settings and custom message for this channel.{reset}
    [ {text_color}147{reset} ] autocsnipe - Automatically send a custom message when a message is deleted.
        {accent_color}Usage:
        {green}[ {text_color}^{green} ] {black}autocsnipe toggle {green}on{reset} - {black}Enable Auto-CSnipe for the current channel.{reset}
        {green}[ {text_color}^{green} ] {black}autocsnipe toggle {green}off{reset} - {black}Disable Auto-CSnipe for the current channel.{reset}
        {green}[ {text_color}^{green} ] {black}autocsnipe custom {green}<message>{reset} - {black}Set a custom message to send when a message is deleted.{reset}
        {green}[ {text_color}^{green} ] {black}autocsnipe clear{reset} - {black}Clear the custom message and revert to the default: `cs`.{reset}
        {green}[ {text_color}^{green} ] {black}autocsnipe list{reset} - {black}Show the current Auto-CSnipe settings for this channel.{reset}"""