

from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from pyrogram.errors import (
    PeerIdInvalid,
    UserNotParticipant
)
from bot import (
    AUTH_CHANNEL,
    SUB_CHANNEL,
    COMMM_AND_PRE_FIX,
    IS_BLACK_LIST_ED_MESSAGE_TEXT,
    START_COMMAND
)
from bot.bot import Bot
from bot.hf.flifi import uszkhvis_chats_ahndler
from bot.sql.users_sql import (
    add_user_to_db,
    get_chek_dmid
)
from bot.sql.blacklist_sql import (
    check_is_black_list
)


@Bot.on_message(
    ~filters.command(START_COMMAND, COMMM_AND_PRE_FIX) &
    ~uszkhvis_chats_ahndler([AUTH_CHANNEL]) &
    filters.incoming &
    filters.private
)
async def on_pm_s(client: Bot, message: Message):
    check_ban = check_is_black_list(message)
    if check_ban:
        await message.reply_text(
            text=IS_BLACK_LIST_ED_MESSAGE_TEXT.format(
                reason=check_ban.reason
            )
        )
        return
    if SUB_CHANNEL != -100:
      try:
        await client.get_chat_member(SUB_CHANNEL, message.from_user.id)
      except UserNotParticipant:
          chat = await client.get_chat(SUB_CHANNEL)
          username = f" [@{chat.username}] " if chat.username else ""
          return await message.reply_text(f"You Need to Join {chat.title}{username} in order to Use This Bot!.")
    fwded_mesg = None
    if message.edit_date:
        ym = get_chek_dmid(message.message_id)
        reply_to_message_id = None
        if ym:
            reply_to_message_id = ym.message_id
        await message.copy(
            chat_id=AUTH_CHANNEL,
            disable_notification=True,
            reply_to_message_id=reply_to_message_id,
            reply_markup=message.reply_markup
        )
    else:
        fwded_mesg = await message.forward(
            chat_id=AUTH_CHANNEL,
            disable_notification=True
        )

    if not fwded_mesg:
        return

    add_user_to_db(
        fwded_mesg.message_id,
        message.from_user.id,
        message.message_id,
        0,
        0
    )

