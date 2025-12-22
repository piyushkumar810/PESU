import csv

print("WITHOUT newline='':\n")

with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//concepts//using_of_newline_in_csv//demo.csv", "w") as file:      # ❌ no newline
    writer = csv.writer(file)
    writer.writerow(["ID", "Name"])
    writer.writerow([1, "Piyush"])
    writer.writerow([2, "Rohit"])

with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//concepts//using_of_newline_in_csv//demo.csv", "r") as file:
    for line in file:
        print(repr(line))


print("\nWITH newline='':\n")

with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//concepts//using_of_newline_in_csv//demo2.csv", "w", newline="") as file:   # ✅ newline=""
    writer = csv.writer(file)
    writer.writerow(["ID", "Name"])
    writer.writerow([1, "Piyush"])
    writer.writerow([2, "Rohit"])

with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//concepts//using_of_newline_in_csv//demo2.csv", "r") as file:
    for line in file:
        print(repr(line))


'''
| Case                 | Newlines per row |
| -------------------- | ---------------- |
| Without `newline=""` | **2 newlines** ❌ |
| With `newline=""`    | **1 newline** ✅  |

'''