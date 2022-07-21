class Lexico:
    def __init__(self, arquivo):
        with open(arquivo, "r") as reader:
            self.text = reader.read()
        self.posicao = 0

    def prox_token(self):
        token = ''
        if self.posicao > (len(self.text) - 1):
            return None
        for indice, c in enumerate(self.text[self.posicao]):
            if c in '0123456789':
                token=c
                self.posicao += indice + 1
                while True:
                    if self.text[self.posicao] in '0123456789' or self.text[self.posicao] == '.':
                        c = self.text[self.posicao]
                        token+=c
                        self.posicao += indice+1
                    else:
                        break
                return token

            if c == 'e':
                print(indice)
                if self.text[self.posicao + 1] == 'x' and self.text[self.posicao + 2] == 'p':
                    token = 'exp'
                    self.posicao += indice + 3
                    return token

            if c in '+-^/*[]()=':
                token = c
                self.posicao += indice + 1
                return token

            if c in ['','\n', '\t', ' ']:
                indice += 1
                self.posicao += indice
                return token

                    

    
    