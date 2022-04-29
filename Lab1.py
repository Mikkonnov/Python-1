a = int(input())
b = int(input())
c = int(input())
d = int(input())
divs = [a, b, c, d]
divs1 = []
for i in range (0, 4):
    if divs[i] < 0 and divs[i] % 2 != 0:
        divs1.append(divs[i])
Full = (sorted(divs1))
Min = (divs1[0])
print (Min)
