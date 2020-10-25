#Lista Capicua

def listaCapicua(lista):
    if isinstance(lista,list) and (lista!=[]):
        return AuxCapicua(lista)
    else:
        print("Debe ingresar una lista y no puede estar vacía")

def AuxCapicua(lista):
    print(lista)
    print(invertirLista(lista))
    if lista==(invertirLista(lista)):
        print("Es capicua")
    elif lista!=(invertirLista(lista)):
        print("No es capicua")
    else:
        return AuxCapicua(lista)
###########################################

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
