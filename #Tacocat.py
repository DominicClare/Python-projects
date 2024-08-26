#Tacocat

string = input("please input a word: ")
string_r = string[::-1]

if string == string_r:
    print("Is a palindrome!")
else:
    print("Is not a palindrome!")