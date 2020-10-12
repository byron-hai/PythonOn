# -*- coding: utf-8 -*-
from singly_linkedList import Node, LinkedList

class Solution(LinkedList):

    def reverse(self, head):
        if not head:
            return head

        prev = None

        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        return prev


if __name__ == "__main__":

    head = node = Node(0)
    for i in range(1, 5):
        new = Node(i)
        node.next = new
        node = new

    lnklst = Solution()
    lnklst.traverse(head)
    head1 = lnklst.reverse(head)
    print("Reversed list:")
    lnklst.traverse(head1)

