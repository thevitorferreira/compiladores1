from src.Lex import Lexico
from src.Sintatico import Sintatico
from src.Semantico import Semantico

class compilador:
    def __init__(self):
        pass

    def lexico(self):
        lex = Lexico("txt/arquivo.txt")
        token = lex.prox_token()
        tokens = []
        while(token != None):
            tokens.append(token)
            token = lex.prox_token()
        return tokens

    def sintatico(self):
        tokens = self.lexico()
        sintatico = Sintatico(tokens)
        casamento = sintatico.analisador_sintatico()
        return casamento
    
    def semantico(self):
        tokens = self.lexico()
        flag = Semantico(tokens).analisador_semantico()
        return flag
    
    def main(self):
        flag = self.semantico()
        if flag == 'Yes':
            casamento = self.sintatico()
            self.calculadora()

    def calculadora(self):
        token = self.lexico()
        conta = ''
        for i in token:
            conta += i
        for i in range(len(conta)):
            if conta[i] == "^":
                conta = conta.replace("^", "**")
        for i in range(len(conta)):
            if conta[i] == 'e':
                conta = conta.replace("exp", "2.71828")

        print(conta)
        print(eval(conta))

        
if __name__ == '__main__':
    iniciar = compilador()
    iniciar.main()