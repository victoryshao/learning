# 回文链表

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


from collections import deque


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True

        if head.next is None:
            return True

        queue = deque()

        node = head
        while node:
            queue.append(node.val)
            node = node.next

        print(queue)

        origin_node = head
        while origin_node:
            print(origin_node.val)
            if not origin_node.val == queue.pop():
                return False
            origin_node = origin_node.next

        return True


if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(2)
    l.next.next.next = ListNode(1)

    s = Solution()
    print(s.isPalindrome(l))