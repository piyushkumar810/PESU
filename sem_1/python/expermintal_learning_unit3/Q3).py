# write user input to new file .Handel permission if the file cannot be created 
try:
    text = input("Enter text to write into the file: ")

    with open("output.txt", "w") as file:
        file.write(text)

    print("Data written successfully.")

except PermissionError:
    print("Error: You do not have permission to create or write to this file.")

except FileNotFoundError:
    print("Error: Invalid file path.")

except Exception as e:
    print("Unexpected error:", e)
