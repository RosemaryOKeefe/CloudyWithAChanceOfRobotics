label = ["Protein", "34g","Calcium","7mg","32%"]

for i in label:
    for m in i:
        bool = m.isdigit
        if bool:
            if (i.find('mg') != -1):
                i = list(i)
                i.remove('m')
                i.remove('g')
                print(i)
                break
            elif (i.find('g') != -1):
                i = list(i)
                i.remove('g')
                print(i)
                break 
            elif (i.find('%')):
                break
