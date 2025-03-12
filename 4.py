"""
4. Implemente uma função que receba como parâmetro uma lista encadeada
e inverta o encadeamento de seus nós, retornando a lista resultante. Após a
execução desta função, cada nó da lista vai estar referenciando (prox) o nó
que originalmente era seu antecessor, e o último nó da lista passará a ser o
primeiro nó da lista invertida, conforme ilustrado a seguir:

Esta função deve obedecer ao protótipo:
def inverte(lst):
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

    def inverte(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next 
            current.next = prev 
            prev = current 
            current = next_node 

        self.head = prev  

lst = LinkedList()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)

print("Lista original:")
lst.print_list()

lst.inverte()

print("Lista invertida:")
lst.print_list()
