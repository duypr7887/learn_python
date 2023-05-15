"""
2. Tạo 1 set trống có tên set a
a. Thêm Anna vào set a
b. Thêm 1 tuple ('Kenny', 'Jen', 'Danny')
c. In ra set a và tìm chiều dài của nó 
d. Xóa 'Jen' ra khỏi set a
e. Xóa tất cả các giá trị từ set a
"""
# 2
set_a = set()

# a.
set_a.add("Anna")
print(set_a)

# b. c.
set_a.update(['Kenny', 'Jen', 'Danny'])
print(set_a)
lengh = len(set_a)
print(lengh)

# d.
set_a.remove("Jen")
print(set_a)

# e.
set_a.clear()
print(set_a)