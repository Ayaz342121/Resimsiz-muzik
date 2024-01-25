from pyrogram import filters
from pyrogram.types import Message

from LOKESHXMUSIC import app
from LOKESHXMUSIC.core.call import Anony
from LOKESHXMUSIC.utils.database import is_music_playing, music_off
from LOKESHXMUSIC.utils.decorators import AdminRightsCheck
from LOKESHXMUSIC.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.command(["pause","durdur", "dur", "cdurdur", "cdur"  "cpause"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await Anony.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
