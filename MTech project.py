'''import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

fig, ax = plt.subplots()
"""ax.scatter([5, 7, 8, 7, 2, 17, 2, 9,
     4, 11, 12, 9, 6],[99, 86, 87, 88, 100, 86,
     103, 87, 94, 78, 77, 85, 86])"""

ax.scatter(np.random.rand(N), np.random.rand(N))
ax.add_patch( Rectangle((5, 82.5),
                        5, 7.5,
                        fc='none',
                        color ='red',
                        linewidth = 2,
                        linestyle="dotted") )
ax.add_patch( Rectangle((10, 82.5),
                        5, 7.5,
                        fc='none',
                        color ='red',
                        linewidth = 2,
                        linestyle="dotted") )
plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")
plt.title("PLOT-2")
plt.show()'''


def swap(a, b):
    return (b, a)


def fact(n):
    return 1 if (n == 1 or n == 0) else n * fact(n - 1)

# for N different distributions of points we will check the fraction


N = int(input("Enter number of points: "))
best_result = 0
best_result_points = []

return_count = 0

def main_algo(points, N):
    # points = [[2, 3], [3, 5], [5, 2], [6, 4], [3, 2], [5, 6]]
    # initial value of result is very high
    result = 999999999999
    # for every pair of points we need max
    max = 0
    # iterate over every pair of points
    for j in range(0, N):
        for k in range(j + 1, N):
            x1 = points[j][0]
            y1 = points[j][1]
            x2 = points[k][0]
            y2 = points[k][1]
            # please change variables of points if alternate pickup is happended
            if x2 < x1 and y1 < y2:
                x1, x2 = swap(x1, x2)
                y1, y2 = swap(y1, y2)
            # this is 1st case of choosen points
            if x2 > x1 and y1 > y2:
                # initialize every region count to 0
                yGy1 = yLy2 = xLx1 = xGx2 = x1LxLx2 = y2LyLy1 = x1LxAyLy2 = yLy1AxLx2 = 0
                # go through all the points
                for l in range(0, N):
                    # if current point matches to the points pair then continue
                    if l == j or l == k:
                        continue
                    currentx = points[l][0]
                    currenty = points[l][1]

                    # these are corresponding to all the condition of 8 regions
                    if currenty > y1:
                        yGy1 += 1
                    elif currenty < y2:
                        yLy2 += 1
                    if currentx < x1:
                        xLx1 += 1
                    elif currentx > x2:
                        xGx2 += 1
                    if currentx > x1 and currentx < x2:
                        x1LxLx2 += 1
                    if currenty > y2 and currenty < y1:
                        y2LyLy1 += 1
                    if currentx > x1 and currenty > y2:
                        x1LxAyLy2 += 1
                    if currenty < y1 and currentx < x2:
                        yLy1AxLx2 += 1
                # now found out the region containing maximum number of points
                max = yGy1
                if yLy2 > max:
                    max = yLy2
                if xLx1 > max:
                    max = xLx1
                if xGx2 > max:
                    max = xGx2
                if x1LxLx2 > max:
                    max = x1LxLx2
                if y2LyLy1 > max:
                    max = y2LyLy1
                if x1LxAyLy2 > max:
                    max = x1LxAyLy2
                if yLy1AxLx2 > max:
                    max = yLy1AxLx2

            # this is 2nd case of choosen points
            # please change variables of points if alternate pickup is happended
            if x2 > x1 and y2 > y1:
                x1, x2 = swap(x1, x2)
                y1, y2 = swap(y1, y2)
            if x2 < x1 and y2 < y1:
                yGy1 = yLy2 = xLx2 = xGx1 = x2LxLx1 = y2LyLy1 = xLx1AyGy2 = xGx2AyLy1 = 0
                # go through all the points
                for l in range(0, N):
                    # if current point matches to the points pair then continue
                    if l == j or l == k:
                        continue
                    currentx = points[l][0]
                    currenty = points[l][1]

                    # these are corresponding to all the condition of 8 regions
                    if currenty > y1:
                        yGy1 += 1
                    elif currenty < y2:
                        yLy2 += 1
                    if currentx < x2:
                        xLx2 += 1
                    elif currentx > x1:
                        xGx1 += 1
                    if currentx > x2 and currentx < x1:
                        x2LxLx1 += 1
                    if currenty > y2 and currenty < y1:
                        y2LyLy1 += 1
                    if currentx < x1 and currenty > y2:
                        xLx1AyGy2 += 1
                    if currenty < y1 and currentx > x2:
                        xGx2AyLy1 += 1
                # now found out the region containing maximum number of points
                max = yGy1
                if yLy2 > max:
                    max = yLy2
                if xLx2 > max:
                    max = xLx2
                if xGx1 > max:
                    max = xGx1
                if x2LxLx1 > max:
                    max = x2LxLx1
                if y2LyLy1 > max:
                    max = y2LyLy1
                if xLx1AyGy2 > max:
                    max = xLx1AyGy2
                if xGx2AyLy1 > max:
                    max = xGx2AyLy1
            # max less than result update max
            # print(max, "****")
            if max < result:
                result = max
    # print(result / N)
    global best_result
    global best_result_points
    if best_result < (result / N):
        best_result_points = points
        best_result = (result / N)


def generate_permutations_and_call_algo(arr, l, r):
    if l == r:
        point_set = []
        for i in range(0, N):
            point_set.append([i, arr[i]])
        # print(point_set)
        main_algo(point_set, N)
    else:
        for i in range(l, r + 1):
            arr[l], arr[i] = arr[i], arr[l]
            generate_permutations_and_call_algo(arr, l + 1, r)
            arr[l], arr[i] = arr[i], arr[l]  # backtrack



arr = []
for i in range(0, N):
    arr.append(i)
generate_permutations_and_call_algo(arr, 0, N - 1)


print("Best result = ", best_result)
print("best result points = ", best_result_points)






