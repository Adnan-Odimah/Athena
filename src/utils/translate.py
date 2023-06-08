""" Contains the translate function """

from googletrans import Translator, constants

translator = Translator(service_urls=["translate.googleapis.com"])


def translate(sentence: str, to_lang: str):
    """Translates a sentence to a langauge inputed"""
    return translator.translate(sentence, dest=constants.LANGCODES[to_lang]).text
