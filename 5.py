"""
5. Considere listas que armazenam cadeias de caracteres e implemente uma
função para testar se duas listas passadas como parâmetros são iguais. Essa
função deve obedecer ao protótipo:

def igual(l1, l2):
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

def igual(l1, l2):
    c1, c2 = l1.head, l2.head

    while c1 and c2:
        if c1.data != c2.data:
            return False
        c1 = c1.next
        c2 = c2.next

    return c1 is None and c2 is None

l1 = LinkedList()
l1.append("A")
l1.append("B")
l1.append("C")

l2 = LinkedList()
l2.append("A")
l2.append("B")
l2.append("C")

l3 = LinkedList()
l3.append("A")
l3.append("B")
l3.append("D")

print("L1 e L2 são iguais?", igual(l1, l2))
print("L1 e L3 são iguais?", igual(l1, l3))
