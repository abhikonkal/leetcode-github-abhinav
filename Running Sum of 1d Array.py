class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        v=[]
        v.append(nums[0])
        sums=v[0]
        for i in range(1,len(nums)):
            sums+=nums[i]
            v.append(sums)
        return v
        #better solution but reversing list is easy in python but not in other lang
        # nums=nums{::-1}
        # v.append(sum(nums))
        # for i in range(0,len(nums)-1):
        #     v.append(v[i]-nums[i])
        # return v
            