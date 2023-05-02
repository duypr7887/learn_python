# Kiểm tra năm nhuận
year = int(input('Nhập vào số năm cần kiểm tra: '))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f'Năm {year} nhuận')
else:
    print(f'Năm {year} không nhuận')