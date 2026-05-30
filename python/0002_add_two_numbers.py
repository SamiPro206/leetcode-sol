"""
Problem: 2 - Add Two Numbers
Difficulty: Medium

Link:
https://leetcode.com/problems/add-two-numbers/

Time Complexity:
O(max(m, n))

Space Complexity:
O(1)

Notes:
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        preHead = ListNode()
        curr = preHead
        acc = 0

        while l1 or l2 or acc != 0:
            l1_v, l1 = (l1.val, l1.next) if l1 else (0, None)
            l2_v, l2 = (l2.val, l2.next) if l2 else (0, None)

            newAdd = l1_v + l2_v + acc
            acc = newAdd // 10

            curr.next = ListNode(newAdd % 10)
            curr = curr.next
        return preHead.next
            
def convertToLL(l):
    if len(l) <= 0: return None
    return ListNode(l[0], convertToLL(l[1:]))

def convertToArray(l):
    if l == None: return []
    return [l.val] + convertToArray(l.next)

def run_tests():
    s = Solution()

    # Test 1
    l1 = convertToLL([2, 4, 3])
    l2 = convertToLL([5, 6, 4])
    r = s.addTwoNumbers(l1, l2)
    assert convertToArray(r) == [7, 0, 8]

    # Test 2
    l1 = convertToLL([0])
    l2 = convertToLL([0])
    r = s.addTwoNumbers(l1, l2)
    assert convertToArray(r) == [0]

    # Test 3
    l1 = convertToLL([9,9,9,9,9,9,9])
    l2 = convertToLL([9,9,9,9])
    r = s.addTwoNumbers(l1, l2)
    assert convertToArray(r) == [8,9,9,9,0,0,0,1]

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()