# 다시
# def get_camera_location():
#     camera = []
#     for i in range(len(graph)):
#         for j in range(len(graph[i])):
#             if 1 <= graph[i][j] <= 5:
#                 camera.append([i,j])
#     return camera

# def monitor_dir(x,y):
#     if graph[x][y] == 1:
#         return (0,1), (1,0), (0,-1), (-1,0)

# def camera_monitor(x,y):

#     maxs = 0
#     for i, j in monitor_dir(x, y):
#         sums = 0
#         mx, my = x+i, y+i
#         if 0<=mx<=n-1 and 0<=my<=m-1:
#             if graph[mx][my] == 0:
#                 graph[mx][my] = "#"
#                 sums += 1
#         maxs = max(sums, maxs)
#     return maxs




# if __name__ == "__main__":
#     n, m  = map(int, input().split())
#     graph = [list(map(int, input().split())) for _ in range(n)]

#     camera_location = get_camera_location()

#     for x, y in camera_location:
#         answer += camera_monitor(camera_location)