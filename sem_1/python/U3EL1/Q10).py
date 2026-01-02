# 10. A file contains one number per line. Raise a custom InvalidNumberError when a line holds letters. Skip the line.
# Define custom exception
class InvalidNumberError(Exception):
    pass


def read_numbers(filename):
    numbers = []

    try:
        with open(filename, "r") as file:
            for line_no, line in enumerate(file, start=1):
                line = line.strip()

                try:
                    # Check if line contains only digits (number)
                    if not line.isdigit():
                        raise InvalidNumberError(
                            f"Invalid number at line {line_no}: {line}"
                        )

                    numbers.append(int(line))

                except InvalidNumberError as e:
                    print(e)
                    # Skip the invalid line
                    continue

    except FileNotFoundError:
        print("File not found!")

    return numbers


# Example usage
result = read_numbers("numbers.txt")
print("Valid numbers:", result)
