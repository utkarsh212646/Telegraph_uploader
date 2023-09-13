from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

Tgraph = Client("Your_Telegram_API_ID", "Your_Telegram_API_HASH", bot_token="Your_Bot_Token")

@Tgraph.on_message(filters.command(["help"]))
async def help(client, message):
    buttons = [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('Our Channel', url='http://telegram.me/Thealphabotz')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await Tgraph.send_message(
        chat_id=message.chat.id,
        text="""There Is Nothing To Know More,
        
Just Send Me A Video/gif/photo Upto 5mb.

I'll upload it to telegra.ph and give you the direct link""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )

@Tgraph.on_callback_query()
async def button(Tgraph, update):
    cb_data = update.data
    if "help" in cb_data:
        await update.message.delete()
        await help(Tgraph, update.message)
    elif "close" in cb_data:
        await update.message.delete()
    elif "home" in cb_data:
        await update.message.delete()
        await home(Tgraph, update.message)

@Tgraph.on_message(filters.private & ~filters.channel)
async def start_message(client, message):
    # Send the start message with the image and force subscription
    await Tgraph.send_photo(
        chat_id=message.chat.id,
        photo="https://telegra.ph/file/e7bece928a05168a46322.jpg",
        caption="Welcome to the bot!\n\nPlease join our channel @thealphabotz to use the bot.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton('Join Channel', url='https://t.me/thealphabotz')]
        ]),
        reply_to_message_id=message.message_id
    )

Tgraph.run()
