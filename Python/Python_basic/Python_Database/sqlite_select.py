import _sqlite3

def demo_select1():
    try:
        with _sqlite3.connect("db.sqlite") as con:
            con.row_factory = _sqlite3.Row
            sql_cmd = """
                select * from person
                where gender = 'M'
            """
            cursor = con.execute(sql_cmd)
            for row in cursor:
                print("{}{}{}{}".format(row["obs"],row["gender"],row["height"],row["weight"]))
    except Exception as e:
        print("Error -> {}".format(e))

def demo_select2(sex:str, h):
    try:
        with _sqlite3.connect("db.sqlite") as con:
            con.row_factory = _sqlite3.Row
            sql_cmd = """
                select * from person
                where gender = ? and height > ?
            """
            cursor = con.execute(sql_cmd, [sex,h])
            for row in cursor:
                print("{} {} {} {}".format(row["obs"],row["gender"],row["height"],row["weight"]))
    except Exception as e:
        print("Error -> {}".format(e))

if __name__ == '__main__':
    # demo_select1()
    demo_select2("M",180)