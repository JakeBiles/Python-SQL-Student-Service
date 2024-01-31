import mysql.connector
from mysql.connector import errorcode
from collections import defaultdict

# Error Dictionaries
possible_errors = {
    errorcode.ER_ACCESS_DENIED_ERROR: "The username or password are incorrect!",
    errorcode.CR_CONN_HOST_ERROR: "The host could not be resolved!",
    errorcode.ER_BAD_DB_ERROR: "The database does not exist!"
}

error_dict = defaultdict(lambda: "Error not captured --")
for error, text in possible_errors.items():
    error_dict[error] = text

# Functions
# Connect to server
def connectHost():
    try:
        host = str(input("Enter the host ip: "))
        database = mysql.connector.MySQLConnection(
            host=host,
            user="default"
        )
        print("Host confirmed!")
        return database

    except mysql.connector.Error as error:
        print(error_dict[error.errno], "Error:", error)

# user login -- left off here (try and ensure pass/user match)
def databaseLogin(database: mysql.connector.MySQLConnection):
    try:
        user = str(input("Enter the username: "))
        password = str(input("Enter the password for " + user + ": "))
        database.cmd_change_user(user,password)
        print("Successful login")
        return database

    except mysql.connector.Error as error:
        print(error_dict[error.errno], "Error:", error)
        database = database = mysql.connector.MySQLConnection( ## Added
            host=database._host,
            user="default",
        )
        return database

# Connect to database
def connectDatabase(database: mysql.connector.MySQLConnection):
    try:
        databaseName = str(
            input("Enter which database you would like to access: "))
        database.database = databaseName

    except mysql.connector.Error as error:
        print(error_dict[error.errno], "Error:", error)

# Authenticate Connection
def databaseConnect(): # Version 1
    database = None
    attempts = 0
    
    while database == None:
        database = connectHost()
        
    while database.user == "default" and attempts < 3:
        database = databaseLogin(database)
        attempts = attempts + 1
        
    while database.database == None and attempts < 3:
        connectDatabase(database)
    
    if attempts < 3:
        print("Connection to", database.database, "successful!")
        return database
    else: 
        print("Failed to connect to database")

# Add Students from file
def addStudents(filename: str, database: mysql.connector.MySQLConnection):
    cursor = database.cursor()
    try:
        file = open(filename, "r")
        sql_insert_student = "INSERT student_info(first_name,last_name,major,current_year,birthday) VALUES(%s,%s,%s,%s,%s);"
        sql_check_exists = "SELECT first_name,last_name,birthday FROM student_info WHERE first_name=%s AND last_name=%s AND birthday=%s;"

        for line in file:
            # Seperate File-Data by comma
            splitLine = line.split(",")

            # Check if name is already present
            cursor.execute(sql_check_exists, (splitLine[0], splitLine[1], splitLine[4]))
            cursor.fetchall()

            # If name not present add it to database
            if cursor.rowcount == 0:
                cursor.execute(sql_insert_student, (splitLine[0], splitLine[1], splitLine[2], splitLine[3], splitLine[4]))

        database.commit()
        cursor.close()
        file.close()

    except FileNotFoundError:
        print("File could not be found!")
