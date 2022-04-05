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

        if int(tehran_h) == 13 and str(tehran_m) == "01":
            await bot.send_sticker("dastan_dogeGP","CAACAgQAAxkBAAEBAj5iTBMhC5XxQNFvkFhHN7mqqm5M4gACogwAArqnYVJUrfskZfzemCME")

        if int(tehran_h) == 14 and str(tehran_m) == "02":
            await bot.send_sticker("dastan_dogeGP","CAACAgQAAxkBAAEBAkZiTBPapCTz-LD55kNWKT9Vj2HHyQAC_wkAAs-jYVIYIFdL6JFqrSME")

        if int(tehran_h) == 15 and str(tehran_m) == "03":
            await bot.send_sticker("dastan_dogeGP","CAACAgQAAxkBAAEBAkpiTBSIciaHugnjz2AJ0TH-ZUdjPgACvQoAApkwYFKtCLZXJXRYRCME")

        if int(tehran_h) == 16 and str(tehran_m) == "04":
            await bot.send_sticker("dastan_dogeGP","CAACAgQAAxkBAAEBAk5iTBUlSgoDCb3x4VC0W5-porfY3QAC7Q8AAgphYFLvRwyahGutIyME")

        if int(tehran_h) == 17 and str(tehran_m) == "05":
            await bot.send_sticker("dastan_dogeGP", "CAACAgQAAxkBAAEBAlJiTBVE8qAXmm1FbvkeOoSimUhIYAAChQsAApvIaFJrJD4SktoNmSME")

        if int(tehran_h) == 18 and str(tehran_m) == "06":
            await bot.send_sticker("dastan_dogeGP", "CAACAgQAAxkBAAEBAlZiTBVVNL9dwdDRIIJt4R_a6rGjSQACkQoAAsRcYFK0zFbIPKOZQCME")

        if int(tehran_h) == 19 and str(tehran_m) == "07":
            await bot.send_sticker("dastan_dogeGP", "CAACAgQAAxkBAAEBAlpiTBVuKdzs4DCDmuwMK3-hwC0zRAACdAwAAqrYYFJCujH6Ba9fDCME")

        if int(tehran_h) == 20 and str(tehran_m) == "08":
            await bot.send_sticker("dastan_dogeGP", "CAACAgQAAxkBAAEBAl5iTBWMJwPlTj7Swnnm-oJAEctW8QACHAsAAnpkYVIvQ0NuLkrEICME")

        if int(tehran_h) == 21 and str(tehran_m) == "09":
            await bot.send_sticker("dastan_dogeGP", "CAACAgQAAxkBAAEBAmJiTBWtT2QriW-k-PQpQqu24s_MnwACGA0AApzGYVIDPUfuV4C4-SME")

        if int(tehran_h) == 22 and str(tehran_m) == "10":
            await bot.send_sticker("dastan_dogeGP", "CAACAgQAAxkBAAEBAmZiTBXJ5cnHqwu-8rV1QOG4QhcbnQACOQ0AAuRjYVJKjL6z4w8Z5yME")

        if int(tehran_h) == 23 and str(tehran_m) == "11":
            await bot.send_sticker("dastan_dogeGP", "CAACAgQAAxkBAAEBAmpiTBX8ayyOKnIX2DopXlTUbY0fkQACCwsAAmhUYVLZKgZRLsCpKyME")

bot.run()