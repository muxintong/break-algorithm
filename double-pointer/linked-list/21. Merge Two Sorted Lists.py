from typing import Optional

'''
pass
main方法验证有问题
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
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


def list2link(list_):
    head = ListNode(list_[0])
    p = head

    for i in range(1, len(list_)):
        p.next = ListNode(list_[i])
        p = p.next

    return head


def print(head: ListNode):
    p = head
    while p:
        print(p.val)
        p = p.next


def main():
    # Input: list1 = [1,2,4], list2 = [1,3,4]
    # Output: [1,1,2,3,4,4]
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    link1 = list2link(list1)
    link2 = list2link(list2)
    solution1 = Solution()
    head = solution1.mergeTwoLists(link1, link2)
    print(head)


    # 输入：
    # [1]
    # []
    # 输出：[]
    # 预期结果：[1]
    list1 = [1]
    list2 = []
    link1 = list2link(list1)
    link2 = list2link(list2)
    solution1 = Solution()
    head = solution1.mergeTwoLists(link1, link2)
    print(head)

if __name__ == '__main__':
    main()
