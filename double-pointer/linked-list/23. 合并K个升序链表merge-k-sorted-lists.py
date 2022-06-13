from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
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
    head = ListNode(list_[0])
    p = head
    for i in range(1, len(list_)):
        p.next = ListNode(list_[i])
        p = p.next

    return head


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
    solution1.mergeKLists([list2link([1, 4, 5]), list2link([1, 3, 4]), list2link([2, 6])])

    print('---')

    # Input: lists = []
    # Output: []
    solution2 = Solution()
    solution2.mergeKLists([])

    print('---')

    # Input: lists = [[]]
    # Output: []
    solution3 = Solution()
    solution3.mergeKLists([[]])


if __name__ == '__main__':
        main()
