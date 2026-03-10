nums = [1,3,4,2,2]

seen = set()

for n in nums:
    if n in seen:
        print(n)
        break
    seen.add(n)