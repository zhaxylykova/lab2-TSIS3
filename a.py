number = int(input())
compare = number
reversenumber = 0
while(number > 0):
    last = number % 10
    reversenumber = reversenumber * 10 + last
    number = number // 10
if(compare == reversenumber):
    print("YES")
else:
    print("NO")   
