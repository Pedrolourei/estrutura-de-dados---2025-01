import random

class jojo:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, name):
        new_node = jojo(name)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def remove(self, node):
        if self.head == self.head.next: 
            self.head = None
            return None
        if node == self.head:
            self.head = self.head.next

        node.prev.next = node.next
        node.next.prev = node.prev
        return node.next 

    def play_game(self):
        if not self.head:
            print("Nenhum guerreiro para lutar!")
            return

        current = self.head
        while self.head != self.head.next:  
            steps = random.randint(1, 5)  
            for _ in range(steps):
                current = current.next
            
            print(f" {current.name} foi eliminado!")
            current = self.remove(current) 

        print(f" {self.head.name} é o sobrevivente!")

warriors = ["Jonathan Joestar", "Joseph Joestar", "Jotaro Kujo", "Josuke Higashikata", "Jolyne Kujo"]
game = CircularDoublyLinkedList()

for warrior in warriors:
    game.insert(warrior)

game.play_game()
