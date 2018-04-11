"""
 Delete Node at a given position in a linked list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def Delete(head, position):
    if head is not None:
        if position == 0:
            head = head.next
        else:
            current = head
            i = 1
            while (current.next is not None and i < position):
                current = current.next
                i += 1
            current.next = current.next.next
    return head
