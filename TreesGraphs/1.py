# Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes.

import queue

# Directed graph
graph1 = {
    'a':['c'],
    'b':['d'],
    'c':['e'],
    'd':['a','d'],
    'e':['b','c'] 
}

def findPath(graph,start,end,path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            path = findPath(graph,node,end,path)
    return path


def breathFirstSearch(graph1,start,end):
    if start == end:
        return True
    q = queue.Queue(len(graph1))
    visited = []
    visited.append(start)
    q.put(start)
    while not q.empty():
        r = q.get()
        if r != None:
            for n in graph1[r]:
                if n not in visited:
                    if n == end:
                        return True
                    else:
                        q.put(n)
                    visited.append(n)
    
    return False



print(findPath(graph1,'b','e',[]))
print(breathFirstSearch(graph1,'b','e'))