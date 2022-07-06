# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy_node = ListNode(-1)
        dummy_node.next = head
        cur = dummy_node
        while(cur.next!=None):
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                
                cur = cur.next
        return dummy_node.next
            
            
# The linked list is empty the head node is None
# the head node has the target value

        