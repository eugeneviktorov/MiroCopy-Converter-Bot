from aiogram import Bot
from bot.locales.index import get_texts
from bot.utils.enums import Locales


async def set_description(bot: Bot) -> None:
    languages = [
        None,
        Locales.RU,
        Locales.ES,
        Locales.PT,
        Locales.ID,
        Locales.AR
    ]

    for lang in languages:
        texts = get_texts(lang)

        await bot.set_my_short_description(short_description=texts.BOT_ABOUT, language_code=lang)
        await bot.set_my_description(description=texts.BOT_DESCRIPTION, language_code=lang)
