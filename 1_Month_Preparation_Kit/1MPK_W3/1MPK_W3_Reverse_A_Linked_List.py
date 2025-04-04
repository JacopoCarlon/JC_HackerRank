

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def reverse(llist):
    # Write your code here
    prev = None
    head = llist
    while head:
        enext = head.next
        head.next = prev
        prev = head
        head = enext
    return prev






