import hashlib,sys
def hash_func():
    def md5():
        print("\n")
        md5text = input("enter the text to convert it into md5: ")
        hash_object_md5 = hashlib.md5(str(md5text).encode('utf-8'))
        print("\n")
        print('Hash for the text in md5 is :  ', hash_object_md5.hexdigest())
        print("\n")
    def sha512():
        print("\n")
        sha512text = input("enter the text to convert it into sha512: ")
        hash_object_sha512 = hashlib.sha512(str(sha512text).encode('utf-8'))
        print("\n")
        print('Hash for the text in sha512 is :  ', hash_object_sha512.hexdigest())
        print("\n")
    def sha256():
        print("\n")
        sha256text = input("enter the text to convert it into sha256: ")
        hash_object_sha256 = hashlib.sha256(str(sha256text).encode('utf-8'))
        print("\n")
        print('Hash for the text in sha256 is :  ', hash_object_sha256.hexdigest())
        print("\n")
    def sha3_256():
        print("\n")
        sha3256text = input("enter the text to convert it into sha3_256: ")
        hash_object_sha3256 = hashlib.sha3_256(str(sha3256text).encode('utf-8'))
        print("\n")
        print('Hash for the text in sha3_256 is :  ', hash_object_sha3256.hexdigest())
        print("\n")
    def sha3_512():
        print("\n")
        sha3512text = input("enter the text to convert it into sha3_512: ")
        hash_object_sha3512 = hashlib.sha3_512(str(sha3512text).encode('utf-8'))
        print("\n")
        print('Hash for the text in sha3_512 is :  ', hash_object_sha3512.hexdigest())
        print("\n")
    menu = str(input("Choose the number which you want to execute  1.md5  2.sha512  3.sha256  4.sha3_256  5.sha3_512 : "))
    if menu == "1":
      md5()
    elif menu == "2":
      sha512()
    elif menu == "3":
      sha256()
    elif menu == "4":
      sha3_256()
    elif menu == "5":
      sha3_512()2
    else: 
      sys.exit(0)
    runagain = str(input("Do you want to use this again (type 1 or 0): "))
    print("\n")
    while runagain == "1":
      hash_func()
    else:
      print("\n")
      print("closing the programme")
      sys.exit(0)
hash_func()
