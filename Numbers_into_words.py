# milliardqa shekemgi kirgizilgen sanlardin jaziliwin shigarip beretin code 


san = input("Bir san kirgizin: ")


while not(len(san) < 10 and len(san) > 0):
    print("1 milliyarddan kishi bolgan sandi kirgizin")
    san = input("san :")


birlikler = ["bir", "eki", "ush", "tort", "bes", "alti", "jeti", "segiz", "togiz"]
onliqlar = ["on", "jigirma", "otiz", "qiriq", "eliw", "alpis", "jetpis", "seksen", "toqsan"]


def juzlikler(job):
    if len(job)==3:
        j = int(job[-3])
    else:
        j = 0
    if len(job)>=2:
        o = int(job[-2])
    else:
        o = 0
    if len(job)>=1:
        b = int(job[-1])
    else:
        b = None

    string = ""
    if j != 0:
        string += (birlikler[j-1] + " juz ")
    if o != 0:
        string += onliqlar[o-1]
    if b != 0:
        string += (' ' + birlikler[b-1])
    return string


def minliqlar(jobjob):
    juz_ret = juzlikler(jobjob[:len(jobjob)-3])
    if juz_ret != "":
        juz_ret += " min "
    juz_ret += juzlikler(jobjob[-3:])
    return juz_ret


def millionliqlar(jobjobjob):
    juz_ret = juzlikler(jobjobjob[:len(jobjobjob)-6])
    if juz_ret != "":
        juz_ret += " million "
    juz_ret += minliqlar(jobjobjob[-6:])
    return juz_ret


length = len(san)
if san == "0":
    print("nol")
elif length < 4:
    print(juzlikler(san))
elif length <7:
    print(minliqlar(san))
else:
    print(millionliqlar(san))


