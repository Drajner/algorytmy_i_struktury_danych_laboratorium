# Zadanie na lab3 - drzewa
**Przedmiot:** AISDI21L

**Autorzy:** Bartłomiej Dudek i Michał Kowalczyk

W pliku **bst_tree.py** znajduje się biblioteka drzewa BST, a w pliku **avl_tree.py** znajduje się biblioteka drzewa AVL. W **avl_bst_benchmark.py** znajduje się funkcja przeprowadzająca testy, po włączniu tego pliku w pythonie, przeprowadza on testy i generuje komplet wykresów, które zapisuje w folderze lab3 znajdującym się w folderze wywołania.

**Wnioski:** Czas tworzenia drzewa, jak i czas usuwania elementów z drzewa avl są znacząco większe od czasu tworzenia drzewa bst. W przypadku czasu poszukiwania elementu czasy są podobne z dorbną przewagą w szybkości dla drzewa avl. Przez fakt, że liczby, z których tworzymy drzewa, są generowane losowo i nie są posortowane, czasy te są porównywalne.
