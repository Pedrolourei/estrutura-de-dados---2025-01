class Pilha:
    def __init__(self, capacidade):
        self.dados = []
        self.capacidade = capacidade

    def empilhar(self, item):
        if len(self.dados) < self.capacidade:
            self.dados.append(item)
        else:
            print("Pilha cheia!")

    def desempilhar(self):
        if not self.vazia():
            return self.dados.pop()
        else:
            print("Pilha vazia!")
            return None

    def topo(self):
        if not self.vazia():
            return self.dados[-1]
        return None

    def vazia(self):
        return len(self.dados) == 0

    def tamanho(self):
        return len(self.dados)

    def mostrar(self):
        print(self.dados)


p = Pilha(10)

for i in range(1, 6):
    p.empilhar(i)

while not p.vazia():
    print("Desempilhado:", p.desempilhar())

def esvaziar_pilha(p):
    while not p.vazia():
        p.desempilhar()
    print("Pilha esvaziada")

p = Pilha(5)

for i in range(5):
    num = int(input(f"Digite o número {i+1}: "))
    p.empilhar(num)

print("Números em ordem inversa:")
while not p.vazia():
    print(p.desempilhar())

texto = Pilha(100)

entrada = input("Digite o texto (use # para apagar): ")

for ch in entrada:
    if ch == "#":
        texto.desempilhar()
    else:
        texto.empilhar(ch)

print("Texto final:", ''.join(texto.dados))

def remover_item(pilha, item_remover):
    temp = Pilha(pilha.capacidade)
    encontrado = False

    # Transfere para pilha temporária, pulando o item
    while not pilha.vazia():
        topo = pilha.desempilhar()
        if topo == item_remover and not encontrado:
            encontrado = True  # remove apenas a primeira ocorrência
        else:
            temp.empilhar(topo)

    # Devolve os itens de volta pra pilha original (mantendo ordem)
    while not temp.vazia():
        pilha.empilhar(temp.desempilhar())

    if encontrado:
        print(f"Item {item_remover} removido.")
    else:
        print(f"Item {item_remover} não encontrado.")
