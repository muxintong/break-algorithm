from typing import Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def list2link(list_):
    head = ListNode(list_[0])
    p = head
    for i in range(1, len(list_)):
        p.next = ListNode(list_[i])
        p = p.next

    return head


def print_link_list(head: Optional[ListNode]) -> Optional[ListNode]:
    p = head
    while p:
        print(p.val)
        p = p.next
    return head


if __name__ == "__main__":
    old_list = [1, 2, 3, 4, 5]
    link = list2link(old_list)
    # Input: list1 = [1,2,4], list2 = [1,3,4]
    # Output: [1,1,2,3,4,4]
    # list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    # link1 = list2link(list1)
    link2 = list2link(list2)
    print_link_list(link2)
