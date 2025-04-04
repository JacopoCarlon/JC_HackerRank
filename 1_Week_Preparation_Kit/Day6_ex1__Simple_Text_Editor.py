# Enter your code here. Read input from STDIN. Print output to STDOUT


q = int(input())

string = ""
oldString = []
oldString.append(string)

for i in range(0, q):
    cmd = input().split(" ")
    
    #print(f'iter:{i} _ cmd:{cmd} ; string:{string} ; oldString:{oldString}')
    
    if cmd[0] == "1" :
        ## append
        oldString.append(string)
        string = string + str(cmd[1])
        
    if cmd[0] == "2" :
        ## delete(k)
        k = int(cmd[1])
        oldString.append(string)
        if len(string) > k : 
            string = string[:-k]
        else :
            string = ""
            
    if cmd[0] == "3" :
        ## print k-th element
        k = int(cmd[1])-1
        if k<0 : 
            pass
        else :
            if len(string) >= k :
                print( f'{string[k]}' )
    
    if cmd[0] == "4":
        ## undo last operation
        string = oldString.pop(-1)

    #print(f'iter:{i}end _ cmd:{cmd} ; string:{string} ; oldString:{oldString}')
