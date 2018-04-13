def string_length(mystring):
    return len(mystring)
user_input = input("Enter a word: ")
length = (str(string_length(user_input)))
printcall = ''.join(["Your word is ", length, " characters long."])
print(printcall)
