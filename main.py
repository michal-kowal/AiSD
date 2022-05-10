# Program dziala na zasadzie listy nastepnikow, poprzednikow, listy braku incydencji. Uzyto do tego slownikow
import copy
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
    while m > 0:
        for j in range(n):
            for k in range(2):
                k = random.randint(0, n-1)
                while k == j or matrix[j][k] == 1:
                    k = random.randint(0, n-1)
                matrix[j][k] = 1
                matrix[k][j] = 1
        m -= n
    for i in range(0, n):
       print(*matrix[i])
    print()
    # na podstawie macierzy sąsiedztwa odtwórz listę następników
    # l_nastepnikow = {}
    # for i in range(1, n + 1):
    #     nastepniki = []
    #     for j in range(0, n):
    #         if matrix[i - 1][j] == 1:
    #             nastepniki.append(j + 1)
    #     l_nastepnikow[i] = nastepniki
    return matrix


def czy_ma_nieskierowany_euler(matrix):
    for i in range(len(matrix)):
        stopien = 0
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                stopien += 1
        if stopien % 2 != 0:
            return False
    return True


def euler_nieskierowany(matrix, v, stos):
    for j in range(len(matrix)):
        if matrix[v][j] == 1:
            matrix[v][j] = 0
            matrix[j][v] = 0
            euler_nieskierowany(matrix, j, stos)
    stos.append(v + 1)


def hamilton_nieskierowany(matrix):
    n = len(matrix)
    odwiedzone = [False for i in range(n)]
    odwiedzone[0] = True
    stos = []
    stos.append(0)
    powrot_z = -1
    while True:
        nastepnik = False
        for i in range(powrot_z + 1, n):
            if (not odwiedzone[i] or (len(stos) == len(matrix) and stos[0] == i)) and matrix[stos[-1]][i] == 1:
                stos.append(i)
                odwiedzone[i] = True
                nastepnik = True
                powrot_z = -1
                break
        if not nastepnik and len(stos) == 1:
            break
        if not nastepnik:
            powrot_z = stos[-1]
            odwiedzone[stos[-1]] = False
            stos.pop()
        if len(stos) == n + 1 and stos[0] == stos[-1]:
            for i in range(n + 1):
                stos[i] += 1
            return stos
    return False

def euler_skierowany(dict, v, stos):
    if len(dict[v]) > 0:
        j = dict[v][0]
        dict[v].remove(j)
        euler_skierowany(dict, j, stos)
    stos.append(v)

def czy_ma_skierowany_euler(dict):
    for i in range(1, len(dict) + 1):
        count = 0
        for j in range(1, len(dict) + 1):
            if i in dict[j]:
                count += 1
        if len(dict[i])%2 != count:
            return False
    return True

def menu():
    petla = True
    l_nastepnikow = {}
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
            try:
                n = int(input("Podaj liczbę wierzchołków: "))
                s = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90]
                i = int(input("Wybierz poziom nasycenia:\n1) 10%\n2) 20%\n3) 30%\n4) 40%\n5) 50%\n6) 60%\n7) 70%\n8) 80%\n9) 90%\n")) - 1
            except ValueError:
                print("nieprawidłowe dane")
                err = True
                break
            if skierowany:
                nasycenie =  (n*(n-1))
                m = math.floor(nasycenie * s[i])
                #l_nastepnikow = generator_grafu(n, m)
                #dane = macierz_sasiedztwa(l_nastepnikow)
            else:
                nasycenie = (n*(n-1))/2
                m = math.floor(nasycenie * s[i])
                dane = generator_grafu(n, m)
            petla = False
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
    if not err:
        petla = True
        while petla:
            print("\n[1] Cykl Eulera\n[2] Cykl Hamiltona\n[3] Wyjscie")
            wybor_cyklu = input()
            if wybor_cyklu == '1':
                if skierowany:
                    stos = []
                    czy_ma = czy_ma_skierowany_euler(dane)
                    euler_skierowany(dane, 1, stos)
                    if czy_ma:
                        if len(dane) + 1 == len(stos):
                            print("Cykl:", end = " ")
                            print(*stos)
                        else:
                            print("Graf wejsciowy nie zawiera cyklu.")
                    else:
                        print("Graf wejsciowy nie zawiera cyklu.")
                else:
                    dane_k = copy.deepcopy(dane)
                    czy_ma = czy_ma_nieskierowany_euler(dane_k)
                    stos = []
                    if czy_ma:
                        euler_nieskierowany(dane_k, 0, stos)
                        if len(dane_k) + 1 == len(stos):
                            print("Cykl:", end=" ")
                            print(*stos)
                        else:
                            print("Graf wejsciowy nie zawiera cyklu.")
                    else:
                        print("Graf wejsciowy nie zawiera cyklu.")
            elif wybor_cyklu == '2':
                if skierowany:
                    print("tu bedzie hamilton dla skierowanego")
                else:
                    dane_k = copy.deepcopy(dane)
                    res = hamilton_nieskierowany(dane_k)
                    if res == False:
                        print("Graf wejsciowy nie zawiera cyklu.")
                    else:
                        print("Cykl:", end=" ")
                        print(res)
            elif wybor_cyklu == '3':
                return 0
            else:
                print("Nieprawidlowe dane")


menu()