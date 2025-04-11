msg=" Hello  all  from   nikhil "

print("1. strip :",msg.strip())
print("4. split :",msg.split())
print("5. upper :",msg.upper())
print("6. lower :",msg.lower())
print("7. replace :",msg.replace("hello","hi"))
print("8. isalpha :",msg.isalpha())
print("9. find :",msg.find("all"))
print("10. count :",msg.count("l"))
words=msg.strip().split(" ")
print("9. split():",words)

print("10. join():","-".join(words))
# print("11. join :" ,msg.join("nikhil Jadhav"))