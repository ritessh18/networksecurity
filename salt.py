import hashlib

def main():
    text = input("Enter a string : ")
    textutf8 = text.encode("utf-8")
    salt = "cdXq126"
    hash = hashlib.md5 (textutf8).hexdigest()
    print (hash+ salt)
    return
main()
