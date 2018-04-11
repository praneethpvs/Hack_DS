"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""

"""
The Below code does the following to find the merger points of two given linked list.
Hypothesis - The two linked List have a merge point.

1. Navigate the first LinkedList and save the Last Node.
2. Link the last node of the List to the First node and form a loop.
3. Now traverse the second linked list to see if there is a loop.
    a. If a loop is detected find out the point of intersection and return its value.
    b. Since the Last Node Value is saved in the first Linked List, break the link between the Last Node and the First Node.
"""


def FindMergeNode(headA, headB):
    if headA is not None and headA.next is not None and headB is not None and headB.next is not None:
        lastA = None
        curA = headA
        while (curA):
            if curA.next is None:
                lastA = curA
                break
            curA = curA.next
        lastA.next = headA

        op = None
        setB = set()
        curB = headB
        while (curB):
            if curB in setB:
                op = curB.data
                break
            setB.add(curB)
            curB = curB.next

        curA.next = None
        return op
