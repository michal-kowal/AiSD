import random
import math
import time


def macierz_sasiedztwa(n):
    matrix = []
    for i in range(len(n)):
        matrix.append([])
        for j in range(len(n)):
            if j + 1 in n[i + 1]:
                matrix[i].append(1)
            else:
                matrix[i].append(0)
    return matrix


def generator_grafu(n, m):
    # generuj pustą macierz sąsziedztwa
    matrix = []
    for i in range(0, n):
        wiersz = []
        for j in range(0, n):
            wiersz.append(0)
        matrix.append(wiersz)
    # wstaw w losowe miejsca jedynki
    for i in range(0, m):
        j = random.randint(1, n - 1)
        k = random.randint(0, j - 1)
        while matrix[j][k] == 1:
            j = random.randint(1, n - 1)
            k = random.randint(0, j - 1)
        matrix[j][k] = 1
    # na podstawie macierzy sąsiedztwa odtwórz listę następników
    l_nastepnikow = {}
    for i in range(1, n + 1):
        nastepniki = []
        for j in range(0, n):
            if matrix[i - 1][j] == 1:
                nastepniki.append(j + 1)
        l_nastepnikow[i] = nastepniki
    # for i in range(0, n):
    #    print(*matrix[i])
    # print(l_nastepnikow)
    return l_nastepnikow


def menu():
    petla = True
    l_nastepnikow = {}
    l_poprzednikow = {}
    l_b_incydencji = {}
    err = False
    skierowany = True
    while petla:
        print('Graf:\n[1] Skierowany\n[2] Nieskierowany')
        decyzja = input()
        if decyzja == '1':
            skierowany = True
            petla = False
        elif decyzja == '2':
            skierowany = False
            petla = False
        else:
            print("Bledne dane")
    petla = True
    while petla:
        print('Dane:\n[1] Wygeneruj graf\n[2] Wprowadz dane wejsciowe\n[3] Wczytaj z pliku')
        opcja = input()
        if opcja == '1':  # Generuj graf
            # Trzeba zmodyfikowac generator grafu aby mogl byc skierowany lub nie
            petla = False
            try:
                l_wierzcholkow = int(input('Podaj liczbe wierzcholkow: '))
            except ValueError:
                print("Podano niepoprawne dane")
                err = True
                break

        elif opcja == '2':
            try:
                l_wierzcholkow = int(input('Podaj liczbe wierzcholkow: '))
            except ValueError:
                print("Podano niepoprawne dane")
                err = True
                break
            if l_wierzcholkow <= 0:
                print('Zla liczba wierzcholkow')
            else:
                if skierowany:
                    err = False
                    for i in range(1, l_wierzcholkow + 1):
                        try:
                            nastepniki = list(map(int, input('Podaj nastepniki wierzcholka ' + str(i) + ': ').split()))
                        except ValueError:
                            print("Podano niepoprawne dane")
                            err = True
                            break
                        nastepniki.sort()
                        l_nastepnikow[i] = []
                        for j in nastepniki:
                            if int(j) < 1 or int(j) > l_wierzcholkow:
                                err = True
                                break
                            l_nastepnikow[i].append(int(j))
                        l_nastepnikow[i] = sorted(l_nastepnikow[i])
                        if err:
                            print("Podano niepoprawne dane")
                            break
                    dane = l_nastepnikow
                    petla = False
                else:
                    l_krawedzi = []
                    try:
                        il_krawedzi = int(input("Ilosc krawedzi: "))
                    except ValueError:
                        print("podano niepoprawne dane")
                        err = True
                        break
                    if il_krawedzi <= 0:
                        print("Zbyt mala ilosc krawedzi")
                    else:
                        for i in range(il_krawedzi):
                            try:
                                print(str(i + 1) + ". krawedz:", end=" ")
                                l_krawedzi.append(int(i) for i in input().split())
                            except KeyError:
                                err = True
                                print("Wprowadzono zle dane")
                                break
                        for i in range(1, l_wierzcholkow + 1):
                            l_nastepnikow[i] = []
                        try:
                            for i, j in l_krawedzi:
                                l_nastepnikow[i].append(j)
                                l_nastepnikow[j].append(i)
                            dane = macierz_sasiedztwa(l_nastepnikow)
                        except ValueError:
                            print("Podano niepoprawne dane")
                            err = True
                            break
                    petla = False
        elif opcja == '3':  # Wczytaj graf
            plik = open('graf.txt')
            try:
                w, k = [int(x) for x in plik.readline().split()]  # wierzcholki, krawedzie
            except ValueError:
                print("Wprowadzono zle dane")
                err = True
                break
            for i in range(1, w + 1):
                l_nastepnikow[i] = []
            if skierowany:
                for i in range(k):
                    w_poczatkowy, w_koncowy = plik.readline().split()
                    err = False
                    if not w_poczatkowy.isnumeric() or not w_koncowy.isnumeric():
                        err = True
                    else:
                        w_poczatkowy = int(w_poczatkowy)
                        w_koncowy = int(w_koncowy)
                        if w_poczatkowy < 1 or w_poczatkowy > w or w_koncowy < 1 or w_koncowy > w or w_koncowy == w_poczatkowy:
                            err = True
                        elif w_koncowy in l_nastepnikow[w_poczatkowy]:
                            err = True
                    l_nastepnikow[w_poczatkowy].append(w_koncowy)
                dane = l_nastepnikow
            else:
                for i in range(k):
                    w1, w2 = [int(x) for x in plik.readline().split()]
                    l_nastepnikow[w1].append(w2)
                    l_nastepnikow[w2].append(w1)
                    dane = macierz_sasiedztwa(l_nastepnikow)
            if err:
                print("Podano bledna krawedz")
                break
            plik.close()
            petla = False
        else:
            print('Nieprawidlowy wybor!')
        print(dane)
    if not err:
        petla = True
        while petla:
            print("Cykl:\n[1] Cykl Eulera\n[2] Cykl Hamiltona\n[3] Wyjscie")
            wybor_cyklu = input()
            if wybor_cyklu == '1':
                if skierowany:
                    print("tu bedzie euler dla skierowanego")
                else:
                    print("tu bedzie euler dla nieskierowanego")
            elif wybor_cyklu == '2':
                if skierowany:
                    print("tu bedzie hamilton dla skierowanego")
                else:
                    print("tu bedzie hamilton dla nieskierowanego")
            elif wybor_cyklu == '3':
                return 0
            else:
                print("Nieprawidlowe dane")


menu()