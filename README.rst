fuzzydict, an ambiguous dictionary
==================================

.. image:: https://travis-ci.org/tfukushima/fuzzydict.png?branch=v0.0.1-cleanup   :target: https://travis-ci.org/tfukushima/fuzzydict

Installation
-------------

.. sourcecode:: bash

    $ easy_install fuzzydict

or

.. sourcecode:: bash

    $ pip install fuzzydict

Usage
-----

.. sourcecode:: python

    >>> from fuzzydict import FuzzyDict
    >>> fdict = FuzzyDict(0.5) # setting a threshold range from 0.0 to 1.0
    >>> # < Assign some values to the 'fdict'>
    >>> fdict
    >>> {'0123456789': 0, 'X123456789': 1, 'XX23456789': 2, 'XXX3456789': 3, 'XXXX456789': 4, 'XXXXX56789': 5, 'XXXXXX6789': 6, 'XXXXXXX789': 7, 'XXXXXXXX89':8, 'XXXXXXXXX9':9, 'XXXXXXXXXX': 10}
    >>> [key for key in fdict.iterkeys('0123456789')]
    ['0123456789', 'X123456789', 'XX23456789', 'XXX3456789', 'XXXX456789', 'XXXXX56789']
    >>> [value for value in fdict.itervalues('0123456789')]
    [0, 1, 2, 3, 4, 5]
    >>> fdict.fuzzy_add('0123456789', 1)  # bulk add
    >>> [(k, v) for (k, v) in fdict.iteritems('0123456789')]
    [('0123456789', 1), ('X123456789', 2), ('XX23456789', 3), ('XXX3456789', 4), ('XXXX456789', 5), ('XXXXX56789', 6)]
    >>> fdict['0123456789']  # You can also access to a FuzzyDict as a normal dict
    1

Test
----

.. sourcecode:: bash

    $ python setup.py test

License
-------

This package is released under `MIT Lisense <http://www.opensource.org/licenses/mit-license.php>`_.
