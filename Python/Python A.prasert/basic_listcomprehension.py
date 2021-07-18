import random
def multidim_list():
    medals = [
        ['th',3,5,2],
        ['kr',10,12,16],
        ['jp',20,30,40]
    ]
    a = [sum(m[1:]) for m in medals]
    print(a)
    b = [(m[0],sum(m[1:])) for m in medals]
    print(b)
    c = [(m[0], m[1], m[2], m[3], sum(m[1:])) for m in medals]
    print(c)

def freq():
    flower = ['ivy','iris','rose','lily','canation','jasmine']
    s = [random.choice(flower) for i in range(10)]
    print(s)
    print(set(s))
    f = [(i,s.count(i)) for i in set(s)]
    print(f)

# multidim_list()
freq()