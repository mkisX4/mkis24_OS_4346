a = []

print("Количество фамилий (целым числом):")
N = int(input())

for i in range(N):
    fam = input()
    a.append(fam.capitalize())

for i in range(N - 1):
    for j in range(N - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a) 
 
