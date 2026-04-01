class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        letters = defaultdict(list) # Positions of the letters in the board
        for row, i in enumerate(board):
            for col,letter in enumerate(i):
                letters[letter].append((row, col))
        seen = set()
        present = set() # Words present in the board
        wordList = {}   # Words as a trie
        for word in words:
            cur = wordList
            for letter in word:
                if letter not in cur:
                    cur[letter] = {}
                cur = cur[letter]
            cur['*'] = ''

        l = len(board)
        # def wordExists(index, element, word):
        #     if index == len(word) - 1:
        #         return True
        #     row, col = element
        #     explore = [[-1,0], [1,0], [0,-1], [0,1]]
        #     for each in explore:
        #         dx, dy = each
        #         x = col + dx
        #         y = row + dy
        #         if (y, x) not in seen and 0 <= x < len(board[0]) and 0 <= y < len(board):
        #             if board[y][x] == word[index + 1]:
        #                 seen.add((y, x))
        #                 if wordExists(index + 1, [y, x], word):
        #                     return True
        #                 seen.remove((y,x))
        def wordExists(letter, element, word):
            if '*' in letter:
                present.add(word)
                letter.pop('*', None)
            # for later in letter:
            row, col = element
            explore = [[-1,0], [1,0], [0,-1], [0,1]]
            for each in explore:
                dx, dy = each
                x = col + dx
                y = row + dy
                if (y, x) not in seen and 0 <= x < len(board[0]) and 0 <= y < len(board):
                    later = board[y][x]
                    if later in letter:
                        seen.add((y, x))
                        newWord = word + later
                        wordExists(letter[later], [y, x], newWord)
                        seen.remove((y,x))           
        # for word in words:
        #     first = word[0]
        #     for each in letters[first]:
        #         seen.add(each)
        #         if wordExists(0, each, word):
        #             present.add(word)
        #             break
        #         seen.remove(each)
        # return list(present)
        cur = wordList
        for letter in cur:
            word = ""
            for each in letters[letter]:
                seen.add(each)
                newWord = word + letter
                wordExists(wordList[letter], each, newWord)
                seen.remove(each)
            seen.clear()
        return list(present)



                    
                




        
        