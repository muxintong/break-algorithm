from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # NOTE:虚拟头结点的使用，否则对于特殊边界情况需特殊处理
        dummy=ListNode(-1)
        dummy.next=head
        # Note:删除节点n时需找到节点n的前驱，由于是倒数，故其前一个节点是n+1，而不是n-1
        precusor_n = self.findNthFromEnd(dummy, n + 1)
        precusor_n.next = precusor_n.next.next
        return dummy.next


    def findNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        for i in range(n):
            p1 = p1.next

        p2 = head
        while p1:
            p1 = p1.next
            p2 = p2.next

        return p2


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
    # Input: head = [1,2,3,4,5], n = 2
    # Output: [1,2,3,5]
    n = 2
    solution1 = Solution()
    head = solution1.removeNthFromEnd(list2link([1, 2, 3, 4, 5]), n)
    print_link_list(head)

    # Input: head = [1, 2], n = 1
    # Output: []
    n = 1
    solution2 = Solution()
    head = solution2.removeNthFromEnd(list2link([1, 2]), n)
    print_link_list(head)

    # Input: head = [1, 2], n = 2
    # Output: [2]
    n = 2
    solution3 = Solution()
    head = solution3.removeNthFromEnd(list2link([1, 2]), n)
    print_link_list(head)

    # Input: head = [1,2], n = 1
    # Output: [1]
    n = 1
    solution4 = Solution()
    head = solution4.removeNthFromEnd(list2link([1, 2]), n)
    print_link_list(head)


if __name__ == '__main__':
    main()
