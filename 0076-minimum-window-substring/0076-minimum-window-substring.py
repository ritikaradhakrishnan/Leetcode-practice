class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #edge case
        if t == "":
            return ""
        
        countT, window = {}, {}
        
        #t's hash map for reference and comparison
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        
        #need would be length of t's hash map to have unique characters in t
        have, need = 0, len(countT)

        #any value would be less than inf so perfect to update
        minResultLength = float("infinity")
        #result is a list with dummy values easy to update any index greater
        result = [-1, -1]

        l = 0

        #lets move through string s:
        # 1. Count every letter and update in window hashmap
        # 2. if that letter in t's hashmap check if both hashmaps equal, then increase have
        # 3. decrement l pointer while have==need

        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                have += 1
            
            while have == need:
                # update our result
                if (r-l+1) < minResultLength:
                    result = [l, r]
                    minResultLength = r-l+1
                #While condition is met we want to keep shrinking the window, pop from left of our window
                window[s[l]] -= 1
                #since we popped from left, its possible have != need
                #check if the char is needed to statisfy ==
                #and check if len(window's hahmap) < reference hashmap
                # if so -> decrement have 
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                #l pointer in the string s needs to move on
                l += 1
            
        l, r = result
        return s[l:r+1] if minResultLength!= float("infinity") else ""

                




        