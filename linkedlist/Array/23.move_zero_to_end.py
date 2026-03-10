nums = [0,1,0,3,12]

pos = 0

for i in nums:
    if i != 0:
        nums[pos] = i
        pos+=1

for i in range(pos,len(nums)):
    nums[i] = 0

print(nums)