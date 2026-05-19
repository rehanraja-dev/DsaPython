# n = [0,1,2,3,1,3,5,6,7,4,3,4,23,53,23,53,53,12]
# m = [1,2,5,7,53]

# frequency = {}

# for num in n:
#     frequency[num] = frequency.get(num,0) + 1

# for num in m :
#     print(frequency.get(num))

n = "aabsjjsssuerrw"
m = ["a", "b", "s"]

frequency = {}

for ch in n :
    frequency[ch] = frequency.get(ch, 0) + 1 

for ch in m :
    print(frequency.get(ch))