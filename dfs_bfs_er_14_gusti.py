import bisect as bs
from collections import deque as d

test = [1,8,15,23,45,78,125,156]
chk = 15
a = bs.bisect_right(test,15)
print('first insert position of item',chk, "in the given sorted array",a)
 
recursive_bfs_order = []
def recursive_bfs(starting_node,graph,q,recursive_bfs_visited):
    if not q:
        return
    cur = q.popleft()
    recursive_bfs_order.append(cur)
    recursive_bfs_visited.add(cur)
    for item in graph[cur]:
        if item not in recursive_bfs_visited:
            q.append(item)
            recursive_bfs_visited.add(item)
        
    recursive_bfs(cur,graph,q,recursive_bfs_visited)

def iterative_bfs(starting_node,graph):
    q = d([[starting_node,0]])
    visited = set()
    level_order = {}
    bfs_order = []
    while q:
        cur = q.popleft()
        level = cur[1]
        cur_node = cur[0]
        visited.add(cur_node)
        bfs_order.append(cur_node)
        if level not in level_order:
            level_order[level] = [cur_node]
        else:
            level_order[level].append(cur_node)
        for item in graph[cur_node]:
            if item not in visited:
                q.append([item,level+1])
    return bfs_order


recursive_dfs_order = []
def recursive_dfs(starting_node, graph, visited):
    if starting_node not in visited:
        visited.add(starting_node)
        recursive_dfs_order.append(starting_node)
    else:
        return
    for item in graph[starting_node]:
        recursive_dfs(item,graph,visited)
        
def iterative_dfs(starting_node,graph):
    st = [starting_node]
    visited = set()
    dfs_order = []
    while st:
        cur_node = st.pop()
        visited.add(cur_node)
        dfs_order.append(cur_node)
        for item in graph[cur_node]:
            if item not in visited:
                st.append(item)
    return dfs_order

graph = {1: [2,3,4], 2: [1,5,6], 3:[1,7], 4: [1,8,9,10], 5: [2], 6:[2], 7: [3], 8: [1,4], 9: [4], 10: [4]}

recursive_bfs(1,graph,d([1]),set())
print('recursive bfs traverse order', recursive_bfs_order)
print('iterative bfs traverse order', iterative_bfs(1,graph))
recursive_dfs(1,graph,set())
print('recursive dfs traverse order', recursive_dfs_order)
print('iterative dfs traverse order', iterative_dfs(1,graph))