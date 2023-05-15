from functools import reduce

def sum(x,y):
    return int(x) + int(y)

def is_leap_year(year : int) -> bool:
    if(year % 100 == 0):
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return year % 4 == 0

def calNumber(birth : list) -> int:
    day = str(birth[0])
    month = str(birth[1])
    year = str(birth[2])
    first_calc = 0
    for x in day + month + year:
        first_calc += int(x)
    while(len(str(first_calc)) >= 2 and int (first_calc)> 11):
        first_calc = int(reduce(sum,[int(x) for x in str(first_calc)]))
    return(first_calc)

def checkCHDs(chd : dict,wishLists : list,day : int, month : int) -> bool:
    for cung in wishLists:
        min_date = int(chd[cung][0].split('/')[0])
        min_month = int(chd[cung][0].split('/')[1])

        max_date = int(chd[cung][1].split('/')[0])
        max_month = int(chd[cung][1].split('/')[1])
        if(min_month != 12) :
            current = day + month * 1000
            min = min_date + min_month * 1000
            max = max_date + max_month * 1000
            if current >= min and current <= max :
                return[True,cung]
            else:
                if (month == 12 and day >=22) or (month ==1 and day <=19):
                    return[True,cung]
        return [False,'']

max_day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
chd = {
    "MaKet" : ["22/12","19/1"],
    "BaoBinh" : ["20/1","18/2"],
    "SongNgu" : ["19/2","20/3"],
    "BachDuong" : ["21/3","20/4"],
    "KimNguu" : ["21/4","20/5"],
    "SongTu" : ["21/5","21/6"],
    "CuGiai" : ["22/6","22/7"],
    "SuTu" : ["23/7","22/8"],
    "XuNu" : ["23/8","22/9"],
    "ThienBinh" : ["23/9","23/10"],
    "BoCap" : ["24/10","23/11"],
    "NhanMa" : ["24/11","21/12"],
}

try:
    birth = [int(x) for x in input("Nhập vào ngày tháng năm sinh của bạn (dd/mm/yyyy): ").split('/')]
except:
    print("Nhập sai quy định ngày sinh!")

wish_numbers = [int(x) for x in input(
    "Nhập vào các con số chủ đạo của bạn muốn (cách nhau bởi dấu phẩy) :").split(',')]
min_year,max_year =  [int(x) for x in input("Nhập vào khoảng năm sinh(1999,2000): ").split(',')]

index = 1 
cung_hds = [0]
for cung in chd:
    print(f'{index}.\t{cung} : {chd[cung][0]} - {chd[cung][1]}')
    cung_hds.append(cung)
    index+=1

choice = [cung_hds[int(x)] for x in input("Nhập vào các con số thứ tự cung bạn muốn chọn (cách nhau bởi dấu phấy): ").split(',')]
print ('\n\n\n Con số chủ đạo của bạn là: ' + str(calNumber(birth)))
result = 0
for year in range(min_year,max_year + 1):
    for month in range(1,13):
        for day in range(1,30 if is_leap_year(year) and month == 2 else 29 if month == 2 else max_day_in_month[month] + 1):
            if(checkCHDs(chd,choice,day,month)[0] == True and calNumber([day,month,year]) in wish_numbers):
                print(f'Ngày sinh : {day}/{month}/{year}, cung {checkCHDs(chd,choice,day,month)[1]}, số chủ đạo {calNumber([day,month,year])}')
                result += 1

print(f'\n\n Tìm ra {result} kết quả phù hợp với yêu cầu!')
input("Ấn phím bất kỳ để thoát!")
