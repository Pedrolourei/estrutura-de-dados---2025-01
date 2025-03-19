class circular:
    def __init__(self):
        self.head = None
        self.next = None
        self.prev = None

    def insert_beginning(self, data):
        new_node = circular(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            tail.next = new_node
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self, data):
        if not self.head:
            self.insert_beginning(data)
            return
        tail = self.head.prev
        new_node = circular(data)
        new_node.next = self.head
        new_node.prev = tail
        tail.next = new_node
        self.head.prev = new_node

    def search(self, data):
        if not self.head:
            return None
        current = self.head
        while True:
            if current.data == data:
                return current
            current = current.next
            if current == self.head:
                break
        return None

    def remove(self, data):
        if not self.head:
            return
        current = self.head
        while True:
            if current.data == data:
                if current == self.head and current.next == self.head:
                    self.head = None
                    return
                elif current == self.head:
                    tail = self.head.prev
                    self.head = self.head.next
                    tail.next = self.head
                    self.head.prev = tail
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
            if current == self.head:
                break

    def insert_ordered(self, data):
        new_node = circular(data)
        if not self.head or self.head.data >= data:
            self.insert_beginning(data)
            return
        current = self.head
        while current.next != self.head and current.next.data < data:
            current = current.next
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node

    def print_list(self):
        if not self.head:
            print("Lista vazia")
            return
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print("(volta para o início)")

    def print_reverse(self):
        if not self.head:
            print("Lista vazia")
            return
        current = self.head.prev
        while True:
            print(current.data, end=" <-> ")
            current = current.prev
            if current.next == self.head.prev:
                break
        print("(volta para o final)")
        
cdll = circular()
cdll.insert_beginning(3)
cdll.insert_beginning(1)
cdll.insert_end(5)
cdll.insert_ordered(4)
cdll.insert_ordered(2)

print("Lista Duplamente Encadeada Circular:")
cdll.print_list()

cdll.remove(3)
print("Após remover 3:")
cdll.print_list()

print("Impressão reversa:")
cdll.print_reverse()
