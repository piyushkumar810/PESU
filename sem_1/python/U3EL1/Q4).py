# convert a string to an integer .Handle ValueError and continue the program without stopping
while True:
    s = input("Enter a number (or 'q' to quit): ")

    if s.lower() == 'q':
        print("Program ended.")
        break

    try:
        number = int(s)
        print("Converted integer:", number)

    except ValueError:
        print("Invalid input! Cannot convert to integer.")
        print("Continuing program...\n")
