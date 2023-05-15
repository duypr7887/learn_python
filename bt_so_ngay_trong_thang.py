#Kiểm tra số ngày trong tháng
month = int(input('Nhập số tháng cần kiểm tra: '))
if month in (1,3,5,7,8,10,12):
    print(f'Tháng {month} có 31 ngày')
elif month in (4,6,9,11):
    print(f'Tháng {month} có 30 ngày')
elif month == 2:
    year = int(input("Nhập vào số năm: "))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f'Tháng {month} năm {year} có 29 ngày')
    else:
        print(f'Tháng {month} năm {year} có 28 ngày')
else:
    print("Bạn đã nhập sai tháng, vui lòng thử lại")