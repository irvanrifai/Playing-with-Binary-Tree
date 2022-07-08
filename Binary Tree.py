class BinaryTree(object):
    def __init__(self,data):
        self.data=data
        self.kiri=None
        self.kanan=None
#No.6
def ukuranPohon(akar):
    if akar is None:
        return 0
    else:
        return (ukuranPohon(akar.kiri)+1+ukuranPohon(akar.kanan))

#No.7
def tinggiPohon(akar):
    if akar is None:
        return 0

    tinggiKiri = tinggiPohon(akar.kiri)
    tinggiKanan = tinggiPohon(akar.kanan)

    if (tinggiKiri>tinggiKanan):
        h=1+tinggiKiri
    
    else:
        h=1+tinggiKanan
        
    return h
    
#No.8 (Cetak Data dan Level with inoder traversal)    
def DataLevel(tree):
    if tree is not None:
        DataLevel(tree.kiri)
        print(tree.data)
        DataLevel(tree.kanan)

def preorderTrav(subpohon):
	if subpohon is not None:
		print(subpohon.data)
		preorderTrav(subpohon.kiri)
		preorderTrav(subpohon.kanan)

def inorderTrav(subpohon):
	if subpohon is not None:
		inorderTrav(subpohon.kiri)
		print(subpohon.data)
		inorderTrav(subpohon.kanan)

def postorderTrav(subpohon):
	if subpohon is not None:
		postorderTrav(subpohon.kiri)
		postorderTrav(subpohon.kanan)
		print(subpohon.data)
"""
def addInNode(nn):
;
def addExNode(nn):
;
def delInNode(nn):
;
def delExNode(nn):
"""
A = BinaryTree(1)
B = BinaryTree(2)
C = BinaryTree(3)
D = BinaryTree(4)
E = BinaryTree(5)
F = BinaryTree(6)
"""G = BinaryTree(67)
H = BinaryTree(83)
I = BinaryTree(31)
J = BinaryTree(11)
K = BinaryTree(51)
L = BinaryTree(20)
M = BinaryTree(97)
N = BinaryTree(20)
O = BinaryTree(28)"""

A.kiri=B ; A.kanan=C

B.kiri=D ; B.kanan=E
#D.kiri=F ; D.kanan=G
#E.kiri=H ; E.kanan=I

C.kanan=F ; #C.kanan=K
"""J.kiri=L ; J.kanan=M
K.kiri=N ; K.kanan=O
"""
