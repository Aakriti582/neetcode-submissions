class Solution:
    from collections import defaultdict
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram= defaultdict(list)
        for x in strs:
            sortedx="".join(sorted(x))
            anagram[sortedx].append(x)
        return list(anagram.values())



        