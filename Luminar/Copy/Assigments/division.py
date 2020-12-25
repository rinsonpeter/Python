x=int(input("enter divident:"))
y=int(input("enter divisor:"))

while y<x:
    x=int(input("enter divident greater than divisor:"))
else:
    x = int(input("enter divident greater than divisor:"))
for i in range(1, 9):
    if y * i > x:
        break
z = i - 1
print("quotient:", z)
print("remainder:", (x - (y * z)))




