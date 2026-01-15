def convert(text):
    text=text.replace("Hello :)","Hello 🙂")
    text=text.replace("Goodbye :("," Goodbye 🙁")
    return text
def main():
    user_input=input("")
    converted= convert(user_input)
    print(converted)
    

main()