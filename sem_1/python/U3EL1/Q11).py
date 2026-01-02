# 11. Read marks from a file. Raise a custom NegativeMarkError when the mark is below zero. Raise a custom HighMarkError when the mark is above one hundred. Save valid marks to a clean file.
# Custom Exceptions
class NegativeMarkError(Exception):
    pass

class HighMarkError(Exception):
    pass


def process_marks(input_file, output_file):
    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:

            for line_no, line in enumerate(infile, start=1):
                line = line.strip()

                try:
                    mark = int(line)

                    if mark < 0:
                        raise NegativeMarkError(
                            f"Line {line_no}: Negative mark {mark}"
                        )

                    if mark > 100:
                        raise HighMarkError(
                            f"Line {line_no}: Mark above 100 ({mark})"
                        )

                    # Valid mark → save to clean file
                    outfile.write(str(mark) + "\n")

                except (NegativeMarkError, HighMarkError) as e:
                    print(e)
                    # Skip invalid marks
                    continue

                except ValueError:
                    print(f"Line {line_no}: Invalid data '{line}'")

    except FileNotFoundError:
        print("Input file not found!")
