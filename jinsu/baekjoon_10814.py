import sys
number = int(sys.stdin.readline())
personal = []

for _ in range(number):
    age, name = sys.stdin.readline().split()
    personal.append((int(age),name))

name_sort = sorted(personal, key = lambda x : x[1])
age_sort = sorted(personal, key = lambda x : x[0])


for i in age_sort:
    print(f"{i[0]} {i[1]}")