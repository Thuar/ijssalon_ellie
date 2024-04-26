from algemene_functies import mijn_functie_2 


def aanbieding_1(smaak, prijs, korting):
        return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak} van {prijs} euro voor {prijs - prijs * korting} euro."
     
print(aanbieding_1("aardbei", 4, 0.1))


def inkomsten_totaal(inkomsten, btw):    
            return  f"Het totaal van alle inkomsten van deze week is {sum(inkomsten)} euro, waarover {sum(inkomsten)*btw} euro btw betaald dient te worden."

btw = 0.09
inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(inkomsten_totaal(inkomsten, btw))


def laag_en_hoog(mijn_lijst):
        return min(mijn_lijst), max(mijn_lijst)

print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))


def gemiddelde(mijn_lijst):
        return f"De gemiddelde inkomsten deze week zijn {sum(mijn_lijst) / len(mijn_lijst)} euro."

print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))


def meervoudig(invoer_lijst):
        return laag_en_hoog(invoer_lijst)

print(meervoudig([10, 5, 3, 2, 1, 2, 9]))


def combinatie(invoer_lijst_2):
        korte_lijst = laag_en_hoog(invoer_lijst_2) 
        uitvoer = mijn_functie_2(korte_lijst[0],korte_lijst[1])
        return uitvoer

print(combinatie([220, 430, 125, 160, 205, 90, 345]))