# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        lists = [[1, 1, 2, 3, 4], [1, 3, 5],[3, 6]]
                              ^
                                         ^ 
                                          ^
        0 <= lists.length <= 1000
        0 <= lists[i].length <= 100
        -1000 <= lists[i][j] <= 1000
        '''
        if lists == [] or lists == [[]]:
            return None
        heap = []
        count = 0
        for each in lists:
            if each:
                first = [each.val, count, each]
                heapq.heappush(heap, first)
                count += 1

        dummy = curr = ListNode()
        while heap:
            _, _, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, [node.next.val, count, node.next])
                count += 1
            
        return dummy.next

        # while heap:
        #     _, _, node = heapq.heappop(heap)
        #     curr.next = node
        #     curr = curr.next
        #     if node.next:
        #         if heap and node.next.val <= heap[0][0]:
        #             curr.next = node.next
        #             curr = curr.next
        #             node = node.next
        #         if node.next:
        #             heapq.heappush(heap, [node.next.val, count, node.next])
        #             count += 1
        
        # return dummy.next