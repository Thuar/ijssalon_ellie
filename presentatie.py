def presenteer(dict_inkomsten, totaal):
    dict_inkomsten = {'Aardbeien-ijs-totaal' : 1000, 'Vanille-ijs-totaal' : 2000, 'Chocolade-ijs-totaal' : 1500, 'Waterijsjes-totaal' : 750}
    
    totaal = sum(value for key , value in dict_inkomsten.items() if key in dict_inkomsten)
    
    uitvoer = totaal
    
    for k,v in dict_inkomsten.items():
        print(k, " : ", v, "euro") 
    print("="*30)
    print(f"totaal : ", uitvoer, "euro")
    