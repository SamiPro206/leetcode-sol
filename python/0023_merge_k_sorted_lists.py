"""
Problem: 23 - Merge k Sorted Lists
Difficulty: Hard

Link:
https://leetcode.com/problems/merge-k-sorted-lists/

Time Complexity:
O(...)

Space Complexity:
O(...)

Notes:
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def merge2Lists(self, h1, h2):
        newMergedList = ListNode(0)
        curr = newMergedList
        while (h1 or h2):
            if h1 and (not h2 or h1.val <= h2.val):
                h1, curr.next = h1.next, h1
            else:
                h2, curr.next = h2.next, h2
            curr = curr.next
        return newMergedList.next
    
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists: return lists
        if len(lists) == 1: return lists[0]
        
        # merge two linked lists:
        if len(lists) == 2: return self.merge2Lists(lists[0], lists[1])
        
        mid = len(lists) // 2
        LHS = self.mergeKLists(lists[:mid])
        RHS = self.mergeKLists(lists[mid:])
        return self.merge2Lists(LHS, RHS)

def run_tests():
    s = Solution()

    def convertToLL(l):
        preHead = ListNode(0)
        curr = preHead
        while len(l) > 0:
            curr.next = ListNode(l[0])
            curr = curr.next
            l = l[1:]
        return preHead.next

    def convertToArray(l):
        if not l: return []
        arr = []
        while l:
            arr = arr + [l.val]
            l = l.next
        return arr

    # Test 1
    lists = [[1,4,5],[1,3,4],[2,6]]
    r = convertToArray(s.mergeKLists([convertToLL(l) for l in lists]))
    assert r == [1,1,2,3,4,4,5,6]
    
    # Test 2
    lists = []
    r = convertToArray(s.mergeKLists([convertToLL(l) for l in lists]))
    assert r == []

    # Test 3
    lists = [[]]
    r = convertToArray(s.mergeKLists([convertToLL(l) for l in lists]))
    assert r == []

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()