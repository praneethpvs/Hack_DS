"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list
"""


def SortedInsert(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        curNode = head
        lastNode = None
        if new_node.data < head.data:
            new_node.next = curNode
            head.prev = new_node
            head = new_node
        else:
            while (curNode):
                if curNode.data > data:
                    new_node.next = curNode
                    new_node.prev = curNode.prev
                    curNode.prev.next = new_node
                    curNode.prev = new_node
                    break
                if curNode.next == None:
                    lastNode = curNode
                curNode = curNode.next
            else:
                if curNode is None:
                    new_node.next = None
                    new_node.prev = lastNode
                    lastNode.next = new_node
    return head
