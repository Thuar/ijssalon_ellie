a = 2
b = 4
c = 10
d = 12
c1 = 3
e1 = 5
f = 100
f1 = 20

def mijn_functie_1(a):
    return a * a

print("Waarde 2 geeft als resultaat", (mijn_functie_1(a)))
print("Waarde 4 geeft als resultaat", mijn_functie_1(b))
print("Waarde 10 geeft als resultaat", mijn_functie_1(c))
print("Waarde 12 geeft als resultaat", mijn_functie_1(d))

def mijn_functie_2(a, b):
    return [a + b, a - b, a * b, a / b]

print("Waarde 12 , 3 geeft als resultaat", (mijn_functie_2(d,c1)))
print("Waarde 12 , 2 geeft als resultaat", (mijn_functie_2(d,a)))
print("Waarde 10 , 5 geeft als resultaat", (mijn_functie_2(c,e1)))
print("Waarde 100 , 20 geeft als resultaat", (mijn_functie_2(f,f1)))


