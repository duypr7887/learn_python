#Kiểm tra số chẳn lẻ
n = int(input("Nhập vào 1 số: "))
t = n % 2
if t == 0:
    print(f'Số {n} là số chẳn')
else:
    print(f'Số {n} là số lẻ')