def write_demo():
    f = open("demo.txt",'w')
    f.write("hello python\n")
    f.write("สวัสดีไพธอน\n")
    f.close

def wirte_context_mgr():
    with open("demo1.txt",'w') as f:
        f.write("hello python\n")
        f.write("สวัสดีไพธอน\n")

def write_list():
    menu = ["mocha","latte","espresso"]
    with open('menu.txt','w', encoding='utf-8') as f:
        for m in menu:
            f.write(m + "\n")

# write_demo()
# wirte_context_mgr()
write_list()