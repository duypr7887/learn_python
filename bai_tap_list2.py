friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]

# lấy ra 4 ng bạn đầu tiên trong list
new_list = friends[:4]
print(new_list)

# lấy ra 4 ng cuối trong list
a_list = friends[3:]
print(a_list)

# Đảo ngược list 
b_list = friends [::-1]
print(b_list)

# lấy những ng vị trí 1 đến hết
c_list = friends [1:]
print(c_list)

# copy thành 1 danh sách mới 
d_list = friends.copy()
print(d_list is friends)

# lấy ra những ng từ thứ 2 đến sát cuối
e_list = friends [1:-1]
print(e_list)
