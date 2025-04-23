class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class BooleanExpressionEvaluator:
    def __init__(self):
        self.operators = Stack()
        self.operands = Stack()
        self.precedence = {
            'not': 3,
            'and': 2,
            'or': 1,
            'xor': 1,
            '(': 0
        }

    def is_operator(self, token):
        return token in ['and', 'or', 'not', 'xor']

    def is_operand(self, token):
        return token.lower() in ['true', 'false']

    def get_precedence(self, operator):
        return self.precedence.get(operator, 0)

    def apply_operator(self):
        if self.operators.is_empty():
            return

        operator = self.operators.pop()

        if operator == 'not':
            if self.operands.size() < 1:
                raise ValueError("Operando insuficiente para operador 'not'")
            operand = self.operands.pop()
            result = not operand
            self.operands.push(result)
        else:
            if self.operands.size() < 2:
                raise ValueError(f"Operandos insuficientes para operador '{operator}'")
            b = self.operands.pop()
            a = self.operands.pop()

            if operator == 'and':
                result = a and b
            elif operator == 'or':
                result = a or b
            elif operator == 'xor':
                result = (a or b) and not (a and b)

            self.operands.push(result)

    def evaluate(self, expression):
        try:
            tokens = self.tokenize(expression)

            for token in tokens:
                if token == '(':
                    self.operators.push(token)

                elif token == ')':
                    while not self.operators.is_empty() and self.operators.peek() != '(':
                        self.apply_operator()

                    if self.operators.is_empty():
                        raise ValueError("Parênteses desbalanceados")
                    self.operators.pop()

                elif self.is_operand(token):
                    self.operands.push(token.lower() == 'true')

                elif self.is_operator(token):
                    while (not self.operators.is_empty() and
                           self.operators.peek() != '(' and
                           self.get_precedence(self.operators.peek()) >= self.get_precedence(token)):
                        self.apply_operator()
                    self.operators.push(token)

                else:
                    raise ValueError(f"Token inválido: {token}")

            return self.operands.pop()

        except Exception as e:
            return f"Erro: {str(e)}"

    def tokenize(self, expression):
        expression = expression.replace('(', ' ( ').replace(')', ' ) ')
        return [token.strip().lower() for token in expression.split() if token.strip()]


evaluator = BooleanExpressionEvaluator()

print("Avaliador de Expressões Booleanas")
print("Digite 'sair' para encerrar")
print("\nExemplos de uso:")
print("- True and False")
print("- (True and False) or not (False or True)")
print("- True xor False")
print("\nOperadores suportados: and, or, not, xor")

while True:
    expression = input("\nDigite a expressão: ")

    if expression.lower() == 'sair':
        break

    result = evaluator.evaluate(expression)
    print(f"Resultado: {result}")
