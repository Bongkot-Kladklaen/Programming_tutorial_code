import mysql.connector
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Jaycop@12345",
        database="testdb"
    )
mycursor = mydb.cursor()

def create_table():
    sql_cmd = """
        create table person(
            id int primary key auto_increment,
            gender char (1),
            weight float ,
            height float
    )"""
    mycursor.execute(sql_cmd)

# def create_table2():
#     sql_cmd = """
#         create table employer(
#             id int primary key auto_increment,
#             name char (50)
#     )"""
#     mycursor.execute(sql_cmd)

def insert_data():
    sql_cmd = """
        insert into person(gender, weight, height) values ('F',45,167);
    """
    mycursor.execute(sql_cmd)
    mydb.commit()

def select_data():
    sql_cmd = """
        select * from person;
    """
    mycursor.execute(sql_cmd)
    for row in mycursor:
        print(row[2], row[3])

def select_data2():
    sql_cmd = """
        select * from person;
    """
    mycursor.execute(sql_cmd)
    result = mycursor.fetchall()
    for row in result:
        print(row[2],row[3])

if __name__ == '__main__':
    # create_table()
    # insert_data()
    # create_table2()
    select_data()
    select_data2()