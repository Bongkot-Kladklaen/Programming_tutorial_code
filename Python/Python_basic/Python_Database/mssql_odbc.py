import pyodbc
# import random

server = '127.0.0.1'
database = 'pythonDB'
username = 'sa'
password = 'Jaycop@12345'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver
                      +';SERVER='+server
                      +';PORT=1433;DATABASE='+database
                      +';UID='+username
                      +';PWD='+ password)
cursor = cnxn.cursor()

def create_table():
    sql = """
        create table Person(
            id int identity(1,1) primary key,
            gender char(1),
            weight real,
            height real
        )
    """
    with cursor.execute(sql):
        print("Successfully")

def insert_demo():
    sql = """
        insert into Person(gender, weight, height) values('M', 68, 175)
    """
    with cursor.execute(sql):
        print("Successfully")

def select_demo():
    sql = """
        select gender, weight, height from Person
    """
    with cursor.execute(sql) as con:
        for row in con:
            print(row)
            print(row[1] / (row[2] / 100) ** 2)
#
#
# def select_demo2(params):
#     sql = """
#         select gender, weight, height from Person
#         where gender = ? and weight >= ?
#     """
#     with pyodbc.connect(con_string) as con:
#         for row in con.execute(sql, params):
#             print(row[0], row[1], row[1] / (row[2] / 100) ** 2)
#
#
# def insert_demo2(params):
#     sql = """
#          insert into Person(gender, weight, height) values(?, ?, ?)
#      """
#     with pyodbc.connect(con_string) as con:
#         con.execute(sql, params)
#
#
# def update_demo(params):
#     sql = """
#          update Person
#             set weight = weight / 2.2
#             where gender = ?
#      """
#     with pyodbc.connect(con_string) as con:
#         con.execute(sql, params)
#
#
# def delete_demo(params):
#     sql = """
#         delete from Person where height < ? and gender = ?
#      """
#     with pyodbc.connect(con_string) as con:
#         con.execute(sql, params)
#
#
if __name__ == '__main__':
    # create_table()
    # insert_demo()
    select_demo()
#     # select_demo2(['F', 50])
#     # insert_demo2(['M', 70, 170])
#     # for _ in range(10):
#     #     g = random.choice('MF')
#     #     w = random.normalvariate(55, 6)
#     #     h = random.normalvariate(160, 7)
#     #     insert_demo2([g, w, h])
#     # update_demo('F')
#     h = float(input("height: "))
#     g = input("M or F: ")
#     delete_demo([h, g])
#     select_demo()
