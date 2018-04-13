"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def MergeLists(headA, headB):
    if headA is None:
        return headB
    elif headB is None:
        return headA
    else:
        curA = headA
        curB = headB
        if headA.data < headB.data:
            head = headA
            curA = curA.next
        else:
            head = headB
            curB = curB.next
        curMerge = head
        while (curA and curB):
            if curA.data < curB.data:
                curMerge.next = curA
                curA = curA.next
            else:
                curMerge.next = curB
                curB = curB.next
            curMerge = curMerge.next
        else:
            if curA is None:
                curMerge.next = curB
            else:
                curMerge.next = curA
    return head
