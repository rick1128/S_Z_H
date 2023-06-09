import asyncio
from html import escape

import aiohttp
from pyrogram import filters, Client 
from pyrogram.types import Message

from Zaid.modules.help import add_command_help
from pyrogram import enums

@Client.on_message(filters.command(["الطقس", "طقس"], ".") & filters.me)
async def get_weather(bot: Client, message: Message):
    if len(message.command) == 1:
        await message.edit("طريقة الاستعمال .الطقس + اسم مدينتك`")
        await asyncio.sleep(3)
        await message.delete()

    if len(message.command) > 1:
        location = message.command[1]
        headers = {"user-agent": "httpie"}
        url = f"https://wttr.in/{location}?mnTC0&lang=en"
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(url) as resp:
                    data = await resp.text()
        except Exception:
            await message.edit("فشل الحصول على توقعات الطقس")

        if "we processed more than 1M requests today" in data:
            await message.edit("`عذرا ، لا يمكننا معالجة هذا الطلب اليوم!`")
        else:
            weather = f"<code>{escape(data.replace('report', 'Report'))}</code>"
            await message.edit(weather, parse_mode=enums.ParseMode.MARKDOWN)


add_command_help(
    "الطقس",
    [
        [".الطقس", "يجلب لك معلومات الطقس في المدينة المحدده."],
    ],
)
