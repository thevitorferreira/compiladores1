from src.Lex import Lexico

class compilador:
    def __init__(self):
        pass

    def lexico():
        lex = Lexico("txt/arquivo.txt")
        token = lex.prox_token()
        tokens = []
        while(token != None):
            tokens.append(token)
            if token != '':
                print(token)
            token = lex.prox_token()
            print(tokens)
        return(tokens)

    def sintatico():
        tokens = compilador.lexico()
        for i in tokens:
            print(i)

if __name__ == '__main__':
    compilador.lexico()