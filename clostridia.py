from create_lin_list import create_lin_list

clo_genera = []
lins = create_lin_list()
for lin in lins:
    if len(lin) == 6:
        if lin[2] == 'Clostridia':
            if not lin[5] in clo_genera:
                clo_genera.append(lin[5])
print(clo_genera)
