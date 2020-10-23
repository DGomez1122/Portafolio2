# Ordenar Lista Ascendente

def largoLista(lista):
    if isinstance(lista,list) and (lista!=[]):
        return AuxlargoLista(lista,0)
    else:
        print("Error")
def AuxlargoLista(lista,cont):
    if lista==[]:
        return cont
    else:
        return AuxlargoLista(lista[1:],cont+1)
        
def ordenarLista(lista):
    if isinstance(lista,list)and lista!=[]:
        return AuxOrdenar(lista,largoLista(lista),0,0)
    else:
        print("Error en parámetros de entrada")
def AuxOrdenar(lista,largo,c1,c2):
    if c2==largo:
        c1+=1
        c2=0
    if c1==largo:
        return lista
    if lista[c1]>lista[c2]:
        return AuxOrdenar(lista,largo,c1,c2+1)
    else:
        numMayor=lista[c2]
        lista[c2]=lista[c1]
        lista[c1]=numMayor
        return AuxOrdenar(lista,largo,c1,c2+1)

