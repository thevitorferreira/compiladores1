from time import time


import time
class Sintatico:
  
    def __init__(self, tokens):
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
        self.tabela = {"id": {"E": "TE'", "E'": "", "T": "PT'", "T'": "", "P": "FP'", "P'": "", "F": "id"},
                       "(": {"E": "TE'", "E'": "", "T": "PT'", "T'": "", "P": "FP'", "P'": "", "F": "(E)"},
                       ")": {"E": "", "E'": "&", "T": "", "T'": "&", "P": "", "P'": "&", "F": ""},
                       "/": {"E": "", "E'": "", "T": "", "T'": "/PT'", "P": "", "P'": "&", "F":""},
                       "*": {"E": "", "E'": "", "T": "", "T'": "*PT'", "P": "", "P'": "&", "F": ""},
                       "+": {"E": "", "E'": "+TE'", "T": "", "T'": "&", "P": "", "P'": "&", "F": ""},
                       "-": {"E": "", "E'": "-TE'", "T": "", "T'": "&", "P": "", "P'": "&", "F": ""},
                       "^": {"E": "", "E'": "", "T": "", "T'": "", "P": "", "P'": "^FP'", "F": ""},
                       "exp[": {"E": "TE'", "E'": "", "T": "exp[F]", "T'": "", "P": "exp[F]", "P'": "", "F": ""},
                       "]": {"E": "", "E'": "", "T": "", "T'": "", "P": "", "P'":"", "F": ""},
                       "$": {"E": "", "E'": "&", "T": "", "T'": "&", "P": "", "P'": "&", "F": ""},
                       }

        self.tokens = tokens
        self.terminais = ['+-/*^()[]','exp'] 
        self.numeros = '0123456789'
        self.pilha = "E$"

    def analisador_sintatico(self):
        tokens_com_id = self.tokenizacao()
        self.casamento = ''
        
        for token in tokens_com_id:
   
            #token = tokens_com_id[10]
            if self.pilha[0] != token:
                while True:
                    if self.pilha[0] == token:
                        self.pilha = self.replace_manual(self.pilha, self.pilha[0], "")
                        self.casamento+=token
                        break
                    if self.pilha[0] == 'i':
                        self.pilha = self.replace_manual(self.pilha, "id", "")
                        self.casamento+= "id"
                        break
                    if self.pilha[0] == 'e':
                        self.pilha = self.replace_manual(self.pilha, "exp[", "")
                        self.casamento+= "exp["
                        break
                    if self.pilha[1] == "'":
                        auxiliar = self.pilha[0]
                        auxiliar+= "'"
                        item_tabela = self.tabela[token][auxiliar]
                       
                        if item_tabela == '&':
                            self.pilha = self.replace_manual(self.pilha, auxiliar, "")
                        else:
                            self.pilha = self.replace_manual(self.pilha, auxiliar, item_tabela)
                        
                    else:
                        item_tabela = self.tabela[token][self.pilha[0]]
                        if item_tabela == '&':
                            self.pilha = self.replace_manual(self.pilha, self.pilha[0], auxiliar)
                        else:
                            self.pilha = self.replace_manual(self.pilha, self.pilha[0], item_tabela)
            elif self.pilha[0] == token:
                self.pilha = self.replace_manual(self.pilha, token, "")
                self.casamento+=token
                return self.casamento

    def replace_manual(self, string, substituir, substituto, substituir_tudo = False):
        i = 0
        while i != len(string):
            if string[i:i+len(substituir)] == substituir:
                string = string[:i] + substituto + string[i+len(substituir):]
                i = i - len(substituir) + len(substituto)
                if not substituir_tudo:
                    return string
            i += 1
        return string

    def tokenizacao(self):
        tokens_com_id = []
  
        for token in self.tokens:
            id = self.isnumero(token)
            if id == True:
                tokens_com_id.append('id')
            else:
                tokens_com_id.append(token)

        tokens_com_id.append('$')
        return tokens_com_id

    def isnumero(self, token):
        for i in token:
            if i in self.numeros:
                return True
            else:
                return False
    








