from icecream import ic

Time = [54946592]
Distance = [302147610291404]
b = 0
res = 1
for z in range(len(Time)):
    for i in range(0, Time[z]):
        a = i * (Time[z] - i)
        if a > Distance[z]:
            b += 1
    res *= b
    b = 0
ic(b, res)
