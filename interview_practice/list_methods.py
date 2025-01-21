my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

my_list.extend([3, 4])
print(my_list) 

my_list.insert(2, 3)  
print(my_list) 

my_list.remove(3)
print(my_list) 

popped_item = my_list.pop()
print(popped_item)  
print(my_list)

my_list.clear()
print(my_list) 

my_list = [1, 2, 3, 4]
index_of_3 = my_list.index(3)
print(index_of_3) 

count_of_2 = my_list.count(2)
print(count_of_2)

my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list.reverse()
print(my_list) 
new_list = my_list.copy()
print(new_list)

my_list = ['Hello', 'World']
result = " ".join(my_list)
print(result)  # Output: "Hello World"

keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

text2 = "hello wor"
print(text2.zfill(10))  # Output: "00042"

text3 = "123 45"
print(text3.split()) 