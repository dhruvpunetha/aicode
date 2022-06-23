'''def dfs(graph,start,visited=None):
    if visited is None:
        visited=set()
    visited.add(start) 
    print(start) 

    for net in graph[start]:
        if(net not in visited):
            dfs(graph,net,visited) 
    return visited 

graph={
    '0': set(['1','2']),
    '1': set(['0','3','5']),
    '2': set(['0','4']),
    '3': set(['1']),
    '4': set(['2']),
    '5': set(['1'])
}
dfs(graph,'0')'''

def DFS(graph, start, goal, visited):
    visited.add(start)
    
    

    if start==goal:
        return

    for neighbour in graph[start]:
        if neighbour not in visited:
            print(neighbour,end=" ")
            DFS(graph, neighbour, goal, visited)

graph = {
    'S' : {'A':3, 'B':2},
    'A' : {'C':4, 'D':1, 'S':3},
    'B' : {'E':3, 'F':1, 'S':2},
    'C' : {'A':4},
    'D' : {'A':1},
    'E' : {'B':3, 'H':5},
    'F' : {'B':1, 'I':2, 'G':3},
    'G' : {'F':3},
    'I' : {'F':2},
    'H' : {'E':5}
}

DFS(graph, 'S', 'G', set())
