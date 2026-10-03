class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_list = dict()
        for elem in nums:
            if not elem in dict_list:
                dict_list[elem] = 0
            dict_list[elem] +=1
        
        result = []
        for key in dict_list.keys():
            result.append((dict_list[key], key))
        result_k = []
        for i in range(k):
            result_k.append(sorted(result)[::-1][i][1])
        return result_k
        
