"""
7. Implemente funções para inserir e retirar um elemento de uma lista circular
simplesmente encadeada (obtenha informações adicionais sobre listas
circulares na bibliografia básica da disciplina).
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def remove(self, data):
        if not self.head:
            return

        current = self.head
        prev = None

        while True:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next
                    if self.head == self.head.next:
                        self.head = None
                    else:
                        self.head = self.head.next
                        tail.next = self.head
                return
            prev = current
            current = current.next
            if current == self.head:
                break 

    def print_list(self):
        if not self.head:
            print("Lista vazia")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(volta para o início)")

clist = CircularLinkedList()
clist.insert(1)
clist.insert(2)
clist.insert(3)
clist.insert(4)

print("Lista circular após inserções:")
clist.print_list()

clist.remove(3)
print("Lista circular após remover 3:")
clist.print_list()

clist.remove(1)
print("Lista circular após remover 1:")
clist.print_list()
