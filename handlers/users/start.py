from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.db_api import db_commands as db
from loader import dp, _


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    print(_("Привет {user}").format(user=message.from_user.full_name))
    text = _("Привет {user}").format(user=message.from_user.full_name)
    await message.answer(text=text)
    await db.add_user(id=message.from_user.id, username=message.from_user.full_name)
