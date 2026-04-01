class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itinerary = defaultdict(list)
        tickets.sort()  # To sort destinations in lexical order
        for ori, dest in tickets:
            itinerary[ori].append(dest)
        iti = ["JFK"]
        def path(city):
            if len(iti) == len(tickets) + 1:
                return True
            
            if city not in itinerary:
                return False

            temp = list(itinerary[city])    # Iterate over a copy as you dont want to iterate something changing.
            for i, dest in enumerate(temp):
                iti.append(dest)
                itinerary[city].pop(i)
                if path(dest): return True
                itinerary[city].insert(i, dest)
                iti.pop()
            return False
        
        path("JFK")
        return iti
        


