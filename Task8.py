#Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively.

a = int(input("A:"))
b = int(input("B:"))

c = list(range(a, b+1))

for i in c:
    print(i)