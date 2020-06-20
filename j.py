def isAnagram(s,t):
    size1 = len(s)
    size2 = len(t)
    if size1 != size2:
        return 0


    s = sorted(s)
    t = sorted(t)

    for i in range(0, size1):
        if s[i] != t[i]:
            return 0
    return 1

s = str(input())
t = str(input())
if isAnagram(s, t):
    print("Yes")
else:
    print("No")    




