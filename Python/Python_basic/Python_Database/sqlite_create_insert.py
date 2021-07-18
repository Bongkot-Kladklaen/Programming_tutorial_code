import sqlite3

def create_table():
    try:
        with sqlite3.connect("sample.sqlite") as con:
            sql_cmd = """
                create table medal(
                    country text primary key,
                    gold integer ,
                    silver integer ,
                    bronze integer 
                );
            """
            con.execute(sql_cmd)
    except Exception as e:
        print("Error -> {}".format(e))

def insert_demo():
    try:
        with sqlite3.connect("sample.sqlite") as con:
            sql_cmd = """
                insert into medal values ('usa',46,37,38)
            """
            con.execute(sql_cmd)
    except Exception as e:
        print("Error -> {}".format(e))
def insert_demo2():
    try:
        with sqlite3.connect("sample.sqlite") as con:
            sql_cmd = """
                begin;
                    insert into medal values ('gbr',27,23,17);
                    insert into medal values ('chn',26,18,26);
                    insert into medal values ('rus',19,17,19);
                commit;
            """
            con.executescript(sql_cmd)
    except Exception as e:
        print("Error -> {}".format(e))

def select_demo():
    try:
        with sqlite3.connect("sample.sqlite") as con:
            con.row_factory = sqlite3.Row
            sql_cmd = """
                select * from medal
            """
            query = con.execute(sql_cmd)
            for row in query:
                print(row["country"], row["gold"], row["silver"], row["bronze"])

    except Exception as e:
        print("Error -> {}".format(e))

if __name__ == '__main__':
    # create_table()
    # insert_demo()
    # select_demo()
    # insert_demo2()
    select_demo()