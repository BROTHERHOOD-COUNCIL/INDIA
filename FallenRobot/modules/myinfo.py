import asyncio
import datetime
import re
from datetime import datetime

from telethon import custom, events

from FallenRobot import telethn as bot
from FallenRobot import telethn as tgbot
from FallenRobot.events import register

edit_time = 5
""" =======================FALLEN ROBOT====================== """
file1 = "https://te.legra.ph/file/4bb026395f51c859a19a8.jpg"
file2 = "https://te.legra.ph/file/e95dfa1aca5f3594c01ae.jpg"
file3 = "https://te.legra.ph/file/19833015e6ee953c10e4c.jpg"
file4 = "https://te.legra.ph/file/83fb9238dbb60ee90e920.jpg"
file5 = "https://te.legra.ph/file/8a3b4e08948e35680dd42.jpg"
""" =======================FALLEN ROBOT====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    await event.get_chat()
    datetime.utcnow()
    firstname = event.sender.first_name
    button = [[custom.Button.inline("information", data="informations")]]
    on = await bot.send_file(
        event.chat_id,
        file=file2,
        caption=f"Hey {firstname}, \n Click on the button below \n to get info about you",
        buttons=button,
    )

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)

    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
    try:
        boy = event.sender_id
        PRO = await bot.get_entity(boy)
        LILIE = "POWERED BY 😈𝐃𝐀𝐑𝐊 𝐇𝐔𝐍𝐓𝐄𝐑😈 \n\n"
        LILIE += f"FIRST NAME : {PRO.first_name} \n"
        LILIE += f"LAST NAME : {PRO.last_name}\n"
        LILIE += f"YOU BOT : {PRO.bot} \n"
        LILIE += f"RESTRICTED : {PRO.restricted} \n"
        LILIE += f"USER ID : {boy}\n"
        LILIE += f"USERNAME : {PRO.username}\n"
        await event.answer(LILIE, alert=True)
    except Exception as e:
        await event.reply(f"{e}")


__command_list__ = ["myinfo"]
