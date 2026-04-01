class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def isPalindrome(string):
            if string == string[::-1]:
                return True
            else:
                return False
        def dfs(i): # Recursively appends all palindromic substrings from i to the current part list,
                    # and explore all palindrome partitions of the string 
            if i >= len(s):
                res.append(part[:])
                return
            for j in range(i, len(s)):
                if isPalindrome(s[i : j + 1]):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res