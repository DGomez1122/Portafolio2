#Devolver Indices

def devolverIndices(lista,lista2):
    if isinstance(lista,list) and isinstance(lista2,list):
        return AuxDevolverIndices(lista,lista2,0,[])
    else:
        print("Error")
        
def AuxDevolverIndices(lista,lista2,cont,resultado):
    if lista2==[]:
        return resultado
    else:
        if lista2[0]==lista[0]:
            return AuxDevolverIndices(lista[1:],lista2[1:],cont+1,resultado+[cont])
        else:
            return AuxDevolverIndices(lista[1:],lista2,cont+1,resultado)
