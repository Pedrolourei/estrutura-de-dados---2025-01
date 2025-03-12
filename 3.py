"""
3. Implemente uma função que construa uma nova lista com a intercalação
dos nós de outras duas listas passadas como parâmetros. Esta função deve
retornar a lista resultante, conforme ilustrado a seguir:

Esta função deve obedecer ao protótipo:
def merge(l1, l2):
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

def merge(l1, l2):
    dummy = Node(0)
    tail = dummy

    c1, c2 = l1.head, l2.head

    while c1 or c2:
        if c1:
            tail.next = c1
            tail = c1
            c1 = c1.next
        if c2:
            tail.next = c2
            tail = c2
            c2 = c2.next

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

l1 = LinkedList()
l1.append(1)
l1.append(3)
l1.append(5)

l2 = LinkedList()
l2.append(2)
l2.append(4)
l2.append(6)
l2.append(8)  

print("Lista 1:")
l1.print_list()

print("Lista 2:")
l2.print_list()

merged = merge(l1, l2)

print("Lista intercalada:")
merged.print_list()
