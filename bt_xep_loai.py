#Xếp loại học lực
dtb = float(input("Nhập vào điểm trung bình: "))
if dtb >= 9:
    print('Bạn là học sinh giỏi, điểm trung bình của bạn là: ',dtb)
elif dtb >= 7 and dtb < 9:
    print('Bạn là học sinh khá, điểm trung bình của bạn là: ',dtb)
elif dtb >= 6 and dtb >= 5:
    print('Bạn là học sinh trung bình, điểm trung bình của bạn là: ',dtb)
else :
    print('Bạn là học sinh kém, điểm trung bình của bạn là: ',dtb)