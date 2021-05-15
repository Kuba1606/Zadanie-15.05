print("KALKULATOR")

import math #import modułu math

#definicje poszczególnych funkcji kalkulatora
def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    return x / y

def potegowanie(x, y):
    return x ** y

def pierwiastkowanie(x):
    return math.sqrt(x)

def sinus(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tg(x):
    return math.tg(x)


wyjscie = False          #Powrót do programu
while wyjscie == False:

    print("=== M E N U ===\n"
    "1| Dodawanie\n"
    "2| Odejmowanie\n"
    "3| Mnożenie\n"
    "4| Dzielenie\n"
    "5| Potegowanie\n"
    "6| Pierwiatek z liczby\n"
    "7| Wartość sinus z kąta\n"
    "8| Wartość cosinus z kąta\n"
    "9| Wartość tangens z kąta\n"
    "0| Wyjscie\n")

    choice = input("Wybierz numer operacji z Menu: ")

    #Instrukcja warunkowa - wyjście z programu
    if choice == '0':
        pytanie = input("Wyjść z programu? (T/N): ")
        if pytanie == 'T':
            wyjscie = True
            print('Koniec programu!')
            exit()
        elif pytanie == 'N':
            wyjscie = False


    #Interakcja z użytkownikiem, wypisanie na ekranie działania oraz wyniku wybranej funkcji
    if choice == '1':
        x = float(input("Podaj pierwszą liczbę: "))
        y = float(input("Podaj drugą liczbę: "))
        print(x, "+", y, "=", dodawanie(x, y))

    elif choice == '2':
        x = float(input("Podaj pierwszą liczbę: "))
        y = float(input("Podaj drugą liczbę: "))
        print(x, "-", y, "=", odejmowanie(x, y))

    elif choice == '3':
        x = float(input("Podaj pierwszą liczbę: "))
        y = float(input("Podaj drugą liczbę: "))
        print(x, "*", y, "=", mnozenie(x, y))

    elif choice == '4':
        x = float(input("Podaj pierwszą liczbę: "))
        y = float(input("Podaj drugą liczbę: "))
        print(x, "/", y, "=", dzielenie(x, y))

    elif choice == '5':
        x = float(input("Podaj pierwszą liczbę: "))
        y = float(input("Podaj drugą liczbę: "))
        print(x, "**", y, "=", potegowanie(x, y))

    if choice == '6':
        x = float(input("Podaj liczbe do pierwiastkowania: "))
        print(x,"sqrt", "=", pierwiastkowanie(x))

    if choice == '7':
        x = float(input("Wartość sinus z kąta: "))
        print(x,"sin", "=", sinus(x))

    if choice == '8':
        x = float(input("Wartość cosinus z kąta: "))
        print(x,"cos", "=", cos(x))

    if choice == '9':
        x = float(input("Wartość tangens z kąta: "))
        print(x,"tg", "=", tg(x))
    else:
        print("Witam ponownie :)")
