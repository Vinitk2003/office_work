#type conversion is doing automatically
# a =
# sum =  2
# b = 4.25a + b # 2 + 4.25 = 6.25
# print(sum)

#type casting is doing manually
a, b = 1, "2"
c = int(b)
sum = a + c
print(sum)

#also use this
a = int("23")
b = 33.4

mul = a * b
print(mul)
print(type(a))



