students = [["SV001", "Bod", 23],
            ["SV002", "Kenny", 34], 
            ["SV003", "Henry", 45]]

# Lấy ra thông tin sinh viên thứ 1 và in dưới dạng ""ID: {id}, name: {name}, - age:{age}""
a_student = students[0]
print("ID: ", a_student[0])
print("Name: ", a_student[1])
print("Age: ", a_student[2])

# lấy ra tuổi sinh viên thứ 2 
# print(students[1][-1])
# b_student = students[1]
print("Tuổi sinh viên thứ 2: ",students[1][-1])

# lấy ra thông tin 2 sinh viên cuối cùng
c_student = students[1:]
print(c_student[0])
print(c_student[1])

# lấy ra id của sinh viên thứ 3
print("Id của sinh viên thứ 3: ", students[-1][0])