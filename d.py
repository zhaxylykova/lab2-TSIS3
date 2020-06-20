def tribonacci(a,b,c,s):
    if s == 1:
        return a+b+c
    d = a+b+c
    return tribonacci(b,c,d,s-1)    


number = int(input())
a = 1
b = 1
c = 2

if number == 0:
    print("0")
    exit(0)
if number == 1:
    print("1")
    exit(0)
if number == 2:
    print("1")   
    exit(0)
if number == 3:
    print("2")   
    exit(0)    
else:
    print(tribonacci(a,b,c,number-3))         