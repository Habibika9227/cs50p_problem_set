

# def main():
#     var_set={
#         "apple":130,
#         "avocado":50,
#         "banana":110,
#         "cantaloupe":50,
#         "grapefruit":60,
#         "grapes":90,
#         "honeydew Melon":50,
#         "kiwifruit":90,
#         "lemon":15,
#         "lime":20,
#         "nectarine":60,
#         "orange":80,
#         "peach":60,
#         "pear":100,
#         "pineapple":50,
#         "plums":70,
#         "strawberries":50,
#         "sweet cherries":100,
#         "tangerine":50,
#         "watermelon":80


#     }
#     get_users=input("Item: ").lower()
#     for keys,values in var_set.items():
#         if get_users==keys:
#             print(f"Calories: {values}")

# main()

#Let's play with tuples.
# var=(23.5,45)
# condinates=var
# lat,long=condinates
# print(lat)
# for lat in var:
#     print(lat[1])


#set
# var_set={"red","blue","green"}
# for set_in in var_set:
#     print(set_in(set_in[0]))

# var_set=set()
# while True:
#     word=input("Enter word(or q): ")
#     if word=="q":
#         break
#     var_set.add(word)

# print(var_set)

# var2={"apple","orange","Lemon"}
# if "apples" in var2:
#     print("found!!")
# else:
student ={}
while True:
    name=input("Enter name: ")
    keys=input("major: ")
    student[name]=keys
    if name=="q" or keys=="q":
        break

print(student)
