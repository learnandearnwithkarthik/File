# (c) adarsh-goel

import asyncio
import traceback
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid
from WebStreamer.vars import Var
Broadcast_IDs = {}

BROADCAST_AS_COPY = Var.BROADCAST_AS_COPY

async def send_msg(user_id, message):
    try:
        if BROADCAST_AS_COPY is False:
            await message.forward(chat_id=user_id)
        elif BROADCAST_AS_COPY is True:
            await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : Deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : Blocked The Bot\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : User ID Invalid\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"
