from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can force your group's users to join a particular chat. 
The chat can be a group or channel. It can be private or public.

Use below buttons to learn more !

By @ImDark_Empire
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="ποΈ Return Home ποΈ", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("π€ Bot Status and More Bots π€", url="https://t.me/SLBotOfficial/28")],
        [
            InlineKeyboardButton("β How to Use β", callback_data="help"),
            InlineKeyboardButton("βΎοΈ About βΎοΈ", callback_data="about")
        ],
        [InlineKeyboardButton("β₯ More Amazing bots β₯", url="https://t.me/SLBotOfficial")],
        [InlineKeyboardButton("π« Support Group π«", url="https://t.me/trtechguide")],
    ]

    # Help Message
    HELP = """
1) Add me as **Admin** to a group.

2) Add me to the particular chat as **Admin** where you want to force your users to join. It can be any group or channel, public or private.

3) Use /fsub chat_id/username to make me functional. Use /id if you need chat id.
Example : `/fsub -1001505616678` or `/forcesubscribe -1001375849192`

4) [Optional] Use /settings to change settings!

5) You are good to go. Leave the rest to me.

π€ **Available Commands** π€

/fsub - See current force subscribe chat
/fsub chat_id/username - Force users to join the particular chat
/settings - Change Group Settings
/id - Get the chat id of any group or channel
/about - About The Bot
/help - This Message
/start - Start the Bot

**Note** - You can also use `/forcesubscribe` instead of `/fsub`
    """

    # About Message
    ABOUT = """
**About This Bot** 

A telegram force subscribing bot by @SLBotOfficial

Source Code : [Click Here](https://github.com/DARKEMPIRESL/ForceSubscribeBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @ImDark_Empire
    """
