#nested if

age = 45
  # Example age, you can change this value to test

if age == 18:
    print("You are an adult")
    if 18 <= age <= 60:  # Checks if age is between 18 and 60
        print("You are young")
    elif age >= 65:  # If age is 65 or more
        print("You are a senior citizen")
    else:
        print("You are not an adult")
else:
    print("You are a minor")


# practice enter num is odd or even
# num = int(input("enter num"))

# if(num %2 == 0):
#     print("num is even")
# else:
    # print("num is odd")

#find gretest num from three numbers

# num1 = int(input("enter num1 "))
# num2 = int(input("enter num2 "))
# num3 = int(input("enter num3 "))

# if(num1 >= num2 and num1 >= num3):
#     print("first num is large : " , num1)
# elif(num2 >= num3):
#     print("second num is large : " , num2)
# else:
#     print("third num is largest : ", num3)

# num multiple of seven

# x = int(input("enter nnum "))

# if(x % 7 == 0):
#     print("num is multiple of 7")
# else:
#     print("num is not multiple of 7")


str1 = "hello"
print(str1[::-1])