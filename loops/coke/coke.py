print("Amount Due:50")
var=50
accepted_denominations=[5,10,25]

while var > 0:
    user_input=int(input("Insert Coin: "))
    if user_input not in  accepted_denominations:
        print(f"Amount Due: {var}")
        continue
    if user_input>var:
        var2=user_input-var
        print(f"Change Owed: {var2}")
        break
    var-=user_input
    print(f"Amount Due: {var}")


   

        

    

    
    
        
    

    