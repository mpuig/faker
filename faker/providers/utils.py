# -*- coding: utf-8 -*-


def clean(text):
    return text.lower().\
        replace(" ", '').\
        replace(",", '').\
        replace("ä", 'ae').\
        replace("ö", 'oe').\
        replace("ü", 'ue').\
        replace("ß", 'ss')
