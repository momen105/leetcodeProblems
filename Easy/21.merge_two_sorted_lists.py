# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node as the head of the merged list
        dummy = ListNode(0)
        # Create a pointer to the current node
        curr = dummy

        # Traverse both lists until one of them reaches the end
        while l1 and l2:
            # Compare the values of the current nodes from both lists
            if l1.val <= l2.val:
                # Set the next node of the current node to l1 and move l1 forward
                curr.next = l1
                l1 = l1.next
            else:
                # Set the next node of the current node to l2 and move l2 forward
                curr.next = l2
                l2 = l2.next
            # Move the current pointer forward
            curr = curr.next

        # Append the remaining nodes from the non-empty list
        curr.next = l1 if l1 else l2
        print(dummy.next)
        # Return the head of the merged list
        return dummy.next


l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

# Create an instance of the Solution class
solution = Solution()

# Call the mergeTwoLists method on the instance
merged_list = solution.mergeTwoLists(l1, l2)
print(merged_list)
