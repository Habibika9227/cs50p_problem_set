
def main():
    quiz=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()
    if quiz=="42" or quiz=="forty-two" or quiz=="FoRty TwO" or quiz=="forty two" :
        print("Yes")

    # elif quiz=="forty-two":
    #     print("Yes")

    # elif quiz=="forty two":
    #     print("Yes")

    else:
        print("No")

main()