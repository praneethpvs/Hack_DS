"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
from collections import Counter
from collections import OrderedDict


def RemoveDuplicates(head):
    temp_list = []
    prev_node = head
    if head is not None and head.next is not None:
        curr_list = head
        current = head

        while (curr_list):
            temp_list.append(curr_list.data)
            curr_list = curr_list.next

        temp_dict = Counter(temp_list)

        while (current.next):
            if temp_dict[current.data] > 1:
                temp_dict[current.data] -= 1
                if current == head:
                    head = head.next
                    prev_node = head
                    current = head
                else:
                    prev_node.next = current.next
                    prev_node = prev_node.next
                    current = prev_node.next
            else:
                current = current.next
    return head
