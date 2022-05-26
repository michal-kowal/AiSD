# n-ilosc przedmiotow; r-rozmiar przedmiotu; w-waga przedmiotu; b-rozmiar plecaka
def main():
    print("[1] Wprowadz dane\n[2] Wczytaj z pliku\n[3] Generuj dane")
    dane = input()
    error = False
    elementy = []   # taka macierz zawierajaca kolejno: indeks, waga, wartosc
    if dane == '1':
        n = int(input("Podaj ilosc elementow: "))
        if n >= 0:
            for i in range(n):
                r = int(input("\nPodaj rozmiar elementu " + str(i + 1) + ': '))
                w = int(input("Podaj wartosc elementu " + str(i + 1) + ': '))
                if r < 0 or w < 0:
                    print("Niepoprawne dane")
                    error = True
                    return 0
                else:
                    elementy.append([i + 1, r, w])
            b = int(input("Podaj rozmiar plecaka: "))
        else:
            error = True
            print("Zbyt mala liczba elementow")
            return 0
    elif dane == '2':
        file = open("file.txt")
        n, b = [int(i) for i in file.readline().split()]
        if n < 0 or b < 0:
            print("Bledne dane")
            error = True
            return 0
        else:
            for i in range(n):
                r, w = [int(j) for j in file.readline().split()]
                if r < 0 or w < 0:
                    print("Bledne dane")
                    error = True
                    return 0
                else:
                    elementy.append([i + 1, r, w])
    elif dane == '3':
        print("dane sie generujo")
    else:
        print("Zla opcja")
    if not error:
        dalej = True
        while dalej:
            print("\n[1] AD - algorytm programowania dynamicznego\n[2] AZ - algorytm zachlanny\n[3] AB - algorytm silowy\n[4] Wyjscie")
            algorytm = int(input("Wybierz opcje: "))
            if algorytm == '1':
                wynik = "Tu bedzie AD"
            elif algorytm == '2':
                wynik = "Tu bedzie AZ"
            elif algorytm == '3':
                wynik = "Tu bedzie AB"
            elif algorytm == '4':
                dalej = False
            else:
                print("Podano zle dane")


try:
    main()
except Exception:
    print("Wprowadzono zle dane")