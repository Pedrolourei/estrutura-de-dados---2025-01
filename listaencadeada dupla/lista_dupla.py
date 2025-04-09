class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def remove(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def insert_ordered(self, data):
        new_node = Node(data)
        if not self.head or self.head.data >= data:
            self.insert_beginning(data)
            return
        current = self.head
        while current.next and current.next.data < data:
            current = current.next
        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

dll = DoublyLinkedList()
dll.insert_beginning(3)
dll.insert_beginning(1)
dll.insert_end(5)
dll.insert_ordered(4)
dll.insert_ordered(2)

print("Lista Duplamente Encadeada:")
dll.print_list()

dll.remove(3)
print("Após remover 3:")
dll.print_list()
