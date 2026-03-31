class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        for n in nums:
            if n in seen:
                seen[n] += 1
            else :
                seen[n] = 1
        max_key = max(seen, key=seen.get)
        return max_key


        