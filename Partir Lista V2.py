#Partir Lista V2

def partirListaV2(lista):
    if isinstance(lista,list):
        return AuxPartirV2(lista,[],[],[])
    else:
        print("Error")
def AuxPartirV2(lista,sublista,negativos,resultado):
    if lista==[]:
        if sublista==[]:
            return resultado+[negativos]
        else:
            return resultado+[sublista]+[negativos]
    elif lista[0]>=0:
        return AuxPartirV2(lista[1:],sublista+[lista[0]],negativos,resultado)
    else:
        return AuxPartirV2(lista[1:],[],negativos+[lista[0]],resultado+[sublista])
