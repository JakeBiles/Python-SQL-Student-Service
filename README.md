# Python-SQL-Student-Service
 A Pseudo Student Account and Information Service Program

# What this project aims to achieve 
|          Goal         |   Status   |  Version Implmented  | Latest Update |               DESC               |
|          :---:        |    :---:   |         :---:        |      :--:     |               :--:               |
|     SQL Connection    |    Ready   |          V.1         |      V.1      |    Connection w/ SQLConnector    |
|      SQL DB AUTH      |   Partial  |         ~V.1         |      V.1      |    Allow Startup DB Selection    |
|  Student Info Table   |    Ready   |          V.1         |      V.1      |        Contains Names/ID         |
| Student Account Table |  Not Ready |                      |               |   Contains Passwords/UserNames   |
| Student Grades Table  |  Not Ready |                      |               |      Contains Grades/Class       |
|   Password Encoding   |  Not Ready |                      |               |   Password Hidden Within Table   |
|     Student Login     |  Not Ready |                      |               | Allow a Student to Connect to DB |
|      Admin Login      |  Not Ready |                      |               |  Allow an Admin to Connect to DB |
|   Winodow Interface   |  Not Ready |                      |               |     GUI Instead of Terminal      |
|    Grade Entering     |  Not Ready |                      |               |  Allow an Admin to enter Grades  |
|     Grade Checker     |  Not Ready |                      |               |   Allow a Student to check GPA   | 

# Primary Features of this project
-On startup an admin will be able to select which database to connect to.
-Once connected to the desired database, assuming creditintials are correct, the admin can then select Admin, Teacher or Student mode.
-Student mode will allow users to enter credintials to check grades or recieve their student ID.
-Teacher mode will allow users to enter credintials to enter or modify grades.
-Admin mode will allow modify student data.

# Primary Language Used
This system primarly uses the Python language using the MYSQLConnector module.

# Data Protection and Error Handling -- Testing
Various test cases will be ran on each implmented feature, ensuring that the code is valid and without fault. A primary example of this would be prepared statements, where each SQL Query is made using prepared statements. This protects agianst injection, alongside this, encoding for passwords will be used so if a breach is achieved the passwords that are assigned to admin and student accounts are encoded.
