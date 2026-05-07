from enum import Enum


class Command(str, Enum):
    START = "start"


class Locales(str, Enum):
    EN = "en"
    RU = "ru"
    ES = "es"
    PT = "pt"
    ID = "id"
    AR = "ar"
