def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    cislo = int(cislo)
    
    jednotky = [
        "nula", "jedna", "dva", : "tři", "čtyři",
        "pět", "šest",  "sedm",  "osm",  "devět",
        "deset",  "jedenáct",  "dvanáct", "třináct",
        "čtrnáct",  "patnáct",  "šestnáct",  "sedmnáct",
        "osmnáct",  "devatenáct" ]
    
    desitky ={
        20: "dvacet",
        30: "třicet",
        40: "čtyřicet",
        50: "padesát",
        60: "šedesát",
        70: "sedmdesát",
        80: "osmdesát",
        90: "devadesát",
        100: "sto"}
    
    if cislo < 20:
        return jednotky[cislo]
    
    elif cislo in desitky:
        return desitky[cislo]
    
    elif 20 < cislo < 100:
        des = (cislo // 10) * 10  
        jed = cislo % 10        
        return desitky[des] + " " + jednotky[jed]
    
    else:
        return "None"
    
   
    if cislo < 0 or cislo > 100:
            return "None"
    if cislo in cisla:
        return cislo[cisla] 
    else:
       return "None"  
   
    

if __name__ == "__main__":
   while True:
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
