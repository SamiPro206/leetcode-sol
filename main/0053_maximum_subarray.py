"""
Problem: 53 - Maximum Subarray
Difficulty: Medium

Link:
https://leetcode.com/problems/maximum-subarray/

Time Complexity:
O(n log(n))

Space Complexity:
O(n log(n))

Notes:
"""


class Solution(object):
    def maxCrossArray(self, nums, l, r, mid):
        ls = rs = float('-inf')
        
        sum = 0
        i = mid
        while i >= l:
            sum += nums[i]
            if ls < sum:
                ls = sum
            i -= 1
        
        sum = 0
        j = mid + 1
        while j <= r:
            sum += nums[j]
            if rs < sum:
                rs = sum
            j += 1

        return max(ls, rs, ls+rs)

    def find_maxSubArray(self, nums, l, r):
        if l == r: return nums[l]

        mid = (l+r) // 2
        
        m1 = self.find_maxSubArray(nums, l, mid)
        m2 = self.find_maxSubArray(nums, mid+1, r)
        m3 = self.maxCrossArray(nums, l, r, mid)

        return max(m1, m2, m3)

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.find_maxSubArray(nums, 0, len(nums)-1)
        

def run_tests():
    s = Solution()

    # Test 1
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    assert s.maxSubArray(nums) == 6

    # Test 2
    nums = [1]
    assert s.maxSubArray(nums) == 1

    # Test 3
    nums = [5,4,-1,7,8]
    assert s.maxSubArray(nums) == 23
    
    # Test 4
    nums = [1, 2]
    assert s.maxSubArray(nums) == 3
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()