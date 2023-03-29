# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 递归反转单链表，返回反转后的头指针
    # 明确递归函数reverse_recursive含义：输入一个单链表头指针，该方法递归反转单链表，并返回反转后的表头指针
    def reverse_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if len(head) == 0: return None
        if len(head) == 1: return head[0]

        last = self.reverse_recursive(head.next)
        head.next.next = head
        head.next = None

        return last

    # 迭代反转一个单链表，返回反转后的表头指针
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None

        pre = None
        cur = head
        nxt = head

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre

    # 入参：两个非空链表表示两个非负整数，每位数字逆序存储；
    # addTwoNumbers含义：将两个数字相加，并以相同形式返回一个表示和的链表
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if len(l1) == 0: return self.reverse(l2)
        if len(l2) == 0: return self.reverse(l1)

        n1 = self.addTwoNumbers(l1, l2)


def main():
    # 输入：l1 = [2,4,3], l2 = [5,6,4]
    # 输出：[7,0,8]
    # 解释：342 + 465 = 807.
    solution1 = Solution(l1=[2, 4, 3], l2=[5, 6, 4])
    head1 = solution1.addTwoNumbers()
    while head1:
        print(head1.val)
        head1 = head1.next

    print('---')

    # 输入：l1 = [0], l2 = [0]
    # 输出：[0]
    solution2 = Solution()
    head2 = solution2.addTwoNumbers()
    while head2:
        print(head2.val)
        head2 = head2.next

    print('---')

    # 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    # 输出：[8,9,9,9,0,0,0,1]
    solution3 = Solution()
    head3 = solution3.addTwoNumbers()
    while head3:
        print(head3.val)
        head3 = head3.next


if __name__ == '__main__':
    main()
