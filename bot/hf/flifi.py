
from typing import List, Union
from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)


def uszkhvis_chats_ahndler(chats: List[Union[str, int]]):
    async def func(flt, client: Client, message: Message):
        chats = flt.chats
        return bool(
            message.chat and (
                message.chat.id in chats
            )
        )
    # "chats" kwarg is accessed with "flt.chats" above
    return filters.create(func, chats=chats)
