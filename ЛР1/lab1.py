import numpy as np


print("Задание 1")
a = np.zeros(10, dtype=int)
print(a)

print("\nЗадание 2")
a = np.zeros(10, dtype=int)
a[4] = 1
print(a)

print("\nЗадание 3")
a = np.random.randint(0, 10, 20)
print(a)
print(np.nonzero(a)[0])

print("\nЗадание 4")
a = np.random.random((3, 3, 3))
print(a)

print("\nЗадание 5")
a = np.random.random(10)
print(a)
print(a.mean())

print("\nЗадание 6")
a = np.random.randint(1, 10, (5, 3))
b = np.random.randint(1, 10, (3, 2))
c = a @ b
print(a)
print(b)
print(c)

print("\nЗадание 7")
a = np.random.randint(1, 10, (4, 4))
b = np.random.randint(1, 10, (4, 4))
c = a @ b
print(c)
print(np.diag(c))

print("\nЗадание 8")
a = np.random.random(20)
a[np.argmax(a)] = 0
print(a)

print("\nЗадание 9")
a = np.random.randint(1, 11, 20)
print(a)
print(np.unique(a))

print("\nЗадание 10")
a = np.random.randint(1, 10, (4, 4))
b = a - a.mean(axis=1, keepdims=True)
print(a)
print(b)

print("\nЗадание 11")
a = np.random.randint(1, 10, (4, 4))
print(a)
a[[0, 1]] = a[[1, 0]]
print(a)

print("\nЗадание 12")
a = np.random.randint(1, 101, 20)
n = 5
result = np.sort(a)[-n:][::-1]
print(a)
print(result)

print("\nЗадание 13")
a = np.random.randint(1, 11, (5, 5))
print(a)
print(a.sum(axis=1))

print("\nЗадание 14")
a = np.random.randint(-10, 11, 10) / 10
print(a)
a = np.sign(a)
print(a)

print("\nЗадание 15")
a = np.random.randint(1, 101, 12)
parts = np.split(a, 3)
sums = np.array([part.sum() for part in parts])
print(a)
print(parts)
print(sums)
