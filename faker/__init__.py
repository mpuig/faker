# -*- coding: utf-8 -*-

__title__ = 'faker'
__version__ = '0.2.0'
__author__ = 'Marc Puig'
__license__ = 'ISC'
__copyright__ = 'Copyright 2012 Marc Puig'

import os
#import glob
import yaml

from providers.address import Address
from providers.internet import Internet
from providers.name import Name
from providers.company import Company


class Faker(object):
    """ This is the base class to generate fake objects"""

    def __init__(self):
        # Load the locales
        self.load_locales()
        self.new()

    def new(self):
        self.name = Name(locales=self.locales)
        self.address = Address(locales=self.locales)
        self.internet = Internet(locales=self.locales)
        self.company = Company(locales=self.locales)

    def load_locales(self):
        self.locales = {}
        path = os.path.dirname(__file__)
        #os.chdir(os.path.join(path, './locales/')
        #for yml in glob.glob("*.yml"):
        for yml in [os.path.join(path, './locales/en.yml')]:
            f = open(yml)
            self.locales.update(yaml.safe_load(f))
            f.close()
