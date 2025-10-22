import heapq
import collections
def countPaths(n:int,roads: list[list[int]])->int :
    graph= collections.defaultdict(list)
    for u,v,w in roads:
        graph[u].append((v,w))
        graph[v].append((u,w))#binary-xiang-graph
    ways=[0]*n
    ways[0]=1
    dist=[float('inf')]*n
    dist[0]=0
    pq=[(0,0)]#time，k目标点
    MOD=10**9+7
    while pq:
        time,u=heapq.heappop(pq)#优化数组，time最低的在最前面
        if time > dist[u]:
            continue
        for v,w in graph[u]:
            newtime= time+w
            if newtime<dist[v]:
                dist[v]=newtime
                heapq.heappush(pq,(newtime,v))
                ways[v]=ways[u]#findfastest way , inherit last num of ways U
            elif newtime==dist[v]:
                ways[v]=(ways[v]+ways[u])%MOD
    return ways[n-1]
n=7
roads=[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(countPaths(n,roads))