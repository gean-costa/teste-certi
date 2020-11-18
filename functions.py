from num_dict import unidades, dezenas, centenas


def numero_extenso(num):
    extenso = []

    if len(num) == 1:
        extenso.append(unidades.get(int(num)))

    elif len(num) == 2:
        if int(num[0]) == 1:
            extenso.append(dezenas.get(int(num[0:])))
        else:
            extenso.append(dezenas.get(int(num[0])))
            extenso.append(unidades.get(int(num[1])))

    if len(num) == 3:
        if int(num[1]) == 0:
            extenso.append(centenas.get(int(num[0])))
            extenso.append(unidades.get(int(num[-1])))
        elif int(num[1]) == 1:
            extenso.append(centenas.get(int(num[0])))
            extenso.append(dezenas.get(int(num[1:])))
        else:
            extenso.append(centenas.get(int(num[0])))
            extenso.append(dezenas.get(int(num[1])))
            extenso.append(unidades.get(int(num[2])))
    
    extenso = [ext for ext in extenso if ext is not None and ext != "zero"]

    if len(extenso) == 1 and extenso[0] == "cento":
        extenso[0] = "cem"

    return " e ".join(extenso)
