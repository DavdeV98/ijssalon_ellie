from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro."
    return uitvoer

def inkomsten_totaal(inkomsten):
    totaal = 0
    for a in inkomsten:
        totaal += a
    bedrag_btw = totaal * 0.09
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag_btw} euro btw betaald dient te worden"
    return uitvoer

def laag_en_hoog(mijn_lijst):
    uitvoer = []
    uitvoer.append(max(mijn_lijst))
    uitvoer.append(min(mijn_lijst))
    return uitvoer

def gemiddelde(mijn_lijst):
    avg = sum(mijn_lijst)/len(mijn_lijst)
    uitvoer = f"De gemiddelde inkomsten deze week zijn {avg} euro."
    return uitvoer

def meervoudig(invoer_lijst):
    uitvoer = laag_en_hoog(invoer_lijst)
    return uitvoer

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer