print("Hello World ")

a = [1, "Hello", [3.14, 'Hello World']]
a.append(2)
print(a)

a = 10
print(type(a))

b = 20.17
print(type(b))

c = 87+3j
print(type(c))

s = "this is a python demo"
print(s)

print(type(s))

print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s)

a = [1, "10 bananas", 2, " 1 watermelon", 3, "4 apples"]
print(a)

print(a[1])
print(a[3])
print(a[5])

tup = tuple(['hi', 'tuples'])
print(tup)
print(tup[0])
print(tup[1])

set("use of sets")


d = {1: "hello!", 2: "there", 3: "how", 4: "are", 5: "you?"}
print(d)

d1 = dict(a="hello!", b="there", c="how", d="are", e="you?")
print(d1)


name = "Berry"
name = "black"
name = "straw"
name = "blue"

print(name)

name4 = "Hello"
print(name4)

x = y = z = "hi"
print(x, y, z)


age = 20
if age >= 18:
    print("qualify")
else: 
    print("disqualify") 

marks = 80
res = "Pass" if marks >= 75 else "Fail"
print(f"Result: {res}") 


age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")



age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")


n = 100
for i in range(0, n):
    print(i)