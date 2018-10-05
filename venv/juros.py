from math import *
def __init__(self, valor, tempo, fValor, perc):
    self.valor = valor
    self.tempo = tempo
    self.fValor = fValor
    self.perc = perc


def JurosSimples(valor, perc, tempo):
    fValor =valor + ((valor * (perc/100)) * tempo)
    return round(fValor,2)

def JurosComposto(valor, perc, tempo):
    perc = 1+(perc/100)
    fValor = valor*(perc**tempo)
    return round(fValor,2)


def SimplesInicial(fValor,perc,tempo):
    perc = perc/100
    valor = fValor/(1+(perc*tempo))
    return round(valor,2)


def CompostoInicial(fValor, perc, tempo):
    perc =1+ perc /100
    valor = fValor/((perc**tempo))
    return round(valor,2)

def SimplesTempo(fValor, valor, perc):
    perc = perc/100
    tempo = (fValor-valor)/(valor*perc)
    return round(tempo,2)

def CompostoTempo(fValor, valor, perc):
    perc=perc/100
    tempo = log(fValor/valor)/log(1+perc)
    return round(tempo, 2)

def SimplesJuros(fValor,valor,tempo):
    perc = (fValor-valor)/(valor*tempo)
    perc = perc*100
    return round(perc, 2)

def CompostoJuros(fValor,valor,tempo):
    perc = ((fValor/valor)**(1 / tempo)) - 1
    perc = perc*100
    return round(perc,2)