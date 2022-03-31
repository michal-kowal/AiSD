import math
import random
import statistics
import time


class Node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.val = key
        self.height = 1

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


def minimal(wezel, tryb):
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

def post_order_deletion(root):
    if root:
        post_order_deletion(root.left)
        post_order_deletion(root.right)
        print(root.val)
        #root.val = None
        deletion(root, root.val, "3")

def sub_root_pre_order(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return sub_root_pre_order(root.right, key)
    return sub_root_pre_order(root.left, key)

# level order w celu wyswietlania struktury drzewa
def level_order(root):
    h = height(root)
    for i in range(1, h + 1):
        print_current(root, i)


def print_current(root, level):
    if root is None:
        return
    if level == 1:
        if root.left is None and root.right is not None:
            print("K:", root.val, " LP:", root.left, " PP:", root.right.val)
        elif root.left is not None and root.right is None:
            print("K:", root.val, " LP:", root.left.val, " PP:", root.right)
        elif root.left is not None and root.right is not None:
            print("K:", root.val, " LP:", root.left.val, " PP:", root.right.val)
        elif root.left is None and root.right is None:
            print("K:", root.val, " LP:", root.left, " PP:", root.right)
    elif level > 1:
        print_current(root.left, level - 1)
        print_current(root.right, level - 1)


def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


def mediana(tab, lr):
    global med
    #print(tab)
    if len(tab) > 1:
        if len(tab) % 2 == 1:
            median = math.ceil(len(tab) / 2) - 1
        else:
            median = math.ceil(len(tab) / 2) - 1
        #print(tab[median])
        med.append(tab[median])
        if len(tab[:median]) >= 1:
            mediana(tab[:median], lr)
        if len(tab[median + 1:]) >= 1:
            mediana(tab[median + 1:], lr)
    elif len(tab) == 1:
        med.append(tab[0])


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
        if typ == 1:
            global med
            med = []
            drzewo_start = time.time()
            tab.sort()
            mediana(tab, 'l')
            med_final = []
            if len(med) % 2 == 1:
                med_final.append(med[0])
                j = len(med)//2 + 1
                for i in range(1, len(med)//2 + 1):
                    med_final.append(med[i])
                    med_final.append(med[j])
                    j += 1
            else:
                j = len(med) // 2
                for i in range(0, len(med) // 2):
                    med_final.append(med[i])
                    med_final.append(med[j])
                    j += 1
            drzewo = Node(med_final[0])
            for i in range(1, len(med_final)):
                drzewo = insert(drzewo, med_final[i])
            drzewo_stop = time.time()
            powtorz = False
        elif typ == 2:
            drzewo_start = time.time()
            drzewo = Node(tab[0])
            for i in range(1, len(tab)):
                drzewo = insert(drzewo, tab[i])
            drzewo_stop = time.time()
            powtorz = False
        else:
            print("Wybierz poprawna opcje")
        print("Czas operacji: ", drzewo_stop - drzewo_start)
        if dane == "1":
            print("Dane wejsciowe: ", *tab)
            print("Struktura drzewa: Klucz, Lewy Potomek, Prawy Potomek")
            level_order(drzewo)
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
            print("Struktura drzewa: Klucz, Lewy Potomek, Prawy Potomek")
            level_order(drzewo)
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
        elif procedura == "6":
            print()
            print("Kolejność usuwania elementów: ")
            start_POD = time.time()
            post_order_deletion(drzewo)
            end_POD = time.time()
            print("Czas operacji: ", end_POD - start_POD)
            #print("Struktura drzewa: Klucz, Lewy Potomek, Prawy Potomek")
            #level_order(drzewo)
        elif procedura == "7":
            print(level_order(drzewo))
            print()
            key = int(input("Podaj od wartość klucza od którego ma się stworzyć poddrzewo: "))
            print()
            print("Dane wyjściowe: ")
            start_SRPO = time.time()
            print(pre_order(sub_root_pre_order(drzewo, key)))
            end_SRPO = time.time()
            print("Czas operacji: ", end_SRPO - start_SRPO)
        elif procedura == "8":
            print(pre_order(drzewo))
            start_DSW = time.time()
            end_DSW = time.time()
            print("Czas operacji: ", end_DSW - start_DSW)
        elif procedura == "9":
            powtorz = False
        else:
            print("Wybierz poprawna opcje")


menu()