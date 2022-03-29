import random
import time


class Node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
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

def minimal(wezel,tryb):
    print()
    if tryb != "3":
        print("Sciezka poszukiwania:", end=" ")
    start = time.time()
    obecny = wezel
    if tryb != "3":
        print(obecny.val, end=" ")
    while obecny.left is not None:
        obecny = obecny.left
        if tryb != "3":
            print(obecny.val, end=" ")
    end = time.time()
    if tryb != "3":
        print("\nElement minimalny: ", obecny.val)
        print("Czas poszukiwania: ", end - start)
        print()
    return obecny


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

def deletion(root, key, tryb):
    parent = None
    curr = root
    while curr and curr.val != key:
        parent = curr
        if key < curr.val:
            curr = curr.left
        else:
            curr = curr.right
    if curr is None:
        return root
    if curr.left is None and curr.right is None:
        if curr != root:
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None
        else:
            root = None
    elif curr.left and curr.right:
        successor = minimal(curr.right, tryb)
        val = successor.val
        deletion(root, successor.val, tryb)
        curr.val = val
    else:
        if curr.left:
            child = curr.left
        else:
            child = curr.right
        if curr != root:
            if curr == parent.left:
                parent.left = child
            else:
                parent.right = child
        else:
            root = child
    return root
 
def in_order(root):
    if root:
        in_order(root.left)
        print(root.val, end=" ")
        in_order(root.right)

def pre_order(root):
    if root:
        print(root.val, end=" ")
        pre_order(root.left)
        pre_order(root.right)

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
        #print(drzewo.val)
        #print(drzewo.right.val)
        #print(drzewo.left.val)
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
            minimal(drzewo, procedura)
        elif procedura == "2":
            maximal(drzewo)
            print("")
        elif procedura == "3":
            remove_keys = list(map(int, input("podaj wartości kluczy do usunięcia: ").split()))
            start_deletion = time.time()
            for i in range(0, len(remove_keys)):
                deletion(drzewo, remove_keys[i], procedura)
            end_deletion = time.time()
            print()
            print("Czas operacji: ", end_deletion - start_deletion)
            print(in_order(drzewo)) #Tutaj na razie printuje w in order bo nie ma innej możliwości sprawdzenia czy element jest usuwany
            print()
        elif procedura == "4":
            print("Elementy drzewa w porzadku in-order:", end=" ")
            start_in_order = time.time()
            in_order(drzewo)
            end_in_order = time.time()
            print()
            print("Czas operacji: ", end_in_order - start_in_order)
            print()
        elif procedura == "5":
            print("Elementy drzewa w porzadku pre-order:", end=" ")
            start_pre_order = time.time()
            pre_order(drzewo)
            end_pre_order = time.time()
            print()
            print("Czas operacji: ", end_pre_order - start_pre_order)
            print()
        elif procedura == "9":
            powtorz = False
        else:
            print("Wybierz poprawna opcje")


menu()