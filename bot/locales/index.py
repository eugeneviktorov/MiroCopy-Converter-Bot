from bot.locales import en, ru, es, pt, id, ar
from bot.utils.enums import Locales


def get_texts(language_code: str | None):
    if not language_code:
        return en

    code = language_code.lower()

    if code.startswith(Locales.RU):
        return ru
    if code.startswith(Locales.ES):
        return es
    if code.startswith(Locales.PT):
        return pt
    if code.startswith(Locales.ID):
        return id
    if code.startswith(Locales.AR):
        return ar
    return en
