import pyodbc

def createDbConnection():
    connection = pyodbc.connect(Driver="{ODBC Driver 17 for SQL Server}", Server=".", Database="Customers", UID="", PWD="")
    return connection

def closeDbConnection(connection):
    try:
        connection.close()
    except pyodbc.ProgrammingError:
        pass

