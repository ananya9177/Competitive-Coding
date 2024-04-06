from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        ans = []
        pdic = Counter(p)
        k = len(p)
        
        # Initial sliding window
        window = Counter(s[:k])
        
        # Check if the initial window is an anagram
        if window == pdic:
            ans.append(0)
        
        # Move the sliding window along the string
        for i in range(1, len(s) - k + 1):
            # Update the sliding window by adding the new character and removing the old character
            window[s[i + k - 1]] += 1
            window[s[i - 1]] -= 1
            
            # Remove keys with zero count to keep the window Counter compact
            if window[s[i - 1]] == 0:
                del window[s[i - 1]]
            
            # Check if the current window is an anagram
            if window == pdic:
                ans.append(i)
        
        return ans

        
