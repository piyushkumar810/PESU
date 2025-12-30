usages={}
try:
    with open("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//problem11_telecome_data_recovery//usage_logs.csv","r",newline="")as usage_file_read:
        reader1=csv.DictReader(usage_file_read)
        for row1 in usage_file_read:
            print(row1)
except FileNotFoundError:
    print("file not found")