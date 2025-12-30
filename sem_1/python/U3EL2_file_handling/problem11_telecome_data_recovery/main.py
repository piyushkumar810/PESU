# Mission: The Telecom Data Recovery & Billing Audit
# The Scenario: You are working for a telecom company that has two separate datasets. 
# A system glitch has caused "Garbage Data" (non-numeric strings or empty values) to appear in the usage logs. 
# You must recover the clean data, merge it with user profiles, and calculate monthly bills based on specific slabs.
# . The Input Files
# · user_profiles.csv: Contains UserlD, Name, and PlanType.
# · usage_logs.csv: Contains LoglD, UserlD, and DataUsedMB
# 。Challenge: The DataUsedMB column contains corrupted entries like "150MB", "NULL", or "-50".

# ---------------explanation
'''
📌 What is the problem about?

You are working for a telecom company.
Due to a system glitch, the usage data is corrupted.

Your job is to:
Clean the corrupted data
Merge two datasets
Calculate monthly bills using slabs

This is a real-world data engineering / data processing problem.
'''

import csv
# first creating user_profile.csv
user_profile_data=[['UserID','Name','PlanType'],
                   ["U101", "Piyush", "Basic"],
                   ["U102", "Rohit", "Premium"],
                   ["U103", "Aman", "Standard"],
                   ["U104", "Neha", "Basic"]]

usage_logs_data=[['LoglD','UserlD','DataUsedMB'],
                 ["L1", "U101", "500"],
                 ["L2", "U101", "150MB"],
                 ["L3", "U102", "NULL"],
                 ["L4", "U102", "-50"],
                 ["L5", "U103", "1800"],
                 ["L6", "U104", ""],
                 ["L7", "U104", "300"]]

with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//problem11_telecome_data_recovery//user_profile.csv","w",newline="")as user_file:
    write=csv.writer(user_file)
    write.writerows(user_profile_data)

with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//problem11_telecome_data_recovery//usage_logs.csv","w",newline="")as usage_file:
    write=csv.writer(usage_file)
    write.writerows(usage_logs_data)


# READ user_profile.csv INTO DICTIONARY
users={}
try:
    with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//problem11_telecome_data_recovery//user_profile.csv","r",newline="")as user_file_read:
        reader=csv.DictReader(user_file_read)
        for row in reader:
            users[row["UserID"]] = {
                "Name": row["Name"],
                "PlanType": row["PlanType"]
            }
            
except Exception as e:
    print("file not found exception",e)

# read usage_logs.csv into dictionary
usages={}
try:
    with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//problem11_telecome_data_recovery//usage_logs.csv","r",newline="")as usage_file_read:
        reader1=csv.DictReader(usage_file_read)
        for row1 in usage_file_read:
            print(row1)

except FileNotFoundError:
    print("file not found")