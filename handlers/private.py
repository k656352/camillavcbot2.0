from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text("How Are You 🥰")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎀
ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ  ɢʀᴏᴜᴩ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ. 🇱🇰
ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ ᴀɴᴅ ᴘʟᴀʏ ᴍᴜsɪᴄ ғʀᴇᴇʟʏ 🤗 Developed By (https://t.me/tujan2) !**

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔨Nothing🔨", url="https://github.com/kidiloskahyper45")
                  ],[
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ Group 😉", url="https://t.me/ankimusicgroup"
                    ),
                    InlineKeyboardButton(
                        "ᴄʜᴀɴɴᴇʟ", url="https://t.me/Malayalam_Chatting_Links"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "➕ᴀᴅᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs➕", url="https://t.me/Wlaker95_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Yes iᴍ online 🇱🇰**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊Uᴩᴅᴀᴛᴇs", url="https://t.me/rosebakthan")
                ]
            ]
        )
   )
