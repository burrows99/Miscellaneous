graph=[[0,2,4,0,0,0],
       [0,0,1,7,0,0],
       [0,0,0,0,3,0],
       [0,0,0,0,0,1],
       [0,0,0,2,0,5],
       [0,0,0,0,0,0]]
inf=9999999999999
def repeating(graph,node,d,n):
    if(n==0):
        return(d)
    else:
        minDistance=inf
        for distance in graph[node]:
            if(distance!=0):
                minDistance=min(minDistance,distance)
        nextNode=graph[node].index(minDistance)
        d[nextNode]=min(d[nextNode],graph[node][nextNode]+d[node])
        return(repeating(graph,nextNode,d,n-1))
def dijkstra(graph,source):
    #initialization
    n=len(graph)
    d=[inf]*n
    d[source]=0
    for node,distance in enumerate(graph[source]):
        if(distance!=0):
            d[node]=distance
    minDistance=inf
    for distance in d:
        if(distance!=0):
            minDistance=min(minDistance,distance)
    node=d.index(minDistance)
    
    #algorithm starts
    return(repeating(graph,node,d,n-2))
source=0
print(dijkstra(graph,source))
