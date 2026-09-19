class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups={}
        for num in nums:
            if num not in groups:
                groups[num]=0
            groups[num]+=1

        sorted_groups = dict(
            sorted(groups.items(), key=lambda x: x[1], reverse=True))
        

        return list(sorted_groups.keys())[:k]
