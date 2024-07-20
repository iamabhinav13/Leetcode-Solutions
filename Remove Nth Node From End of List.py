class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        # Create a dummy node that points to the head
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Move the first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers until first reaches the end
        while first is not None:
            first = first.next
            second = second.next
        
        # Skip the nth node from the end
        second.next = second.next.next
        
        return dummy.next

# Helper function to create a list from an array
def create_list(arr):
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert linked list to list
def list_to_array(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr
