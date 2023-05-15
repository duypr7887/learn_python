# Tìm những số chia hết cho 3 từ 10 đến 50(dùng for và continue)
'''for i in range (10,51):
    if i % 3 == 0:
        print (i,end = " ")'''
for i in range (10,51):
    if i % 3 != 0:
        continue
    else:
        print(i, end=" ")