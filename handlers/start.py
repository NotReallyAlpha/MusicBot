import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
Hey {message.from_user.mention()} !

        This is [{bn}](t.me/{bu}), Belongs to THE END network !

┏━━━━━━━━━━━━━━┓
┣★
┣★ ᴍᴀᴅᴇ ʙʏ: [THE END](t.me/THE_END_NETWORK)
┣★
┗━━━━━━━━━━━━━━┛

💞 If you having any queries regarding me, Try: (t.me/THE_END_MUSIC_SUPPORT)
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Try: add to your group !", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "✨ Owner ❤️", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "✨ Support 💜", url=f"https://t.me/THE_END_NETWORK"
                    )
                ],[
                    InlineKeyboardButton(
                        "🔎 Inline 🔎", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "✨ DEv 💫", url="t.me/Deveshi"
                    )]
            ]
       ),
    )

