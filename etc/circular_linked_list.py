class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # 삽입
    def insert_node(self, data):
        new_node = Node(data)

        # 리스트가 비어있을 경우
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def delete_node(self, data):
        current = self.head

        # 리스트가 비어 있는 경우
        if not current:
            print("삭제할 데이터가 없습니다.")
            return

        # 리스트가 하나의 노드만 가지고 있는 경우
        if current.next == self.head and current.data == data:
            self.head = None # 헤드 초기화
            return

        # 삭제하려는 노드가 헤드인 경우
        if current.data == data:
            tail = self.head

            while tail.next != self.head:
                tail = tail.next
            self.head = current.next # 헤드를 다음 노드로 변경
            tail.next = self.head # 마지막 노드를 새 헤드와 연결
            current = None
            return

        # 삭제하려는 노드가 중간이나 끝에 있는 경우
        prev = None
        while current.next != self.head and current.data != data:
            prev = current
            current = current.next

        if current.data != data:
            print("삭제할 데이터가 없습니다.")
            return

        # 삭제하려는 노드가 마지막 노드인 경우
        if current.next == self.head:
            prev.next = self.head
        else:
            prev.next = current.next
        current = None

    # 출력
    def print_list(self):
        current = self.head
        while True:
            print(current.data, end="->")
            current = current.next
            if current == self.head:
                break
        print("(head)")


cll = CircularLinkedList()
cll.insert_node(10)
cll.insert_node(20)
cll.print_list()
cll.delete_node(10)



