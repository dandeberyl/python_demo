# python arrays
import array
import array as arr

a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for i in range(0, 7):
    print(a[i], end=" ")
print(a[0])

print(a[2])

print(*a)

a.insert(1, 430000)
print(*a)
b = arr.array('d', [2.5, 3.2, 3.3])
print(b[1])
b = arr.array('f', [2.8, 3.2, 3.3])
print(b[1])
print(*b)

# slicing

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 2, 3, 8, 2, 2, 3, 2]
b = arr.array('i', a)

res = a[3:8]
print(res)

res = a[5:]
print(res)

res = a[:]
print(res)

# search
print(a.index(2))

# update
a[2] = 7800
print(a)

# counting
count = a.count(2)
print(count)

#reverse
a.reverse()
print(*a)

#extend
a.extend([60,70,80,90,100])
print(a)


