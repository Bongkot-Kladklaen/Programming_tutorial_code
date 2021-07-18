import mysql.connector
import pandas as pd
#
# def execute_query(sql_cmd, con_string, params=None):
#     try:
#         with mysql.connector.connect(con_string) as con:
#             if params:
#                 return con.execute(sql_cmd, params)
#             else:
#                 return con.execute(sql_cmd)
#     except Exception as e:
#         print(f'error -> {e}')


if __name__ == '__main__':
    # f-string (string interpolation Python 3.6)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Jaycop@12345"
    )
    print(mydb)
    # cursor = execute_query('select * from city where population > 1000000 limit 10', con_string)
    # cursor = execute_query(
    #     'SELECT * FROM city WHERE population > ?  AND population < ? ORDER BY population DESC LIMIT 10',
    #     con_string, [1000000, 5000000])
    # for row in cursor:
    #     print(f'city = {row[1]}, population = {row[4]}')

    sql_cmd = 'SELECT * FROM city WHERE population > ?  AND population < ? ORDER BY population DESC LIMIT 10'
    df = pd.read_sql(sql_cmd, mysql.connector.connect(mydb), params=[1000000, 5000000])
    print(df)
    print(df[['Name', 'Population']])
    print(df['Population'].sum())


