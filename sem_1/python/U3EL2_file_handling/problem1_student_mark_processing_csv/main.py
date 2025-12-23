import csv

student={}

with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//problem1_student_mark_processing_csv//students.csv","r",newline="") as file:
    reader=csv.DictReader(file)
    '''DictReader reads each row as a dictionary
        Column names become keys
        Example row becomes: {'RollNo':'1', 'Name':'Piyush', 'Subject':'Maths', 'Marks':'50'} '''
    # ------- checking how reader stores 
    # for row in reader:
    #     print(row)
    # -----------output
    '''
    {'RollNo': '1', 'Name': 'Piyush', 'Subject': 'Maths', 'Marks': '50'}
    {'RollNo': '1', 'Name': 'Piyush', 'Subject': 'Science', 'Marks': '60'}
    {'RollNo': '1', 'Name': 'Piyush', 'Subject': 'English', 'Marks': '40'}
    {'RollNo': '2', 'Name': 'Rohit', 'Subject': 'Maths', 'Marks': '30'}
    {'RollNo': '2', 'Name': 'Rohit', 'Subject': 'Science', 'Marks': '35'}
    {'RollNo': '2', 'Name': 'Rohit', 'Subject': 'English', 'Marks': '25'}
    '''

    for row in reader:
        roll=row["RollNo"]
        name=row["Name"]
        marks=int(row["Marks"])


        '''{'RollNo': '1', 'Name': 'Piyush', 'Subject': 'Maths', 'Marks': '50'}
        first row came inside roll it will check is roll 1 is prestnt inside the student
        first time no
        then student will save roll 1 with name and totalmark
         
        {'RollNo': '1', 'Name': 'Piyush', 'Subject': 'Science', 'Marks': '60'}
        2nd time loop runs again it will check is roll 1 present inside the student
        2nd time yes
        it will go to the else blockand for roll 1 it will keep no adding his totalmark 
         '''
        if roll not in student:
            student[roll]={
                "Name":name,
                "TotalMark":marks,
                "Count":1
            }
        else:
            student[roll]["TotalMark"]+=marks
            student[roll]["Count"]+=1

with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//problem1_student_mark_processing_csv//student_summary.csv","w",newline="") as file:
    fieldnames=["RollNo","Name","AverageMarks","Result"]
     # Defines column headings for the output CSV file

    writer=csv.DictWriter(file,fieldnames=fieldnames) 
    '''Creates a DictWriter object
        Used to write rows as dictionaries'''

    writer.writeheader()
    '''
    writeheader():
        Is used only with DictWriter
        Writes one row only
        Should be called before writing data rows --> as writerow()
        It is optional, but recommended


    eg:-✅ What if we DON'T write writeheader()?
            output will be :- 1,Piyush,50,Pass

            ❌ No column headings
            ❌ Hard to understand data
            ❌ Bad for reports/exam answers

        ✅ With writeheader()
            ------ output -------
            RollNo,Name,AverageMarks,Result
            1,Piyush,50,Pass

            ✔ Clear
            ✔ Structured
            ✔ Professional
    '''

    

    '''
    Loops through each student stored in the dictionary
        roll → Roll number
        data → Name, Total, Count
    '''
    for roll,data in student.items():
        avg=data["TotalMark"]/data["Count"]
        result="Pass" if avg>=40 else "Fail"

        writer.writerow({
            "RollNo":roll,
            "Name":data["Name"],
            "AverageMarks":round(avg,2),
            "Result":result
        })
        '''
        Writes one row per student into output CSV
        round(average, 2) limits average to 2 decimal places
        '''

print("student_summary.csv successfuly created")