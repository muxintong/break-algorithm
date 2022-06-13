"""
链表成环判定：使用双指针中的快慢指针解决
procedure：
每当慢指针 slow 前进一步，快指针 fast 就前进两步。

如果 fast 最终遇到空指针，说明链表中没有环；
如果 fast 最终和 slow 相遇，那肯定是 fast 超过了 slow 一圈，说明链表中含有环。
"""
from typing import Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 链表成环判定：快慢指针技巧，含环返回True，不含返回False
def linkedlist_hasCircle(head: Optional[ListNode]) -> bool:
    fast = head
    slow = head
    # 终止条件：快指针走到末尾时停止
    while fast and fast.next:
        # 过程：快走两步，慢走一步，若此过程中二者相遇则说明链表含环
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True

    return False


# 含环链表返回环起点
def linkedlist_circle_point(head: Optional[ListNode]) -> Optional[ListNode]:
    fast = head
    slow = head
    # 成环判定：快两步，慢一步，二者相等时即含环
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # 【相遇点】快慢指针相遇=>含环=>在快慢指针相遇点终止循环
        if slow == fast: break

    if fast == None or fast.next == None:
        # fast与空指针说明无环
        return None

    # 【环起点】使慢指针重新指向链表头，二者同步前进，再次相交点就是环起点
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow
