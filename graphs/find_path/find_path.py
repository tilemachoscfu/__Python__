myGraph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D', 'F'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

# find path from start to end using recursion with backtracking
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if (start == end):
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            return newpath
    return None

# find all path
def find_all_path(graph, start, end, path=[]):
    path = path + [start]
    print(path)
    if (start == end):
        return [path]
    if not start in graph:
        return None
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_path(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

print(find_all_path(myGraph, 'A', 'F'))
