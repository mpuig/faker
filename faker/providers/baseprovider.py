# -*- coding: utf-8 -*-
import random
import re
import string


# Source: http://stackoverflow.com/a/7534478
def get_var(input_dict, accessor_string):
    """Gets data from a dictionary using a dotted accessor-string"""
    current_data = input_dict
    for chunk in accessor_string.split('.'):
        current_data = current_data.get(chunk, {})
    return current_data


class BaseProvider(object):

    def __init__(self, locales):
        self.locales = locales
        self.new()

    def new(self):
        raise NotImplementedError

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        raise NotImplementedError

    def numerify(self, input_num):
        ## TODO: make sure numerify results doesn’t start with a zero
        return "".join([
            re.sub(r"#", random.choice(string.digits), i) for i in input_num])

    def letterify(self, input_string):
        return "".join([
            re.sub(r"\?", random.choice(string.uppercase), i) for i in input_string])

    def bothify(self, input_string):
        return self.letterify(self.numerify(input_string))

    def regexify(self, key):
        # Segurament no fa falta, ja que el 99% es pot fer sense
        # expressions regulars
        pass

    # Helper for the common approach of grabbing a translation
    # with an array of values and selecting one of them.
    def fetch(self, key):
        fetched = get_var(self.locales, "en.faker.%s" % key)
        if fetched:
            fetched = random.choice(fetched)
            #if fetched.match(/^\//) and fetched.match(/\/$/):  # A regex
            #    return regexify(fetched)
            #else:
            #    return fetched
        return fetched

    # Load formatted strings from the locale, "parsing" them
    # into method calls that can be used to generate a
    # formatted translation: e.g., "#{first_name} #{last_name}".
    def parse(self, key):
        fetched = self.fetch(key)
        matches = re.findall(r"#{([A-Za-z]+\.)?([^\}]+)\}([^#]+)?", fetched)

        texts = []
        for (kls, meth, etc) in matches:
            text = ''
            # If the token had a class Prefix (e.g., Name.first_name)
            # grab the constant, otherwise use self
            class_name = kls[:-1].strip()
            if class_name:
                module = __import__(
                    class_name.lower(), globals(), locals(), [], -1
                    )
                cls = getattr(module, class_name)
                instance = cls(locales=self.locales)
                text = getattr(instance, meth)
            else:
                # If the class has the method, call it, otherwise
                # fetch the transation (i.e., faker.name.first_name)
                try:
                    text = getattr(self, meth)
                except:
                    key2 = "%s.%s" % (key.split('.')[0], meth)
                    text = self.fetch(key2)

            # And tack on spaces, commas, etc. left over in the string
            text = "%s%s" % (text, etc)
            texts.append(text)

        return "".join(texts)
