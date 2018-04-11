"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def Reverse(head):
    flag = False
    if head is not None and head.next is not None:
        prev_node = None
        current = head
        while (current is not None):
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        head = prev_node
    return head
