# Viết chương trình nhập vào từ bàn phím bán kính r của đường tròn, in ra kết quả cho pi = 3.14
# a, Chu vi = ?
# b, Diện tích = ?

r = int(input("Nhập vào bán kính của đường tròn: "))

chu_vi = 2 * r * 3.14
dien_tich = 3.14 * (r**2)

print (chu_vi)
print (dien_tich)