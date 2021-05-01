from typing import Tuple, Any

from aiogram import types
from data.config import I18N_DOMAIN, LOCALES_DIR
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from utils.db_api import db_commands as db


async def get_lang(user_id):
    user = await db.select_user(id=user_id)
    if user.language:
        return user.language


class ACLMiddleware(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        user = types.User.get_current()
        if await get_lang(user.id) == None:
            print(user.locale)
            return user.locale
        else:
            print("db lan")
            return await get_lang(user.id)


def setup_middleware(dp):
    i18n = ACLMiddleware(I18N_DOMAIN, LOCALES_DIR)
    dp.middleware.setup(i18n)
    print("123")
    return i18n
