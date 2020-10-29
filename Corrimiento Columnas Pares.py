#Corrimiento Columnas Pares

        
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

def corrimiento1_columnas_pares(matriz):
    if isinstance(matriz,list):
        if len(matriz)==largo(matriz[0]):
            cantidad_pares=largo(matriz[0])//2
            return Auxcorrimiento1_columnas_pares(matriz,0,0)
        else:
            return ("Error en tamaño de la matriz")
    else:
        return("Error en parámetros de entrada")
def Auxcorrimiento1_columnas_pares(matriz,i,j):
    if i == largo(matriz)-1:
        return matriz
    if j == largo(matriz):
        return Auxcorrimiento1_columnas_pares(matriz,i+1,0)
    if j % 2 == 0:
        temp=matriz[-i+1][j]
        matriz[-i+1][j]=matriz[-i][j]
        matriz[-i][j]=temp
        return Auxcorrimiento1_columnas_pares(matriz,i,j+2)
    else:
        return Auxcorrimiento1_columnas_pares(matriz,i,j+1)





















    
        

    
    
    
