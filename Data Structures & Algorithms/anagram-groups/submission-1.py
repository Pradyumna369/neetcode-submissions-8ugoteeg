class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strDict = {}
        # for string in strs:
        #     strCounter = Counter(string)
        #     key = set()
        #     for char in strCounter:
        #         key.add(frozenset(char, strCounter[char]))
        #     if key not in strDict:
        #         strDict[key] = [string]
        #     else:
        #         strDict[key].append(string)
        # ans = []
        # ans.add(strDict.values)
        # return ans
        
        # res = defaultdict(list)
        # for s in strs:
        #     sortedS = ''.join(sorted(s))
        #     res[sortedS].append(s)
        # return list(res.values())

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

