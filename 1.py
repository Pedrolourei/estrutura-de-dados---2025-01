"""
   1. Considere listas de valores inteiros e implemente uma função que receba
como parâmetros uma lista encadeada e um valor inteiro n, retire da lista
todas as ocorrências de n e retorne a lista resultante. Esta função deve
obedecer ao protótipo:

def retira_n(lst, n):
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def retira_n(self, n):
        while self.head and self.head.data == n:
            self.head = self.head.next
        
        current = self.head
        while current and current.next:
            if current.next.data == n:
                current.next = current.next.next
            else:
                current = current.next

lst = LinkedList()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(2)
lst.append(4)

print("Lista original:")
lst.print_list()

lst.retira_n(2)

print("Lista após remover 2:")
lst.print_list()
