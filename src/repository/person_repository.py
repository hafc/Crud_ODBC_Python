from datetime import datetime
from typing import List
import repository.database_connection
import models.person

def create_new_person(person):
    connection =  repository.database_connection.createDbConnection()
    cursor = connection.cursor()
    params = (person.name, person.email, person.salary, person.age, datetime.today())
    query = '''INSERT INTO [dbo].[Persons]([Name],[Email],[Salary],[Age],[CreatedAt]) VALUES(?,?,?,?,?)'''
    cursor.execute(query, params)
    connection.commit()
    cursor.close()
    repository.database_connection.closeDbConnection(connection)

def update_person(id, person):
    connection = repository.database_connection.createDbConnection()
    cursor = connection.cursor()
    query = '''UPDATE [dbo].[Persons] SET Name = ?, Email = ?, Salary = ?, Age = ? where Id = ?'''
    params = (person.name, person.email, person.salary, person.age, id)
    cursor.execute(query, params)
    connection.commit()
    cursor.close()
    repository.database_connection.closeDbConnection(connection)

def delete_person(id):
    connection = repository.database_connection.createDbConnection()
    cursor = connection.cursor()
    query = '''DELETE FROM [dbo].[Persons] WHERE Id = ?'''
    params = (id)
    cursor.execute(query, params)
    connection.commit()
    cursor.close()
    repository.database_connection.closeDbConnection(connection)

def get_all_persons():
    connection = repository.database_connection.createDbConnection()
    persons: List[models.person.person] = list()
    cursor = connection.cursor()
    query = '''SELECT * FROM [dbo].[Persons]'''
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        persons.append(models.person.person(row[1], row[2], row[3], row[4]))

    cursor.close()
    return persons    