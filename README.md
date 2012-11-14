Faker
=====
This module is a port of Ruby Faker library
[github](https://github.com/stympy/faker) that generates fake data.

It was starded to test [Gustosity](http://gustosity.com/), looking for
an easy method to create real-looking test data for recipes and user activity,
and having the database populated with more than one or two records while
I was doing development.

It uses EXACTLY the same YML files used in the original Ruby module, and the
only big difference is that this module doesn't parse regular expressions.


Installing
----------
```bash
pip install dummydata
```

Usage
-----
```python
fake = Faker()
fake.name
fake.address
fake.company
```

Contributing
------------
If you'd like to contribute code or formats/data for another locale, fork
the project at [github](https://github.com/mpuig/dummydata), make your changes,
then send a pull request.


Contact
-------
Comments and feedback are welcome. Send me a message at
marc.puig (at) gmaildotcom

License
-------
This code is free to use under the terms of the ISC license.


