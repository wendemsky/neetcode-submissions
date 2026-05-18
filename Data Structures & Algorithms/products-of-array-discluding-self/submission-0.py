class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        output = []
        for i, n in enumerate(nums):
            output.append(prefix)
            prefix *= nums[i]
        # print(output)

        postfix = 1
        for i in range(len(nums)-2, -1, -1):
            # print(i)
            postfix *= nums[i+1]
            # print(postfix)
            output[i] *= postfix
            # print(output)



        return output