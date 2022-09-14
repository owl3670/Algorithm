class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.before = None
    
    def set_next(self, next):
        self.next = next
        next.before = self

class CircularQueue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.set_next(self.tail)
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
            self.tail.set_next(self.head)
        self.tail = new_node
        self.count = self.count + 1

    def dequeue(self):
        if self.head is None:
            return None
        else:
            data = self.head.data
            self.head.before.set_next(self.head.next)
            self.head = self.head.next
            self.count = self.count - 1
            return data

    def move_head(self, d):
        if self.head is not None:
            for _ in range(d):
                self.head = self.head.next

def solution():
    h = int(input())
    d = int(input())
    q = CircularQueue()
    for i in range(h):
        q.enqueue(i+1)

    while q.count != 1:
        q.move_head(d-1)
        print(q.dequeue())

    print(q.dequeue())

def main():
    solution()