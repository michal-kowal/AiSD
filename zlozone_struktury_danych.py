import random


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
        if typ == 1:
            #avl(tab)
            powtorz = False
        elif typ == 2:
            print(bst(tab))
            powtorz = False
        else:
            print("Wybierz poprawna opcje")

menu()