# Chuong trinh tim UCLN

uocA = []
uocB = []
uoc_chung = []

# tim uoc so tu nhien
def UCLN(a, b):
    global uocA
    global uocB
    global uoc_chung

    # tim uoc a
    for i in range(1, a + 1, 1):
        if a % i == 0:
            uocA.append(i)
    
    # tim uoc b
    for j in range(1, b + 1, 1):
        if b % j == 0:
            uocB.append(j)
    
    # tim uoc chung
    for h in range(0, len(uocA), 1):
        uoc = uocA[h]
        for k in range(0, len(uocB), 1):
            if uocB[k] == uoc:
                uoc_chung.append(uoc)
    
    ucln = max(uoc_chung)
    print("[{}]".format(ucln))

UCLN(10, 24)
