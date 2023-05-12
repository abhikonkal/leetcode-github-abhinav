class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp=[0]*(len(questions)+1)
        max_sum=0

        for i in range(len(questions)-1,-1,-1):
            future=questions[i][1]+1+i
            if future>=len(questions):
                dp[i]=questions[i][0]
            else:
                dp[i]=questions[i][0]+dp[future]
            max_sum=max(max_sum,dp[i])

            dp[i]=max(dp[i],dp[i+1])

        
                    
        return max_sum

