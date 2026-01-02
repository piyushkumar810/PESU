# 7.
# Read a file that contains one integer per line. Handle lines that are empty or invalid. Save valid integers in a clean output file.
try:
    with open("input.txt", "r") as infile, open("clean_output.txt", "w") as outfile:
        for line in infile:
            line = line.strip()

            if line == "":
                continue   # Skip empty lines

            try:
                number = int(line)
                outfile.write(str(number) + "\n")
            except ValueError:
                # Skip invalid integers
                continue

    print("Valid integers saved to 'clean_output.txt'.")

except FileNotFoundError:
    print("Error: 'input.txt' file not found.")

except PermissionError:
    print("Error: Permission denied while creating output file.")
