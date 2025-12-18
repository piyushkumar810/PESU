# open a text file and read the first five lines. Handle error when the file is empty

try:
    with open("data.txt", "r") as file:
        lines = file.readlines()

        if len(lines) == 0:
            raise ValueError("File is empty")

        print("First five lines:")
        for line in lines[:5]:
            print(line.strip())

except FileNotFoundError:
    print("Error: File not found")

except ValueError as ve:
    print("Error:", ve)

except Exception as e:
    print("Unexpected error:", e)
