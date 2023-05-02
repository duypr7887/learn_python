#Kiểm tra tháng thuộc quý mấy 
n = int(input("Nhập vào số tháng"))
if n in (1,2,3):
    print(f'Tháng {n} thuộc 1')
elif n in (4,5,6):
    print(f'Tháng {n} thuộc quý 2')
elif n in (7,8,9):
    print(f'Tháng {n} thuộc quý 3')
elif n in (10,11,12):
    print (f'Tháng {n} thuộc quý 3')
else:
    print("Bạn đã nhập số tháng, vui lòng nhập lại")