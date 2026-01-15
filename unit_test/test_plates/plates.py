
def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
        
        if not(2<=len(s)<=6):
             return 
        #checking the first two characters to be letters
        if not(s[0].isalpha() and s[1].isalpha()):
             return False
        #checking the number positions
        number_flag=False

        for number in s[2:]:
             if number.isdigit():
                if not number_flag:
                   if number=="0":
                       return False
                number_flag=True
             else:
                if number_flag:
                    return False
                
        return True
                        
if __name__=="__main__":
    main()
