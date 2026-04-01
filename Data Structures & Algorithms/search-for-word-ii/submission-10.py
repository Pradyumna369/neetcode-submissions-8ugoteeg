class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        from collections import defaultdict

        letters = defaultdict(list)
        for r, row in enumerate(board):
            for c, ch in enumerate(row):
                letters[ch].append((r, c))

        present = set()
        wordList = {}
        for w in words:
            cur = wordList
            for ch in w:
                cur = cur.setdefault(ch, {})
            cur['*'] = ''  # word end marker

        rows, cols = len(board), len(board[0])
        seen = set()

        def wordExists(node, pos, word):
            if '*' in node:
                present.add(word)
                node.pop('*', None)   # prune found word

            r, c = pos
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen:
                    ch = board[nr][nc]
                    if ch in node:
                        seen.add((nr, nc))
                        wordExists(node[ch], (nr, nc), word + ch)
                        seen.remove((nr, nc))

        for ch in wordList:
            if ch in letters:
                for start in letters[ch]:
                    seen.add(start)
                    wordExists(wordList[ch], start, ch)
                    seen.remove(start)
        return list(present)
