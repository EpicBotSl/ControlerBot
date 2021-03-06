from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

You can use me to manage channels with tons of features. Use below buttons to learn more !

By @NA_VA_N_JA_NA1
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="ποΈ Return Home ποΈ", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("π€ Bot Status and More Bots π€", url="https://t.me/EpicBotsSl")],
        [
            InlineKeyboardButton("How to Use β", callback_data="help"),
            InlineKeyboardButton("βΎοΈ About βΎοΈ", callback_data="about")
        ],
        [InlineKeyboardButton("β₯ More Amazing bots β₯", url="https://t.me/EpicBotsSl")],
        [InlineKeyboardButton("π« Support Group π«", url="https://t.me/EpicChats")],
    ]

    # Help Message
    HELP = """
Everything is self explanatory after you add a channel.
To add a channel use keyboard button 'Add Channels' or alternatively for ease, use `/add` command

π€ **Available Commands** π€

/about - About The Bot
/help - This Message
/start - Start the Bot

Alternative Commands
/channels - List added Channels
/add - Add a channel
/report - Report a Problem
    """

    # About Message
    ABOUT = """
**About This Bot** 

A telegram channel automation bot by @EpicBots

Source Code : [Click Here](https://github.com/EpicBotSl/ControlerBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @NA_VA_N_JA_NA1
    """
