import csv
# with open("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_1\\python\\csv_file\\emp_det.txt") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     line_count = 0

#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#             line_count += 1

# print(f'Processed {line_count} lines.')




with open("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_1\\python\\csv_file\\emp_det.txt", mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1

        print(f'\t{row["Name"]} works in the {row["Department"]} department '
              f'and was born in {row["City"]}.')
        line_count += 1

print(f'Processed {line_count} lines.')



# ---------------------- csv write
