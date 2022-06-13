# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    '''
    双指针快慢指针技巧，每当慢指针 slow 前进一步，快指针 fast 就前进两步。
    如果 fast 最终遇到空指针，说明链表中没有环；
    如果 fast 最终和 slow 相遇，那肯定是 fast 超过了 slow 一圈，说明链表中含有环。
    '''
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast != None and fast.next != None:
            # 慢一步、快两步
            slow = slow.next
            fast = fast.next.next

            # 快慢相遇：含环
            if slow == fast:
                return True

        return False


