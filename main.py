# Program dziala na zasadzie listy nastepnikow, poprzednikow, listy braku incydencji. Uzyto do tego slownikow
import random

def generuj_listy(n, p, b):
    for i in n.keys():
        p[i] = []
    for i in n.keys():
        for j in n[i]:
            if i not in p[j]:
                p[j].append(i)
    for i in n.keys():
        b[i] = []
        for k in range(1, len(n) + 1):
            if k not in n[i] and k not in p[i]:
                b[i].append(k)

def macierz_grafu(następniki, poprzedniki, bezincydejki, n):
    #generuj macierz pustą
    matrix = []
    for i in range(0, n):
        wiersz = []
        for j in range(0, n+3):
            wiersz.append(0)
        matrix.append(wiersz)
    #mordowanie z listą następników
    for i in range(0, n):
        if len(list(następniki.values())[i]) == 0:
            continue
        else:
            matrix[i][n] = list(następniki.values())[i][0]
    for i in range(0, n):
        for j in list(następniki.values())[i]:
            if len(list(następniki.values())[i]) == 0:
                continue
            else:
                matrix[i][j-1] = list(następniki.values())[i][-1]
    #mordowanie z listą poprzedników
    for i in range(0, n):
        if len(list(poprzedniki.values())[i]) == 0:
            continue
        else:
            matrix[i][n+1] = list(poprzedniki.values())[i][0]
    for i in range(0, n):
        for j in list(poprzedniki.values())[i]:
            if len(list(poprzedniki.values())[i]) == 0:
                continue
            else:
                matrix[i][j-1] = (list(poprzedniki.values())[i][-1] + 5)
    #mordowanie z listą bla bla bla
    for i in range(0, n):
        if len(list(bezincydejki.values())[i]) == 0:
            continue
        else:
            matrix[i][n+2] = list(bezincydejki.values())[i][0]
    for i in range(0, n):
        for j in list(bezincydejki.values())[i]:
            if len(list(bezincydejki.values())[i]) == 0:
                continue
            else:
                matrix[i][j-1] = -(list(bezincydejki.values())[i][-1])
    #PRRYNT
    for i in range(len(matrix)):
        print(*matrix[i])


def macierz_sasiedztwa(n, p):
    matrix = []
    for i in range(len(n)):
        matrix.append([])
        for j in range(len(n)):
            if j + 1 in n[i + 1]:
                matrix[i].append(1)
            elif j + 1 in p[i + 1]:
                matrix[i].append(-1)
            else:
                matrix[i].append(0)
    print("Macierz sasiedztwa:")
    [print(*matrix[i]) for i in range(len(matrix))]


def menu():
    petla = True
    l_nastepnikow = {}
    l_poprzednikow = {}
    l_b_incydencji = {}
    err = False
    while petla:
        print('[1] Wygeneruj graf\n[2] Wprowadz dane wejsciowe\n[3] Wczytaj z pliku')
        opcja = input()
        if opcja == '1':    # Generuj graf
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
                    if err:
                        print("Podano niepoprawne dane")
                        break
                if not err:
                    generuj_listy(l_nastepnikow, l_poprzednikow, l_b_incydencji)
                petla = False
        elif opcja == '3':  # Wczytaj graf
            plik = open('graf.txt')
            try:
                w, k = [int(x) for x in plik.readline().split()]    # wierzcholki, krawedzie
            except ValueError:
                print("Wprowadzono zle dane")
                err = True
                break
            for i in range(1, w + 1):
                l_nastepnikow[i] = []
            for i in range(k):
                w_poczatkowy, w_koncowy = plik.readline().split()
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
            plik.close()
            if not err:
                generuj_listy(l_nastepnikow, l_poprzednikow, l_b_incydencji)
            petla = False
        else:
            print('Nieprawidlowy wybor!')
        print(l_nastepnikow)
        print(l_poprzednikow)
        print(l_b_incydencji)
    if not err:
        petla = True
        while petla:
            print("[1] Wygeneruj macierz grafu\n[2] Wygeneruj macierz sasiedztwa")
            wybor_macierz = input()
            if wybor_macierz == '1':
                macierz_grafu(l_nastepnikow, l_poprzednikow, l_b_incydencji, l_wierzcholkow)
                petla = False
            elif wybor_macierz == '2':
                macierz_sasiedztwa(l_nastepnikow, l_poprzednikow)
                petla = False
            else:
                print("Wybrano nieprawidlowa opcje")

menu()