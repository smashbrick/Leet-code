class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n
        postfix = [1] * n

        prod = 1
        for i in range(n):
            prefix[i] = prod
            prod *= nums[i]

        prod = 1
        for i in range(n - 1, -1, -1):
            postfix[i] = prod
            prod *= nums[i]

        return [prefix[i] * postfix[i] for i in range(n)]