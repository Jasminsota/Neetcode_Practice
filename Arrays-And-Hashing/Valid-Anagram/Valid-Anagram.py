class Solution:
    #Solution #1
    def isAnagram(self, s: str, t: str) -> bool:
        #Decisive filter, there's no way both strings 
        # are anagrams if they don't have the same length
        if len(s)!=len(t):
            return False
        #Initialize two dictionaries, to count frecuencies
        #  in both strings
        count_s, count_t = {}, {}
        # We count the frecuencies of each element in the strings
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        #Return True if the elements of both strings have the same frecuencies
        return count_s == count_t

    #Solution #2
    def isAnagram_2(self, s: str, t: str) -> bool:
        #Return true if the sort of both strings is identical
        return sorted(s) == sorted(t)
