import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-9J1E8GH\SQLEXPRESS;'
                      'Database=FORM_1;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()


cursor.execute(''' INSERT INTO [USER_TABLE] (ID, FIRST NAME, LAST NAME, EMAIL) VALUES ('0,1,2','FIRST NAME' 'LAST NAME' 'EMAIL') ''')
cursor.commit()
print("Data sent to database successfully.")

#NOW LETS READ TABLE
cursor.execute('SELECT * FROM [USER_TABLE]')

for i in cursor:
    print(i)