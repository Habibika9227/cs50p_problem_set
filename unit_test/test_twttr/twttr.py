
def main():
    
    data=input().strip()    
    content=shorten(data)
    print(content)

def shorten(word):
    variable=""
    
    for char in word:
         
         if  char not in "aeiouAEIOU":
            variable+=char

    return variable
        
        
if __name__ == "__main__":
    main()
