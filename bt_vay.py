# 1 người vay 400tr. Lãi năm đầu 0%, lãi năm 2 trở đi là 10%. Mỗi tháng trả 10tr thì bao giờ hết nợ (while True) 
# ghi chú: có thể dùng hàm khác gợi ý miễn sao có kết quả 
loan_amount = 400_000_000 # số tiền vay ban đầu
monthly_payment = 10_000_000 # số tiền trả hàng tháng
interest_rate = 0.1 # lãi suất hàng năm

current_balance = loan_amount
total_paid = 0
month = 0

while current_balance > 0:
    month += 1
    if month <= 12:
        monthly_interest = 0 # năm đầu lãi suất là 0%
    else:
        monthly_interest = interest_rate / 12 # lãi suất từ năm thứ 2 là 10% hàng năm
    interest_payment = current_balance * monthly_interest
    current_balance += interest_payment - monthly_payment
    if current_balance < 0: # nếu số tiền còn lại nhỏ hơn 0 thì gán cho nó bằng 0
        current_balance = 0
    total_paid += monthly_payment
    print(f"Tháng {month}: số tiền còn lại là {current_balance:,.0f} VND")
    
print(f"Đã trả tổng số tiền là {total_paid:,.0f} VND trong {month} tháng")
