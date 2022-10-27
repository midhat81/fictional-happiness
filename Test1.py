import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-OC1AU1B\SQLEXPRESS;'
                      'Database=test_db_yt;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()


cursor.execute(''' INSERT INTO [USER_NAME] (ID,NAME) VALUES ('5','IQBAL') ''')
cursor.commit()
print("Data sent to database successfully.")


# NOW LETS READ TABLE
#cursor.execute('SELECT * FROM [USER_NAME]')

#for i in cursor:
    #print(i)
    
cursor.execute(''' INSERT INTO [USER_NAME] (ID,NAME) VALUES('6', 'UMER')''')
cursor.commit()
print("Data Sent to databse successfully")

 #NOW LETS READ TABLE
cursor.execute('SELECT * FROM [USER_NAME]')

for i in cursor:
    print(i)