class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = defaultdict(list)

        for word in strs:
            sortedWord = ''.join(sorted(word))
            anaMap[sortedWord].append(word)
        return list(anaMap.values())
        