class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def search(self, key):
        if not self.head:
            return False

        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    def remove(self, key):
        if not self.head:
            return

        current = self.head
        prev = None

        while True:
            if current.data == key:
                if prev:
                    prev.next = current.next
                else:
                    if current.next == self.head:
                        self.head = None
                    else:
                        tail = self.head
                        while tail.next != self.head:
                            tail = tail.next
                        self.head = current.next
                        tail.next = self.head
                return
            prev = current
            current = current.next
            if current == self.head:
                break

    def count(self):
        if not self.head:
            return 0

        count = 1
        temp = self.head.next
        while temp != self.head:
            count += 1
            temp = temp.next
        return count

cll = CircularLinkedList()
cll.insert_end(10)
cll.insert_end(20)
cll.insert_end(30)

print(cll.search(20))
print(cll.count())
cll.remove(20)
print(cll.search(20))
print(cll.count())
