class Nodo:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (
            self.esquerda and self.esquerda.chave,
            self.chave,
            self.direita and self.direita.chave
        )

class BinaryTree:
    def __init__(self):
        self.raiz = None

# Inserção
def insert(root, key):
    if root is None:
        return Nodo(key)
    if key < root.chave:
        root.esquerda = insert(root.esquerda, key)
    else:
        root.direita = insert(root.direita, key)
    return root

# Busca
def buscar(root, key):
    if root is None:
        return None
    if key == root.chave:
        return root
    elif key < root.chave:
        return buscar(root.esquerda, key)
    else:
        return buscar(root.direita, key)

# Impressão - Pré-Ordem (N, E, D)
def pre_ordem(root):
    if root:
        print(root.chave, end=' ')
        pre_ordem(root.esquerda)
        pre_ordem(root.direita)

# Impressão - Pós-Ordem (E, D, N)
def pos_ordem(root):
    if root:
        pos_ordem(root.esquerda)
        pos_ordem(root.direita)
        print(root.chave, end=' ')

# Impressão - Em Ordem (E, N, D)
def em_ordem(root):
    if root:
        em_ordem(root.esquerda)
        print(root.chave, end=' ')
        em_ordem(root.direita)

# Remoção
def remove(root, key):
    if root is None:
        return None
    
    if key < root.chave:
        root.esquerda = remove(root.esquerda, key)
    elif key > root.chave:
        root.direita = remove(root.direita, key)
    else:
        if root.esquerda is None:
            return root.direita
        elif root.direita is None:
            return root.esquerda
        else:
            # Substituir pelo maior da subárvore esquerda (ou menor da direita)
            temp = root.esquerda
            while temp.direita:
                temp = temp.direita
            root.chave = temp.chave
            root.esquerda = remove(root.esquerda, temp.chave)
    return root

# ----------------------------
# Teste do código completo
# ----------------------------
arvore = BinaryTree()
arvore.raiz = insert(arvore.raiz, 6)
insert(arvore.raiz, 2)
insert(arvore.raiz, 1)
insert(arvore.raiz, 4)
insert(arvore.raiz, 3)
insert(arvore.raiz, 8)

print("Árvore (pré-ordem): ", end='')
pre_ordem(arvore.raiz)
print()

print("Árvore (em ordem): ", end='')
em_ordem(arvore.raiz)
print()

print("Árvore (pós-ordem): ", end='')
pos_ordem(arvore.raiz)
print()

print("Buscando 4:", buscar(arvore.raiz, 4))
print("Buscando 10:", buscar(arvore.raiz, 10))

print("Removendo 6...")
arvore.raiz = remove(arvore.raiz, 6)

print("Árvore após remoção (em ordem): ", end='')
em_ordem(arvore.raiz)
print()
