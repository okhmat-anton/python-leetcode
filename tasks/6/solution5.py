class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy

        # Loop until either list1 or list2 is empty
        while list1 and list2:
            if list1.val <= list2.val:
                # Append the node from list1
                current.next = list1
                list1 = list1.next
            else:
                # Append the node from list2
                current.next = list2
                list2 = list2.next
            # Move to the next node in the merged list
            current = current.next

        # Attach the remaining nodes, if any
        current.next = list1 if list1 else list2

        # Return the merged list, which starts at dummy.next
        return dummy.next


s = Solution()
print(s.mergeTwoLists([1, 2, 4], [1, 3, 4]))
