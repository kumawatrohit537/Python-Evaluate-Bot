# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import os
from io import BytesIO
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

FayasNoushad = Client(
    "Python-Evaluate-Bot",
    bot_token = os.environ["1634306566:AAFvCRV-KJOmPsJjHif27XLsGZK3M_QxHkg"],
    api_id = int(os.environ["6679335"]),
    api_hash = os.environ["f950d009ad64dda30c58c5c92004dd58"]
)

START_TEXT = """
Hello {}
I am a python evaluate telegram bot.

> `I can evaluate python code`

Made by @Thanos_Powerr
"""

BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚙ Join Updates Channel ⚙', url='https://telegram.me/BOTS4U_AND_LOOTS4U')
        ]]
    )

@FayasNoushad.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )

def evaluate(text, is_round=False):
    if is_round:
        return round(eval(text))
    else:
        return float(eval(text))

@FayasNoushad.on_message(
    filters.private &
    filters.reply &
    filters.command(["eval", "evaluate", "run"])
)
async def evaluation(bot, update):
    output = evaluate(update.reply_to_message.text)
    try:
        if len(output) < 4096:
            await update.reply_text(
                text=output,
                reply_markup=BUTTONS,
                disable_web_page_preview=True,
                quote=True
            )
        else:
            with BytesIO(str.encode(str(output))) as output_file:
                output_file.name = "output.txt"
                await update.reply_document(
                    document=output_file,
                    caption="Made by @Thanos_Powerr",
                    reply_markup=BUTTONS,
                    quote=True
                )
    except Exception as error:
        await update.reply_text(
            text=error,
            reply_markup=BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )

FayasNoushad.run()
