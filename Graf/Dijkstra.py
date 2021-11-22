def Dijkstra(file, file2):                                                       #0 infoarena Memory limit exceeded
    import heapq                                                                 #Afisarea este corecta
    f = open(file, "r")
    g = open(file2, "w")
    n, m = [int(n) for n in f.readline().split()]
    L = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v, c = [int(n) for n in f.readline().split()]
        L[u].append([c, v])
    d = (n+1)*[float('inf')]
    d[1] = 0
    q = [[0, 1]]
    while q:
        u = heapq.heappop(q)[1]
        for l in L[u]:
            c, v = l
            if d[u] + c < d[v]:
                d[v] = d[u] + c
                heapq.heappush(q, l)
    g.write(" ".join(['0' if n == float('inf') else str(n) for n in d[2:]]))
Dijkstra("dijkstra.in", "dijkstra.out")