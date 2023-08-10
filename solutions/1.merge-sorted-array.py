from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for i in range(n):
        #     for j in range(m+n):
        #         if nums2[i] < nums1[j] or (nums1[j] == 0 and j > m-1):
        #             print("SHIFTING THE ARRAY!")
        #             for z in range(m+n-1, j, -1):
        #                 nums1[z] = nums1[z-1]
        #             print("SHIFTED ARRAY:")
        #             print(nums1)
        #             nums1[j] = nums2[i]
        #             print("INSERTING FROM NUMS2")
        #             print(nums1)
        #             break


        # Bc both sets are sorted the largest number is at the end so we compare and fill in the largest number 
        # in our new list. 
        
        # set p1 at the end of nums1, p2 at the end of nums2, and set p at the end of where nums1 will eventually be
        p1, p2, p = m - 1, n - 1, m + n - 1
        
        # while both pointers are not 0
        while p1 >= 0 and p2 >= 0:
            # Check if the last element filled in first arr is bigger
            if nums1[p1] > nums2[p2]:
                # If it is we put it into our final array (nums1 is final and inital)
                nums1[p] = nums1[p1]
                # dec counter from nums1 filled bc we used the number
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are remaining elements in nums2, copy them to nums1
        nums1[:p2 + 1] = nums2[:p2 + 1]



# Test cases
solution = Solution()

nums1 = [-1,3,0,0,0,0,0]
m = 2
nums2 = [0,0,1,2,3]
n = 5
solution.merge(nums1, m, nums2, n)
expected_output1 = [1, 2, 2, 3, 5, 6]
assert nums1 == expected_output1, f"Expected: {expected_output1}, Got: {nums1}"

# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3
# solution.merge(nums1, m, nums2, n)
# expected_output1 = [1, 2, 2, 3, 5, 6]
# assert nums1 == expected_output1, f"Expected: {expected_output1}, Got: {nums1}"

# nums1 = [4, 5, 6, 0, 0, 0]
# m = 3
# nums2 = [1, 2, 3]
# n = 3
# solution.merge(nums1, m, nums2, n)
# expected_output2 = [1, 2, 3, 4, 5, 6]
# assert nums1 == expected_output2, f"Expected: {expected_output2}, Got: {nums1}"

print("All test cases passed!")