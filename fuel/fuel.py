

def main():
    while True:
      try:
          get_input=input("Fracton: ")
          
          cal1=get_input.split("/")
          x=int(cal1[0])
          y=int(cal1[1])
          
          if x>y or y==0:
             continue
          if x<=0 or y<=0:
             continue
          result=round((x/y)*100)
        
          break # Exit the loop only if no error happens
      except (ValueError,ZeroDivisionError):
         
         continue
    if result<=1:
       print("E")
    elif result>=99:
       print("F")
    
    else: 
       print(f"{result}%")

main()
    
   
   

