# 6.
# Read a 'marks.txt' file. Some lines hold invalid marks. Handle conversion errors. Print total and average marks from valid lines.

total = 0
count = 0

try:
    with open("marks.txt", "r") as file:
        for line in file:
            try:
                mark = float(line.strip())
                total += mark
                count += 1
            except ValueError:
                # Invalid mark → skip and continue
                continue

    if count > 0:
        average = total / count
        print("Total Marks:", total)
        print("Average Marks:", average)
    else:
        print("No valid marks found.")

except FileNotFoundError:
    print("Error: 'marks.txt' file not found.")
