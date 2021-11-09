class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]: # Accepted
        d = [[] for _ in range(n)]
        for i in connections:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        nivel = n*[0]
        nivel_min = n*[0]
        visited = n*[False]
        critical = []
        def DFS(n):
            visited[n] = True
            nivel_min[n] = nivel[n]
            for i in d[n]:
                if visited[i] is False:
                    nivel[i] = nivel[n] + 1
                    DFS(i)
                    nivel_min[n] = min(nivel_min[n], nivel_min[i])
                    if nivel[n] < nivel_min[i]:
                        critical.append([n, i])
                elif nivel[i] < nivel[n] - 1:
                    nivel_min[n] = min(nivel[i], nivel_min[n])
        for i in range(n):
            if visited[i] is False:
                DFS(i)
        return critical