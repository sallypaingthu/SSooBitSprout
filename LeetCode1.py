###############
### HASHMAP ###
###############
# -----------------------------------------------------------------------------
# 383. Ransom Note
# -----------------------------------------------------------------------------
# Given two strings ransomNote and magazine, 
# return true if ransomNote can be constructed by using the letters 
# from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
print("383. Ransom Note")
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # Create a hashmap to count characters in the magazine
        magazine_count = {}
    
        # Count occurrences of each letter in the magazine
        for char in magazine:
            if char in magazine_count:
                magazine_count[char] += 1
            else:
                magazine_count[char] = 1
    
        # Check if we can construct the ransomNote
        for char in ransomNote:
            if char in magazine_count and magazine_count[char] > 0:
                magazine_count[char] -= 1
            else:
                return False
        return True
    
solution = Solution()
print(solution.canConstruct("a", "b"))      # Output: False
print(solution.canConstruct("aa", "ab"))    # Output: False
print(solution.canConstruct("aa", "aab"))   # Output: True
print("-" * 80)

# -----------------------------------------------------------------------------
# 205. Isomorphic Strings
# -----------------------------------------------------------------------------
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character 
# while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.
print("205. Isomorphic Strings")
class Solution(object):
    def isIsomorphic(self, s, t):
        # Check if lengths are the same
        if len(s) != len(t):
            return False
        
        # Hashmaps for character mapping
        s_to_t = {}
        t_to_s = {}
        
        # Iterate through the indices of the strings
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            
            # Check mapping from s to t
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t
            
            # Check mapping from t to s
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s
            
        return True
    
solution = Solution()
print(solution.isIsomorphic("egg", "add"))      # Output: True
print(solution.isIsomorphic("foo", "bar"))      # Output: False
print(solution.isIsomorphic("paper", "title"))  # Output: True
print(solution.isIsomorphic("ab", "aa"))        # Output: False
print("-" * 80)

# -----------------------------------------------------------------------------
# 290. Word Pattern
# -----------------------------------------------------------------------------
# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection 
# between a letter in pattern and a non-empty word in s. Specifically:
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
print("290. Word Pattern")
class Solution(object):
    def wordPattern(self, pattern, s):
        # Split the string into words
        words = s.split()
        
        # If lengths differ, return False
        if len(pattern) != len(words):
            return False

        # Create mapping dictionaries
        char_to_word = {}
        word_to_char = {}

        # Traverse both pattern and words simultaneously
        for char, word in zip(pattern, words):
            # Check character to word mapping
            if char not in char_to_word:
                char_to_word[char] = word
            elif char_to_word[char] != word:
                return False

            # Check word to character mapping
            if word not in word_to_char:
                word_to_char[word] = char
            elif word_to_char[word] != char:
                return False

        return True

solution = Solution()
print(solution.wordPattern("abba", "dog cat cat dog"))   # Output: True
print(solution.wordPattern("abba", "dog cat cat fish"))  # Output: False
print(solution.wordPattern("aaaa", "dog cat cat dog"))   # Output: False
print(solution.wordPattern("abab", "red blue red blue")) # Output: True
print("-" * 80)

# -----------------------------------------------------------------------------
# 242. Valid Anagram
# -----------------------------------------------------------------------------
# Given two strings s and t, return true if t is anagram of s, and false otherwise.
print("242. Valid Anagram")
class Solution(object):
    def isAnagram(self, s, t):
        # Step 1: Check if lengths are the same
        if len(s) != len(t):
            return False
        
        # Step 2: Count characters
        count = {}
        for char in s:
            # if count dictionary doesn't have this char as key,
            #   do 0+1
            # else n+1
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False
        
        return True
    
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Output: True
print(solution.isAnagram("rat", "car"))          # Output: False
print(solution.isAnagram("listen", "silent"))    # Output: True
print(solution.isAnagram("hello", "billion"))    # Output: False
print("-" * 80)

# -----------------------------------------------------------------------------
# 49. Group Anagrams
# -----------------------------------------------------------------------------
# Given an array of strings strs, group the anagrams  together. 
# You can return the answer in any order.
print("49. Group Anagrams")
class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}
        
        for s in strs:
            # Create a character count tuple
            char_count = [0] * 26  # For lowercase English letters
            
            # Reset Index to Zero for Unicode code point of character
            # and +1 for char in s # ord('a') is 97
            for char in s:
                char_count[ord(char) - ord('a')] += 1
                
            # Convert the list to a tuple to use as a dictionary key
            count_key = tuple(char_count)
            
            # Append the original string to the list of its anagrams
            if count_key not in anagrams:
                anagrams[count_key] = []
            anagrams[count_key].append(s)
        
        # Return the grouped anagrams as a list of lists
        return list(anagrams.values())

solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

print(solution.groupAnagrams([""]))  
# Output: [[""]]

print(solution.groupAnagrams(["a"]))  
# Output: [["a"]]
print("-" * 80)

# -----------------------------------------------------------------------------
# 1. Two Sum
# -----------------------------------------------------------------------------
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.
print("1. Two Sum")
class Solution(object):
    def twoSum(self, nums, target):
        nums_dict = {}
        
        for i in range(len(nums)):
            
            # Calculate the number needed to reach the target
            search_num = target - nums[i]
            
            # Check if the needed number is already in the dictionary
            if search_num in nums_dict:
                return [nums_dict[search_num], i]
            
            # Store the index of the current number
            nums_dict[nums[i]] = i
            
        return []

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))   # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))        # Output: [1, 2]
print(solution.twoSum([3, 3], 6))           # Output: [0, 1]
print(solution.twoSum([1, 5, 3, 2], 8))     # Output: []
print("-" * 80)

# -----------------------------------------------------------------------------
# 202. Happy Number
# -----------------------------------------------------------------------------
# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, 
# replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), 
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
print("202. Happy Number")
class Solution(object):
    def isHappy(self, n):
        def get_next(number):
            total_sum = 0
            while number > 0:
                digit = number % 10     # Last digit
                total_sum = total_sum + digit ** 2
                number = number // 10   # Front digit
            return total_sum

        seen = {} # Hash map to track seen numbers
        while n != 1:
            if n in seen:
                return False  # Cycle detected
            seen[n] = True    # Mark the number as seen
            n = get_next(n)
        return True  # Happy number found
    
solution = Solution()
print(solution.isHappy(19))  # Output: True (19 is a happy number)
print(solution.isHappy(2))   # Output: False (2 is not a happy number)
print(solution.isHappy(7))   # Output: True (7 is a happy number)
print(solution.isHappy(4))   # Output: False (4 is not a happy number)
print("-" * 80)

# -----------------------------------------------------------------------------
# 219. Contains Duplicate II
# -----------------------------------------------------------------------------
# Given an integer array nums and an integer k, 
# return true if there are two distinct indices i and j in the array 
# such that nums[i] == nums[j] and abs(i - j) <= k.
print("219. Contains Duplicate II")
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        index_map = {}
        
        for i, num in enumerate(nums):
            if num in index_map:
                # Check if the previous index is within the range k
                if abs(i - index_map[num]) <= k:
                    return True
            
            # Update the current index of the number
            index_map[num] = i
            
        return False
    
solution = Solution()
print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))        # Output: True
print(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))        # Output: True
print(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # Output: False
print(solution.containsNearbyDuplicate([], 0))                  # Output: False
print("-" * 80)

# -----------------------------------------------------------------------------
# 128. Longest Consecutive Sequence
# -----------------------------------------------------------------------------
# Given an unsorted array of integers nums, 
# return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
print("128. Longest Consecutive Sequence")
class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # Only start counting streaks from the beginning of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
    
solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4 (1, 2, 3, 4)
print(solution.longestConsecutive([0, -1]))                 # Output: 2 (-1, 0)
print(solution.longestConsecutive([]))                      # Output: 0
print(solution.longestConsecutive([1, 2, 3, 4, 5]))        # Output: 5 (1, 2, 3, 4, 5)
print(solution.longestConsecutive([5, 7, 8, 9, 10, 11]))   # Output: 6 (5, 6, 7, 8, 9, 10, 11)
print("-" * 80)