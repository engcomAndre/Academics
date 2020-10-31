# -*-coding:UTF-8 -*-
##########################################################
# Author:André Vieira da Silva
# Nome: Arvore Trie.py Funções:delete,mostrarpalavras,mostrarNos
# Data:06/03/2017
##########################################################

class Trie(object):
    def __init__(self, value=None):
        self.children = {}
        self.value = value
        self.flag = False  # Indica o fim de uma palavra

    def add(self, char):
        val = self.value + char if self.value else char
        self.children[char] = Trie(val)

    def insert(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.add(char)
            node = node.children[char]
        node.flag = True

    def find(self, word):
        print("função find")
        node = self
        for char in word:
            print(node.children)
            if char not in node.children:
                return None
            node = node.children[char]
        return node.value

def delete(node, word, i):
    pos = word[0]  #caso a palavra não tenha interseções com outras /todos os seus nós só tenham um filho
    if node == None:
        return
    node1 = node
    node2 = node
    while i < len(word):
        tst = word[i]
        if len(node2.children) > 1:#caso a palavra tenha interseções com outras sem repetição de caracteres
            node1 = node2
            pos = tst
            node2 = node2.children[tst]
        else:node2 = node2.children[tst]
        i+=1
    i = 0
    while i < len(word):
        tst = word[i]
        if pos in node.children and node.value == node1.value:
            del node.children[pos]
            break # i = len(word)para quem quer ser elegante!!!se preferir
        node = node.children[tst]
        i+=1

def mostrarpalavras(node):
    if node == None:
        return
    for i in node.children:
        mostrarpalavras(node.children[i])
    if node.flag == True:
        print(node.value)

def mostrarNos(node,char = 0):
    if node == None:
        return
    if char != 0:
        print(node.children)
        node = node.children[char]
        for i in node.children:
            print(node.children)
            mostrarNos(node.children[i])
    else:
        for i in node.children:
            print(node.children)
            mostrarNos(node.children[i])


trie = Trie()
for word in ['banana', 'bacana','gloria', 'glorioso','malandramente']:
    trie.insert(word)

mostrarpalavras(trie)
delete(trie,'banana',0)
delete(trie,'malandramente',0)

trie.insert('menino')
trie.insert('menina')

trie.insert('meninada')
mostrarpalavras(trie)
delete(trie,'menino',0)

print()
mostrarpalavras(trie)







