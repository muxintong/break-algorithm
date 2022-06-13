from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        # NOTE:use is or ==
        while p1 != p2:
            if p1 == None:
                p1 = headB
            else:
                p1 = p1.next

            if p2 == None:
                p2 = headA
            else:
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
    # intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    # Output: Intersected at '8'
    # Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
    # From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5].
    # There are 2 nodes before the intersected node in A;
    # There are 3 nodes before the intersected node in B.
    solution1 = Solution()
    intersect_head = solution1.getIntersectionNode(list2link([4, 1, 8]), list2link([5, 8]))
    print_link_list(intersect_head)


if __name__ == '__main__':
    main()
