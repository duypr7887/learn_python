# Số hoàn thiện (hay còn gọi là số hoàn chỉnh, số hoàn hảo hoặc hoàn thành) là một số nguyên dương mà tổng các ước nguyên dương chính của nó (số nguyên dương bị nó chia hết ngoại trừ nó) bằng chính nó. Tìm tất cả số hoàn thiện trong phạm vi từ 1 tới 1000.

#Kiểm tra số hoàn hảo 
"""number = int(input("Nhập vào 1 số: "))
s = 0 
for i in range (1, number, 1):
    if number%i==0:
        s=s+i
if s==number:
    print(f'Số {number} là số hoàn chỉnh')
else:
    print(f'Số {number} không là số hoàn chỉnh')"""

# Số hoàn hảo thì 1 tới 1000 
for number in range (1,1001):
        s = 0 
        for i in range (1, number, 1):
            if number%i==0:
                s=s+i
        if s == number:
             print(s,end = " ")