class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # sentinel node as pseudo-head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        if index < 0:
            index = 0

        self.size += 1
        # find predecessor of the node to be added
        pred = self.head
        for _ in range(index):
            pred = pred.next

        # node to be added
        to_add = ListNode(val)
        # insertion itself
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return

        self.size -= 1
        # find predecessor of the node to be deleted
        pred = self.head
        for _ in range(index):
            pred = pred.next

        # delete pred.next
        pred.next = pred.next.next

    def print(self) -> None:
        p = self.head
        while p.next:
            p = p.next
            print(p.val)


# Your MyLinkedList object will be instantiated and called as such:
linkedList = MyLinkedList()

linkedList.addAtHead(1)
linkedList.print()
print('---')


linkedList.addAtTail(3)
linkedList.print()
print('---')


linkedList.addAtIndex(1, 2)  # 链表变为1-> 2-> 3
linkedList.print()
print('---')


linkedList.get(1)  # 返回2
linkedList.print()
print('---')

linkedList.deleteAtIndex(1)  # 现在链表是1-> 3
linkedList.print()
print('---')

linkedList.get(1)  # 返回3
linkedList.print()
print('---')

