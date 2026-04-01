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

        def wordExists(letter, element, word):
            if '*' in letter:
                present.add(word)
                # letter.pop('*', None)
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
        cur = wordList
        for letter in cur:
            for each in letters[letter]:
                seen.add(each)
                wordExists(wordList[letter], each, letter)
                seen.remove(each)
        return list(present)



                    
                




        
        