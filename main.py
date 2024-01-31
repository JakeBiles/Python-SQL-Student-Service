import database_Functions as dbfx
import main_Functions as mfx

database = dbfx.databaseConnect()

if database:
    cursor = database.cursor()
    dbfx.addStudents("tests.txt", database)
    database.close()
