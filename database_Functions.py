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
        db = mysql.connector.MySQLConnection(
            host=host,
            user="default"
        )
        print("Host confirmed!")
        return db

    except mysql.connector.Error as error:
        print(error_dict[error.errno], "Error:", error)

# user login -- left off here (try and ensure pass/user match)
def databaseLogin(db: mysql.connector.MySQLConnection):
    try:
        cursor = db.cursor()
        user = str(input("Enter the username: "))
        password = str(input("Enter the password for " + user + ": "))
        print("Successful login")

    except mysql.connector.Error as error:
        print(error_dict[error.errno], "Error:", error)

# Connect to database
def connectDatabase(db: mysql.connector.MySQLConnection):
    try:
        databaseName = str(
            input("Enter which database you would like to access: "))
        db.database = databaseName

    except mysql.connector.Error as error:
        print(error_dict[error.errno], "Error:", error)

# Authenticate Connection
def databaseConnect():
    db = None
    
    while db == None:
        db = connectHost()
    while db.user == "default":
        databaseLogin(db)
    while db.database == None:
        connectDatabase(db)
    
    print("Connection to", db.database, "successful!")
    return db

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
