# Enter your code here. Read input from STDIN. Print output to STDOUT

numQ = int(input().strip())

if numQ > 0:
    queue = []
    
    for _ in range(numQ) :
        cmd = input().strip().split()
        if int(cmd[0]) == 1 :
            ## Enqueue
            queue.append(int(cmd[1]))
        elif int(cmd[0]) == 2 : 
            ## Dequeue
            queue = queue[1:]
        elif int(cmd[0]) == 3 : 
            ## Print front
            print(queue[0])
        ## else continue
    




