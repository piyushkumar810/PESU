# Read a text file of names. Ask the user for a search name. Handle FileNotFoundError and
# handle cases where search name is not found.
try:
    search_name = input("Enter the name to search: ").strip().lower()

    with open("names.txt", "r") as file:
        names = [line.strip().lower() for line in file]

    if search_name in names:
        print("Name found in the file.")
    else:
        print("Name not found in the file.")

except FileNotFoundError:
    print("Error: The file 'names.txt' does not exist.")

except Exception as e:
    print("Unexpected error:", e)
