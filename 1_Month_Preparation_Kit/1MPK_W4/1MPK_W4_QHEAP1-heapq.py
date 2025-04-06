# Enter your code here. Read input from STDIN. Print output to STDOUT

import heapq

min_heap = []
delete_set = set()
## ... why use set ? because 
##      <
##          It is guaranteed that the element to be deleted will be there in the heap. 
##          Also, at any instant, only distinct elements will be in the heap.
##      >

num_queries = int(input())

for _ in range(num_queries):
    cmd = list(map(int, input().split()))
    
    if cmd[0] == 1:
        ## -> ... Add element
        heapq.heappush(min_heap, cmd[1])
    
    elif cmd[0] == 2 :
        ## -> ... <should> delete element, 
        ## but *actually* that only needs to be done before a print ...
        delete_set.add(cmd[1])
        
    elif cmd[0] == 3 : 
        ## -> ... Print minimum
        ## pop minimum if it is in delete_set, and remove that value from deleteset
        while min_heap and min_heap[0] in delete_set:
            delete_set.remove(heapq.heappop(min_heap))

        print(min_heap[0])
    
    else :
        pass    


## end .






