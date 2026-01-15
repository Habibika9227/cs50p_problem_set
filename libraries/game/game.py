import random
def main():
    
    while True:
        
        try:
            level=int(input("Level: ").strip())
            
            if level > 0 :
                break
        except ValueError:
            pass

    secret=random.randint(1,level)

    while True:
        Guess=int(input("Guess: "))
        if Guess < secret:
            print("Too small!")
            continue


        elif Guess > secret:
            print("Too large!")
            continue

        else:
            print("Just right!")
            break
main()


            

            

           
