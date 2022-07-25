from operator import truediv


class Semantico:
    def __init__(self, tokens):
        self.casamento = tokens
    

    def analisador_semantico(self):
        parenteses = self.transforma_tokens()
        if parenteses == "SUCESSO!":
            return "Yes"
        else:
            return "No"

    def transforma_tokens(self):
        token = ''
        for i in self.casamento:
            token += i
        retorno = self._parentesis(token)
        retorno = self._exp(token)
        return retorno

    def _parentesis(self, token):
        aberto = False
        for parentesis in token:
            if parentesis == ")":
                fechado = True
                if aberto != True:
                    ciclo = False
                    raise Exception("ERRO! Parenteses fechando sem abertura")
                else:
                    ciclo = True
                    aberto = False
            if parentesis == "(":
                if aberto != False:
                    raise Exception("ERRO! Parenteses precisa ser fechado")
                aberto = True
                ciclo = False
        return "SUCESSO!"

    def _exp(self, token):
        aberto = False
        for parentesis in token:
            if parentesis == "]":
                fechado = True
                if aberto != True:
                    ciclo = False
                    raise Exception("ERRO! colchetes fechando sem abertura")
                else:
                    ciclo = True
                    aberto = False
            if parentesis == "[":
                if aberto != False:
                    raise Exception("ERRO! colchete precisa ser fechado")
                aberto = True
                ciclo = False
        return "SUCESSO!"
                




