# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #base case
        node = head
        if(not head or head.next==None):
            return head
        node2 = node.next
        prev = None
        head = node2
        while(node):
            if(prev and node2):
                prev.next = node2
            if(node2):
                node.next = node2.next
                node2.next = node
            prev = node
            node = node.next
            if(node):
                node2 = node.next
            
        
        
        return head
            
        