import hashlib 
str2hash = input("Enter a string : ")
result = hashlib.md5(str2hash.encode())

print("The hexadecimal equivalent of md5 is : ")
print(result.hexdigest())