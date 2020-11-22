from num_dict import unidades, dezenas, centenas


def um_alg(num: str) -> str:
    return unidades.get(int(num))


def dois_alg(num: str) -> str:
    extenso = []

    if int(num[0]) == 1:
        extenso.append(dezenas.get(int(num[0:])))
    else:
        extenso.append(dezenas.get(int(num[0])))
        extenso.append(unidades.get(int(num[1])))

    extenso = [ext for ext in extenso if ext is not None and ext != "zero"]

    return " e ".join(extenso)


def tres_alg(num: str) -> str:
    extenso = []

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


def numero_extenso(num: str) -> str:
    num_palavra = ""

    if len(num) == 1:
        num_palavra = um_alg(num)
    elif len(num) == 2:
        num_palavra = dois_alg(num)
    else:
        num_palavra = tres_alg(num)
    
    return num_palavra
