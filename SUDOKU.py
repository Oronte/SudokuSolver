def test(C):
    '''IN : liste de 9 entiers
    OUT : bool si tous les chiffres sont presents'''
    L=[1,2,3,4,5,6,7,8,9]
    for x in C:
        for y in L:
            if x==y:
                L.remove(y)
    if L==[]:
        return True
    return False
assert test([1,2,3,4,5,6,7,8,9])==True
assert test([1,2,3,10,5,6,7,8,9])==False

def ligne_complete(L,i):
    return test(L[i])

def colone_complete(L,j):
    l=[]
    for i in L:
        l.append(i[j])
    return test(l)

def carre_complet(L,k):
    c=[]
    i0=k//3*3
    j0=k%3*3
    for i in range(i0,i0+3):
        for j in range(j0,j0+3):
            c.append(L[i][j])
            return test(c)

def sudoku_complet(L):
    for i in range(0,9):
        if not ligne_complete(L,i):
            return False
        if not colone_complete(L,i):
            return False
        if not carre_complet(L,i):
            return False
    return True
M=[[1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 1, 4, 3, 6, 5, 8, 9, 7],
    [3, 6, 5, 8, 9, 7, 2, 1, 4],
    [8, 9, 7, 2, 1, 4, 3, 6, 5],
    [5, 3, 1, 6, 4, 2, 9, 7, 8],
    [6, 4, 2, 9, 7, 8, 5, 3, 1],
    [9, 7, 8, 5, 3, 1, 6, 4, 2]]
P=[[2,0,0,0,9,0,3,0,0],
   [0,1,9,0,8,0,0,7,4],
   [0,0,8,4,0,0,6,2,0],
   [5,9,0,6,2,1,0,0,0],
   [0,2,7,0,0,0,1,6,0],
   [0,0,0,5,7,4,0,9,3],
   [0,8,5,0,0,9,7,0,0],
   [9,3,0,0,5,0,8,4,0],
   [0,0,2,0,6,0,0,0,1]]
def nmb_ligne(L,i):
    l=[]
    for x in L[i]:
        if x!=0:
            l.append(x)
    return l

def nmb_colonne(L,j):
    l=[]
    for i in range(0,9):
        if L[i][j]!=0:
            l.append(L[i][j])
    return l

def nmb_carre(L,i,j):
    l=[]
    i0=i//3*3
    j0=j//3*3
    for k in range(i0,i0+3):
        for h in range(j0,j0+3):
            if L[k][h]!=0:
                l.append(L[k][h])
            return l


def nmb_possible(L,i,j):
    C=[1,2,3,4,5,6,7,8,9]
    for k in nmb_ligne(L,i):
        if k in C:
            C.remove(k)
    for k in nmb_colonne(L,j):
        if k in C:
            C.remove(k)
    for k in nmb_carre(L,i,j):
        if k in C:
            C.remove(k)
    return C

def tour(L):
    a=0
    for i in range(9):
        for j in range(9):
            if L[i][j]==0 and len(nmb_possible(L,i,j))==1:
                L[i][j]=nmb_possible(L,i,j)[0]
                a+=1
    if a>0:
        return True
    return False

def tours(L):
    for i in range(9):
        for j in range(9):
            if L[i][j]==0 and len(nmb_possible(L,i,j))==1:
                L[i][j]=nmb_possible(L,i,j)[0]
    return L

def complete(L):
    while tour(L)==True:
        tours(L)
    for h in range(9):
        for g in range(9):
            if L[h][g]==0:
                return False
    print(L)
    return True


def affichage(L):
    for i in range(9):
       print(L[i])



