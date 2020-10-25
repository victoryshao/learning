# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1, node2 = l1, l2

        x = 1

        num1 = 0
        while node1:
            num1 += int(node1.val) * x
            x *= 10
            node1 = node1.next

        y = 1
        num2 = 0
        while node2:
            num2 += int(node2.val) * y
            y *= 10
            node2 = node2.next

        result = num1 + num2
        print(result)

    def add_two_numbers(self, l1, l2):
        result = ListNode(0)
        head = result
        carry = 0
        while l1 is not None or l2 is not None:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry
            carry = sum // 10
            sum = sum % 10

            result.next = ListNode(sum)
            result = result.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            result.next = ListNode(carry)

        return head.next


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    # s.addTwoNumbers(l1, l2)
    a = s.add_two_numbers(l1, l2)
    while a:
        print(a.val)
        a = a.next