import urllib.request

def read_from_url(link):
    with urllib.request.urlopen(link) as f:
        s = f.read()
    print(s)
    print(type(s))
    s1 = s.decode("utf8")
    print(s1)
    print(type(s1))
    print(s1)
    return s.decode("utf8")

read_from_url("https://dl.dropboxusercontent.com/u/23148470/planet.txt")