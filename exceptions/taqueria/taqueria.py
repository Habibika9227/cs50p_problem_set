
var={
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "Super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}
total=0.0
while True:
    try:
        item=input("Item: ").lower()
        if item in var:
            total+=var[item]
            print(f"${total:.2f}")
    except EOFError:
        print()
        break
    
        


 