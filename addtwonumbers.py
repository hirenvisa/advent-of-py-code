import collections 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if l1 is None and l2 is None:
            return None
                
        while l1 is not None and l2 is not None:

            data: int = 0

            if l1 is not None: 
                data += l1.val
            if l2 is not None:
                data += l2.val

            if data <= 9:
                l1.val = data
                if l2 is not None and l2.next is not None:
                    l1.next = ListNode(0)
            else:
                l1.val = data - 10
                if l1 is not None and l1.next is None:
                    l1.next = ListNode(1)

            l1 = l1.next
            l2 = l2.next

class main():
    l1 = ListNode(9)
    l2 = ListNode(5)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)

    sol = Solution()
    sol.addTwoNumbers(l1, l2)

    while l1 is not None:
        print(l1.val)
        l1 = l1.next

    