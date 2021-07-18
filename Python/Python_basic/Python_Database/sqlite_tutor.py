import _sqlite3

def demo_select():
    try:
        with _sqlite3.connect("db.sqlite") as con:
            con.row_factory = _sqlite3.Row
            sql_cmd = """
                select gender,height,weight,weight / ((height/100) * (height/100)) as bmi from person
                where gender == 'F'
            """
            for row in con.execute(sql_cmd):
                # print(row)
                # print(row[1], row[2])
                print(row["gender"], row["height"], row["bmi"])
    except Exception as e:
        print("Eroro -> {}".format(e))

if __name__ == '__main__':
    demo_select()