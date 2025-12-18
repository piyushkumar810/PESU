# 8. Process a text file that holds daily expenses. Each line has category and amount. 
# Handle missing file, split errors, invalid amounts and empty lines. 
# Create a cleaned version and a rejected version.

try:
    with open("expenses.txt", "r") as infile, \
         open("cleaned_expenses.txt", "w") as clean_file, \
         open("rejected_expenses.txt", "w") as reject_file:

        for line_no, line in enumerate(infile, start=1):
            line = line.strip()

            # Handle empty line
            if not line:
                reject_file.write(f"Line {line_no}: Empty line\n")
                continue

            # Handle split error
            try:
                category, amount = line.split(",")
            except ValueError:
                reject_file.write(f"Line {line_no}: Invalid format -> {line}\n")
                continue

            category = category.strip()
            amount = amount.strip()

            # Handle invalid amount
            try:
                amount = float(amount)
                clean_file.write(f"{category},{amount}\n")
            except ValueError:
                reject_file.write(f"Line {line_no}: Invalid amount -> {line}\n")

    print("Processing completed.")
    print("✔ Valid records saved in 'cleaned_expenses.txt'")
    print("✖ Invalid records saved in 'rejected_expenses.txt'")

except FileNotFoundError:
    print("Error: 'expenses.txt' file not found.")

except PermissionError:
    print("Error: Permission denied while writing output files.")
