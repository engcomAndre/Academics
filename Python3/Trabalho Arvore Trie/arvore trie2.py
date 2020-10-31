import collections
import doctest

class Trie:
    """
    Implements a Trie (also known as 'digital tree',  'radix tree' or 'prefix tree').

    Where common starting letters of many words are stored just once.
    """
    def __init__(self):
        self.child = collections.defaultdict(Trie)

    def insert(self, string):
        """
        Add a given string to the trie, modifying it **in place**.

        >>> t = Trie()
        >>> t.insert('hello')
        >>> t.insert('hi')
        >>> list(sorted(t.child.keys()))
        ['h']
        >>> first_node = t.child['h']
        >>> list(sorted(first_node.child.keys()))
        ['e', 'i']

        As you can see, the same `h` was written only once,
        and it is connected with both `i` and `e`.
        """
        node = self
        for char in string:
            node = node.child[char]
        node = node.child[None]


    def __contains__(self, word):
        """
        >>> t = Trie()
        >>> t.insert('example')
        >>> 'example' in t
        True
        >>> 'exemplum' in t
        False
        >>> t.insert('bana')
        >>> 'banana' in t
        False
        >>> t.insert('banning')
        >>> t.insert('banned')
        """
        trie = self

        for char in word:
            if char in trie.child:
                trie = trie.child[char]
            else:
                return False

        return True

    def __str__(self, depth = 0):
        """
        Shows a nicely formatted and indented Trie.

        Cannot be tested as equivalent representations
        are arbitrarly chosen from (`dict`s are not ordered).
        """
        s = []
        for i in self.child:
            s.append( '{}{} {}'.format(
                ' ' * depth, i or '#', '\n' + self.child[i].__str__(depth + 1)))
        return ''.join(s)

if __name__ == '__main__':
    doctest.testmod()
    trie = Trie()
    for word in ('banning', 'banned', 'banana', 'bad', 'cooking', 'cought', 'count'):
        trie.insert(word)
    print(trie)