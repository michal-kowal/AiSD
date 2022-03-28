import random
import time


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def minimal(wezel):
    print()
    print("Sciezka poszukiwania:", end=" ")
    start = time.time()
    obecny = wezel
    print(obecny.val, end=" ")
    while obecny.left is not None:
        obecny = obecny.left
        print(obecny.val, end=" ")
    end = time.time()
    print("\nElement minimalny: ", obecny.val)
    print("Czas poszukiwania: ", end - start)
    print()


def maximal(wezel):
    print()
    print("Sciezka poszukiwania:", end=" ")
    start = time.time()
    obecny = wezel
    print(obecny.val, end=" ")
    while obecny.right is not None:
        obecny = obecny.right
        print(obecny.val, end=" ")
    end = time.time()
    print("\nElement maksymalny: ", obecny.val)
    print("Czas poszukiwania: ", end - start)
    print()


def in_order(root):
    if root:
        in_order(root.left)
        print(root.val, end=" ")
        in_order(root.right)


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
        if typ == 1:
            tab.sort()
            #drzewo = insert(drzewo, mediana)
            powtorz = False
        elif typ == 2:
            drzewo = Node(tab[0])
            for i in range(1, len(tab)):
                drzewo = insert(drzewo, tab[i])
            powtorz = False
        else:
            print("Wybierz poprawna opcje")
        #print("K-klucz, P-przodek, PP-prawy potomek, LP-lewy potomek")
        #for i in tab:
        #    print("K:",i," P:",," PP:",," LP:",)
        #print(drzewo.right.val)
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
            minimal(drzewo)
        elif procedura == "2":
            maximal(drzewo)
            print("")
        elif procedura == "4":
            print("Elementy drzewa w porzadku in-order:", end=" ")
            start_in_order = time.time()
            in_order(drzewo)
            end_in_order = time.time()
            print()
            print("Czas operacji: ", end_in_order - start_in_order)
            print()
        elif procedura == "9":
            powtorz = False
        else:
            print("Wybierz poprawna opcje")


menu()