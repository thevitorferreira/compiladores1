from genericpath import exists
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

    def exponential(self, x):
        # initialize sum of series
        sum = 1.0
        for i in range(10, 0, -1):
            sum = 1 + int(x) * sum / i
        return sum

    def calculadora(self):
        token = self.lexico()
        conta = ''
        for i in token:
            conta += i
        for i in range(len(conta)):
            if conta[i] == "^":
                conta = conta.replace("^", "**")
        conta1 = conta.split('[')[1]
        conta2 = conta1.split(']')[0]
        exp = self.exponential(conta2)
        exp = str(exp)
        conta_nova = []
        for i in range(len(conta)):
            if conta[i] != 'e':
                conta_nova.append(conta[i])
            else:
                break
        conta_exp = ''
        for i in conta_nova:
            conta_exp+=i
        print(eval(conta_exp+exp))
        
        

        
if __name__ == '__main__':
    iniciar = compilador()
    iniciar.main()