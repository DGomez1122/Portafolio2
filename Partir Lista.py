#Partir Lista

def partirLista(lista):
    if isinstance(lista,list):
        return AuxPartir(lista,[],[])
    else:
        print("Error")
def AuxPartir(lista,sublista,resultado):
    if lista==[]:
        if sublista==[]:
            return resultado
        else:
            return resultado+[sublista]
    elif lista[0]>=0:
        return AuxPartir(lista[1:],sublista+[lista[0]],resultado)
    else:
        return AuxPartir(lista[1:],[],resultado+[sublista])
