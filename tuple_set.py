"""
Tuple
Các kiểu tuple
tup1 = 1,2,3
tup2 = (1,2,3)
tup3 = 1,
tup4 = (4,)
Không thể thay đổi các giá trị bên trong tuple
Bản thân tuple không thể thay đổi
"""

# Update giá trị tuple
tup1 = 1,2,3
tup1 += (4,5,6)
print(tup1)

"""
Set
Dùng để lưu trữ nhiều giá trị bên trong 1 biến, set không thể chứa giá trị trùng lặp, ko có thứ tự, có thể update
# ten_bien.add(giá trị)
# ten_bien.update([các giá trị])
# ten_bien.remove(giá trị)
# ten_bien_2 = ten_bien_1.copy()
# ten_bien.clear()
Đc sử dụng để so sánh 2 hay nhiều tập hợp để tìm giá trị chung.
Chỉ đc thêm các giá trị ko thể thay đổi trực tiếp trên nó.
"""

# Cài đặt môi trường ảo cho Python / python -m venv venv
# hiển thị list danh sách thư viện đã cài đặt / pip freeze
# Tạo file chứa tất cả thông tin của các thư viện / pip freeze > requirments.txt
# Cài đặt lại file requirments pip install -r .\requirments.txt