# Viết chương trình nhập vào từ bàn phím bán kính r của đường tròn, in ra kết quả cho pi = 3.14
# a, Chu vi = ?
# b, Diện tích = ?

r = float(input("Nhập vào bán kính của đường tròn: "))

chu_vi = 2 * r * 3.14
dien_tich = 3.14 * (r**2)
# cách in ra màn hình, cách 1:
print ("Chu vi của hình tròn là: ",chu_vi)
print ("Diện tính của hình tròn là: ",dien_tich)
#cách 2
print('Chu vi hình tròn là {}, diện tích hình tròn là {}'.format(chu_vi,dien_tich))
#cách 3:
print(f'Chu vi hình tròn là: {chu_vi}, diện tích hình tròn là: {dien_tich}')