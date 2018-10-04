def __init__(self, valor, tempo, fValor, perc):
    self.valor = valor
    self.tempo = tempo
    self.fValor = fValor
    self.perc = perc


def JurosSimples(valor, perc, tempo):
    fValor =valor+( (valor * (perc/100)) * tempo)
    return fValor

def JurosComposto(valor, perc, tempo):
    fValor = ((valor * (perc/100))**tempo)
    return fValor

