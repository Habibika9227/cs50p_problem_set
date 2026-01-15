


def main():
    data=input().strip()
    content=convert(data)
    var=gauge(content)
    print(var)

def convert(fraction):
    convert_text=fraction.split("/")
    x=int(convert_text[0])
    y=int(convert_text[1])
    
     
    if x>y:
         raise ValueError
    elif y==0:
         raise ZeroDivisionError 
    elif x<0 or y<0:
         raise ValueError  
    elif x<0 or y<0:
         raise ValueError
    cal=(x/y)*100

    return int(round(cal))


def gauge(percentage):
    if percentage<=1:
         return f"E"
    elif percentage>=99:
         return f"F"
    else:
         return f"{percentage}%"


if __name__ == "__main__":
    main()