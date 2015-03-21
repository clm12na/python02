fichero = open('pokemon') #Abrimos el fichero que contiene los nombres de los pokemon
#lo primero que haremos sera convertir dicho fichero en una lista
Pokemon_List = fichero.read().split() #con esta funcion se separa el elemento de la lista cada vez que encuentra un espacio, asi lo almacenaremos por palabras

AuxList = [] 
Final_List = []

for elemento in Pokemon_List: #vamos a recorrer toda la lista para que se utilice como primera palabra de la cadena todas y cada una de las alabras del texto
    AuxList.append(elemento) #introducimos la siguiente palabra del fichero para formar una nueva lista auxiliar a partir e ella
    i=0
    while i < len(Pokemon_List): 
        if(Pokemon_List[i] not in AuxList and AuxList[-1][-1]==Pokemon_List[i][0]): #comprobamos que la parabra no este ya en la lista para no repetir y si coninciden la ultima letra con la primera
            AuxList.append(Pokemon_List[i]) #introducimos la palabra en la lista auxiliar
            i=0 #ponemos i a 0 para volver a recorrer toda la lista
        else:
            i=i+1
    if (len(Final_List)<len(AuxList)):
        #si la lista auxiliar actual es mayor que la final, copiamos la auxiliar
        Final_List=AuxList  
    AuxList=[] #borramos la lista auxiliar para empezar de nuevo

print (Final_List)
print "Numero de palabras que coinciden: ",len(Final_List)