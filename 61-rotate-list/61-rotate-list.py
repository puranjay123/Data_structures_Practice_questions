# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=1
        if not head:
            return None
        cur =head
        while(cur.next):
            cur = cur.next
            length +=1
        k=k%length
        cur.next = head
        temp = head
        for _ in range(length-k-1):
            temp = temp.next
            
        answer=temp.next
        temp.next =None
        return answer
            
        
        