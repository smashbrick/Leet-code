class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        mostFreq =  freq.most_common(k)
        print(mostFreq)
        result = []
        for num, count in mostFreq:
            result.append(num)
        return result

        