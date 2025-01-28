def initialize_messages(bot):
    custom_messages = bot.get_cog('CustomMessages')

    kill_messages = custom_messages.get_messages('kill') if custom_messages else []
    autoreplies = custom_messages.get_messages('autoreplies') if custom_messages else []
    autoreplies_multi = custom_messages.get_messages('autoreplies_multi') if custom_messages else []
    outlast_messages = custom_messages.get_messages('outlast') if custom_messages else []
    protection_messages = custom_messages.get_messages('protection') if custom_messages else []

    return {
        'kill': kill_messages,
        'autoreplies': autoreplies,
        'autoreplies_multi': autoreplies_multi,
        'outlast': outlast_messages,
        'protection': protection_messages
    }
