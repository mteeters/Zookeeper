# put your python code here
a = abs(int(input()))
b = abs(int(input()))
c = abs(int(input()))

a += a % 2
b += b % 2
c += c % 2

a = a // 2
b = b // 2
c = c // 2

print(a + b + c)
