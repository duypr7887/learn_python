# Năm 2017 dân số VN 95.5tr người. Trung bình 1 năm tăng 1.2%. Hỏi sau bao nhiêu năm thì dân số tăng lên 150tr. (dùng while True)
danso = 95.5
nam = 0
while True:
    danso = danso * 1.012
    nam += 1
    if danso > 150:
        print(f"Sau {nam} năm, dân số của Việt Nam sẽ đạt {danso:.2f} triệu người.")
        break
