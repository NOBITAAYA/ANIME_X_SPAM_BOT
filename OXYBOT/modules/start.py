from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("★𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦★", data="help_back")
    ],
    [
        Button.url("★𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥★", "https://t.me/Devilspambotrepo"),
        Button.url("★𝗦𝗨𝗣𝗣𝗢𝗥𝗧★", "https://t.me/Box_of_bot")
    ],
    [
        Button.url("★𝗖𝗢𝗗𝗘𝗥★", "https://t.me/Daddy_deviLl_mere")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})**\n"
        await event.client.send_file(
            event.chat_id,
            "https://telegra.ph/file/7b23e31e05a689b217552.jpg",
            caption=TEXT,
            buttons=START_BUTTON
        )
