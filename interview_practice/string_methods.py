text =  " hello goodmorning"
print(text.capitalize())
print(text.lower())
print(text.upper())
print(text.title())
print(text.swapcase())
print(text.strip())
print(text.lstrip())
print(text.rstrip())
print(text.replace("goodmorning", "world"))
print(text.split())
print(text.find("world"))
# print(text.index("world"))
# print(text.count())
print(text.isalnum())
print(text.isalpha())
print(text.isdigit())
print(text.isspace())
print(text.endswith("world"))

text1 = "testhook"
print(text1.removeprefix("test"))
print(text1.removesuffix("hook"))
print(text1.zfill(15)) 

words = ['hello', 'world']
print(  'vaidik'.join(words))  # Output: "hello world"
