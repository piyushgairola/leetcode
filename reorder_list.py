class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorder(self,head):
        temp = head
        ls=[]
        n=0
        while(temp.next):
            ls.append(temp)
            n +=1
        curr = ListNode(val = head.val)
        for i in range(n/2):
             curr.next = ls[n-1-i]
             ls[n-1-i].next = ls[i+1]

             curr = 
