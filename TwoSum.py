def twoSum(nums, target):
    hashMap = {}
    for index, number in enumerate(nums):
        remainder = target-number


        if remainder in hashMap:
            print (index, hashMap[remainder])
        else:
            hashMap[number]=index
        
            
            
            
#Driver       
if __name__=="__main__":
    nums1=[3,2,3]
    target = 6
    twoSum(nums1, target)