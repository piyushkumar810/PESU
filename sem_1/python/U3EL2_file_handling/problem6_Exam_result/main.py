# question
'''
Question

Write a Python program to merge exam results using two CSV files.

Two CSV files are provided:

theory_marks.csv containing the columns:
RollNo, Subject, Marks

lab_marks.csv containing the columns:
RollNo, Subject, Marks

The program should perform the following tasks:
    Read both CSV files from disk.
    Calculate the total marks per student by combining theory and lab marks.
    Create a new CSV file named final_result.csv.
    Store the following columns in the output file:
        RollNo
        TotalMarks
        Result

    Assign Result as:
        Pass if TotalMarks ≥ 40
        Fail otherwise.
'''

import csv
total_marks={}

with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//problem6_Exam_result//theory_mark.csv","r",newline="") as theory_file:
    theory_reader=csv.DictReader(theory_file)

    for row in theory_reader:
        roll=row["RollNo"]
        mark=int(row["Marks"])
        
        if roll in total_marks:
            total_marks[roll] = total_marks[roll] + mark
        else:
            total_marks[roll] = mark

with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//problem6_Exam_result//lab_mark.csv","r",newline="") as lab_file:
    lab_reader=csv.DictReader(lab_file)

    for row in lab_reader:
        roll=row["RollNo"]
        mark=int(row["Marks"])
        
        if roll in total_marks:
            total_marks[roll] = total_marks[roll] + mark
        else:
            total_marks[roll] = mark

with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//problem6_Exam_result//final_result.csv","w",newline="") as file:
    fieldnames = ["RollNo", "TotalMarks", "Result"]
    writer=csv.DictWriter(file,fieldnames=fieldnames)

    writer.writeheader()

    for roll in total_marks:
        total=total_marks[roll]
        result="Pass" if total>=40 else "Fail"

        writer.writerow({
            "RollNo":roll,
            "TotalMarks":total,
            "Result":result
        })
print("final_result.csv created successfully.")
