# Read a line from a text file. try to convert the line to int .Handle valueerror ans continue
try:
    with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//expermintal_learning_unit3//content.txt", "r") as file:
        line = file.readline().strip()
        number = int(line)
        print("Converted number:", number)

except FileNotFoundError:
    print("Error: File not found")

except ValueError:
    print("Error: Cannot convert the line to an integer")

except Exception as e:
    print("Unexpected error:", e)
