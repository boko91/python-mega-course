def string_length(mystring):
    return len(mystring)
user_input = str(input("Enter a word: "))
length = string_length(user_input)
printcall = ''.join(["Your word is ", length, " characters long."])
print(printcall)
