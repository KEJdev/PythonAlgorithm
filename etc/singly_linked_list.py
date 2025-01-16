class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 삽입
    def insert_node(self, data):
        new_node = Node(data)

        # head 없으면 첫번째 노드 데이터 삽입
        if not self.head:
            self.head = new_node
            return

        # 만약 데이터가 비어있지 않다면
        current = self.head

        # 끝 노드를 찾을 때까지 이동
        while current.next:
            current = current.next

        # 마지막 노드의 다음을 새 노드로 연결
        current.next = new_node
        return

    def insert_multiple(self, data_list):
        """
        :param data_list: [10,20,30]
        :return: 10 -> 20 -> 30
        """

        for data in data_list:
            self.insert_node(data)

    # 삭제
    def delete_node(self, data):
        current = self.head

        # 삭제할 노드가 헤드에 있다면
        if current and current.data == data:
            # 헤드를 다음 노드로 저장
            self.head = current.next
            # 현재 노드 메모리 헤제
            current = None
            return

        # 삭제할 노드 찾기
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if not current:
            print("삭제할 데이터가 없습니다.")
            return

        prev.next = current.next
        current = None

    # 출력
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("NULL")
        return


ll = LinkedList()
ll.insert_node(10)
ll.print_list()
ll.delete_node(10)

