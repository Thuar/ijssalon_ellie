prijzen = {
    "aardbei" : "3",
    "vanille" : "4",
    "chocolade" : "5"
}
prijzen.update({"aardbei" : 3 * 0.8})
aanbieding = prijzen ["aardbei"]
reclame_tekst = (f"Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts €{aanbieding}")
reclame_tekst2 = reclame_tekst[:62]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split()
for el in reclame_tekst4:
    if len(el)<5:
        el = el.lower()
        print(el)
    else:
        el = el.upper()
        print(el)
        