import sys
N = int(sys.stdin.readline())
start_time = 0
end_time = 0
con = []
result = 0

for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    con.append((s,e))

con.sort(key = lambda time : time[0])
# print(con)
con.sort(key = lambda time : time[1]) 
# print(con)   

for i in con:
    if i[0] >= start_time:
        result += 1
        start_time = i[1]

print(result)
    
