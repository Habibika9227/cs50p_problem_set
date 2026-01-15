
# user_input=input("Input: ")
# empty_string=""
# for con in user_input:
#     if con not in "aeiouAEIOU":
#         empty_string+=con
        
# print(empty_string)

# f
# string="Good boy"
# clean=""
# for char in string:
#     if char.isalpha() or char.isspace():
#         clean+=char

# print(clean)
var=" good boy good man"
# count=0
# for char in var:
#     if  char.isspace():
#         count+=1
# print(count)
clean=var.lower().split()
print(set(clean))
