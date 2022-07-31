#Given an array A of positive integers. Your task is to find the leaders in the array.
#An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader.
def leaders(self, A,N):
        #Code here
        max=A[N-1]
        revlead=[]
        revlead.append(max)
        for i in range(N-2,-1,-1):
            if max <=A[i]:
                max=A[i]
                revlead.append(max)
        revlead.reverse()
        return revlead