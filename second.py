#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # set1=set(arr)
        # list1=list(set1)
        # firstmax=max(list1)
        # list1.remove(firstmax)
            
        # if list1:
        #     return max(list1)
        # return -1
        
        firstmax=max(arr)
        secondmax=float('-inf')
        for i in arr:
            if i>secondmax and i<firstmax:
                secondmax=i
            
        return secondmax if secondmax != float('-inf') else -1  
        
        # n = len(arr)
        # maxx = arr[0]
        # s_maxx = 0
        # for i in range(n):
        #     if maxx < arr[i]:
        #         maxx = arr[i]
        #         s_maxx = maxx
        # if s_maxx != 0:
        #     return s_maxx
        # else:
        #     return -1