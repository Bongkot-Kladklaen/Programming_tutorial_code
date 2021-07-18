import csv
def demo():
    with open("rio2016.csv") as f:
        data = f.read()
        print(data)

def read_csv():
    with open("rio2016.csv") as f:
        data = csv.reader(f)
        print(data)
        for row in data:
            print("{:25}: {:2} {:2} {:2} {:3}".format(row[0], row[1], row[2], row[3],int(row[1]) + int(row[2]), int(row[3])))

def read_csv_tab():
    with open("rio2016tab.txt") as f:
        data = csv.reader(f, delimiter="\t")
        print(data)
        for row in data:
            print("{:25}: {:2} {:2} {:2} {:3}".format(row[0], row[1], row[2], row[3],int(row[1]) + int(row[2]), int(row[3])))
def read_csv_header():
    with open("rio2016_header_column.csv") as f:
        data = csv.DictReader(f)
        print(data)
        print(data.fieldnames)
        for row in data:
            print(row)
            # print(row["country"], row['gold'])
        # for row in data:
            # print("{:25}: {:2} {:2} {:2} {:3}".format(row[0], row[1], row[2], row[3],int(row[1]) + int(row[2]), int(row[3])))

# read_csv_tab()
read_csv_header()
