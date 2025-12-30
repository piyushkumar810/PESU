try:
    customers_df = pd.read_csv("C://Users//piyush kumar//OneDrive//Desktop//GitHub//PESU//sem_1//python//U3EL2_file_handling//U3EL3_fille_handling//customer.csv")

    # for index, row in customers_df.iterrows():
    #     print(row)
    for x in customers_df:
        print(x)
except FileNotFoundError:
    print("invalid file")
