from typing import Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    p1 = head
    p2 = head.next

    head.next = None
    while p2:
        p3 = p2.next  # 记录p2指针的后继节点

        p2.next = p1  # 反转p2指针的指向

        # 指针p1，p2同时向后移动一位
        p1 = p2
        p2 = p3

    return p1
