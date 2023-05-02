#Giải phương trình bậc 2: ax^2 + bx + c = 0
# Tính delta, delta = b^2 - 4ac
#so sánh delta với 0:
 #delta < 0 = phươn trình vô nghiệm
 #delta = 0 = phương trình có 1 nghiệm x1 = x2 = -b/2a
 #delta > 0 = phương trình có 2 nghiệm x1 = -b + Căn delta/2a, x2= -b - Căn delta/2a

from math import sqrt
a = float(input("Nhập vào giá trị a của phương trình: "))
b = float(input("Nhập vào giá trị b của phương trình: "))
c = float(input("Nhập vào giá trị c của phương trình: "))

delta = (b**2) - (4*a*c)

if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print('Phương trình có 1 nghiệm kép: ',  -b/(2*a))
else:
    print('Phương có có 2 nghiệm khác biệt')
    x1 = (-b + sqrt(delta)/2*a)
    x2 = (-b - sqrt(delta)/2*a)
    print('Nghiệm x1 là: ',x1)
    print('Nghiệm x2 là: ',x2)