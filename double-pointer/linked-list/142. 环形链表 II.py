# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: break  # 快慢指针相遇点跳出循环，此时快2k步，慢k步

        # 成环判定:fast遇空则无环
        if fast == None or fast.next == None: return None

        # 若含环，则找到环起点
        # 快慢指针中的任意一个重新指向头，二者同步前进，再次相遇点就是环起点
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
