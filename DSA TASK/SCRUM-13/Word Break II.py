from typing import List

def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    # Helper function to perform DFS
    def dfs(s: str, wordDict: set, start: int, memo: dict) -> List[str]:
        # If we've reached the end of the string, return a list containing an empty string
        if start == len(s):
            return [""]
        
        # If we've already computed the result for this start position, return it
        if start in memo:
            return memo[start]
        
        res = []
        for end in range(start + 1, len(s) + 1):
            # If the current substring is a valid word
            if s[start:end] in wordDict:
                # Get all the segmentations for the remaining substring
                sublist = dfs(s, wordDict, end, memo)
                for sub in sublist:
                    # If sub is not empty, add a space before it
                    if sub:
                        res.append(s[start:end] + " " + sub)
                    else:
                        res.append(s[start:end])
        
        # Memoize the result
        memo[start] = res
        return res
    
    # Convert wordDict to a set for faster lookups
    wordSet = set(wordDict)
    # Initialize memoization dictionary
    memo = {}
    # Call the helper function
    return dfs(s, wordSet, 0, memo)

# Example usage
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(wordBreak(s, wordDict))
