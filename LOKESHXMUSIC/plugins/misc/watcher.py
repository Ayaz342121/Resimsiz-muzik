from pyrogram import filters
from pyrogram.types import Message

from LOKESHXMUSIC import app
from LOKESHXMUSIC.core.call import Anony

welcome = 200
close = 300


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await Anony.stop_stream_force(message.chat.id)
