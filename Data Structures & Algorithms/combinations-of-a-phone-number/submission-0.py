class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        number -> characters[]
        2-9
        combinations

        digits = 34
        [d/e/f],[g/h/i]
        '''
        if digits == "":
            return []
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        ans = []
        def backtrack(i, word):
            if i == len(digits):
                ans.append(word)
                return
            possibilities = mapping[digits[i]]
            for each in possibilities:
                newWord = word + each
                backtrack(i + 1, newWord)
        backtrack(0, "")
        return ans


        