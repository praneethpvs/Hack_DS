"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list
"""


def Reverse(head):
    if head is not None and head.next is not None:
        prevNode = None
        curNode = head
        while (curNode):
            tempNode = curNode.next
            curNode.next = prevNode
            curNode.prev = tempNode

            prevNode = curNode
            if tempNode is not None:
                head = tempNode
            curNode = tempNode
    return head







