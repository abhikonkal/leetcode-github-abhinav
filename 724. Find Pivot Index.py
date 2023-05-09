class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rsum=sum(nums)
        lsum=0
        for index,nums in enumerate(nums):
            rsum-=nums
            if lsum==rsum:
                return index
            lsum+=nums
        return -1

