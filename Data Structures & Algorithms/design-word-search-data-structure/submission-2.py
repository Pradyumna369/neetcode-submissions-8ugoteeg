class WordDictionary:
    '''
    addWord(word)
    search(word) -> true/false
    1 <= word.length <= 20
    lowercase English letters, atmost 2 .'s
    dictionary = {
            d  : {
                e:{
                },
                a: {
                    y: {
                        * : True
                    }
                }
            }
        }
    word = "d.y"
    possible = [da, de]
    word = day -> True
    '''

    def __init__(self):
        self.dictionary = {}

    def addWord(self, word: str) -> None:
        cur = self.dictionary
        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                cur[c] = {}
                cur = cur[c]
        cur['*'] = {}

    def search(self, word: str) -> bool:
        cur = self.dictionary
        possible = deque([cur])
        for c in word:
            l = len(possible)
            for _ in range(l):
                cur = possible.popleft()
                if c == '.':
                    for each in cur:
                        possible.append(cur[each])
                else:
                    if c in cur:
                        possible.append(cur[c])
        for node in possible:
            if '*' in node:
                return True
        return False
            











        
