class Node:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)

        if self.size == 0:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            tail.next = new_node
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
        else:
            tail = self.head.prev
            new_node = Node(val)
            new_node.next = self.head
            new_node.prev = tail
            tail.next = new_node
            self.head.prev = new_node
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next

            prev_node = curr.prev
            new_node = Node(val)
            new_node.prev = prev_node
            new_node.next = curr
            prev_node.next = new_node
            curr.prev = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if self.size == 1:
            self.head = None
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next

            prev_node = curr.prev
            next_node = curr.next
            prev_node.next = next_node
            next_node.prev = prev_node

            if curr == self.head:
                self.head = next_node

        self.size -= 1
