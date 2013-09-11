# -*- coding: utf-8 -*-

class FuzzyDict(dict):
    """FuzziDict, an ambiguous dictionary.

    An instance of this class has an ambiguity in it and generates a
    series of characters as keys and the match ranks as values based on
    the ambiguity when it is given a string.

    Attributes:
        threshold: The threshold determins how much this dictionary
            ambiguous.
            e.g., An instance of this class initialized by
            `threshold = 0.5` privides a series of characters which
            ambiguous characters are in the range from zero to the
            length of the characters times `threshold` for each other.
    """
    def __init__(self, threshold, initDict = {}):
        """Initialize this class with the given threshold for the
        ambiguity.

        Args:
            threshold: The threshold reperents the ambiguity of this
                instance. The threshold should be `float`, otherwise it
                would be converted into the `float` value finally.
            initDict: The initial dictioanry this instance wil have.
                Default to an empty dictionary.
        """
        self.threshold = float(threshold)
        for k, v in initDict.items():
            self[k] = v

    def _get_fuzzy_elements(self, key):
        key_length = len(key)
        if self.has_key(key):
            yield key, self[key]
        chars = int(key_length * self.threshold)
        keys = [x for x in self.keys() if len(x) == key_length and x != key]
        for k in keys:
            match = 0
            for i in range(0, key_length):
                if key[i] == k[i]:
                    match += 1
            if chars <= match and self.has_key(k):
                yield k, self[k]
        raise StopIteration()

    def update(self, that):
        """Merge the dictionary of this instance with the given dictionary.

        Args:
            that: The dictionary to merge with this instance.
        Raises:
            TypeError: If the given `obj` is not an instance of `dict`.
        """
        if isinstance(that, dict):
            super(FuzzyDict, self).update(that)
        else:
            raise TypeError()

    def iterkeys(self, key):
        """Returns an iterator of ambiguous keys associated with the
        given key.

        Args:
            key: The key for the associated ambiguous keys.
        Returns:
            A generator of the series of keys associated with the given
            key.
        Raises:
            StopIteration: If the generator doesn't have further value.
        
        >>> fdict = FuzzyDict(0.5)
        >>> [key for key in fdict.iterkeys('0123456789')]
        ['0123456789', 'X123456789', 'XX23456789', 'XXX3456789', \
        'XXXX456789', 'XXXXX56789']
        """
        for k, _ in self._get_fuzzy_elements(key):
            yield k
        raise StopIteration()

    def itervalues(self, key):
        """Return an iterator of ambiguous values associated with the
        given key.

        Args:
            key: The key for the associated ambiguous keys.
        Returns:
            A generator of the series of valuse associated with the
            given key.
        Raises:
            StopIteration: If the generator doesn't have further value.

        >>> fdict = FuzzyDict(0.5)
        >>> [value for value in fdict.itervalues('0123456789')]
        [1, 2, 3, 4, 5, 6]
        """
        for _, v in self._get_fuzzy_elements(key):
            yield v
        raise StopIteration()

    def iteritems(self, key):
        """Return an iterator of ambiguous keys and dvalues associated
        with the given key.

        Args:
            key: The key for the associated ambiguous values.
        Returns:
            A generator of the series of key and value pairs associated
            with the given key.
        Raises:
            StopIteration: If the generator doesn't have further value.

        >>> fdict = FuzzyDict(0.5)
        >>> [value for value in fdict.itervalues('0123456789')]
        [1, 2, 3, 4, 5, 6]
        """
        for k, v in self._get_fuzzy_elements(key):
            yield k, v
        raise StopIteration()

    def put(self, key, value):
        """Assign the given value to entries associated with the given
        key.

        Args:
            key: The key for the associated ambiguous values.
            value: The value for the associated entires with the given
                   key.

        >>> fdict = FuzzyDict(0.5)
        fdict.assign('0123456789', 1)
        >>> [value for value in fdict.itervalues('0123456789')]
        [1, 1, 1, 1, 1, 1]
        """
        for k, _ in self._get_fuzzy_elements(key):
            self[k] = value

    def add(self, key, value):
        """Add the given value to entires associated with the given
        key.

        Args:
            key: The key for the associated ambiguous values.
            value: The value to be added to the associated valuses with
                the given key.

        >>> fdict = FuzzyDict(0.5)
        >>> fdict.add('0123456789', 1)  # bulk add
        >>> [key for key in fdict.iterkeys('0123456789')]
        [2, 3, 4, 5, 6, 7]
        """
        for k, _ in self._get_fuzzy_elements(key):
            self[k] += value
