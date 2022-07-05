# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        one = headA
        two = headB
        while one is not two:
            one = headB if one is None else one.next
            two = headA if two is None else two.next
        return one
            
            
        
        # first_set = set()
        # curr = headA
        # while curr:
        #     first_set.add(curr)
        #     curr = curr.next
        # curr = headB
        # while curr:
        #     if curr in first_set:
        #         return curr
        #     curr = curr.next
        # return None
        