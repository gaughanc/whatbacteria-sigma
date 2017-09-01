def create_lin_list():
    with open("bactree.txt") as rd:
        lins = rd.readlines()
    for i, lin in enumerate(lins):
        lin = lin.strip('",\n')
        lin = lin.split(";")
        lins[i] = lin
    return(lins)

if __name__ == "__main__":
    print(create_lin_list())
