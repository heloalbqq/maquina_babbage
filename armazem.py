class Armazen:
    def __init__(self):
        self.memoria = {}

    def armazenamento(self, endereco, codigo_rest):
        self.memoria[endereco] = codigo_rest
        
    def retorna(self, endereco):
        return self.memoria.get(endereco, 0)