from pyrogram import Client, filters
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
 "https://files.catbox.moe/0lpzv8.jpg"
]

@HKZ.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=f"""𝖧𝖾𝗒 𝗍𝗁𝖾𝗋𝖾 {message.from_user.mention},

```𝖨 𝖺𝗆 [𝖤𝗅𝗂𝗓𝖺𝖻𝖾𝗍𝗁 𝖮𝗅𝗌𝖾𝗇](t.me/HollywoodMalayalamMovieBot), 𝖨 𝖼𝖺𝗇 𝗌𝗁𝖺𝗋𝖾 𝗒𝗈𝗎 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆 𝖣𝗎𝖻𝖻𝖾𝖽 𝖧𝗈𝗅𝗅𝗒𝗐𝗈𝗈𝖽 𝖬𝗈𝗏𝗂𝖾𝗌. 𝖩𝗎𝗌𝗍 𝖲𝖾𝗇𝖽 𝖬𝖾 𝗍𝗁𝖾 𝖬𝗈𝗏𝗂𝖾 𝖭𝖺𝗆𝖾 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍.

𝖥𝗈𝗋 𝗆𝗈𝗋𝖾 𝗁𝗂𝗍 /𝗁𝖾𝗅𝗉..!```""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("𝖬𝗈𝗏𝗂𝖾𝗌 𝖫𝗂𝗌𝗍", callback_data="List")
            ]]
            )
        )

@HKZ.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_text(
        text=f"""𝖧𝖾𝗒 {message.from_user.mention},

𝖳𝗁𝗂𝗌 𝗂𝗌 𝗆𝗒 𝗁𝖾𝗅𝗉 𝗉𝖺𝗇𝖾𝗅...!
➖➖➖➖➖➖➖➖➖➖

𝖩𝗎𝗌𝗍 𝖲𝖾𝗇𝖽 𝖬𝖾 𝗍𝗁𝖾 𝖬𝗈𝗏𝗂𝖾 𝖭𝖺𝗆𝖾 𝖺𝗇𝖽 𝖸𝖾𝖺𝗋 𝖢𝗈𝗋𝗋𝖾𝖼𝗍𝗅𝗒.

𝖤𝗀:- 𝖨𝖼𝖾 𝖠𝗀𝖾 2002

𝖨𝗇𝗌𝗍𝗋𝗎𝖼𝗍𝗂𝗈𝗇𝗌
➖➖➖➖➖➖➖➖➖➖

𝖶𝗁𝖾𝗇 𝗒𝗈𝗎 𝗐𝗂𝗅𝗅 𝗋𝖾𝗊𝗎𝖾𝗌𝗍 𝗍𝗁𝖾 𝖬𝗈𝗏𝗂𝖾 𝖸𝗈𝗎 𝗐𝖺𝗇𝗍 𝗍𝗈 𝗅𝗈𝗀𝗂𝗇 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖯𝗁𝗈𝗇𝖾 𝖭𝗎𝗆𝖻𝖾𝗋.

𝖳𝗁𝖾𝗇 𝖸𝗈𝗎 𝗐𝗂𝗅𝗅 𝖱𝖾𝖼𝖾𝗂𝗏𝖾 𝖺 𝖢𝗈𝖽𝖾 𝖿𝗋𝗈𝗆 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆, 𝖩𝗎𝗌𝗍 𝖲𝖾𝗇𝖽 𝗍𝗁𝖾 𝖢𝗈𝖽𝖾 𝗍𝗈 𝖬𝖾.

𝖠𝖿𝗍𝖾𝗋 𝖫𝗈𝗀𝗂𝗇 𝖳𝗁𝖾 𝖬𝗈𝗏𝗂𝖾 𝖥𝗂𝗅𝖾 𝗐𝗂𝗅𝗅 𝖻𝖾 𝗎𝗉𝗅𝗈𝖺𝖽 𝗂𝗇 𝗒𝗈𝗎𝗋 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖲𝖺𝗏𝖾𝖽 𝖬𝖾𝗌𝗌𝖺𝗀𝖾𝗌.

𝖨𝖿 𝗒𝗈𝗎 𝖽𝗂𝖽𝗇'𝗍 𝗀𝗈𝗍 𝗍𝗁𝖾 𝖬𝗈𝗏𝗂𝖾, 𝖯𝗅𝖾𝖺𝗌𝖾 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖠𝗀𝖺𝗂𝗇.

𝖭𝗈𝗍𝖾:- 𝖸𝗈𝗎 𝖼𝖺𝗇 𝗈𝗇𝗅𝗒 𝗋𝖾𝗊𝗎𝖾𝗌𝗍 2 𝖬𝗈𝗏𝗂𝖾𝗌 𝗂𝗇 𝖺 𝗐𝖾𝖾𝗄..!""",
          reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("𝖬𝗈𝗏𝗂𝖾𝗌 𝖫𝗂𝗌𝗍", callback_data="List")
            ]]
            )
        )

@HKZ.on_message(filters.command("list"))
async def list_cmd(client, message):
    await message.reply_photo(
        photo="""𝖧𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖫𝗂𝗌𝗍 𝗈𝖿 𝖬𝗈𝗏𝗂𝖾𝗌 𝖨 𝗁𝖺𝗏𝖾..!
➖➖➖➖➖➖➖➖➖➖

300
2012
𝖠𝗀𝖾𝗇𝗍 𝖢𝗈𝖽𝗒 𝖡𝖺𝗇𝗄𝗌
𝖠𝗏𝖾𝗇𝗀𝖾𝗋𝗌 𝖨𝗇𝖿𝗂𝗇𝗂𝗍𝗒 𝖶𝖺𝗋
𝖠𝗇𝖺𝖼𝗈𝗇𝖽𝖺
𝖠𝗇𝖺𝖼𝗈𝗇𝖽𝖺𝗌: 𝖳𝗁𝖾 𝖧𝗎𝗇𝗍 𝖿𝗈𝗋 𝗍𝗁𝖾 𝖡𝗅𝗈𝗈𝖽 𝖮𝗋𝖼𝗁𝗂𝖽 𝖠𝗇𝖺𝖼𝗈𝗇𝖽𝖺𝗌: 𝖳𝗋𝖺𝗂𝗅 𝗈𝖿 𝖡𝗅𝗈𝗈𝖽
𝖡𝖾𝗇-𝖧𝗎𝗋 (1959)
𝖡𝖾𝗇-𝖧𝗎𝗋 2016
𝖡𝗅𝖺𝖼𝗄 𝖶𝗂𝖽𝗈𝗐
𝖢𝖺𝗉𝗍𝖺𝗂𝗇 𝖯𝗁𝗂𝗅𝗅𝗂𝗉𝗌
𝖢𝖹12 𝖢𝗁𝗂𝗇𝖾𝗌𝖾 𝖹𝗈𝖽𝗂𝖺𝖼
𝖣𝗂𝖾 𝖠𝗇𝗈𝗍𝗁𝖾𝗋 𝖣𝖺𝗒
𝖣𝗂𝖾 𝖧𝖺𝗋𝖽
𝖣𝗃𝖺𝗇𝗀𝗈 𝖴𝗇𝖼𝗁𝖺𝗂𝗇𝖾𝖽
𝖣𝗈𝖼𝗍𝗈𝗋 𝖲𝗍𝗋𝖺𝗇𝗀𝖾 𝗂𝗇 𝗍𝗁𝖾 𝖬𝗎𝗅𝗍𝗂𝗏𝖾𝗋𝗌𝖾 𝗈𝖿 𝖬𝖺𝖽𝗇𝖾𝗌𝗌
𝖤𝗑𝗈𝖽𝗎𝗌 𝖦𝗈𝖽𝗌 𝖺𝗇𝖽 𝖪𝗂𝗇𝗀𝗌
𝖥𝖺𝗇𝗍𝖺𝗌𝗍𝗂𝖼 𝖥𝗈𝗎𝗋
𝖦𝗈𝖽𝗓𝗂𝗅𝗅𝖺
𝖦𝗁𝗈𝗌𝗍 𝖱𝗂𝖽𝖾𝗋
𝖦𝗈𝗋𝗀𝖾𝗈𝗎𝗌
𝖧𝗈𝗅𝗅𝗈𝗐 𝖬𝖺𝗇
𝖧𝗈𝗆𝖾 𝖠𝗅𝗈𝗇𝖾 2: 𝖫𝗈𝗌𝗍 𝗂𝗇 𝖭𝖾𝗐 𝖸𝗈𝗋𝗄
𝖧𝗈𝗍𝖾𝗅 𝖳𝗋𝖺𝗇𝗌𝗒𝗅𝗏𝖺𝗇𝗂𝖺
𝖨𝖼𝖾 𝖠𝗀𝖾
𝖩𝖺𝖼𝗄 𝗍𝗁𝖾 𝖦𝗂𝖺𝗇𝗍 𝖲𝗅𝖺𝗒𝖾𝗋
𝖩𝗎𝗆𝖺𝗇𝗃𝗂
𝖩𝗎𝗆𝖺𝗇𝗃𝗂: 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝗍𝗁𝖾 𝖩𝗎𝗇𝗀𝗅𝖾
𝖩𝗎𝗆𝖺𝗇𝗃𝗂: 𝖳𝗁𝖾 𝖭𝖾𝗑𝗍 𝖫𝖾𝗏𝖾𝗅 
𝖩𝗎𝗋𝖺𝗌𝗌𝗂𝖼 𝖯𝖺𝗋𝗄
𝖩𝗎𝗋𝖺𝗌𝗌𝗂𝖼 𝖶𝗈𝗋𝗅𝖽 𝖣𝗈𝗆𝗂𝗇𝗂𝗈𝗇
𝖪𝗂𝗇𝗀 𝖪𝗈𝗇𝗀
𝖬𝖺𝗇 𝗈𝖿 𝖲𝗍𝖾𝖾𝗅
𝖬𝖾𝗇 𝗂𝗇 𝖡𝗅𝖺𝖼𝗄
𝖬𝖾𝗇 𝗂𝗇 𝖡𝗅𝖺𝖼𝗄 2
𝖬𝖾𝗇 𝗂𝗇 𝖡𝗅𝖺𝖼𝗄 𝖨𝗇𝗍𝖾𝗋𝗇𝖺𝗍𝗂𝗈𝗇𝖺𝗅
𝖬𝗈𝗇𝗌𝗍𝖾𝗋 𝖧𝗈𝗎𝗌𝖾
𝖭𝗂𝗀𝗁𝗍 𝖺𝗍 𝗍𝗁𝖾 𝖬𝗎𝗌𝖾𝗎𝗆
𝖯𝖺𝖼𝗂𝖿𝗂𝖼 𝖱𝗂𝗆
𝖯𝖺𝗌𝗌𝗂𝗈𝗇 𝗈𝖿 𝗍𝗁𝖾 𝖢𝗁𝗋𝗂𝗌𝗍
𝖲𝗉𝗂𝖽𝖾𝗋-𝖬𝖺𝗇
𝖲𝗉𝗂𝖽𝖾𝗋-𝖬𝖺𝗇 2
𝖲𝗉𝗂𝖽𝖾𝗋-𝖬𝖺𝗇 3
𝖲𝗉𝗂𝖽𝖾𝗋-𝖬𝖺𝗇: 𝖧𝗈𝗆𝖾𝖼𝗈𝗆𝗂𝗇𝗀
𝖲𝗉𝗂𝖽𝖾𝗋-𝖬𝖺𝗇: 𝖥𝖺𝗋 𝖥𝗋𝗈𝗆 𝖧𝗈𝗆𝖾
𝖲𝗉𝗂𝖽𝖾𝗋-𝖬𝖺𝗇: 𝖭𝗈 𝖶𝖺𝗒 𝖧𝗈𝗆𝖾
𝖲𝗍𝗎𝖺𝗋𝗍 𝖫𝗂𝗍𝗍𝗅𝖾 2
𝖲𝗍𝗎𝖺𝗋𝗍 𝖫𝗂𝗍𝗍𝗅𝖾 3: 𝖢𝖺𝗅𝗅 𝗈𝖿 𝗍𝗁𝖾 𝖶𝗂𝗅𝖽
𝖳𝗁𝖾 𝖠𝖽𝗏𝖾𝗇𝗍𝗎𝗋𝖾𝗌 𝗈𝖿 𝖳𝗂𝗇𝗍𝗂𝗇: 𝖳𝗁𝖾 𝖲𝖾𝖼𝗋𝖾𝗍 𝗈𝖿 𝗍𝗁𝖾 𝖴𝗇𝗂𝖼𝗈𝗋𝗇
𝖳𝗁𝖾 𝖠𝗆𝖺𝗓𝗂𝗇𝗀 𝖲𝗉𝗂𝖽𝖾𝗋-𝖬𝖺𝗇
𝖳𝗁𝖾 𝖠𝗆𝖺𝗓𝗂𝗇𝗀 𝖲𝗉𝗂𝖽𝖾𝗋-𝖬𝖺𝗇 2
𝖳𝗁𝖾 𝖠𝗇𝗀𝗋𝗒 𝖡𝗂𝗋𝖽𝗌
𝖳𝗁𝖾 𝖠𝗇𝗀𝗋𝗒 𝖡𝗂𝗋𝖽𝗌 2
𝖳𝗁𝖾 𝖢𝗈𝗇𝗃𝗎𝗋𝗂𝗇𝗀
𝖳𝗁𝖾 𝖣𝖺 𝖵𝗂𝗇𝖼𝗂 𝖢𝗈𝖽𝖾
𝖳𝗁𝖾 𝖧𝖺𝗇𝗀𝗈𝗏𝖾𝗋
𝖳𝗁𝖾 𝖨𝗇𝖼𝗋𝖾𝖽𝗂𝖻𝗅𝖾 𝖧𝗎𝗅𝗄
𝖳𝗁𝖾 𝖬𝖺𝗍𝗋𝗂𝗑
𝖳𝗁𝖾 𝖬𝗎𝗆𝗆𝗒 𝖱𝖾𝖻𝗂𝗋𝗍𝗁
𝖳𝗁𝖾 𝖲𝗆𝗎𝗋𝖿𝗌
𝖳𝗁𝖾 𝖲𝗆𝗎𝗋𝖿𝗌 2
𝖳𝗂𝗍𝖺𝗇𝗂𝖼
𝖴𝗇𝖼𝗁𝖺𝗋𝗍𝖾𝖽
𝖵𝖺𝗇 𝖧𝖾𝗅𝗌𝗂𝗇𝗀
𝖵𝖾𝗇𝗈𝗆
𝖵𝖾𝗇𝗈𝗆: 𝖫𝖾𝗍 𝗍𝗁𝖾𝗋𝖾 𝖻𝖾 𝖢𝖺𝗋𝗇𝖺𝗀𝖾

𝖭𝗈𝗍𝖾:- 𝖸𝗈𝗎 𝖼𝖺𝗇 𝗈𝗇𝗅𝗒 𝗋𝖾𝗊𝗎𝖾𝗌𝗍 2 𝖬𝗈𝗏𝗂𝖾𝗌 𝗂𝗇 𝖺 𝗐𝖾𝖾𝗄..!"""
    )


@HKZ.on_callback_query()
async def callback(bot, msg):

    if msg.data == "list":
        await msg.message.edit_text("""𝖧𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖫𝗂𝗌𝗍 𝗈𝖿 𝖬𝗈𝗏𝗂𝖾𝗌 𝖨 𝗁𝖺𝗏𝖾..!
➖➖➖➖➖➖➖➖➖➖

300
2012
𝖠𝗀𝖾𝗇𝗍 𝖢𝗈𝖽𝗒 𝖡𝖺𝗇𝗄𝗌
𝖠𝗏𝖾𝗇𝗀𝖾𝗋𝗌 𝖨𝗇𝖿𝗂𝗇𝗂𝗍𝗒 𝖶𝖺𝗋
𝖠𝗇𝖺𝖼𝗈𝗇𝖽𝖺
𝖠𝗇𝖺𝖼𝗈𝗇𝖽𝖺𝗌: 𝖳𝗁𝖾 𝖧𝗎𝗇𝗍 𝖿𝗈𝗋 𝗍𝗁𝖾 𝖡𝗅𝗈𝗈𝖽 𝖮𝗋𝖼𝗁𝗂𝖽 𝖠𝗇𝖺𝖼𝗈𝗇𝖽𝖺𝗌: 𝖳𝗋𝖺𝗂𝗅 𝗈𝖿 𝖡𝗅𝗈𝗈𝖽
𝖡𝖾𝗇-𝖧𝗎𝗋 (1959)
𝖡𝖾𝗇-𝖧𝗎𝗋 2016
𝖡𝗅𝖺𝖼𝗄 𝖶𝗂𝖽𝗈𝗐
𝖢𝖺𝗉𝗍𝖺𝗂𝗇 𝖯𝗁𝗂𝗅𝗅𝗂𝗉𝗌
𝖢𝖹12 𝖢𝗁𝗂𝗇𝖾𝗌𝖾 𝖹𝗈𝖽𝗂𝖺𝖼
𝖣𝗂𝖾 𝖠𝗇𝗈𝗍𝗁𝖾𝗋 𝖣𝖺𝗒
𝖣𝗂𝖾 𝖧𝖺𝗋𝖽
𝖣𝗃𝖺𝗇𝗀𝗈 𝖴𝗇𝖼𝗁𝖺𝗂𝗇𝖾𝖽
𝖣𝗈𝖼𝗍𝗈𝗋 𝖲𝗍𝗋𝖺𝗇𝗀𝖾 𝗂𝗇 𝗍𝗁𝖾 𝖬𝗎𝗅𝗍𝗂𝗏𝖾𝗋𝗌𝖾 𝗈𝖿 𝖬𝖺𝖽𝗇𝖾𝗌𝗌
𝖤𝗑𝗈𝖽𝗎𝗌 𝖦𝗈𝖽𝗌 𝖺𝗇𝖽 𝖪𝗂𝗇𝗀𝗌
𝖥𝖺𝗇𝗍𝖺𝗌𝗍𝗂𝖼 𝖥𝗈𝗎𝗋
𝖦𝗈𝖽𝗓𝗂𝗅𝗅𝖺
𝖦𝗁𝗈𝗌𝗍 𝖱𝗂𝖽𝖾𝗋
𝖦𝗈𝗋𝗀𝖾𝗈𝗎𝗌
𝖧𝗈𝗅𝗅𝗈𝗐 𝖬𝖺𝗇
𝖧𝗈𝗆𝖾 𝖠𝗅𝗈𝗇𝖾 2: 𝖫𝗈𝗌𝗍 𝗂𝗇 𝖭𝖾𝗐 𝖸𝗈𝗋𝗄
𝖧𝗈𝗍𝖾𝗅 𝖳𝗋𝖺𝗇𝗌𝗒𝗅𝗏𝖺𝗇𝗂𝖺
𝖨𝖼𝖾 𝖠𝗀𝖾
𝖩𝖺𝖼𝗄 𝗍𝗁𝖾 𝖦𝗂𝖺𝗇𝗍 𝖲𝗅𝖺𝗒𝖾𝗋
𝖩𝗎𝗆𝖺𝗇𝗃𝗂
𝖩𝗎𝗆𝖺𝗇𝗃𝗂: 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝗍𝗁𝖾 𝖩𝗎𝗇𝗀𝗅𝖾
𝖩𝗎𝗆𝖺𝗇𝗃𝗂: 𝖳𝗁𝖾 𝖭𝖾𝗑𝗍 𝖫𝖾𝗏𝖾𝗅 
𝖩𝗎𝗋𝖺𝗌𝗌𝗂𝖼 𝖯𝖺𝗋𝗄
𝖩𝗎𝗋𝖺𝗌𝗌𝗂𝖼 𝖶𝗈𝗋𝗅𝖽 𝖣𝗈𝗆𝗂𝗇𝗂𝗈𝗇
𝖪𝗂𝗇𝗀 𝖪𝗈𝗇𝗀
𝖬𝖺𝗇 𝗈𝖿 𝖲𝗍𝖾𝖾𝗅
𝖬𝖾𝗇 𝗂𝗇 𝖡𝗅𝖺𝖼𝗄
𝖬𝖾𝗇 𝗂𝗇 𝖡𝗅𝖺𝖼𝗄 2
𝖬𝖾𝗇 𝗂𝗇 𝖡𝗅𝖺𝖼𝗄 𝖨𝗇𝗍𝖾𝗋𝗇𝖺𝗍𝗂𝗈𝗇𝖺𝗅
𝖬𝗈𝗇𝗌𝗍𝖾𝗋 𝖧𝗈𝗎𝗌𝖾
𝖭𝗂𝗀𝗁𝗍 𝖺𝗍 𝗍𝗁𝖾 𝖬𝗎𝗌𝖾𝗎𝗆
𝖯𝖺𝖼𝗂𝖿𝗂𝖼 𝖱𝗂𝗆
𝖯𝖺𝗌𝗌𝗂𝗈𝗇 𝗈𝖿 𝗍𝗁𝖾 𝖢𝗁𝗋𝗂𝗌𝗍
𝖲𝗉𝗂𝖽𝖾𝗋-𝖬𝖺𝗇
𝖲𝗉𝗂𝖽𝖾𝗋-𝖬𝖺𝗇 2
𝖲𝗉𝗂𝖽𝖾𝗋-𝖬𝖺𝗇 3
𝖲𝗉𝗂𝖽𝖾𝗋-𝖬𝖺𝗇: 𝖧𝗈𝗆𝖾𝖼𝗈𝗆𝗂𝗇𝗀
𝖲𝗉𝗂𝖽𝖾𝗋-𝖬𝖺𝗇: 𝖥𝖺𝗋 𝖥𝗋𝗈𝗆 𝖧𝗈𝗆𝖾
𝖲𝗉𝗂𝖽𝖾𝗋-𝖬𝖺𝗇: 𝖭𝗈 𝖶𝖺𝗒 𝖧𝗈𝗆𝖾
𝖲𝗍𝗎𝖺𝗋𝗍 𝖫𝗂𝗍𝗍𝗅𝖾 2
𝖲𝗍𝗎𝖺𝗋𝗍 𝖫𝗂𝗍𝗍𝗅𝖾 3: 𝖢𝖺𝗅𝗅 𝗈𝖿 𝗍𝗁𝖾 𝖶𝗂𝗅𝖽
𝖳𝗁𝖾 𝖠𝖽𝗏𝖾𝗇𝗍𝗎𝗋𝖾𝗌 𝗈𝖿 𝖳𝗂𝗇𝗍𝗂𝗇: 𝖳𝗁𝖾 𝖲𝖾𝖼𝗋𝖾𝗍 𝗈𝖿 𝗍𝗁𝖾 𝖴𝗇𝗂𝖼𝗈𝗋𝗇
𝖳𝗁𝖾 𝖠𝗆𝖺𝗓𝗂𝗇𝗀 𝖲𝗉𝗂𝖽𝖾𝗋-𝖬𝖺𝗇
𝖳𝗁𝖾 𝖠𝗆𝖺𝗓𝗂𝗇𝗀 𝖲𝗉𝗂𝖽𝖾𝗋-𝖬𝖺𝗇 2
𝖳𝗁𝖾 𝖠𝗇𝗀𝗋𝗒 𝖡𝗂𝗋𝖽𝗌
𝖳𝗁𝖾 𝖠𝗇𝗀𝗋𝗒 𝖡𝗂𝗋𝖽𝗌 2
𝖳𝗁𝖾 𝖢𝗈𝗇𝗃𝗎𝗋𝗂𝗇𝗀
𝖳𝗁𝖾 𝖣𝖺 𝖵𝗂𝗇𝖼𝗂 𝖢𝗈𝖽𝖾
𝖳𝗁𝖾 𝖧𝖺𝗇𝗀𝗈𝗏𝖾𝗋
𝖳𝗁𝖾 𝖨𝗇𝖼𝗋𝖾𝖽𝗂𝖻𝗅𝖾 𝖧𝗎𝗅𝗄
𝖳𝗁𝖾 𝖬𝖺𝗍𝗋𝗂𝗑
𝖳𝗁𝖾 𝖬𝗎𝗆𝗆𝗒 𝖱𝖾𝖻𝗂𝗋𝗍𝗁
𝖳𝗁𝖾 𝖲𝗆𝗎𝗋𝖿𝗌
𝖳𝗁𝖾 𝖲𝗆𝗎𝗋𝖿𝗌 2
𝖳𝗂𝗍𝖺𝗇𝗂𝖼
𝖴𝗇𝖼𝗁𝖺𝗋𝗍𝖾𝖽
𝖵𝖺𝗇 𝖧𝖾𝗅𝗌𝗂𝗇𝗀
𝖵𝖾𝗇𝗈𝗆
𝖵𝖾𝗇𝗈𝗆: 𝖫𝖾𝗍 𝗍𝗁𝖾𝗋𝖾 𝖻𝖾 𝖢𝖺𝗋𝗇𝖺𝗀𝖾

𝖭𝗈𝗍𝖾:- 𝖸𝗈𝗎 𝖼𝖺𝗇 𝗈𝗇𝗅𝗒 𝗋𝖾𝗊𝗎𝖾𝗌𝗍 2 𝖬𝗈𝗏𝗂𝖾𝗌 𝗂𝗇 𝖺 𝗐𝖾𝖾𝗄..!"""
        )
    elif msg.data == "mission":
        await msg.message.edit_text("""𝖳𝗁𝗂𝗌 𝗂𝗌 𝗍𝗁𝖾 𝗉𝗋𝗈𝖼𝖾𝗌𝗌 𝗍𝗈 𝗅𝗈𝗀𝗂𝗇 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖺𝖼𝖼𝗈𝗎𝗇𝗍. 𝖨 𝖺𝗆 𝗅𝗈𝗀𝗂𝗇 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖺𝖼𝖼𝗈𝗎𝗇𝗍 𝗍𝗈 𝗎𝗉𝗅𝗈𝖺𝖽 𝗍𝗁𝖾 𝖿𝗂𝗅𝖾 𝗂𝗇 𝗒𝗈𝗎𝗋 𝖲𝖺𝗏𝖾𝖽 𝖬𝖾𝗌𝗌𝖺𝗀𝖾𝗌

𝖤𝗇𝗍𝖾𝗋 𝗍𝗁𝖾 𝗉𝗁𝗈𝗇𝖾 𝗇𝗎𝗆𝖻𝖾𝗋, 𝖺𝗅𝗈𝗇𝗀 𝗐𝗂𝗍𝗁 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝖼𝗈𝖽𝖾. 𝖤𝗑𝖺𝗆𝗉𝗅𝖾: +91876543210"""
        )


@HKZ.on_message(filters.text)
async def titanic_txt(client, message):
    await message.reply(
        text=f"<b>Here is What I Found for Your Query #{message.text}</b>..!",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(f"<b>{message.text}</b> Malayalam Dubbed Full Movie @HollywoodMalayalamMovieBot.mkv</b>", callback_data="mission")
            ]]
            )
        )

@HKZ.on_message(filters.text)
async def robbhood_txt(client, message):
    await message.reply(
        text=f"<b>Here is What I Found for Your Query #{message.text}</b>..!",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(f"<b>{message.text} Malayalam Dubbed Full Movie @HollywoodMalayalamMovieBot.mkv</b>", callback_data="mission")
            ]]
            )
        )

@HKZ.on_message(filters.text)
async def natm_txt(client, message):
    await message.reply(
        text=f"<b>Here is What I Found for Your Query #{message.text}</b>..!",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(f"<b>{message.text} Malayalam Dubbed Full Movie @HollywoodMalayalamMovieBot.mkv</b>", callback_data="mission")
            ]]
            )
        )
    

@HKZ.on_message(filters.text)
async def iceage_txt(client, message):
    await message.reply(
        text=f"<b>Here is What I Found for Your Query #{message.text}</b>..!",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(f"<b>{message.text} Malayalam Dubbed Full Movie @HollywoodMalayalamMovieBot.mkv</b>", callback_data="mission")
            ]]
            )
        )


print("Bot Started..!")

HKZ.run()


                              

