def f(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(kwargs["age"])

def full_name(**parts):
    d = []
    for k in ("first_name", "middle_name", "last_name"):
        if k in parts:
            # print(parts[k])
            d.append(parts[k])
    return " ".join(d)

f(name = "peter", age=21, hero="spiderman")
s = full_name(first_name="peter", last_name="parker")
print(s)
print("-" * 10)
t = full_name(first_name="george", middle_name="p",last_name="wood")
print(t)
print("-" * 10)
u = full_name(first_name="taylor")
print(u)