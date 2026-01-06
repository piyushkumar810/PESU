# to check is 
# python -c "import psycopg2; python -c "import psycopg2; print(psycopg2.__version__)"



import psycopg2

print(psycopg2.__version__)

try:
    # connect to the school database
    conn=psycopg2.connect(
        dbname="School",
        user="postgre",
        password="piyush",
        host="localhost"
    )
    
    if conn:
        print("connection to the postgresql establiched successfuly")
    else:
        print("connection to the postgresql encountered an error")
    
    
    #step 2: open cursor
    cur=conn.cursor()
    
    
    # step 3: create table
    cur.execute(''' create table if not exists studnt(
                student_id serial primary key,
                student_name varchar(80) not null,
                grade varchar(50) not null,
                section varchar(50) not null)
                ''') 
    
    # step 4:-save changes
    conn.commit()
    
    # step 5:-close connection and cursor
    cur.close()
    conn.close()
    
    print("Table created successfully")

except Exception as e:
    print("Database not connected", e)