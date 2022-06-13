# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list2link(list_: list) -> ListNode:
    """
    输入一个数组list，返回转换为链表的头结点
    :param list_:
    :return:
    """
    head = ListNode(list_[0])
    p = head
    for i in range(1, len(list_)):
        p.next = ListNode(list_[i])
        p = p.next

    return head


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None: return None

        slow = head
        fast = head
        while fast:
            if slow.val != fast.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = None

        return head


def main():
    # 输入：head = [1,1,2,3,3]
    # 输出：[1,2,3]
    slution1 = Solution()
    head1 = slution1.deleteDuplicates(list2link([1, 1, 2, 3, 3]))
    p = head1
    while p:
        print(p.val)
        p = p.next


if __name__ == '__main__':
    main()
