def twosum(nums,target):
    list1 = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                list1.extend([i,j])
    list1 = list(set(list1))
    return list1

print(twosum([2,7,11,15],9))
print(twosum([3,2,4],6))
print(twosum([3,3],6))