def BFS(graph , start):
    queue = [start]
    visited = {start}
    while queue:
        vertex = queue.pop(0)
        for ne in graph[vertex]:
            visited.add(ne)
            queue.append(ne)
    return visited
def DFS(graph , start , visited):
    visited[start] = True
    for ne in graph[start]:
        if not visited[ne]:
            DFS(graph , ne , visited)
Code Breakdown
BFS: Uses queue. Pop(0) gets the first element.
DFS: Uses recursion. Visits neighbors depth-first.