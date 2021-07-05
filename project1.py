import hashlib 
str2hash = input("Enter a string : ")
result = hashlib.md5(str2hash.encode())

print("The hexadecimal equivalent of md5 is : ")
print(result.hexdigest())

result = hashlib.sha384(str2hash.encode())
print("The hexadecimal equivalent of SHA256 is :")


result = hashlib.sha512(str2hash.encode())
print("The hexadecimal equivalent of SHA512 is : ")
print(result.hexdigest())


result = hashlib.sha1(str2hash.encode())
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())

