"""
Problem: 2 - Add Two Numbers
Difficulty: Medium

Link:
https://leetcode.com/problems/add-two-numbers/

Time Complexity:
O(max(m, n))

Space Complexity:
O(n+m)

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

        def rec(l1, l2, acc=0):
            if l1 == None and l2 == None and acc == 0: return None

            # nodes value
            l1_v = l1.val if l1 != None else 0
            l2_v = l2.val if l2 != None else 0
            
            # next nodes
            l1_n = l1.next if l1 != None else None
            l2_n = l2.next if l2 != None else None

            newAdd = l1_v + l2_v + acc
            newVal = newAdd % 10
            newAcc = newAdd // 10

            return ListNode(
                newVal, 
                rec(l1_n, l2_n, newAcc)
            )
        return rec(l1, l2)

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