from os import remove
from re import findall

from pyrogram import Client, filters

from Zaid import SUDO_USER


_SCRTXT = """
**✅ تم إلغاء CC بنجاح!**

**سورس ->** {}
**كمية ->** {}
**تم تخطي ->** {}
**تم وجودCc ->** {}


🥷 **ألغيت بواسطة ->** {}
👨‍🎤 **المساعدة ->** @Rickthon_Group 🐲
"""


@Client.on_message(
    filters.command(["كشط"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def cc_scraper(c, m):
    txt = ""
    skp = 0
    spl = m.text.split(" ")
    e3 = await m.reply_text("...", quote=True)
    if not spl:
        return await e3.edit("الاوامر دي فاي كامل.. 😔")
    elif len(spl) == 2:
        _chat = spl[1].strip()
        limit = 100
    elif len(spl) > 2:
        _chat = spl[1].strip()
        try:
            limit = int(spl[2].strip())
        except ValueError:
            return await e3.edit("يجب أن يكون رقم البطاقة المراد كشطها عددًا صحيحًا!")

    await e3.edit(f"`Scrapping from {_chat}. \n اكبح جماح نفسك...`")
    _get = lambda m: getattr(m, "text", 0) or getattr(m, "caption", 0)
    _getcc = lambda m: list(filter(bool, findall("\d{16}\|\d{2,4}\|\d{2,4}\|\d{2,4}", m)))

    async for x in c.get_chat_history(_chat, limit=limit):
        if not (text := _get(x)):
            skp += 1
            continue
        if not (cc := _getcc(text)):
            skp += 1
        else:
            txt += "\n".join(cc) + "\n"

    cap = _SCRTXT.format(
        _chat,
        str(limit),
        str(skp),
        str(txt.count("\n")),
        m.from_user.mention,
    )
    file = f"x{limit} تم إلغاء CC بواسطة ZaidUB.txt"
    with open(file, "w+") as f:
        f.write(txt)
    del txt
    y = await c.send_document(
        m.chat.id,
        file,
        caption=cap,
        reply_to_message_id=m.id,
    )
    remove(file)
    await e3.delete()
