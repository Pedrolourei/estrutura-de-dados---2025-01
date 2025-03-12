"""

2. Considere listas de valores inteiros e implemente uma função que receba
como parâmetro uma lista encadeada e um valor inteiro n e divida a lista em
duas, de forma a segunda lista começar no primeiro nó logo após a
ocorrência de n na lista original. A figura a seguir ilustra esta separação:

A função deve retornar a referência para a segunda subdivisão da lista
original, enquanto lst deve continuar apontando para o primeiro elemento da
primeira subdivisão da lista. Essa função deve obedecer ao protótipo:

def separa(lst, n):
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

    def separa(self, n):
        current = self.head

        while current and current.next:
            if current.data == n:
                second_half = current.next  
                current.next = None  
                return second_half
            current = current.next

        return None  

lst = LinkedList()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)

print("Lista original:")
lst.print_list()

second_half = lst.separa(3)

print("Primeira subdivisão:")
lst.print_list()

print("Segunda subdivisão:")
if second_half:
    current = second_half
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
else:
    print("None")
