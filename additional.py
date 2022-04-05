from pyrogram import Client,filters
from pyrogram.types import Message

import time
import pytz
import datetime



api_id = 19504232
api_hash = "014607e14241d2da92b94b61a5e8d7ec"
bot = Client("addition",api_id,api_hash)
@bot.on_message()

async def atim(Client, m:Message):
    while True:
        tz_TH = pytz.timezone("Asia/Tehran")

        datetime_TH = datetime.datetime.now(tz_TH)
        tehran_h = datetime_TH.strftime("%H")
        tehran_m = datetime_TH.strftime("%M")
        print(tehran_m)
        if int(tehran_m)+int(tehran_h) == 0:
            await bot.send_sticker("dastan_dogeGP","CAACAgQAAxkBAAEBAAEKYkcbatBQXp7Ji5a4MusY7q30GsAAAvgJAAIWaDlS9B_G6Vsq1TUjBA")
            time.sleep(60)


bot.run()