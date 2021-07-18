for row in range(8):
    for col in range(8):
        if (col+row) % 2 == 0:
            print(f"x",end="")
        else:
            print(f"o",end="")

    print("")