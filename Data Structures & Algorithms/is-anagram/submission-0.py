class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ideas: use hashmap, run through s once
        # if char not in seen, add that char into hashmap 
        # if char in seen, +1 it value

        seen = {}

        for n in s:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1

        map = {}

        for n in t:
            if n in map:
                map[n] += 1
            else:
                map[n] = 1

        if map == seen:
            return True
        return False