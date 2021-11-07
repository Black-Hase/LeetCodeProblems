class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        t=0
        x=0
        i=0
        #k=0
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        C=[0]*total
        #half=total//2
        #print(half)
       # print('length of C arrary: ', len(C))
        #for k in range(len(C)):
         #   print(C[k])
        #merg sort

        while i< total: 
        #t< len(nums1) and x < len(nums2):
        #for i in range(len(C)):
           # print(C[i])
            #print(i,t,x)
            #print(C)
            if x < len(nums2) and t < len(nums1) and A[t] < B[x]:
                # print('test1A')
                C[i]=A[t]
                i=i+1
                t=t+1
                #print('test1B')
            elif  t < len(nums1) and x < len(nums2):
            #elif B[x] < A[t] and x<len(B)-1:
                C[i]=B[x]
                x=x+1
                i=i+1
                # print('test2')
            else:
                break
        while x<len(nums2):
            C[i]=B[x]
            x=x+1
            i=i+1
        while t<len(nums1):
            C[i]=A[t]
            t=t+1
            i=i+1

        #print(C)

        #Math
        #if length of C is even
        if len(C) % 2==0:
            med1 = int(len(C)/2-1)
            med2 = int(len(C)/2)
            return ((C[med1]+C[med2])/2)
        #if length of C is odd
        else:
            med3 = int((len(C)+1)/2 - 1)
            return ((C[med3]))
