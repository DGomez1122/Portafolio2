#Invertir una lista

def invertirLista(lista):
    if isinstance(lista,list) and (lista!=[]):
        return AuxInvertir(lista,[])
    else:
        print("Debe ingresar una lista y no puede estar vacía")

def AuxInvertir(lista,res):
    if lista==[]:
        return res
    else:
        if(lista[-1],int) and (lista[-1]>=0):
            return AuxInvertir(lista[:-1],res+[lista[-1]])
        else:
            return AuxInvertir(lista[:-1],res)
