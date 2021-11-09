import sys
sys.setrecursionlimit(10 ** 6)

def DFS(file, file2):        # 75 infoarena: time limit exceeded
    f = open(file, "r")
    g = open(file2, "w")
    n, m = [int(n) for n in f.readline().split()]
    d = [[] for _ in range(n + 1)]
    for i in range(m):
        n1, n2 = [int(n) for n in f.readline().split()]
        d[n1].append(n2)
        d[n2].append(n1)
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
    f.close()
    g.close()


DFS("dfs.in", "dfs.out")

