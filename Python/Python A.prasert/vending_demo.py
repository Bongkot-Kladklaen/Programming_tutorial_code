import csv
import random
import datetime
def vending_transcation(machine_id, product_id):
    with open("sales.csv","a",newline="", encoding="utf8") as f:
        fw = csv.writer(f)
        temp = random.randint(10,40)
        timestamp = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")
        fw.writerow([machine_id, product_id,temp,timestamp])

def vending_menu():
    while True:
        p = input("product code {[q]uit: ")
        if p != "q":
            machine_id = random.choice(["HUA","SAM","SIL","SUK"])
            vending_transcation(machine_id, p)
        else:
            break

vending_menu()