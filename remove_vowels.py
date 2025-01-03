vowels="aeiou"
result=""

user_inp=input("Enter the text")

for x in user_inp:
    if x not in vowels:
        result += x

print(result)