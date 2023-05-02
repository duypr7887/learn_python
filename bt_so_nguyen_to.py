#Nhập vào 1 số, cho biết số đó có phải số nguyên tố (số nguyên tố là số > 0, và chia hết cho 1 và chính nó) 
#Kết thúc chương trình hỏi người dùng Bạn có muốn tiếp tục sử dụng phần mềm không?
#Nếu chọn không thì thoát chương trình 
while True:
    num = int(input("Nhập một số nguyên dương: "))
    if num <= 1:
        print(num, "không phải là số nguyên tố")
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, "là số nguyên tố")
        else:
            print(num, "không phải là số nguyên tố")
    choice = input("Bạn có muốn tiếp tục sử dụng phần mềm không? (nhập Y để tiếp tục, bất kỳ ký tự nào khác để thoát): ")
    if choice.lower() != 'y':
        break

