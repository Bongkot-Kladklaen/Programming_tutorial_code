def temperature_table():
    for celsius in range(101):
        f = (celsius * 9 / 5) + 32
        # print(celsius, "=", f)
        print("{}c = {:.2f}f".format(celsius, f))
# temperature_table()

def multi_table(from_n,to_n):
    for i in range(from_n, to_n + 1):
        for j in range(1, 13):
            print("{} * {} = {}".format(i,j,i*j))
        print("-" * 20)

multi_table(2,3)