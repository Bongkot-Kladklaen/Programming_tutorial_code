import _sqlite3,random
import pandas as pd
import matplotlib.pyplot as plt

def create_table(db):
    try:
        with _sqlite3.connect(db) as con:
            sql_cmd = '''
                drop table if exists person;
                create table person(
                    obs integer primary key autoincrement,
                    gender text,
                    weight real,
                    height real
                );
            '''
            con.executescript(sql_cmd)
    except Exception as e:
        print(f"Eroro -> {e}")

def create_data(db, rows = 10):
    data = [(random.choice("MF"), random.normalvariate(57, 4.5), random.normalvariate(160, 6)) for _ in range(rows)]
    print(data)
    try:
        with _sqlite3.connect(db) as con:
            sql_cmd = 'insert into person(gender, weight, height) values (?, ?, ?)'
            con.executemany(sql_cmd, data)
    except Exception as e:
        print(f"Error -> {e}")

def pd_read_sql(db):
    with _sqlite3.connect(db) as con:
        sql_cmd = '''
            select obs, gender, weight, height
            from person
            order by height
        '''
        df = pd.read_sql(sql_cmd, con, index_col='obs')
    print(df)
    df['bmi'] = df.weight / (df.height / 100) ** 2
    df['height'].plot.hist(alpha = .7)
    # df.plot.scatter(x = 'weight', y = 'height')
    # df.plot.scatter(x = 'bmi' , y = 'weight')
    # print(f"mean(bmi) = {df.bmi.mean():.2f}")
    plt.show()

if __name__ == '__main__':
    db = 'sample.sqlite'
    # create_table(db)
    # create_data(db,100)
    pd_read_sql(db)
