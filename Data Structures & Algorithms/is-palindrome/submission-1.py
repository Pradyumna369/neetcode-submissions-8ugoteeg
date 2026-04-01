class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for char in s:
            if char.isalnum():
                string += char.lower()
        # l = len(string)
        # if l % 2 == 0:
        #     i = (l // 2) - 1
        #     j = l // 2
        # else:
        #     i = l // 2 - 1
        #     j = l // 2 + 1
        # while i >= 0 and j < l:
        #     if string[i] != string[j]:
        #         return False
        #     i -= 1
        #     j += 1
        # return True
        return string == string[::-1]
        
        