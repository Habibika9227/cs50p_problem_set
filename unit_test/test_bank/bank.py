
def main():
    data=input().lower().strip()
    content=value(data)
    print(f"${content}")


def value(greeting):
    text=greeting.lower()
    if text.startswith("hello"):
        return 0
    elif text.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
