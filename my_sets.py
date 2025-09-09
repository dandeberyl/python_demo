my_set = {"one", "two", "three"}
print(set)

set1 = set()
print(set1)

set1.update([5, 6])
print(set1)

tup = ("Hi", "there", "Hello")
print(set(tup))

for i in set1:
    print(i, end=" ")

print("one" in set1)