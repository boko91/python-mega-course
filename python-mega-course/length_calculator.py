def string_length(mystring):
    return len(mystring)

user_input = input("Enter a word: ")

try:
    user_input.encode('ascii')
except UnicodeEncodeError:
    print("Bad input!!! You broke the rules. Good bye.")
else:
    length = str(string_length(user_input))
    printcall = ''.join(["Your word is ", length, " characters long."])
    print(printcall)
