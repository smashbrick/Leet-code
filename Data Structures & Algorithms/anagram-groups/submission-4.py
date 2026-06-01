class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
                anagram_map = defaultdict(list)
                for s in strs:
                    char_count = [0] * 26
                    for word in s:
                        char_count[ord(word) - ord("a")] += 1 
                    key = tuple(char_count)
                    anagram_map[key].append(s)
                return list(anagram_map.values())
                                                                            

        
            


        
        
           

            
            
        
       