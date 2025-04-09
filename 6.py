"""
6. Considere listas que armazenam cadeias de caracteres e implemente uma
função para criar uma cópia de uma lista encadeada. Essa função deve
obedecer ao protótipo:

def copia(lst):
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

def copia(lst):
    if lst.head is None:
        return LinkedList()

    new_list = LinkedList()
    current = lst.head

    while current:
        new_list.append(current.data)
        current = current.next

    return new_list

lst = LinkedList()
lst.append("A")
lst.append("B")
lst.append("C")

print("Lista original:")
lst.print_list()

copied_lst = copia(lst)

print("Lista copiada:")
copied_lst.print_list()
