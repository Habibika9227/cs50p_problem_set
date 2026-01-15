user_input=input("camelCase: ")
result=""

for char in user_input:
    if char.isupper():
     result+="_"
     result+=char.lower()  
    else:
     result+=char
print(f"snake_case: {result}")


