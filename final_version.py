# konštanty
    # znaky a písmená
cSamohlasky="aeiouyAEIOUY"
cSpoluhlasky="bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
cIntrepZnamienka = ".?!"
    # ASCII kód
cPrveMalePismeno = 97 # hodnota malého a v ASCII kóde
cRozdielHodnotPismen = 32 # rozdiel medzi hodnotou veľkého a malého pismena
cPismenAbecedy = 26 # počet pśsmen anglickej abecedy

def vypocitajSifra1(iVeta):
    lSifra = ""
    lPoslednaMedzera: int = 0
    for poz in range(len(iVeta)):
        pismeno = iVeta[poz]
        if pismeno == " " or pismeno in cIntrepZnamienka:
            lSifra += " " + iVeta[(poz-1):(lPoslednaMedzera):-1] if lPoslednaMedzera != 0 else iVeta[(poz-1)::-1]
            lPoslednaMedzera = poz
    lNoveSlovo = ""
    for pismeno in lSifra:
        if ord(pismeno) >= cPrveMalePismeno:
            lNoveSlovo += chr(ord(pismeno) - cRozdielHodnotPismen)
        else:
            lNoveSlovo += pismeno
    lSifra = lNoveSlovo
    return lSifra

def vypocitajSifra2(iVeta):
    lPosun: int = 1
    lSifra = ""
    for pismeno in iVeta:
        lPosun = lPosun%cPismenAbecedy
        lPoradiePismena = ord(pismeno)
        if pismeno == " " or pismeno in cIntrepZnamienka:
            lPosun = 1
            lSifra += pismeno
        else:
            if (lPoradiePismena + lPosun >= cPrveMalePismeno and lPoradiePismena + lPosun <= cPrveMalePismeno + (cPismenAbecedy-1)) \
                or (lPoradiePismena + lPosun >= cPrveMalePismeno - cRozdielHodnotPismen and lPoradiePismena + lPosun <= cPrveMalePismeno - cRozdielHodnotPismen + (cPismenAbecedy-1)):
            # zisťujeme či sa novo vzniknuté písmeno nachádza medzi veľkými alebo malými písmenami ASCII kódu
                lSifra += chr(lPoradiePismena + lPosun)
            else:
                lSifra += chr(lPoradiePismena + lPosun - cPismenAbecedy)
            lPosun += 1
    return lSifra

def vypocitajSifra3(iVeta):
    import random
    sos: int = -1 # sos -> start of sequence -> najde prve pismeno v slove
    eos: int = 0 # eos -> end of sequence -> najde prazdny string " " medzeru -> eos - 1 bude teda posledne pismeno v slove
    wordCount: int = 0
    result: str = ""
    for i in range(len(iVeta)):
        if iVeta[i] == " " or iVeta[i] in cIntrepZnamienka:
            eos = i
            wordCount += 1
            length = eos - sos - 1
            wordFirst = iVeta[sos+1:sos+2]
            wordLast = iVeta[eos-1:eos]
            if length > 2:
                wordShuffled = wordFirst
                middleChars = iVeta[sos+2:eos-1]
                remainingChars = middleChars # temp string, lebo nepozname listy ani tuples :(
                for i in range(len(remainingChars)):
                    charIndex = random.randint(0,len(remainingChars)-1)
                    wordShuffled += remainingChars[charIndex]
                    remainingChars = remainingChars[:charIndex] + remainingChars[charIndex+1:]
                wordShuffled += wordLast
            else:
                wordShuffled = iVeta[sos+1:eos]
            if i <= len(iVeta) - 1:
                if iVeta[i] in cIntrepZnamienka:
                    result += wordShuffled + iVeta[i]
                else:
                    result += wordShuffled + " "
            sos = eos
    return result

def komprimuj(iVeta):
    lVelke = True
    lSifra = ""
    for pismeno in iVeta:
        if pismeno == " ":
            lVelke = True if not lVelke else False
        else:
            if pismeno in cIntrepZnamienka:
                lSifra += pismeno
            elif ord(pismeno) >= cPrveMalePismeno and lVelke:
                lSifra += chr(ord(pismeno) - cRozdielHodnotPismen)
            elif ord(pismeno) < cPrveMalePismeno and not lVelke:
                lSifra += chr(ord(pismeno) + cRozdielHodnotPismen)
            else:
                lSifra += pismeno
    return lSifra

def zamenaRetazca(iVeta, iRetazec):
    lVeta = ""
    lPoslednaNahrada: int = 0
    if iRetazec != "" and iRetazec in iVeta:
        for i in range(len(iVeta)):
            if i < lPoslednaNahrada:
                continue
            if iRetazec == iVeta[i:(i+len(iRetazec))]:
                lVeta += "_"
                lPoslednaNahrada = i+len(iRetazec)
            else:
                lVeta += iVeta[i]
    else:
        lVeta = iVeta
    return lVeta

def vypocitajSifra4(iVeta: str, iNtica: int):
    lPoslednySek: int = 0
    lSifra = ""
    lNoveSlovo = ""
    for i in range(len(iVeta)):
        if i == len(iVeta) - 1:
            lSifra += iVeta[-2:lPoslednySek:-1]
        elif (i+1) % iNtica == 0 and lPoslednySek == 0:
            lSifra += iVeta[i::-1]
            lPoslednySek = i
        elif (i+1) % iNtica == 0:
            lSifra += iVeta[i:lPoslednySek:-1]
            lPoslednySek = i
    for pismeno in lSifra: # napíšme všetky písmená veľkým ako je v príklade zadania..
        if ord(pismeno) >= cPrveMalePismeno:
            lNoveSlovo += chr(ord(pismeno)-cRozdielHodnotPismen)
        else:
            lNoveSlovo += pismeno
    lSifra = lNoveSlovo
    lSifra += iVeta[-1]
    return lSifra


def sifry(iVeta):
    sifra1 = vypocitajSifra1(iVeta=iVeta)
    sifra2 = vypocitajSifra2(iVeta=iVeta)
    sifra3 = vypocitajSifra3(iVeta=iVeta)
    komprimVeta = komprimuj(iVeta=iVeta)
    print("Šifra 1: " + sifra1)
    print("Šifra 2: " + sifra2)
    print("Šifra 3: " + sifra3)
    print("Kompresia: " + komprimVeta)

    retazec = input("Zadaj reťazec: ")
    cenzurovanyText = zamenaRetazca(iVeta=iVeta, iRetazec=retazec)
    print("Cenzúrovaný text: " + cenzurovanyText)

    ntica = int(input("Zadaj n: "))
    sifra4 = vypocitajSifra4(iVeta=iVeta, iNtica=ntica)
    print("Šifra 4: " + sifra4)

def slova1(iVeta):
    pocet_slov=1
    slova_na_samohlasku=0
    slova_na_spoluhlasku=0

    if iVeta[0] in cSamohlasky:
        slova_na_samohlasku=slova_na_samohlasku+1
    elif iVeta[0] in cSpoluhlasky:
        slova_na_spoluhlasku=slova_na_spoluhlasku+1

    for a in range(len(iVeta)):
        if iVeta[a]==" ":
            pocet_slov=pocet_slov+1
            if iVeta[a+1] in cSamohlasky:
                slova_na_samohlasku=slova_na_samohlasku+1
            elif iVeta[a+1] in cSpoluhlasky:
                slova_na_spoluhlasku=slova_na_spoluhlasku+1

    print("Počet slov vo vete: "+str(pocet_slov))
    print("Počet slov začínajúcich na samohlásku: "+str(slova_na_samohlasku))
    print("Počet slov začínajúcich na spoluhlásku: "+str(slova_na_spoluhlasku))
    print("Dĺžky slov vo vete:")

def slova2(iVeta):
    posledna_medzera=-1
    sucasna_medzera=0
    dlzka_max_slova=0
    poradie_max_slova=0
    count_slovo = 0
    najdlhsie_slova = ""

    for a in range(len(iVeta)):
        # <--2024-10-23 - SJ - nova konstanta
        # if iVeta[a]==" " or iVeta[a] in ".?!":
        if iVeta[a]==" " or iVeta[a] in cIntrepZnamienka:
        # SJ-->
            sucasna_medzera=a
            count_slovo +=1
            print(iVeta[(posledna_medzera+1):sucasna_medzera]+" - "+str(sucasna_medzera-(posledna_medzera+1)))
            if (sucasna_medzera-(posledna_medzera+1))>dlzka_max_slova:
                najdlhsie_slova = ""
                dlzka_max_slova=(sucasna_medzera-(posledna_medzera+1))
                poradie_max_slova = count_slovo
            if len(iVeta[(posledna_medzera+1):sucasna_medzera]) == dlzka_max_slova:
                najdlhsie_slova += iVeta[(posledna_medzera+1):sucasna_medzera]
            posledna_medzera=sucasna_medzera 

    print("Dĺžka najdlhšieho slova: "+str(dlzka_max_slova))
    print("Poradové číslo najdlhšieho slova: "+ str(poradie_max_slova))
    print("Slová s najväčšou dĺžkou: ")
    for i in range(int(len(najdlhsie_slova)/dlzka_max_slova)):
        print(najdlhsie_slova[i*dlzka_max_slova:(i*dlzka_max_slova+dlzka_max_slova)])

def poctySlov(iVeta):
    slova1(iVeta=iVeta)
    slova2(iVeta=iVeta)

def mainloop():
    veta = input("Zadaj vetu: ")
    ###### !!! cvicna veta !!! #######
    # veta = "Katka a Zdenka su sestry."
    poctySlov(iVeta=veta)
    sifry(iVeta=veta)


mainloop()