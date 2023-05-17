# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        v=[]
        temp=head
        cnt=0
        while(temp):
            v.append(temp.val)
            temp=temp.next
            cnt+=1
        t_sum=0
        n=cnt
        for i in range(0,int(n/2)):
            tm_sum=v[i]+v[n-i-1]
            if tm_sum>t_sum:
                t_sum=tm_sum

        return t_sum
