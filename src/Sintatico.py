from lib2to3.pgen2 import grammar
from src.Lex import Lexico

class Sintatico:
    """
    Tirando recursividade á esquerda

    E  -> T E'
    E' -> + T E'
    E' -> - T E'
    E' -> & 
    T  -> P T'
    T' -> * P T'
    T' -> / P T'
    T' -> &
    P  -> F P'
    P  -> exp[F] P'
    P' -> ^ F P'
    P' -> &
    F  -> (E)
    F  -> id

    """
    def __init__(self):
        self.grammar = {
            'E'  : ['T', 'E1'],
            'E1' : [['+', 'T', 'E1'], ['-', 'T', 'E1'], ['&']],
            'T'  : ['P', 'T1'],
            'T1' : [['*', 'P', 'T1'], ['/', 'P', 'T1'], ['&']],
            'P'  : [['F', 'P1'], ['exp[', 'F', ']', 'P1']],
            'P1' : [['^', 'F', 'P1'], ['&']],
            'F'  : [['(', 'E', ')'], ['id']]
            
        }

        self.first = {
            'E' : ['(', 'id', 'exp['], 
            'E1': ['+', '-', '&'], 
            'T' : ['(', 'id', 'exp['], 
            'T1': ['*', '/', '&'], 
            'P' : ['(', 'id', 'exp['], 
            'P1': ['^', '&'], 
            'F' : ['(', 'id']
            
        }
        self.follow = {
            'E' : ['$', ')'], 
            'E1': ['$', ')'], 
            'T' : ['$', '+', '-', ')'], 
            'T1': ['$', '+', '-', ')'], 
            'P' : ['$', '+', '-', ')', '*', '/'], 
            'p1': ['$', '+', '-', ')', '*', '/'], 
            'F' : ['$', '+', '-', ')', '*', '^', '/', ']']
        }
        self.tabela = {'id': {'E': [], 'E\'': [], 'T': [], 'T\'': [], 'P': [], 'P\'': [], 'F': []},
                       '(': {'E': [], 'E\'': [], 'T': [], 'T\'': [], 'P': [], 'P\'': [], 'F': []},
                       ')': {'E': [], 'E\'': [], 'T': [], 'T\'': [], 'P': [], 'P\'': [], 'F': []},
                       '/': {'E': [], 'E\'': [], 'T': [], 'T\'': [], 'P': [], 'P\'': [], 'F': []},
                       '*': {'E': [], 'E\'': [], 'T': [], 'T\'': [], 'P': [], 'P\'': [], 'F': []},
                       '+': {'E': [], 'E\'': [], 'T': [], 'T\'': [], 'P': [], 'P\'': [], 'F': []},
                       '-': {'E': [], 'E\'': [], 'T': [], 'T\'': [], 'P': [], 'P\'': [], 'F': []},
                       '^': {'E': [], 'E\'': [], 'T': [], 'T\'': [], 'P': [], 'P\'': [], 'F': []},
                       'exp[': {'E': [], 'E\'': [], 'T': [], 'T\'': [], 'P': [], 'P\'': [], 'F': []},
                       ']': {'E': [], 'E\'': [], 'T': [], 'T\'': [], 'P': [], 'P\'': [], 'F': []},
                       '$': {'E': [], 'E\'': [], 'T': [], 'T\'': [], 'P': [], 'P\'': [], 'F': []},
                       }


        self.terminais = ['+-/*^()[]','exp']
        self.numeros = '0123456789'
        self.pilha = ['E']
            
    def configura_tabela(self):
        for terminal in grammar:
            regra = first[terminal]
            for simbolo in regra:
                tabela[simbolo]= [grammar[terminal]]
        print(tabela)
    def isnumero(self, token):
        for i in token:
            if i in self.numeros:
                flag = True
            else:
                flag = False
        return flag

    def analise(self, token):
        token = token

if __name__ == '__main__':
    x = Sintatico()
    x.main()





