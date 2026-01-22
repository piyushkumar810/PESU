# to check is 
# python -c "import psycopg2; python -c "import psycopg2; print(psycopg2.__version__)"



import psycopg2
print(psycopg2.__version__)

try:
    # connect to the school database
    conn=psycopg2.connect(
        dbname="School",
        user="postgres",
        password="Piyush810",
        host="localhost"
    )
    

    if conn:
        print("connection to the postgresql establiched successfuly")
    else:
        print("connection to the postgresql encountered an error")

    '''
    if conn:
    --------or----------
    if conn is not None:
    print("Connection established")
    
    this is better ans readable'''
    
    
    #step 2: open cursor
    cur=conn.cursor()
    
    
    # step 3: create table
    # cur.execute(''' CREATE TABLE students(
    #     student_id SERIAL PRIMARY KEY,
    #     student_name VARCHAR(80) NOT NULL,
    #     grade VARCHAR(10) NOT NULL,
    #     section VARCHAR(5) NOT NULL
    #         );''') 

    # print("Table created successfully")


    #--------------------------- just inserting some data
    # print("triyng to insert data")

    # cur.execute('''insert into students(student_name,grade,section)
    #             values('piyush kumar', 'A', 'MCA-C');
    #  ''')
    
    # print("data inserted successfully")


    # ----------------------- deleting one record or one piyush kumar data
    # cur.execute('''
    #         delete from students where student_id=2;
    # ''')
    # print("successfully deleted one record")


    # -----------------------------fetcing data
    print("trying to fetch data")

    cur.execute('''select * from students;
    ''')
    print("data fetched successfully")
    
    ''' this way the output will not reflect here '''

    # ------------------------- if you want to see the output here
    rows = cur.fetchall()
    '''👉 Retrieves all rows from database'''

    # to display it
    for i in rows:
        print(i)


    # step 4:-save changes
    conn.commit()
    
    # step 5:-close connection and cursor
    cur.close()
    conn.close()

except Exception as e:
    print("Database not connected", e)