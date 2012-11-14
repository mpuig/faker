# -*- coding: utf-8 -*-
from baseprovider import BaseProvider
from utils import clean
import random


class Name(BaseProvider):
    """Basic definition of an internet user"""

    def __init__(self, locales):
        super(Name, self).__init__(locales)

    def new(self):
        self.first_name = self.fetch('name.first_name')
        self.last_name = self.fetch('name.last_name')
        self.prefix = self.fetch('name.prefix')
        self.suffix = self.fetch('name.suffix')
        self.name = self.parse('name.name')
        self.bio = "lorem ipsum"
        self.title = ' '.join([
            self.fetch('name.title.descriptor'),
            self.fetch('name.title.level'),
            self.fetch('name.title.job')
            ])

        # users internet stuff
        self.username = clean(random.choice([
                    "%s%s" % (self.first_name, self.last_name),
                    "%s%s" % (self.first_name[0], self.last_name),
                    "%s%s%s" % (
                        self.first_name[:len(self.first_name)],
                        random.choice(['', '.', '_']),
                        self.last_name),
                    ]))
        self.email = "@".join([self.username, self.fetch('internet.free_email')])

    def __str__(self):
        return "%s (%s)\n%s" % (
            self.name,
            self.username,
            self.title)
