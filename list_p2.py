# list trong list
friends = [["Duy",35],["Tuyết",28],["Thanh",23]]
print(type(friends[0]))

# copy list
list1 = [1,2,3]
list2 = list1.copy()
# is
# id lấy id của list
print(id(list1),id(list2))
print(list1 is list2) 
print(list1 == list2)

# list slicing (lấy ra 1 phần trong list ban đầu  thành list mới)
a = [1,3,10,1000,45]
new_list = a [0:2:1] #[start:stop:step]
new_list = a [:: -1] #lấy đảo ngược list

print(new_list is a)
print(new_list)

