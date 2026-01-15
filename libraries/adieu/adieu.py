import inflect



def main():
    empty_list=[]
    p=inflect.engine()
    
 
    while True:
        try:
            data=input().title()
            empty_list.append(data)
        except EOFError:
            break

    print(f"Adieu, adieu, to {p.join(empty_list)}")
    


main()