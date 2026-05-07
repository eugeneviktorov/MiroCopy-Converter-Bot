from aiogram.types import BotCommand

from bot.locales.index import get_texts
from bot.utils.enums import Command, Locales


def get_commands_en():
    return [
        BotCommand(command=Command.START, description=get_texts(Locales.EN).START_CMD),
    ]


def get_commands_ru():
    return [
        BotCommand(command=Command.START, description=get_texts(Locales.RU).START_CMD),
    ]


def get_commands_es():
    return [
        BotCommand(command=Command.START, description=get_texts(Locales.ES).START_CMD),
    ]


def get_commands_pt():
    return [
        BotCommand(command=Command.START, description=get_texts(Locales.PT).START_CMD),
    ]


def get_commands_id():
    return [
        BotCommand(command=Command.START, description=get_texts(Locales.ID).START_CMD),
    ]


def get_commands_ar():
    return [
        BotCommand(command=Command.START, description=get_texts(Locales.AR).START_CMD),
    ]
