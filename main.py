from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
import random

HKZ = Client(
    name="HollywoodMalayalamMovieBot",
    api_id= "25988816",
    api_hash= "7ad4c2b1e5556277d341477b0776b2de",
    bot_token= "7788724835:AAFgateQxHSVuVijaetiV4FaTDJ9dFrsP9g"
)

PICS = [
 "http://ibb.co/tmwS2Gx"
]

@HKZ.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=f"""𝖧𝖾𝗒 𝗍𝗁𝖾𝗋𝖾 (message.from_user.mention),

𝖨 𝖺𝗆 [𝖤𝗅𝗂𝗓𝖺𝖻𝖾𝗍𝗁 𝖮𝗅𝗌𝖾𝗇](t.me/HollywoodMalayalamMovieBot), 𝖨 𝖼𝖺𝗇 𝗌𝗁𝖺𝗋𝖾 𝗒𝗈𝗎 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆 𝖣𝗎𝖻𝖻𝖾𝖽 𝖧𝗈𝗅𝗅𝗒𝗐𝗈𝗈𝖽 𝖬𝗈𝗏𝗂𝖾𝗌. 𝖩𝗎𝗌𝗍 𝖲𝖾𝗇𝖽 𝖬𝖾 𝗍𝗁𝖾 𝖬𝗈𝗏𝗂𝖾 𝖭𝖺𝗆𝖾 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍.

𝖥𝗈𝗋 𝗆𝗈𝗋𝖾 𝗁𝗂𝗍 /𝗁𝖾𝗅𝗉..!""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("𝖬𝗈𝗏𝗂𝖾𝗌 𝖫𝗂𝗌𝗍", callback_data="List")
            ]]
            )
        )

@HKZ.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=f"""𝖧𝖾𝗒 (message.from_user.mention),

𝖳𝗁𝗂𝗌 𝗂𝗌 𝗆𝗒 𝗁𝖾𝗅𝗉 𝗉𝖺𝗇𝖾𝗅...!
➖➖➖➖➖➖➖➖➖➖

𝖩𝗎𝗌𝗍 𝖲𝖾𝗇𝖽 𝖬𝖾 𝗍𝗁𝖾 𝖬𝗈𝗏𝗂𝖾 𝖭𝖺𝗆𝖾 𝖺𝗇𝖽 𝖸𝖾𝖺𝗋 𝖢𝗈𝗋𝗋𝖾𝖼𝗍𝗅𝗒.

𝖤𝗀:- 𝖨𝖼𝖾 𝖠𝗀𝖾 2002

𝖨𝗇𝗌𝗍𝗋𝗎𝖼𝗍𝗂𝗈𝗇𝗌
➖➖➖➖➖➖➖➖➖➖

𝖶𝗁𝖾𝗇 𝗒𝗈𝗎 𝗐𝗂𝗅𝗅 𝗋𝖾𝗊𝗎𝖾𝗌𝗍 𝗍𝗁𝖾 𝖬𝗈𝗏𝗂𝖾 𝖸𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝗅𝗈𝗀𝗂𝗇 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖯𝗁𝗈𝗇𝖾 𝖭𝗎𝗆𝖻𝖾𝗋.

𝖳𝗁𝖾𝗇 𝖸𝗈𝗎 𝗐𝗂𝗅𝗅 𝖱𝖾𝖼𝖾𝗂𝗏𝖾 𝖺 𝖢𝗈𝖽𝖾 𝖿𝗋𝗈𝗆 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆, 𝖩𝗎𝗌𝗍 𝖲𝖾𝗇𝖽 𝗍𝗁𝖾 𝖢𝗈𝖽𝖾 𝗍𝗈 𝖬𝖾.

𝖠𝖿𝗍𝖾𝗋 𝖫𝗈𝗀𝗂𝗇 𝖳𝗁𝖾 𝖬𝗈𝗏𝗂𝖾 𝖥𝗂𝗅𝖾 𝗐𝗂𝗅𝗅 𝖻𝖾 𝗎𝗉𝗅𝗈𝖺𝖽 𝗂𝗇 𝗒𝗈𝗎𝗋 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖲𝖺𝗏𝖾𝖽 𝖬𝖾𝗌𝗌𝖺𝗀𝖾𝗌.

𝖨𝖿 𝗒𝗈𝗎 𝖽𝗂𝖽𝗇'𝗍 𝗀𝗈𝗍 𝗍𝗁𝖾 𝖬𝗈𝗏𝗂𝖾, 𝖯𝗅𝖾𝖺𝗌𝖾 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖠𝗀𝖺𝗂𝗇.""",
          reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("𝖬𝗈𝗏𝗂𝖾𝗌 𝖫𝗂𝗌𝗍", callback_data="List")
            ]]
            )
        )
