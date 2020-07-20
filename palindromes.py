nums = 0
for s in range(999, 100, -1):
    for o in range(s, 100, -1):
        r = s * o
        if r > nums:
            q = str(s* o)
            if q == q[::-1]:
                nums = s * o
print("The largest palindome made by 2 three digit numbers: " +str(int(nums)))
