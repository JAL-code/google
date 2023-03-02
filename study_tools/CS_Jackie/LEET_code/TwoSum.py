# Print the two

class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype List[int]
        """

        compliments = {}

        for index, number in enumerate(nums):
            print(f"i: {index}, n: {number}")

            compliment = target - number
            print(f"c: {compliment}")
            # Check for compliment in array
            if compliment in compliments:
                print(f"Found compliment")
                return [compliments[compliment], index]
            
            compliments[number] = index

        return []
    
nums = [2,7,11,15]
target = 13
ciw = Solution()
answer = ciw.twoSum(nums, target)
print(answer)

