from Lex import Lexico

class compilador:
    def __init__(self):
        pass

    def lexico():
        lex = Lexico("arquivo.txt")
        token = lex.prox_token()
        while(token != None):
            if token != '':
                print(token)
            token = lex.prox_token()
    

if __name__ == '__main__':
    compilador.lexico()