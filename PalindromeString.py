file=open("palindromestring.txt",'w')
str=input("Enter String: ")
file.write("Enter String:")
file.write(str)
file.write('\n')
Temp=str[::-1]
if str==Temp:
    print("True")
    file.write("Given string is palindrome")
else:
    print("False")
    file.write("Given string is not a palindrome")
