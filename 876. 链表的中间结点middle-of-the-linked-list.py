from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 快慢指针的使用：
        # 二者同时从头出发，快指针每次前进两步，慢指针每次前进一步，
        # 当快指针到达链表尾部时，慢指针正好到达链表中点。
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow


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


def main():
    # Input: head = [1,2,3,4,5]
    # Output: [3,4,5]
    # Explanation: The middle node of the list is node 3.
    # solution1 = Solution()
    # head = solution1.middleNode(list2link([1, 2, 3, 4, 5]))
    # print_link_list(head)


    # Input: head = [1,2,3,4,5,6]
    # Output: [4,5,6]
    # Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
    solution2 = Solution()
    head = solution2.middleNode(list2link([1,2,3,4,5,6]))
    print_link_list(head)


if __name__ == '__main__':
    main()
