#Partir lista en pares e impares y que se ordenen ascendentemente

def partirParImpar(lista1,lista2):
    if isinstance(lista1,list) and isinstance(lista2,list):
        return partirAux(lista1,lista2,[],[],[])
    else:
        print("Error en parámmetros de entrada")
def partirAux(lista1,lista2,pares,impares,res):
    if lista1==[] and lista2==[]:
        return res+[ordenarLista(pares)]+[ordenarLista(impares)]
    else:
        if lista1[0]%2==0 and lista2[0]%2==0:
            return partirAux(lista1[1:],lista2[1:],pares+[lista1[0]]+[lista2[0]],impares,res)
        if lista1[0]%2!=0 and lista2[0]%2!=0:
            return partirAux(lista1[1:],lista2[1:],pares,impares+[lista1[0]]+[lista2[0]],res)
        if lista1[0]%2!=0 and lista2[0]%2==0:
            return partirAux(lista1[1:],lista2[1:],pares+[lista2[0]],impares+[lista1[0]],res)
        else:
            return partirAux(lista1[1:],lista2[1:],pares+[lista1[0]],impares+[lista2[0]],res)

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



        
            
