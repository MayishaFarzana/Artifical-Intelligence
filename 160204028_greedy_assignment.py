inf = 10000000
h = [55, 42, 34, 25, 20, 17, 0, inf, 80]

graph = [ [(2, 22), (3, 32), (8, 35)],
[(8, 45), (4, 36), (5, 27), (3, 28)],
[(0, 22), (3, 31), (6, 47)],
[(0, 32), (2, 31), (1, 28), (6, 30)],
[(1, 36), (6, 26)],
[(1, 27)],
[(2, 47), (3, 30), (4, 26)],
[],
[(0, 35), (1, 45)] ]

from queue import PriorityQueue
Q = PriorityQueue()

def empty():
    return Q.empty()
def push(val):
    Q.put(val)
def pop():
    if (empty()):
        return None
    return Q.get()

# push(5)
# push(1)
# push(10)
# push(20)
# push(2)
#
# while (empty() == False):
#     print(pop())

def gready_best_first():
    source = 8 # i
    goal = 6 # g
    parent = [-1] * len(graph)
    vis = [False] * len(graph)

    push((h[source], source))
    vis[source] = True
    while (empty() == False):
        u = pop()
        if (u[1] == goal):
            break
        #cost = u[0]
        #node_name = u[1]
        for adj in graph[u[1]]:
            v = adj[0]
            if (vis[v] == False):
                push((h[v], v))
                vis[v] = True
                parent[v] = u[1]


    # finding path
    tmp = goal
    sum = 0
    print("Possible path is: ", end = ' ')
    while (parent[tmp] != -1):
        u = parent[tmp]
        v = tmp
        print(chr(ord('a') + tmp), end = ' ')
        for adj in graph[u]:
            if (adj[0] == v):
                sum += adj[1]
                break
        tmp = parent[tmp]
    print(chr(ord('a') + tmp))
    print("Total path cost = ", sum)

gready_best_first()
