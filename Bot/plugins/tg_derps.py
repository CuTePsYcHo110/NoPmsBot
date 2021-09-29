


from pyrogram.types import (
    CallbackQuery,
    Message
)
from typing import List
from bot import (
    AUTH_CHANNEL,
    DELETED_MESSAGES_NOTIFICATION_TEXT,
    DERP_USER_S_TEXT
)
from bot.bot import Bot
from bot.sql.users_sql import (
    get_chek_dmid,
    get_chek_mdid
)


@Bot.on_deleted_messages()
async def on_del_mesgs(client: Bot, messages: List[Message]):
    for message in messages:
        if message.chat is not None:
            kopp = get_chek_mdid(message.message_id)
            if kopp:
                await client.delete_messages(
                    chat_id=int(kopp.chat_id),
                    message_ids=kopp.mu_id,
                    revoke=True
                )
        else:
            ym = get_chek_dmid(message.message_id)
            if ym:
                await client.send_message(
                    chat_id=AUTH_CHANNEL,
                    text=DELETED_MESSAGES_NOTIFICATION_TEXT,
                    reply_to_message_id=ym.message_id
                )


@Bot.on_callback_query()
async def on_cb_qry(_, callback_query: CallbackQuery):
    await callback_query.answer(
        text=DERP_USER_S_TEXT,
        show_alert=False,
        cache_time=0
    )
