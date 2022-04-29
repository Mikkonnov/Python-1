"""Формируется матрица F следующим образом: если в Е количество чисел, больших К в четных столбцах в области 
2 больше, чем произведение чисел в нечетных строках в области 4, то поменять в С симметрично области 1 и 
4 местами, иначе С и В поменять местами несимметрично. При этом матрица А не меняется. После чего 
вычисляется выражение: К*(A*F)+ K* F T . Выводятся по мере формирования А, F и все матричные операции 
последовательно."""

import random
import time

def print_matrix(M,matr_name,tt):
        print ( "матрица "+matr_name+" промежуточное время = " +str(format(tt, '0.2f'))+ " seconds.")
        for i in M:         # делаем перебор всех строк матрицы
            for j in i:     # перебираем все элементы в строке 
                print("%5d" % j, end = ' ')
            print() 
  
N = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:\n"))
while N < 6 or N > 100:
    N = int(input("Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:\n"))    
K = int(input("Введите число К\n"))
start = time.time()
A,F,AF,FT = [],[],[],[]     # задаем матрицы 
for i in range(N):
    A.append([0]*N)
    F.append([0]*N)
    AF.append([0]*N)
    FT.append([0]*N)        
time_next = time.time()

for i in range(N):          # заполняем матрицу А         
    for j in range(N):            
        A[i][j] = random.randint(-10,10)
time_prev = time_next
time_next = time.time()
print_matrix(A,"A",time_next-time_prev)
    
for i in range(N):           # F
    for j in range(N):
        F[i][j] = A[i][j]    
time_prev = time_next
time_next = time.time()
print_matrix(F,"F",time_next-time_prev)

E = []                       # задаем матрицу E
size = N // 2
for i in range(size):
    E.append([0] * size)
    
for i in range(size):        # формируем подматрицу E         
    for j in range(size):
        E[i][j] = F[i][j]
time_prev = time_next
time_next = time.time()
print_matrix(E,"E",time_next-time_prev)
    
C = []                       # задаем матрицу C
size = N // 2
for i in range(size):
    C.append([0] * size)
    
for i in range(size):        # формируем подматрицу C         
    for j in range(size):
        C[i][j] = F[i + N % 2 + size][j + N % 2 + size]
time_prev = time_next
time_next = time.time()
print_matrix(C,"C",time_next-time_prev)
    
cnt = 0
multipl = 1

for i in range (size):        # работаем с подматрицей E
    for j in range (size):               
        if j % 2 == 0 and i < j and j > size - 1 - i and E[i][j] > K: 
            cnt += 1
        elif j % 2 != 0 and i > j and j < size - 1 - i:
            multipl *= E[i][j]
    
if cnt > multipl:
    for i in range (size):
        for j in range (size):
            if i > j and j < size - 1 - i:
                b = C[i][j]
                C[i][j] = C[j][i]
                C[j][i] = b
                F[i + N % 2 + size][j + N % 2 + size] = C[i][j]
    print_matrix(C,"C изменённая",time_next-time_prev)
    print_matrix(F,"F",time_next-time_prev)
else:
    for i in range (size):
        for j in range (size):
            a = F[i][j + N % 2 + size]
            F[i][j + N % 2 + size] = C[i][j]
            C[i][j] = a
            F[i + N % 2 + size][j + N % 2 + size] = C[i][j]
    print_matrix(C,"C изменённая",time_next-time_prev)
    print_matrix(F,"F",time_next-time_prev)                          
time_prev = time_next
time_next = time.time()
print_matrix(A,"A",0)

for i in range (N):         # A * F
    for j in range (N):
        s = 0
        for m in range (N):
            s = s + A[i][m] * F[m][j]
        AF[i][j] = s    
time_prev = time_next
time_next = time.time()
print_matrix(A,"A * F",time_next-time_prev)

for i in range (N):          # K * (A * F)
    for j in range (N):
        AF[i][j] = AF[i][j] * K
time_prev = time_next
time_next = time.time()
print_matrix(AF,"K * (A * F)",time_next-time_prev)
    
for i in range(N):            # FT
    for j in range(i,N,1):
        FT[i][j],FT[j][i] = F[j][i],F[i][j]
time_prev = time_next
time_next = time.time()
print_matrix(FT,"F^T",time_next-time_prev)
                
for i in range(N):            # K * FT
    for j in range(N):
        FT[i][j] = K*FT[i][j]
time_prev = time_next
time_next = time.time()
print_matrix(FT,"K * F^T",time_next-time_prev)
    
for i in range(N):            # K * (A * F) + K * FT
    for j in range(N):
        AF[i][j] = AF[i][j]+FT[i][j]    
time_prev = time_next
time_next = time.time()
print_matrix(AF,"(K * A) * F + K * F^T",time_next-time_prev)
    
finish = time.time()
result = finish - start

print("Program time: " + str(result) + " seconds.")    
