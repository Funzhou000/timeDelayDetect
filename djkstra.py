import heapq
import collections
def networkDelayTime(times:list[list[int]],n:int,k:int):#time(u(source_pot)v(end_spot)w(timeFu to v))
    graph=collections.defaultdict(list)
    #当你在操作一个字典（dict）时，如果你想往一个可能还不存在的键（key）中添加元
    #素（例如，添加到一个列表/list里） ，你就不需要事先检查这个键是否存
    #在，collections.defaultdict(list) 会在你第一次访问这个不存在的键时，自动为
    #你创建一个空的列表（list）作为对应的值（value）。
    for u,v,w in times:
        #sort like u=3(2,6)(3,7)f 3 to 2/3/etc 's time
        graph[u].append((v,w))
        # 2. 初始化
        # dist 数组用于存储从源节点 k 到达每个节点 i 的最短时间
        # 节点编号从 1 到 n，所以数组大小为 n + 1，方便索引
        # 初始时，所有距离都设为无穷大 (float('inf'))
    dist=[float('inf')]*(n+1)#列表乘法，以[]内的数值初始化n+1个
    dist[k]=0
    pq=[(0,k)]#use tuple元组save figure to make sure it neverchange
    while pq:
        #pop minimize time(former elem)
        time,u=heapq.heappop(pq)      
        if time >dist[u]:
            continue#which mean i'v better choice
        for v,w in graph[u]:
            new_time=time+w
            if new_time < dist[v]:
                dist[v]=new_time       
                heapq.heappush(pq,(new_time,v))
    max_time = max(dist[1:])
    return max_time if max_time != float('inf') else -1
times=[[2,1,1],[2,3,1],[3,4,1]]
n=4
k=2
print(networkDelayTime(times,n,k))