import time
import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

print (time.ctime())

N = int(input("Введите N > 3\n"))
while N < 4:
    N = int(input("Недопустмое значение N\nВведите N > 3\n"))
size = N // 2
K = int(input("Введите K\n"))

start = time.time()

A = np.zeros((N, N), dtype = int) #Задаём матрицы А и Ф = 0
F = np.zeros((N, N), dtype = int)

for i in range (N): #Задаём матрицу А
    for j in range (N):
        A[i][j] = random.randint(-10,10)

print ("\nMatrix A:")
for i in A:
    for j in i:
        print ("%5d" % j, end = ' ')
    print () #

for i in range (N): #Задаём матрицу Ф = А
    for j in range (N):
        F[i][j] = A[i][j]

print ("\nMatrix F:")
for i in F:
    for j in i:
        print ("%5d" % j, end = ' ')
    print ()

E = np.zeros((size, size), dtype = int) #Задаём матрицу Е
cnt = 0
mult = 1

for i in range (size):
    for j in range (size):
        E[i][j] = F[i][j]
        if (j+1) % 2 == 0 and E[i][j] > K:
            cnt += 1
        if (i+1) % 2 != 0:
            mult *= E[i][j]

print ("\nMatrix E:")
for i in E:
    for j in i:
        print ("%5d" % j, end = ' ')
    print ()
print ("\nСумма =", cnt, "\nПроизведение =", mult)

if cnt < mult:
    for i in range (size):
        for j in range (size):
            F[i][j + size + N % 2], F[N - 1 - i][j + size + N % 2] = F [N - 1 - i][j + size + N % 2], F[i][j + size + N % 2]
else:
    for i in range (size):
        for j in range (size):
            F[i][j + size + N % 2], F[i + size + N % 2][j + size + N % 2] = F[i + size + N % 2][j + size + N % 2], F[i][j + size + N % 2]

print ("\nMatrix F(modified):")
for i in F:
    for j in i:
        print ("%5d" % j, end = ' ')
    print ()

if np.linalg.det(A) == 0 or np.linalg.det(F) == 0:
    print ("Вычисления невозможны")

elif np.linalg.det(A) > np.trace(F):
    Matrix = (((np.linalg.inv(A)).dot(np.transpose(A)))-(np.transpose(F) * K)) #A-1*AT – K * FТ

else:
    Matrix = ((A + np.tril(A) - np.linalg.det(F))*K) #(A +GТ-F-1)*K

print ("\nCalculations Matrix:")
for i in Matrix:
    for j in i:
        print ("%5d" % j, end = ' ')
    print ()

finish = (time.time() - start)
print ("\n", "Time", finish, "seconds")

# MATPLOTLIB:
plt.title("Changing element of matrix rows")  # 1 пример
plt.xlabel("Matrix column number")
plt.ylabel("Element value")

for j in range(N):
    plt.plot([i for i in range(N)], F[j][::], marker='o')

plt.show()

np.random.seed(123)                           # 2 пример
for j in range (N):
    plt.pcolormesh(F, cmap='plasma', edgecolors="k", shading='flat')
plt.title("Changing element of matrix rows")

plt.show()

fig, ax = plt.subplots()                      # 3 пример

for j in range (N):
    ax.scatter([i for i in range(N)], F[j][::])

ax.set(title = 'Changing element of matrix rows')
plt.xlabel("Matrix column number")
plt.ylabel("Element value")
plt.show()

# SEABORN:
sns.set_style("whitegrid")                    # 1 пример
sns.boxplot(data = F)
plt.xlabel("Matrix column number")
plt.ylabel("Element value")
plt.show()

sns.set_theme(style = "darkgrid")             # 2 пример
plt.xlabel("Matrix column number")
plt.ylabel("Element value")
sns.lineplot(data = F)
plt.show()

sns.heatmap(data = F, annot=True)             # 3 пример
plt.xlabel("Matrix column number")
plt.ylabel("Matrix row number")
plt.show()
