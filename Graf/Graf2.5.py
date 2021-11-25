import collections
import sys
import heapq
class Graf:
    def Orientat(self):
        f = open(self.file, "r")
        L1 = [int(n) for n in f.readline().split()]
        d = [[] for _ in range(L1[0] + 1)]
        for i in range(L1[1]):
            n1, n2 = [int(n) for n in f.readline().split()]
            d[n1].append(n2)
        f.close()
        return L1, d

    def Neorientat(self):
        f = open(self.file, "r")
        L1 = [int(n) for n in f.readline().split()]
        d = [[] for _ in range(L1[0] + 1)]
        for i in f:
            n1, n2 = [int(n) for n in i.split()]
            d[n1].append(n2)
            d[n2].append(n1)
        f.close()
        return L1, d

    def Hakimi_Citire(self):
        f = open(self.file, "r")
        L = [int(n) for n in f.readline().split()]
        f.close()
        return L

    def Drum_Minim(self):
        f = open(self.file, "r")
        L1 = [int(n) for n in f.readline().split()]
        L = [[] for _ in range(L1[0] + 1)]
        for i in range(L1[1]):
            u, v, c = [int(n) for n in f.readline().split()]
            L[u].append([c, v])
        f.close()
        return L1, L

    def Multimi_Disjuncte(self):
        f = open(self.file, "r")
        L1 = [int(n) for n in f.readline().split()]
        L = []
        for i in range(L1[1]):
            L.append([int(n) for n in f.readline().split()])
        f.close()
        return L1, L

    def __init__(self, file, file2, cod):
        self.file = file
        self.file2 = file2
        self.cod = cod
        self.L1 = None
        self.L = None
        if cod == 1:
            self.L1, self.L = self.Neorientat()
        if cod == 2:
            self.L1, self.L = self.Orientat()
        if cod == 3:
            self.L1 = self.Hakimi_Citire()
        if cod == 4:
            self.L1, self.L = self.Multimi_Disjuncte()
        if cod == 5:
            self.L1, self.L = self.Drum_Minim()

    def BFS(self):
        g = open(self.file2, "w")
        n, m, s = self.L1
        d = self.L
        q = collections.deque()
        q.append(s)
        r = (n + 1) * [-1]
        r[s] = 0
        v = (n + 1) * [False]
        v[s] = True
        while q:
            n = q.popleft()
            for i in d[n]:
                if v[i] is False:
                    q.append(i)
                    v[i] = True
                    r[i] = r[n] + 1
        g.write(" ".join(str(n) for n in r[1:]))
        g.close()

    def DFS(self):
        sys.setrecursionlimit(10 ** 6)
        g = open(self.file2, "w")
        n, m = self.L1
        d = self.L
        r = 0
        v = (n + 1) * [False]

        def DFS_Recursie(n):
            v[n] = True
            for k in d[n]:
                if v[k] is False:
                    DFS_Recursie(k)
        for i in range(1, n + 1):
            if v[i] is False:
                r += 1
                DFS_Recursie(i)
        g.write(str(r))
        g.close()

    def CTC(self):
        sys.setrecursionlimit(10 ** 6)
        g = open(self.file2, "w")
        n, m = self.L1
        d = self.L
        ids = (n+1)*[0]
        lowlink = (n+1)*[0]
        ctc = []
        stack = collections.deque()
        onstack = (n+1) * [False]
        nid = 0

        def DFS(n):
            nonlocal nid
            nid += 1
            ids[n] = nid
            lowlink[n] = nid
            stack.append(n)
            onstack[n] = True
            for i in d[n]:
                if ids[i] == 0:
                    DFS(i)
                    lowlink[n] = min(lowlink[n], lowlink[i])
                elif onstack[i]:
                    lowlink[n] = min(lowlink[n], ids[i])
            if lowlink[n] == ids[n]:
                k = stack.pop()
                c = [k]
                onstack[k] = False
                while k != n:
                    k = stack.pop()
                    onstack[k] = False
                    c.append(k)
                ctc.append(c)

        for i in range(1, n + 1):
            if ids[i] == 0:
                DFS(i)
        g.write(str(len(ctc)))
        for c in ctc:
            g.write('\n' + " ".join(str(n) for n in c))
        g.close()

    def sortaret(self):
        g = open(self.file2, "w")
        n, m = self.L1
        d = self.L
        v = (n + 1) * [False]
        r = []

        def DFS(n):
            v[n] = True
            for k in d[n]:
                if v[k] is False:
                    DFS(k)
            r.append(n)

        for i in range(1, n + 1):
            if v[i] is False:
                DFS(i)

        g.write(" ".join(str(n) for n in r[::-1]))
        g.close()

    def Hakimi(self):
        g = open(self.file2, "w")
        L = self.L1

        def Recursie(L):
            L.sort(reverse=True)
            n = L[0]
            L = L[1:]
            if n > len(L):
                return "Nu"
            if n == 0:
                return "Da"
            for i in range(n):
                L[i] -= 1
                if L[i] < 0:
                    return "Nu"
            return Recursie(L)

        if sum(L) % 2 != 0:
            g.write("Nu")
        else:
            g.write(Recursie(L))
        g.close()

    def criticalConnections(self):
        g = open(self.file2, "w")
        n = self.L1[0]
        d = self.L
        nivel = n * [0]
        nivel_min = n * [0]
        visited = n * [False]
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
        g.write(str(critical))
        g.close()

    def Kruskal(self):
        g = open(self.file2, "w")
        n, m = self.L1
        L = self.L
        L.sort(key=lambda k: k[2])
        h = (n + 1) * [0]
        tata = (n + 1) * [0]
        R = []
        cost = 0

        def Reprezentare(u):
            while tata[u] != 0:
                u = tata[u]
            return u

        def Reuniune(u, v):
            ru, rv = Reprezentare(u), Reprezentare(v)
            if h[ru] > h[rv]:
                tata[rv] = ru
            else:
                tata[ru] = rv
                if h[ru] == h[rv]:
                    h[rv] += 1

        i = 0
        while len(R) < n - 1:
            if Reprezentare(L[i][0]) != Reprezentare(L[i][1]):
                u, v, c = L[i]
                R.append((u, v))
                cost += c
                Reuniune(u, v)
            i += 1
        g.write(str(cost) + "\n" + str(n - 1))
        for m in R:
            g.write("\n" + " ".join(str(n) for n in m))
        g.close()

    def Disjuncte(self):
        g = open(self.file2, "w")
        n, m = self.L1
        L = self.L
        h = (n + 1) * [0]
        tata = (n + 1) * [0]

        def Reprezentare(u):
            while tata[u] != 0:
                u = tata[u]
            return u

        def Reuniune(u, v):
            ru, rv = Reprezentare(u), Reprezentare(v)
            if h[ru] > h[rv]:
                tata[rv] = ru
            else:
                tata[ru] = rv
                if h[ru] == h[rv]:
                    h[rv] += 1

        for i in L:
            c, u, v = i
            if c == 1:
                Reuniune(u, v)
            else:
                if Reprezentare(u) != Reprezentare(v):
                    g.write("NU" + "\n")
                else:
                    g.write("DA" + "\n")
        g.close()

    def Dijkstra(self):
        g = open(self.file2, "w")
        n, m = self.L1
        L = self.L
        d = (n + 1) * [float('inf')]
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
        g.close()

    def Bellman(self):
        g = open(self.file2, "w")
        n, m = self.L1
        L = self.L
        d = (n + 1) * [float('inf')]
        d[1] = 0
        q = collections.deque()
        q.append([0, 1])
        stop = 0
        flag = True
        while q:
            if stop == n * m:
                flag = False
                break
            stop += 1
            u = q.popleft()[1]
            for l in L[u]:
                c, v = l
                if d[u] + c < d[v]:
                    d[v] = d[u] + c
                    q.append(l)
        if flag:
            g.write(" ".join(['0' if n == float('inf') else str(n) for n in d[2:]]))
        else:
            g.write("Ciclu negativ!")
        g.close()
Graf_a = Graf("bfs.in", "bfs.out", 2)
Graf_a.BFS()
Graf_b = Graf("ctc.in", "ctc.out", 2)
Graf_b.CTC()
Graf_c = Graf("dfs.in", "dfs.out", 1)
Graf_c.DFS()
Graf_d = Graf("hakimi.in", "hakimi.out", 3)
Graf_d.Hakimi()
Graf_e = Graf("sortaret.in", "sortaret.out", 2)
Graf_e.sortaret()
Graf_f = Graf("critical.in", "critical.out", 1)
Graf_f.criticalConnections()
Graf_g = Graf("apm.in", "apm.out", 4)
Graf_g.Kruskal()
Graf_h = Graf("disjoint.in", "disjoint.out", 4)
Graf_h.Disjuncte()
Graf_i = Graf("dijkstra.in", "dijkstra.out", 5)
Graf_i.Dijkstra()
Graf_j = Graf("bellmanford.in", "bellmanford.out", 5)
Graf_j.Bellman()