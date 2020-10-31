import argparse, os, sys


class Trie:
    '''A simple tree structure to handle looking up all words starting
       with a given prefix'''

    def __init__(self, achar):
        self.char = achar
        self.children = {}

    def insert_word(self, aword):
        '''load a word into the trie'''
        cur = self
        for achar in aword:
            nxt = cur.children.get(achar)
            if nxt is None:
                nxt = Trie(achar)
                cur.children[achar] = nxt
            cur = nxt


def walk(trie, s):
    '''Walk the trie to the end of the prefix s'''
    cur = trie
    for c in s:
        cur = cur.children.get(c)
        if cur is None:
            return cur
    return cur


def print_all_words(trie, s=""):
    '''print all the words in this trie with prefix s appended.'''
    if trie is None:
        return
    if len(trie.children) == 0:
        print(s)
    else:
        for k, v in trie.children.items():
            print_all_words(v, s + v.char)

s
words = ["t","te","ted","bob","mis","missa"]

root = Trie("")
for word in words:
    root.insert_word(word.strip("\n") + "\0")

print_all_words(root,"")

