class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        count = []
        for i in range(len(nums)):
            sum =0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    sum+=1
            count.append(sum)   
        return count            
          

        