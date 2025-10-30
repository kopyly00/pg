def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    

    if cilova_pozice[0] < 1 or cilova_pozice[0] > 8 or cilova_pozice[1] < 1 or cilova_pozice[1] > 8:
        return False

    if cilova_pozice in obsazene_pozice:
        return False

    typ = figurka["typ"]
    pozice = figurka["pozice"]

    r = cilova_pozice[0] - pozice[0]
    s = cilova_pozice[1] - pozice[1]


    # pěšec
    if typ == "pěšec":
        if r!= 0 and s != 0:
         return False
        if s != 0:
         return False
        if r == 1:
         return True
        if r == 2:
           if pozice[0] == 1:
             mezi = (pozice[0] + 1, pozice[1])
             if mezi not in obsazene_pozice:
                 return True
             else:
                return False
           else:
             return False    
        if r < 0:
           return False
        return False

    # jezdec
    if typ == "jezdec":
        if (abs(r) == 2 and abs(s) == 1) or (abs(r) == 1 and abs(s) == 2):
           return True #bez kontroly obsazené pozice, protoze preskakuje
        else:
           return False
    
    # věž
    if typ == "věž":
        if r != 0 and s != 0: #ze nejde diagonálně
            return False
        if r != 0:
            if r > 0:
                krok = 1
            else:
                krok = -1
            x = pozice[0] + krok
            while x != cilova_pozice[0]:
                if (x, pozice[1]) in obsazene_pozice:
                    return False
                x = x + krok
        if s != 0:
            if s > 0:
                krok = 1
            else:
                krok = -1
            y = pozice[1] + krok
            while y != cilova_pozice[1]:
                if (pozice[0], y) in obsazene_pozice:
                    return False
                y = y + kroky
        return True

    # střelec
    if typ == "střelec":
        if abs(r) != abs(s):
            return False
        if r > 0:
            krokx = 1
        else:
            krokx = -1
        if s > 0:
            kroky = 1
        else:
            kroky = -1
        x = pozice[0] + krokx
        y = pozice[1] + kroky
        while x != cilova_pozice[0] and y != cilova_pozice[1]:
            if (x, y) in obsazene_pozice:
                return False
            x = x + krokx
            y = y + kroky
        return True

    # dáma
    if typ == "dáma":
        if r == 0 or s == 0 or abs(r) == abs(s):
            if r == 0:
                krokx = 0
            elif r > 0:
                krokx = 1
            else: 
                krokx = -1
            if s == 0:
                kroky = 0
            elif s > 0:
                kroky = 1
            else:
                kroky = -1
            x = pozice[0] + krokx
            y = pozice[1] + kroky
            while (x, y) != cilova_pozice:
                if (x, y) in obsazene_pozice:
                    return False
                x = x + krokx
                y = y + kroky
            return True
        else:
            return False

    # král
    if typ == "král":
        if (abs(r) == 1 or abs(r) == 0) and (abs(s) == 1 or abs(s) == 0) and not (r == 0 and s == 0):
            if cilova_pozice not in obsazene_pozice:
                return True
        else:
            return False

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))
    print(je_tah_mozny(kral, (4, 6), obsazene_pozice))
    print(je_tah_mozny(kral, (6, 6), obsazene_pozice))