
month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
def get_mount_name(m:int):
    return month[m - 1]

people = [
    ['Supasate','Choochaisri',30],
    ['Somchai','Python',22],
    ['Thongchai','Java',42],
    ['Thana','C',15],
    ['Nat','Ruby',20]
]

if __name__ == "__main__":
    # result = get_mount_name(2);
    # print(result)
    # print(month)
    print(people[3][1])
    print(people[2][2] - people[1][2])