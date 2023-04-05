"""
1. Cho  1 list chứa các tuple như sau: friends = [("Bob","Male"),("Anne","Female"),("Max","Male")]
    a. Cho biết chiều dài của friends
    b. Lấy ra phần tử đầu, cuối và giữa kiểm tra kiểu của chúng
    c. Nhập vào tên (name) và giới tính (gender) của 1 người bạn sau đó append vào friends tuple gồm 2 giá trị (name,gender)
"""
# 1.
# a.
friends = [("Bob","Male"),("Anne","Female"),("Max","Male")]

lengh = len(friends)
print(lengh)

# b.
friend1 = friends[0]
print('Friend 1: ',friend1)
print(type(friend1))

friend2 = friends[1]
print('Friend 2: ',friend2)
print(type(friend2))

friend3 = friends[2]
print('Friend 3: ',friend3)
print(type(friend3))

# c
name = input("Nhập vào tên: ")
gender = input("Nhập vào giới tính: ")
friend4 = name, gender
friends.append(friend4)
print(friends)