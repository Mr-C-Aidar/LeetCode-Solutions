#88. Merge Sorted Array
#https://leetcode.com/problems/merge-sorted-array/

from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Merge nums2 into nums1 as one sorted array.
    """
    nums1[:] = nums1[:m] + nums2
    nums1.sort()

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m = 3
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)  # Expected: [1,2,2,3,5,6]