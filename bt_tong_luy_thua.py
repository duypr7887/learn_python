#Tính tổng s = 1!+2!+3!+...+10! (dùng for)
m = 1
sum = 0
for s in range (1,11):
    m = s * m
    sum += m
print(sum)