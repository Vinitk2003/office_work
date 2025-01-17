#list 
marks = [45, 56, 67, 88, 86]
print(marks)
print(type(marks))

#list methods
marks.append(33)  ## add it last
print(marks)

marks.sort(reverse=True)
print(marks)

marks.reverse()
print(marks)

#tuples
tup = (87, 77, 33, 96)
print(type(tup))

tup1 = (1,) # for define tuple single value use comaa seprated
print(tup1)

#tuple methods
tup2 = (2,1,3,1)
print(tup2.index(2))

print(tup2.count(1))




