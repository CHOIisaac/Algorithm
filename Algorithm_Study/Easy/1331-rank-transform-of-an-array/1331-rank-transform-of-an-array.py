class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = sorted(set(arr))
        map_ = {}
        for i, b in enumerate(a):
            map_[b] = i + 1

        result = []
        for aa in arr:
            result.append(map_[aa])
        return result
