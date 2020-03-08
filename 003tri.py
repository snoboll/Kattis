m = list(input().split(" "))
n = list(map(int, m))
if(n[0] + n[1] == n[2]):
    print(m[0] + "+" + m[1] + "=" + m[2])
elif(n[1] + n[2] == n[0]):
    print(m[0] + "=" + m[1] + "+" + m[2])

elif(n[0] - n[1] == n[2]):
    print(m[0] + "-" + m[1] + "=" + m[2])
elif(n[1] - n[2] == n[0]):
    print(m[0] + "=" + m[1] + "-" + m[2])

elif(n[0] * n[1] == n[2]):
    print(m[0] + "*" + m[1] + "=" + m[2])
elif(n[1] * n[2] == n[0]):
    print(m[0] + "=" + m[1] + "*" + m[2])

elif(n[0] / n[1] == n[2]):
    print(m[0] + "/" + m[1] + "=" + m[2])
elif(n[1] / n[2] == n[0]):
    print(m[0] + "=" + m[1] + "/" + m[2])
