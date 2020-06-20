string = str(input())
sortedarray = list(string)
newline = ""
for i in range(len(string)-1):
    for j in range(len(string) - i - 1):
        if(sortedarray[j] > sortedarray[j+1]):
            sortedarray[j], sortedarray[j+1] = sortedarray[j+1], sortedarray[j]

for k in sortedarray:
    newline+=k

print(newline)

