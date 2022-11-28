"""
BREADTH-FIRST SEARCH algorithm
1. Set initial state as the first path of the list
2. While first path does not reach the goal and list is not empty:
    a) Get the first path of the list
    b) Expand the path obtained in previous step
    c) Remove cycles from paths obtained in previous step
    d) Insert remaining paths at the end of the list
3. If the list is not empty, return the first path of the list
else (list is empty), there is not any solution
"""

def expand(l, net):
    res = []
    city = l[-1]
    successors = net[city]
    for i in successors:
        newPath = l.copy()
        newPath.append(i)
        res.append(newPath)
    return res

def removeCycles(l):
    return list(filter(lambda x: x[-1] not in x[:-1], l))

def breadth_first(initial, goal, net):
    print("SEARCHING PATH FROM",initial,"TO",goal,"...\n")
    L = []
    L.append([initial])
    while L and L[0][-1] != goal:
        first = L.pop(0)
        res = expand(first, net)
        res = removeCycles(res)
        L = L + res
    if L:
        print("Solution: ", L[0])
    else:
        print("Ther Is No Solution")

net = {}
net['Barcelona']=['Paris','Rome']
net['Paris']=['Barcelona','London','Berlin','Rome']
net['Rome']=['Barcelona','Paris','Berlin']
net['London']=['Paris','Berlin']
net['Berlin']=['Paris','London','Rome','Vienna','Warsaw']
net['Vienna']=['Berlin','Warsaw','Athens']
net['Warsaw']=['Berlin','Vienna','Moscow']
net['Belgrade']=['Athens','Moscow']
net['Athens']=['Vienna','Belgrade','Moscow']
net['Moscow']=['Warsaw','Belgrade','Athens']

breadth_first('Barcelona','Warsaw',net)