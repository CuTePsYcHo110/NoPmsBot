


from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from pyrogram.errors.exceptions import UserIsBlocked
from bot import (
    AUTH_CHANNEL,
    BAN_COMMAND,
    BOT_WS_BLOCKED_BY_USER,
    COMMM_AND_PRE_FIX,
    DERP_USER_S_TEXT,
    START_COMMAND,
    UN_BAN_COMMAND
)
from bot.hf.fic import vhkzuoi_repliz_handler
from bot.hf.flifi import uszkhvis_chats_ahndler
from bot.hf.gfi import (
    get_file_id
)
from bot.sql.users_sql import (
    add_user_to_db,
    get_user_id
)


@Client.on_message(
    ~filters.command(START_COMMAND, COMMM_AND_PRE_FIX) &
    ~filters.command(BAN_COMMAND, COMMM_AND_PRE_FIX) &
    ~filters.command(UN_BAN_COMMAND, COMMM_AND_PRE_FIX) &
    uszkhvis_chats_ahndler([AUTH_CHANNEL]) &
    vhkzuoi_repliz_handler
)
async def on_pm_s(client: Client, message: Message):
    user_id, reply_message_id = get_user_id(
        message.reply_to_message.message_id
    )
    if not user_id:
        return
    try:
        s_m_ = await send_message_to_user(
            client,
            message,
            user_id,
            reply_message_id
        )
    except UserIsBlocked:
        await message.reply_text(BOT_WS_BLOCKED_BY_USER)
    else:
        if s_m_:
            add_user_to_db(
                reply_message_id,
                user_id,
                0,
                s_m_.message_id,
                message.message_id
            )


async def send_message_to_user(
    client: Client,
    message: Message,
    user_id: int,
    reply_message_id: int
):
    # 🥺 check two conditions 🤔🤔
    if message.media:
        _, file_id = get_file_id(message)
        caption = (
            message.caption and message.caption.html
        ) or ""
        return await client.send_cached_media(
            chat_id=user_id,
            file_id=file_id,
            caption=caption,
            reply_markup=message.reply_markup,
            disable_notification=True,
            reply_to_message_id=reply_message_id
        )
    else:
        caption = (
            message.text and message.text.html
        ) or DERP_USER_S_TEXT
        return await client.send_message(
            chat_id=user_id,
            text=caption,
            disable_web_page_preview=True,
            reply_markup=message.reply_markup,
            disable_notification=True,
            reply_to_message_id=reply_message_id
        )
