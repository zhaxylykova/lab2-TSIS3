def gcd(a, b):
    if b != 0:
        return gcd(b, a % b)
    else:
        return a

def lcm(a, b):
    return a * b // gcd(a, b)

num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)
print(gcd(num1, num2) + lcm(num1, num2))
