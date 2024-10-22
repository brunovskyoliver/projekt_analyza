veta=input("Zadaj vetu: ")
pocet_slov=1
samohlasky="aeiouyAEIOUY"
spoluhlasky="bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
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

for a in range(len(veta)):
    if veta[a]==" " or veta[a] in ".?!":
        sucasna_medzera=a
        print(veta[(posledna_medzera+1):sucasna_medzera]+" - "+str(sucasna_medzera-(posledna_medzera+1)))
        if (sucasna_medzera-(posledna_medzera+1))>dlzka_max_slova:
            dlzka_max_slova=(sucasna_medzera-(posledna_medzera+1))
        posledna_medzera=sucasna_medzera

print("Dĺžka najdlhšieho slova: "+str(dlzka_max_slova))
        
        
