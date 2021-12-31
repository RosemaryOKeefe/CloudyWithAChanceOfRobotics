labelString = ["Protein", "34g", "Sodium", "7mg", "32%"]

for i in labelString:
    for m in i:
        bool = m.isdigit()
        if bool:
            if (i.find('g') != -1) or (i.find('mg')!= -1):
                print(i)
                break
            elif (i.find('%') == -1):
                break