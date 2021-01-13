#initializing the graph
adj_list={ 'A' : ['B','C'], 'B' : ['D', 'E'], 'C' : ['F'], 'D' : [], 'E' : ['F'], 'F' : [] }
status={}
output=[]
parent={}

#initializing the colour of the nodes
for node in adj_list.keys():
    status[node]='Unvisited'
    
#algorithm
def dfs(u):
    global adj_list
    if(status[u]=='Unvisited'):
        status[u]='Visited'
        output.append(u)
        for v in adj_list[u]:
            if(status[v]=='Unvisited'):
                dfs(v)
    return(output)

#main
x=input('Enter the root node:')
traversal=dfs(x)
s=''
for i in range(len(traversal)-1):
    s=s+traversal[i]+'->'
s=s+traversal[-1]
print(s)
