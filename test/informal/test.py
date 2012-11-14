"""
This is an informal test originally written by Marc Puig.
It makes a general verification of the module.
"""
import sys
from faker import Faker


def main():

    # Create objects
    f = Faker()

    # names
    for i in range(10):
        f.new()
        print "*** name"
        print f.name
        print "*** company"
        print f.company
        print "*** address"
        print f.address
        print


if __name__ == '__main__':
    sys.exit(main())
