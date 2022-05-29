import random
import time
from numpy import maximum

# n-ilosc przedmiotow; r-rozmiar przedmiotu; w-waga przedmiotu; b-rozmiar plecaka
def dynamiczne(elementy, plecak):
    matrix = [[0 for i in range(plecak + 1)] for j in range(len(elementy) + 1)]
    for i in range(1, len(elementy) + 1):
        for j in range(1, plecak + 1):
            if elementy[i - 1][1] > j:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1][j - elementy[i - 1][1]] + elementy[i - 1][2])
    # [print(*matrix[i]) for i in range(len(matrix))]
    wybrane = []
    rozmiar = 0
    f_celu = 0
    for i in range(len(elementy), 0, -1):
        if matrix[i][plecak] > matrix[i -1][plecak]:
            wybrane.append(i)
            f_celu += elementy[i - 1][2]
            rozmiar += elementy[i - 1][1]
            plecak -= elementy[i - 1][1]
    return wybrane, rozmiar, f_celu

def merge_sort(array):
    if len(array) > 1:
        srodek = len(array) // 2
        lewa = array[:srodek]
        prawa = array[srodek:]
        merge_sort(lewa)
        merge_sort(prawa)
        i = 0
        j = 0
        k = 0
        while i < len(lewa) and j < len(prawa):
            if lewa[i][-1] >= prawa[j][-1]:
                array[k] = lewa[i]
                i += 1
            else:
                array[k] = prawa[j]
                j += 1
            k += 1
        while i < len(lewa):
            array[k] = lewa[i]
            i += 1
            k += 1
        while j < len(prawa):
            array[k] = prawa[j]
            j += 1
            k += 1
    return array

def zachlany(elementy, plecok):
    # indeks, waga, wartość, wartość przez wagę
    wartosc_przez_wage = [[x[0], x[1], x[2], x[2]/x[1]] for x in elementy]
    wartosc_przez_wage = merge_sort(wartosc_przez_wage)
    #print(wartosc_przez_wage)
    n = len(elementy)
    b = 0
    wartosc = 0
    w_plecaku = []
    for i in range(0, n):
        if b + wartosc_przez_wage[i][1] <= plecok:
            wartosc += wartosc_przez_wage[i][2]
            b += wartosc_przez_wage[i][1]
            w_plecaku.append(wartosc_przez_wage[i][0])
    return [w_plecaku, b, wartosc]

def brutal(elementy, plecok):
    wartosci = []
    binarne = []
    wagi = []
    n = len(elementy)
    form = '0' + str(n) + 'b'
    for i in range(1, (2**n)):
        binary = format(i, form)
        suma_wag = 0
        binarne.append(binary)
        for j in range(n):
            if binary[j] == '1':
                suma_wag += elementy[j][1]
        wagi.append(suma_wag)
        suma_wartosci = 0
        if suma_wag <= plecok:
            for j in range(n):
                if binary[j] == '1':
                    suma_wartosci += elementy[j][2]
            wartosci.append(suma_wartosci)
        else:
            wartosci.append(0)
    maximum = max(wartosci)
    id = wartosci.index(maximum)
    b = wagi[id]
    binary = binarne[id]
    w_plecaku = []
    for j in range(n):
        if binary[j] == '1':
            w_plecaku.append(elementy[j][0])
    return [w_plecaku, b, maximum]



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
        b = int(input("Podaj rozmiar plecaka: "))
        n = int(input("Podaj ilosc elementow: "))
        for i in range(n):
            rozmiar = random.randint(1, b + 1)
            wartosc = random.randint(1, 100)
            elementy.append([i + 1, rozmiar, wartosc])
    else:
        print("Zla opcja")
    if not error:
        dalej = True
        while dalej:
            print("\n[1] AD - algorytm programowania dynamicznego\n[2] AZ - algorytm zachlanny\n[3] AB - algorytm silowy\n[4] Wyjscie")
            algorytm = input("Wybierz opcje: ")
            wynik = ''
            if algorytm == '1':
                start = time.time()
                wynik = dynamiczne(elementy, b)
                end = time.time()
            elif algorytm == '2':
                start = time.time()
                wynik = zachlany(elementy, b)
                end = time.time()
            elif algorytm == '3':
                start = time.time()
                wynik = brutal(elementy, b)
                end = time.time()
            elif algorytm == '4':
                dalej = False
            else:
                print("Podano zle dane")
            if wynik != '':
                print('Elementy w plecaku: ', *wynik[0], '\nWartosc funkcji celu: ', wynik[2], '\nRozmiar przedmiotow: ', wynik[1])
                print('Czas operacji: ', end - start)


try:
    main()
except Exception:
    print("Wprowadzono zle dane")