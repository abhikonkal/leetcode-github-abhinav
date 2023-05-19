import collections
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color={}
        for i in range(0,n):
            if i not in color and graph[i]:
                color[i]=1
                q=collections.deque([i])
                #print(';q',q)
                while q:
                    u=q.popleft()
                    #print(':u',u)
                    for v in graph[u]:
                        if v not in color:
                            color[v]=1-color[u]
                            q.append(v)
                        elif color[v]==color[u]:
                            return False
        return True
