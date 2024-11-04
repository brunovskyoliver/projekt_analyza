veta=input("Zadaj vetu: ")

###### !!! cvicna veta !!! #######
veta = "Katka a Zdenka su sestry."

# konštanty
    # znaky a písmená
samohlasky="aeiouyAEIOUY"
spoluhlasky="bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
intrepZnamienka = ".?!"
    # ASCII kód
prveMalePismeno = 97 # hodnota malého a v ASCII kóde
rozdielHodnotPismen = 32 # rozdiel medzi hodnotou veľkého a malého pismena
pismenAbecedy = 26 # počet pśsmen anglickej abecedy

def vypocitajSifra1(iVeta):
    lSifra = ""
    lPoslednaMedzera: int = 0
    for poz in range(len(iVeta)):
        pismeno = iVeta[poz]
        if pismeno == " " or pismeno in intrepZnamienka:
            lSifra += " " + iVeta[(poz-1):(lPoslednaMedzera):-1] if lPoslednaMedzera != 0 else iVeta[(poz-1)::-1]
            lPoslednaMedzera = poz
    lNoveSlovo = ""
    for pismeno in lSifra:
        if ord(pismeno) >= prveMalePismeno:
            lNoveSlovo += chr(ord(pismeno) - rozdielHodnotPismen)
        else:
            lNoveSlovo += pismeno
    lSifra = lNoveSlovo
    return lSifra

def vypocitajSifra2(iVeta):
    lPosun: int = 1
    lSifra = ""
    for pismeno in iVeta:
        lPosun = lPosun%pismenAbecedy
        lPoradiePismena = ord(pismeno)
        if pismeno == " " or pismeno in intrepZnamienka:
            lPosun = 1
            lSifra += pismeno
        else:
            if (lPoradiePismena + lPosun >= prveMalePismeno and lPoradiePismena + lPosun <= prveMalePismeno + (pismenAbecedy-1)) \
                or (lPoradiePismena + lPosun >= prveMalePismeno - rozdielHodnotPismen and lPoradiePismena + lPosun <= prveMalePismeno - rozdielHodnotPismen + (pismenAbecedy-1)):
            # zisťujeme či sa novo vzniknuté písmeno nachádza medzi veľkými alebo malými písmenami ASCII kódu
                lSifra += chr(lPoradiePismena + lPosun)
            else:
                lSifra += chr(lPoradiePismena + lPosun - pismenAbecedy)
            lPosun += 1
    return lSifra

def vypocitajSifra3(iVeta):
    import random
    sos: int = -1 # sos -> start of sequence -> najde prve pismeno v slove
    eos: int = 0 # eos -> end of sequence -> najde prazdny string " " medzeru -> eos - 1 bude teda posledne pismeno v slove
    wordCount: int = 0
    result: str = ""
    for i in range(len(iVeta)):
        if iVeta[i] == " " or iVeta[i] in intrepZnamienka:
            eos = i
            wordCount += 1
            length = eos - sos - 1
            wordFirst = iVeta[sos+1:sos+2]
            wordLast = iVeta[eos-1:eos]
            if length > 2:
                wordShuffled = wordFirst
                middleChars = iVeta[sos+2:eos-1]
                remainingChars = middleChars # temp string, lebo nepozname listy ani tuples :(
                # while len(remainingChars)>0:
                #     charIndex = random.randint(0,len(remainingChars)-1)
                #     wordShuffled += remainingChars[charIndex]
                #     remainingChars = remainingChars[:charIndex] + remainingChars[charIndex+1:]
                for i in range(len(remainingChars)):
                    charIndex = random.randint(0,len(remainingChars)-1)
                    wordShuffled += remainingChars[charIndex]
                    remainingChars = remainingChars[:charIndex] + remainingChars[charIndex+1:]
                wordShuffled += wordLast
            else:
                wordShuffled = iVeta[sos+1:eos]
            if i <= len(iVeta) - 1:
                if iVeta[i] in intrepZnamienka:
                    result += wordShuffled + iVeta[i]
                else:
                    result += wordShuffled + " "
            sos = eos
    return result

def komprimuj(iVeta):
    return ""

def sifry(iVeta):
    sifra1 = vypocitajSifra1(iVeta=iVeta)
    sifra2 = vypocitajSifra2(iVeta=iVeta)
    sifra3 = vypocitajSifra3(iVeta=iVeta)
    komprimVeta = komprimuj(iVeta=iVeta)
    print("Šifra 1: " + sifra1)
    print("Šifra 2: " + sifra2)
    print("Šifra 3: " + sifra3)
    print("Kompresia: " + komprimVeta)

pocet_slov=1
slova_na_samohlasku=0
slova_na_spoluhlasku=0

if veta[0] in samohlasky:
    slova_na_samohlasku=slova_na_samohlasku+1
elif veta[0] in spoluhlasky:
    slova_na_spoluhlasku=slova_na_spoluhlasku+1

for a in range(len(veta)):
    if veta[a]==" ":
        pocet_slov=pocet_slov+1
        if veta[a+1] in samohlasky:
            slova_na_samohlasku=slova_na_samohlasku+1
        elif veta[a+1] in spoluhlasky:
            slova_na_spoluhlasku=slova_na_spoluhlasku+1

print("Počet slov vo vete: "+str(pocet_slov))
print("Počet slov začínajúcich na samohlásku: "+str(slova_na_samohlasku))
print("Počet slov začínajúcich na spoluhlásku: "+str(slova_na_spoluhlasku))
print("Dĺžky slov vo vete:")

posledna_medzera=-1
sucasna_medzera=0
dlzka_max_slova=0
poradie_max_slova=0
count_slovo = 0
najdlhsie_slova = ""

for a in range(len(veta)):
    # <--2024-10-23 - SJ - nova konstanta
    # if veta[a]==" " or veta[a] in ".?!":
    if veta[a]==" " or veta[a] in intrepZnamienka:
    # SJ-->
        sucasna_medzera=a
        count_slovo +=1
        print(veta[(posledna_medzera+1):sucasna_medzera]+" - "+str(sucasna_medzera-(posledna_medzera+1)))
        if (sucasna_medzera-(posledna_medzera+1))>dlzka_max_slova:
            najdlhsie_slova = ""
            dlzka_max_slova=(sucasna_medzera-(posledna_medzera+1))
            poradie_max_slova = count_slovo
        if len(veta[(posledna_medzera+1):sucasna_medzera]) == dlzka_max_slova:
            najdlhsie_slova += veta[(posledna_medzera+1):sucasna_medzera]
        posledna_medzera=sucasna_medzera 

print("Dĺžka najdlhšieho slova: "+str(dlzka_max_slova))
print("Poradové číslo najdlhšieho slova: "+ str(poradie_max_slova))
print("Slová s najväčšou dĺžkou: ")
for i in range(int(len(najdlhsie_slova)/dlzka_max_slova)):
    print(najdlhsie_slova[i*dlzka_max_slova:(i*dlzka_max_slova+dlzka_max_slova)])


sifry(iVeta=veta)
