# -*- coding: utf-8 -*-
from baseprovider import BaseProvider
from utils import clean


class Company(BaseProvider):
    """Basic definition of a Company"""

    def __init__(self, locales):
        super(Company, self).__init__(locales)

    def new(self):
        self.name = self.parse('company.name')
        self.suffix = self.fetch('company.suffix')
        self.website = "http://www.%s.%s" % (
            clean(self.name),
            self.fetch('internet.domain_suffix')
            )

    def __str__(self):
        return "%s %s\n%s" % (
            self.name,
            self.suffix,
            self.website)
