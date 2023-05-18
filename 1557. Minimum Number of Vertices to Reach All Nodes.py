class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree=[0]*n
        ans=[]
        for i in edges:
            indegree[i[1]]+=1
        for i in range(0,len(indegree)):
            if indegree[i]==0:
                ans.append(i)
        return ans



        

        


