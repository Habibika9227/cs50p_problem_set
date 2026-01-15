

def main():
    while True:
      try:
          get_input=input("Fracton: ")
          result=calculations(get_input)
          break # Exit the loop only if no error happens
      except ValueError:
         pass
         continue
    if result<=1:
       print("E")
    elif result>=99:
       print("F")
    else: 
       print(f"{result}%")

def calculations(cal):
   cal1=cal.split("/")
   x=int(cal1[0])
   y=int(cal1[1])
   result= (x/y) * 100

   if y=="0":
      raise ZeroDivisionError
   return  int(result)
   

  

main()
    
   
   

