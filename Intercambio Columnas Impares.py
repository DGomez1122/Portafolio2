#Intercambiar Columnas Impares

        
def largo(lista):
    if isinstance(lista,list) and (lista!=[]):
        return Auxlargo(lista,0)
    else:
        print("Error en parámetros de entrada")
def Auxlargo(lista,cont):
    if lista==[]:
        return cont
    else:
        return Auxlargo(lista[1:],cont+1)

def Intercambio_columnas_impares(matriz):
    if isinstance(matriz,list):
        if largo(matriz)==largo(matriz[0]):
            mitad=largo(matriz[0])//2
            return AuxIntercambio(matriz,0,0,mitad)
        else:
            return ("Error en tamaño de la matriz")
    else:
        return("Error en parámetros de entrada")
def AuxIntercambio(m,i,j,mitad):
    if i==mitad:
        return m
    elif j==largo(m[0]):
        return AuxIntercambio(m,i+1,0,mitad)
    elif j%2!=0:
        temp=m[i+mitad][j]
        m[i+mitad][j]=m[i][j]
        m[i][j]=temp
        return AuxIntercambio(m,i,j+1,mitad)
    else:
        return AuxIntercambio(m,i,j+1,mitad)
        

    
    
    
