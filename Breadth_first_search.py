graph = [('A',['B','C']),
         ('B',['D', 'E']),
         ('C',['F']),
         ('D',[]),
         ('E',['F']),
         ('F',[])]

def bfs(graph):
    queue=[]
    visited=set()
    for i in graph:
        root=i[0]
        if(root not in visited):
            queue=queue+[root]
            visited.add(root)
        possibilities=[]
        for j in i[1]:
            if(j not in visited):
                possibilities=possibilities+[j]
                visited.add(j)
            else:
                pass
        queue=queue+possibilities
    return(queue)
print(bfs(graph))
