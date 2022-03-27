import random
import time


def bst(elementy):
    # wezel: [klucz, rodzic, lewy, prawy]
    drzewo = {}
    drzewo[0] = [elementy[0], None, None, None]
    for i in range(1, len(elementy)):
        rodzic = 0
        drzewo[i] = [elementy[i], None, None, None]
        while True:
            if elementy[i] < drzewo[rodzic][0]:
                if drzewo[rodzic][2] is None:
                    drzewo[i][1] = rodzic
                    drzewo[rodzic][2] = i
                    break
                else:
                    rodzic = drzewo[rodzic][2]
            else:
                if drzewo[rodzic][3] is None:
                    drzewo[i][1] = rodzic
                    drzewo[rodzic][3] = i
                    break
                else:
                    rodzic = drzewo[rodzic][3]
    return drzewo


def minimalny(tab):
    start = time.time()
    mini = tab[0][0]
    path = []
    index = 0
    path.append(mini)
    while True:
        if tab[index][2] is not None:
            index = tab[index][2]
            mini = tab[index][0]
            path.append(mini)
        else:
            break
    stop = time.time()
    print("============================================")
    print("Element minimalny: ", mini)
    print("Sciezka poszukiwania: ", *path)
    print("Czas operacji: ", stop-start)
    print("============================================")


def maksymalny(tab):
    start = time.time()
    maxi = tab[0][0]
    path = []
    index = 0
    path.append(maxi)
    while True:
        if tab[index][3] is not None:
            index = tab[index][3]
            maxi = tab[index][0]
            path.append(maxi)
        else:
            break
    stop = time.time()
    print("============================================")
    print("Element maksymalny: ", maxi)
    print("Sciezka poszukiwania: ", *path)
    print("Czas operacji: ", stop - start)
    print("============================================")


def menu():
    powtorz = True
    while powtorz:
        try:
            dane = input("[1] Wprowadź dane ręcznie\n[2] Skorzystaj z generatora\n")
            if dane == "1":
                print("Wprowadź dane oddzielając spacją")
                tab = list(map(int, input().split()))
                if len(tab) == 0:
                    print("Nie wprowadzono danych")
                else:
                    powtorz = False
            elif dane == "2":
                #Generowanie danych
                tab = []
                n = int(input("Podaj dlugosc ciagu:\n"))
                for i in range(n):
                    tab.append(random.randint(1, 10 * n))
                powtorz = False
            else:
                print("Wprowadź poprawne dane")
        except ValueError:
            print("Nieprawidłowe dane wejściowe")
    powtorz = True
    while powtorz:
        print("[1] Skonstruuj drzewo AVL \n[2] Skonstruuj losowe drzewo BST")
        typ = int(input())
        print()
        print("Dane wejsciowe: ",*tab)
        print("format drzewa: {węzeł: [klucz, rodzic, lewy potomek, prawy potomek]}")
        if typ == 1:
            # drzewo = avl(tab)
            powtorz = False
        elif typ == 2:
            drzewo = bst(tab)
            powtorz = False
        else:
            print("Wybierz poprawna opcje")
        print(drzewo)
        print()
    powtorz = True
    while powtorz:
        procedura = input("[1] Wyszukaj najmniejszy element w drzewie\n"
                          "[2] Wyszukaj największy element w drzewie\n"
                          "[3] Usuń element o wybranej wartości klucza\n"
                          "[4] Wypisz wszystkie elementy drzewa w porządku rosnącym (in-order)\n"
                          "[5] Wypisz wszystkie elementy drzewa w porządku pre-order\n"
                          "[6] Usuń drzewo element po elemencie (post-order)\n"
                          "[7] Wypisz w porządku pre-order poddrzewa o danym kluczu\n"
                          "[8] Równoważ drzewo przez rotacje (DSW) lub przez usuwanie korzenia\n"
                          "[9] Wyjście\n")
        if procedura == "1":
            minimalny(drzewo)
        elif procedura == "2":
            maksymalny(drzewo)
        elif procedura == "9":
            powtorz = False
        else:
            print("Wybierz poprawna opcje")


menu()