from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    分治思想：把 k 个链表两两合并即可。
    """

    # mergeKLists定义：合并K个排序链表，返回合并后的表头
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        # base case:
        if n == 0: return None
        if n == 1: return lists[0]

        # recursive
        num = n // 2
        left = self.mergeKLists(lists[:num])
        right = self.mergeKLists(lists[num:])

        return self.mergeTwoLists(left, right)

    # 合并两个有序链表
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = dummy
        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next

        if p1:
            p.next = p1

        if p2:
            p.next = p2

        return dummy.next


class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for member in lists:
            while member:
                arr.append(member.val)
                member = member.next

        arr.sort()

        res = ListNode(-1)
        p = res
        for i in arr:
            p.next = ListNode(i)
            p = p.next
            print(p.val)

        return res.next


def list2link(list_):
    head1 = ListNode(list_[0])
    p = head1
    for i in range(1, len(list_)):
        p.next = ListNode(list_[i])
        p = p.next

    return head1


def main():
    # Input: lists = [[1,4,5],[1,3,4],[2,6]]
    # Output: [1,1,2,3,4,4,5,6]
    # Explanation: The linked-lists are:
    # [
    #   1->4->5,
    #   1->3->4,
    #   2->6
    # ]
    # merging them into one sorted list:
    # 1->1->2->3->4->4->5->6
    solution1 = Solution()
    head1 = solution1.mergeKLists([list2link([1, 4, 5]), list2link([1, 3, 4]), list2link([2, 6])])
    while head1:
        print(head1.val)
        head1 = head1.next

    print('---')

    # Input: lists = []
    # Output: []
    solution2 = Solution()
    head2 = solution2.mergeKLists([])
    while head2:
        print(head2.val)
        head2 = head2.next

    print('---')

    # Input: lists = [[]]
    # Output: []
    solution3 = Solution()
    head3 = solution3.mergeKLists([[]])
    while head3:
        print(head3.val)
        head3 = head3.next


if __name__ == '__main__':
    main()
