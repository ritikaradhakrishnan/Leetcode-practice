# # # Definition for singly-linked list.
# # # class ListNode:
# # #     def __init__(self, val=0, next=None):
# # #         self.val = val
# # #         self.next = next
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         #edge cases for empty lists
#         if not lists or len(lists) == 0:
#             return None
        
#         while len(lists) > 1:
#             newList = []
#             for i in range(0, len(lists), 2):
#                 l1 = lists[i]
#                 if (i+1)<len(lists):
#                     l2 = lists[i+1]
#                 else: 
#                     l2 = None
#                 newList.append(self.mergetwolists(l1, l2))
#             lists = newList
#         return lists[0]
            
#     def mergetwolists(self, l1, l2):
#         dummylist = ListNode(-1)
#         tail = dummylist
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 tail.next = l1
#                 l1 = l1.next
#             else:
#                 tail.next = l2
#                 l2 = l2.next
#             tail = tail.next
#         if l1:
#             tail.next = l1
#         else:
#             tail.next = l2
            
#         return dummylist.next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        while len(lists)>1:
            newList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if i+1 < len(lists):
                    l2 = lists[i+1]
                else:
                    l2 = None
                newList.append(self.mergeTwoLists(l1, l2))
            lists = newList
        return lists[0]


    def mergeTwoLists(self, l1, l2):
        dummyNode = ListNode(-1)
        pointer = dummyNode
        while l1 and l2:
            if l1.val <= l2.val:
                pointer.next = l1
                l1 = l1.next
            else:
                pointer.next = l2
                l2 = l2.next
            pointer = pointer.next
        if l1:
            pointer.next = l1
        else:
            pointer.next = l2
        return dummyNode.next
            


        
