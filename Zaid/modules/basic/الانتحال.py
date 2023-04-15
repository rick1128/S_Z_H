import os

from pyrogram import *
from pyrogram.types import *


from Zaid.helper.basic import edit_or_reply, get_text, get_user

from Zaid.modules.help import *

OWNER = os.environ.get("OWNER", None)
BIO = os.environ.get("BIO", "404 : Bio Lost")


@Client.on_message(filters.command("انتحال", ".") & filters.me)
async def clone(client: Client, message: Message):
    text = get_text(message)
    op = await message.edit_text("`جار الانتحال`")
    userk = get_user(message, text)[0]
    user_ = await client.get_users(userk)
    if not user_:
        await op.edit("`انتحل اي واحد؟:(`")
        return

    get_bio = await client.get_chat(user_.id)
    f_name = user_.first_name
    c_bio = get_bio.bio
    pic = user_.photo.big_file_id
    poto = await client.download_media(pic)

    await client.set_profile_photo(photo=poto)
    await client.update_profile(
        first_name=f_name,
        bio=c_bio,
    )
    await message.edit(f"**من الان انا** __{f_name}__")

#RICKTHON
@Client.on_message(filters.command("اعادة", ".") & filters.me)
async def revert(client: Client, message: Message):
    await message.edit("`جار الاعادة`")
    r_bio = BIO

    # Get ur Name back
    await client.update_profile(
        first_name=OWNER,
        bio=r_bio,
    )
    # Delte first photo to get ur identify
    photos = [p async for p in client.get_chat_photos("me")]
    await client.delete_profile_photos(photos[0].file_id)
    await message.edit("`تم الاعادة بنجاح!`")


add_command_help(
    "انتحال",
    [
        ["انتحال", "لانتحال شخص."],
        ["اعادة", "لاعادة حسابك لوضعة الطبيعي."],
    ],
)
