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

        if roll not in student:
            student[roll]={
                "Name":name,
                "TotalMark":marks,
                "Count":1
            }
        else:
            student[roll]["TotalMark"]+=marks
            student[roll]["Count"]+=1