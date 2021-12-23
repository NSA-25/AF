import collections
import sys
import heapq

sys.setrecursionlimit(10 ** 6)


class Graf:
    # Functiile de citire a grafurilor
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

    def Floyd_Citire(self):
        f = open(self.file, "r")
        n = int(f.readline())
        M = []
        for i in range(n):
            l = [float('inf') if (e == 0) else e for e in [int(n) for n in f.readline().split()]]
            l[i] = 0
            M.append(l)
        f.close()
        return n, M

    # Constructorul de graf, avand ca date fisierele de intrare si iesire si datele din fisier
    # Este utilizat si un cod pentru identificarea tipului de graf
    def __init__(self, file, file2, cod):
        self.file = file
        self.file2 = file2
        self.cod = cod
        self.L1 = None  # Datele de pe prima linie
        self.L = None  # Restul datelor
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
        if cod == 6:
            self.L1, self.L = self.Floyd_Citire()

    #Functiile de rezolvare a problemelor
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
        g = open(self.file2, "w")
        n, m = self.L1
        d = self.L
        ids = (n + 1) * [0]
        lowlink = (n + 1) * [0]
        ctc = []
        stack = collections.deque()
        onstack = (n + 1) * [False]
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

        if len(L) == 0:
            g.write("Da")
        elif sum(L) % 2 != 0:
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
        q.append(1)
        stop = 0
        flag = True
        while q:
            if stop == n * m:
                flag = False
                break
            stop += 1
            u = q.popleft()
            for l in L[u]:
                c, v = l
                if d[u] + c < d[v]:
                    d[v] = d[u] + c
                    q.append(v)
        if flag:
            g.write(" ".join(['0' if n == float('inf') else str(n) for n in d[2:]]))
        else:
            g.write("Ciclu negativ!")
        g.close()

    def Darb(self):
        g = open(self.file2, "w")
        n = self.L1[0]
        L = self.L
        viz = (n + 1) * [False]
        viz[1] = True
        r = 1
        u = 1

        def DFS(n, h):
            nonlocal r, u
            h += 1
            if h > r:
                r = h
                u = n
            viz[n] = True
            for k in L[n]:
                if viz[k] is False:
                    DFS(k, h)

        def DFS2(n, h):
            nonlocal r
            h += 1
            if h > r:
                r = h
            viz[n] = False
            for k in L[n]:
                if viz[k]:
                    DFS2(k, h)

        DFS(1, 0)
        r = 0
        DFS2(u, 0)
        g.write(str(r))
        g.close()

    def RoyFloyd(self):
        g = open(self.file2, "w")
        n = self.L1
        M = self.L
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if M[i][j] > M[i][k] + M[k][j]:
                        M[i][j] = M[i][k] + M[k][j]
        g.write(('\n'.join([' '.join([str(i) for i in l]) for l in M])))
        g.close()

    def Euler(self):
        g = open(self.file2, "w")
        n = self.L1[0]
        L = self.L
        for i in range(1, n):
            if len(L[i]) % 2:
                g.write("-1")
                return None
        circuit = []
        drum = collections.deque()
        drum.append(1)
        while drum:
            u = drum[-1]
            if L[u]:
                v = L[u].pop()
                drum.append(v)
                L[v].remove(u)
            else:
                circuit.append(drum.pop())
        g.write(" ".join(str(x) for x in circuit[:-1]))


# Functie meniu pentru a alege ce problema sa fie rezolvata
def Meniu():
    n = int(input(
        "1 BFS\n2 CTC\n3 DFS\n4 Havel-Hakimi\n5 Sortare topologica\n6 Muchie critica\n7 Kruskal\n8 Multimi "
        "Disjuncte\n9 Dijkstra\n10 Bellman-Ford\n "
        "11 Diametrul unui arbore\n12 Roy-Floyd\n13 Ciclu eulerian\nInput: "))
    if n == 1:
        Graf_a = Graf("bfs.in", "bfs.out", 2)
        Graf_a.BFS()
    elif n == 2:
        Graf_b = Graf("ctc.in", "ctc.out", 2)
        Graf_b.CTC()
    elif n == 3:
        Graf_c = Graf("dfs.in", "dfs.out", 1)
        Graf_c.DFS()
    elif n == 4:
        Graf_d = Graf("hakimi.in", "hakimi.out", 3)
        Graf_d.Hakimi()
    elif n == 5:
        Graf_e = Graf("sortaret.in", "sortaret.out", 2)
        Graf_e.sortaret()
    elif n == 6:
        Graf_f = Graf("critical.in", "critical.out", 1)
        Graf_f.criticalConnections()
    elif n == 7:
        Graf_g = Graf("apm.in", "apm.out", 4)
        Graf_g.Kruskal()
    elif n == 8:
        Graf_h = Graf("disjoint.in", "disjoint.out", 4)
        Graf_h.Disjuncte()
    elif n == 9:
        Graf_i = Graf("dijkstra.in", "dijkstra.out", 5)
        Graf_i.Dijkstra()
    elif n == 10:
        Graf_j = Graf("bellmanford.in", "bellmanford.out", 5)
        Graf_j.Bellman()
    elif n == 11:
        Graf_k = Graf("darb.in", "darb.out", 1)
        Graf_k.Darb()
    elif n == 12:
        Graf_l = Graf("royfloyd.in", "royfloyd.out", 6)
        Graf_l.RoyFloyd()
    elif n == 13:
        Graf_m = Graf("ciclueuler.in", "ciclueuler.out", 1)
        Graf_m.Euler()
    else:
        print("Input invalid!")


Meniu()
