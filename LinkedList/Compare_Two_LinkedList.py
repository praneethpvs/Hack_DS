# Body
"""
 Compare two linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def CompareLists(headA, headB):
    if headA is None and headB is None:
        return 1
    else:
        curA = headA
        curB = headB
        while (curA is not None and curB is not None):
            if curA.data != curB.data:
                return 0
            else:
                curA = curA.next
                curB = curB.next
        else:
            if curA == curB:
                return 1
            else:
                return 0
