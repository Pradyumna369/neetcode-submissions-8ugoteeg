class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''
        s = "xyxxyzbzbbisl"
                       ^
        end = 9
        count = 3
        last = {
            x: 3
            y: 4
            }   
        end = 0
        substring = max(end, last[i])      
        '''
        last = defaultdict(int)
        for i, c in enumerate(s):
            last[c] = i

        ans = []
        end = 0
        count = 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            count += 1
            if end == i:
                ans.append(count)
                count = 0
        
        return ans

