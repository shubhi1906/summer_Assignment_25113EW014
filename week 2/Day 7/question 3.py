n = int(input("Enter number of elements: "))
l = []

for i in range(n):
    m = int(input("Enter array elements: "))
    l.append(m)

largest=second=l[0]

for i in l:
    if i > largest:
        second=largest
        largest = i
    elif i>second and i!=largest:
        second=i

print("Largest =", largest)
print("Second largest =", second)
