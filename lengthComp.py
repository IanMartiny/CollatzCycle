#! /usr/bin/env python

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

# 10439860591 = 630138897*1 + 9809721694*1
nums = [(630138897, 9809721694, 10439860591),
        (272500658, 357638239, 9809721694), 
        (187363077, 85137581, 357638239),
        (102225496, 85137581, 85137581), 
        (17087915, 85137581, 85137581),
        (301994, 16785921, 85137581),
        (125743, 176251, 16785921),
        (75235, 50508, 176251)]

x = []
y = []
# need 272500658*x + 357638239*y = 9809721694
for i in range(len(nums)):
    tup = nums[i]
    _, xInit, yInit = egcd(tup[0],tup[1])
    x.append(xInit * tup[2])
    y.append(yInit * tup[2])

    print("x[" + str(i) + "] = " + str(x[i]))
    print("y[" + str(i) + "] = " + str(y[i]))
    print(tup[0]*x[i] + tup[1]*y[i])
    assert tup[0]*x[i] + tup[1]*y[i] == tup[2]

    times = x[i]/tup[1]
    # print("times = " + str(times))
    x[i] = x[i] - times*tup[1]
    print("x[" + str(i) + "] = " + str(x[i]))

    y[i] = y[i] + times*tup[0]
    print("y[" + str(i) + "] = " + str(y[i]))
    print(tup[0]*x[i] + tup[1]*y[i])
    assert tup[0]*x[i] + tup[1]*y[i] == tup[2] 

print("")
yTimes = [0]*len(y)
xTimes = [0]*len(x)
xTimes[0] = x[0]
yTimes[0] = y[0]
for i in range(1, len(x)):
    xTimes[i] = x[i]*yTimes[i-1] + xTimes[i-1]
    yTimes[i] = y[i]*yTimes[i-1] + xTimes[i-1]
    print(str(nums[i][0]) + "*" + str(xTimes[i]) +
            "\t+ " + str(nums[i][1]) + "*" + str(yTimes[i]) +
            "\t= " + str(nums[i][0]*xTimes[i] + nums[i][1]*yTimes[i]))
# print(str(nums[2][0]) + "*" + str(x[2]+x[1]+1) +
        # " " + str(nums[2][1]) + "*" + str(y[2]+y[1]+1) +
        # " = " + str(nums[2][0]*(x[2]+x[1]+1) + nums[2][1]*(y[2]+y[1]+1)))
