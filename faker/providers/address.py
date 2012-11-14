# -*- coding: utf-8 -*-
from baseprovider import BaseProvider
import random


class Address(BaseProvider):
    """This is the usual info needed to create an address"""

    def __init__(self, locales):
        super(Address, self).__init__(locales)

    def new(self):
        self.city = self.parse('address.city')
        self.street_name = self.parse('address.street_name')
        self.secondary_address = self.numerify(
            self.fetch('address.secondary_address'))
        self.street_address = ' '.join([
            self.numerify(self.parse('address.street_address')),
            self.secondary_address])
        self.building_number = self.bothify(
            self.fetch('address.building_number'))
        self.zip_code = self.bothify(
            self.fetch('address.postcode'))
        self.time_zone = self.bothify(
            self.fetch('address.time_zone'))
        self.street_suffix = self.fetch('address.street_suffix')
        self.city_suffix = self.fetch('address.city_suffix')
        self.city_prefix = self.fetch('address.city_prefix')
        self.state_abbr = self.fetch('address.state_abbr')
        self.state = self.fetch('address.state')
        self.country = self.fetch('address.country')
        self.latitude = str(random.randint(-90, 90))
        self.longitude = str(random.randint(-180, 180))

    def __str__(self):
        return "%s\n%s %s\n(%s)" % (
            self.street_address,
            self.zip_code,
            self.city,
            self.country)
