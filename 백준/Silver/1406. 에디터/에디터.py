import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.cursor = None
        self.tail = None

    def insert_node(self, data):
        new_node = Node(data)

        if not self.head:  # 리스트가 비어 있는 경우
            self.head = new_node
            self.tail = new_node
            self.cursor = None
            return

        if self.cursor is None:  # 커서가 None인 경우 (리스트 끝에 삽입)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            return

        prev_node = self.cursor.prev
        new_node.next = self.cursor
        new_node.prev = prev_node
        self.cursor.prev = new_node

        if prev_node:
            prev_node.next = new_node
        else:
            self.head = new_node  # 새 노드가 헤드가 되는 경우

    def cursor_node(self, move):
        """커서를 왼쪽(L) 또는 오른쪽(D)으로 이동"""
        if move == "L":
            if self.cursor is None:
                self.cursor = self.tail
            elif self.cursor.prev:
                self.cursor = self.cursor.prev
        elif move == "D":
            if self.cursor is None:
                return  # 이미 끝에 있음
            elif self.cursor.next:
                self.cursor = self.cursor.next
            else:
                self.cursor = None
                
    def insert_string(self, data_str):
        for char in data_str:
            self.insert_node(char)

    def delete_mode(self):
        """커서 왼쪽 노드를 삭제"""
        if not self.head:  # 리스트가 비어 있는 경우
            return

        if self.cursor == self.head:  # 커서가 맨 앞에 있는 경우
            return

        if self.cursor is None:  # 커서가 리스트 끝에 있는 경우
            if self.tail == self.head:  # 노드가 하나만 있는 경우
                self.head = None
                self.tail = None
                self.cursor = None
                return

            last_node = self.tail
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            last_node = None
            return

        # 삭제 처리
        left_node = self.cursor.prev
        if left_node == self.head:  # 삭제 대상이 헤드인 경우
            self.head = self.cursor
            self.cursor.prev = None
        else:
            left_node.prev.next = self.cursor
            self.cursor.prev = left_node.prev

    def print_result(self):
        """연결 리스트의 데이터를 문자열로 반환."""
        result = []
        node = self.head
        while node is not None:
            result.append(node.data)
            node = node.next
        return ''.join(result)


# 빠른 입력 처리
s = list(sys.stdin.readline().rstrip())

ll = LinkedList()
ll.insert_string(s)

# 명령어 처리
for _ in range(int(sys.stdin.readline().rstrip())):
    temp =list(sys.stdin.readline().rstrip().split())

    if temp[0] == "P":
        ll.insert_node(temp[1])
    elif temp[0] == "L" or temp[0] == "D":
        ll.cursor_node(temp[0])
    elif temp[0] == "B":
        ll.delete_mode()

# 최종 결과 출력
sys.stdout.write(ll.print_result())
