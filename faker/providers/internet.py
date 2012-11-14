# -*- coding: utf-8 -*-
from baseprovider import BaseProvider


class Internet(BaseProvider):
    """Basic definition of internet stuff"""

    def __init__(self, locales):
        super(Internet, self).__init__(locales)

    def new(self):
        pass
