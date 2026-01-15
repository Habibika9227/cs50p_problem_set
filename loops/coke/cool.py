
# def main():
#     print("Amount Due:50")
#     user_input=int(input("insert coin: "))


   
#     while True:
#         if user_input==5:
#             result=50 - user_input
#         elif user_input==10:
#             result=50 - user_input
#         elif user_input== 25:
#             result=50 -user_input
#         else:
#             break

    

# main()
# prompt="\nPlease enter the name of the cities you've visited: "
# prompt+="\n(Enter 'quit' to end the program) "
# # active=True
# while True:
#     message=input(prompt)
#     if message=="quit":
#         print("Finished!!!")
#         break
        

#     else:
#         print(F"I'll love to go {message.title()}")
# count=0
# while count < 10:
#     count+=1

#     if count==5:
#         continue
#     print(count)
# uncomfirmed_users=['Alice','Ali','Abdi','Abdillahi']
# confirmed_users=[]

# while uncomfirmed_users:
#     current_key=uncomfirmed_users.pop()
#     print(f"Verifying users: {current_key}")
#     confirmed_users.append(current_key)

# print("\nVertification completed succesfully")
# for con in confirmed_users:
#     print(con)
# pest_list=['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pest_list)
# removed_list=[]
# while 'cat' in  pest_list:
#     result=pest_list.remove('cat')

#     removed_list.append(result)

    
# print(pest_list)

# empty_dictionary={}
# active=True
# while active:
#    name=input("\n Enter your name: ")
#    response=input("\n Which mountain would like to climb someday? ")
#    empty_dictionary[name]=response
   
#    another_question=input("Would u like to continue the poll running? ")
#    if another_question=="no":
#       active =False
# print("=== POLL RESULT ===")
# for name,value in empty_dictionary.items():
#    print(f"{name} would like to climb {value}")
# #    print(f"{name} would like to climb {value}")
empty_dictionary={}
# active=True
# while active:
#    name=input("\n Enter your name: ")
#    response=input("\n Which mountain would like to climb someday? ")
#    empty_dictionary[name]=response
   
#    another_question=input("Would u like to continue the poll running? ")
#    if another_question=="no":
#       active =False
# print("=== POLL RESULT ===")
# for name,value in empty_dictionary.items():
#    print(f"{name} would like to climb {value}")
# empty_dictionary={}
# active=True
# while active:
#    name=input("\n Enter your name: ")
#    response=input("\n Which mountain would like to climb someday? ")
#    empty_dictionary[name]=response
   
#    another_question=input("Would u like to continue the poll running? ")
#    if another_question=="no":
#       active =False
# print("=== POLL RESULT ===")
# for name,value in empty_dictionary.items():
#    print(f"{name} would like to climb {value}")
# #    print(f"{name} would like to climb {value}")
#    print(f"{name} would like to climb {value}")
empty_dictionary={}
# active=True
# while active:
#    name=input("\n Enter your name: ")
#    response=input("\n Which mountain would like to climb someday? ")
#    empty_dictionary[name]=response
   
#    another_question=input("Would u like to continue the poll running? ")
#    if another_question=="no":
#       active =False
# print("=== POLL RESULT ===")
# for name,value in empty_dictionary.items():
#    print(f"{name} would like to climb {value}")
# #    print(f"{name} would like to climb {value}")
empty_dictionary={}
# active=True
# while active:
#    name=input("\n Enter your name: ")
#    response=input("\n Which mountain would like to climb someday? ")
#    empty_dictionary[name]=response
   
#    another_question=input("Would u like to continue the poll running? ")
#    if another_question=="no":
#       active =False
# print("=== POLL RESULT ===")
# for name,value in empty_dictionary.items():
#    print(f"{name} would like to climb {value}")
# #    print(f"{name} would like to climb {value}")
# empty_dictionary={}
# active=True
# while active:
#    name=input("\n Enter your name: ")
#    response=input("\n Which mountain would like to climb someday? ")
#    empty_dictionary[name]=response
   
#    another_question=input("Would u like to continue the poll running? ")
#    if another_question=="no":
#       active =False
# print("=== POLL RESULT ===")
# for name,value in empty_dictionary.items():
#    print(f"{name} would like to climb {value}")
# #    print(f"{name} would like to climb {value}")



# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
# sandwiches. Then make an empty list called finished_sandwiches. Loop through
# the list of sandwich orders and print a message for each order, such as I made
# your tuna sandwich. As each sandwich is made, move it to the list of finished
# sandwiches. After all the sandwiches have been made, print a message listing
# each sandwich that was made.
# sandwich_orders=["Tuna sandwich","Beef sandwich","Mutton sandwich","vege sandwich"]
# finished_sandwiches=[]

# while sandwich_orders:
#     current_value=sandwich_orders.pop(0)
#     print(f"I made your  {current_value}")
#     finished_sandwiches.append(current_value)

# for sandwich in finished_sandwiches:
#     print(f"{sandwich} was made")






# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

# sandwich_orders=["Tuna sandwich","pastrami","Beef sandwich","pastrami","Mutton sandwich","pastrami","vege sandwich"]
# print("deli has run out of pastrami")
# empty=[]

# while "pastrami" in sandwich_orders:
#     sandwich_orders.remove("pastrami")
    

# while sandwich_orders:
#     popping=sandwich_orders.pop(0)
#     empty.append(popping)
# print(empty) 
# 
# 
# response={}
# active=True
# while active:
#     name=input("Enter your name: ").title()
#     print(f"Hi,{name}")
#     que=input("If you could visit one place in the world, where would you go? ").title()
#     print(f"Good choice, {que} is crazy place.")
#     response[name]=que

#     repeat=input("Do u like to continue? type yes/no ").lower()
#     # print(f"Good choice, {repeat} is crazy place.")
#     if repeat=="no":
#        active=False

# print("=== POLLING RESULT ===")
# for name,value in response.items():
#     print(f"{name} is going to {value}")

guess=8

guses_count=0
while guses_count < 4:
    guess_number=int(input("Guess a number: "))
    guses_count+=1
    if guess_number==8:
        print("You won !!")
    else:
        print("You failed, restart the game.")

print("You may have made four gueses")






