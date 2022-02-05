# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         if(head.next==None):
#             return head
#         # function to rev a linked list
#         def reverse_ll(self,ll):
#             new_ll = ll
#             prev  = None
#             curr  = ll
            
#             while(curr!=None):
#                 temp = curr.next
#                 curr.next = prev
#                 prev = curr
#                 curr = temp
#             return prev,ll
#         start = head
#         iterate = head
#         ans = iterate
#         iterations = 0
#         while(iterate!=None):
#             count = 0
#             ll = start
#             while(count<k-1):
#                 iterate = iterate.next
#                 count+=1
            
#             end  = iterate.next
#             iterate.next = None
#             new_ll,prev = reverse_ll(self,ll)
            
#             print(new_ll)
#             prev.next = end
#             iterate = iterate.next
#             start = end
#             if(iterations == 0):
#                 ans = new_ll
#             iterations+=1
#         return ans
            
            
            
#             #returns head and tail
            
        