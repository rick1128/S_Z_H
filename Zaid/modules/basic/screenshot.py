import asyncio

from pyrogram import filters, Client 
from pyrogram.raw import functions
from pyrogram.types import Message


from Zaid.modules.help import add_command_help


@Client.on_message(
    filters.command(["سكرين شوت", "سك"], ".") & filters.private & filters.me
)
async def screenshot(bot: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        bot.send(
            functions.messages.SendScreenshotNotification(
                peer=await bot.resolve_peer(message.chat.id),
                reply_to_msg_id=0,
                random_id=bot.rnd_id(),
            )
        ),
    )


add_command_help(
    "سكرين شوت",
    [
        [
            ".سكرين شوت",
            "Send a notification in a private chat (not secret) to annoy or troll your friends.",
        ],
    ],
)
