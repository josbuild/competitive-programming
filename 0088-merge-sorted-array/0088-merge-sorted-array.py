class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left_pt, right_pt = m - 1, n - 1
        for i in range(len(nums1) - 1, -1, -1):
            if left_pt >= 0 and right_pt >= 0:
                if nums2[right_pt] >= nums1[left_pt]:
                    nums1[i] = nums2[right_pt]
                    right_pt -= 1
                else:
                    nums1[i] = nums1[left_pt]
                    left_pt -= 1
            elif left_pt >= 0:
                nums1[i] = nums1[left_pt]
                left_pt -= 1
            elif right_pt >= 0:
                nums1[i] = nums2[right_pt]
                right_pt -= 1
            else:
                pass

            
            
        