class Sintatico:
    def __init__(self):
        self.grammar =  {
            "E'": [["E"]],
            "E": [
                ["E", "+", "T"],
                ["E", "-", "T"],
                ["T"]
            ],
            "T": [
                ["T", "*", "P"],
                ["T", "/", "P"],
                ["P"]
            ],
            "P": [
                ["P", "^", "F"],
                ["exp", "[", "F", "]"],
                ["F"]
            ],
            "F": [
                ["(", "E", ")"],
                ["id"] 
            ]
        }
        self.terminais = ['+-/*^()[]','exp']
        self.numeros = '0123456789'
        self.casamento = []
        self.pilha = ['E']

    def isnumero(self, token):
        for i in token:
            if i in self.numeros:
                flag = True
            else:
                flag = False
        return flag

    def main(self):
        pass
if __name__ == '__main__':
    x = Sintatico()
    x.main()


"""commit"""


