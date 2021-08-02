class Cadena():
    def __init__(self,cadena):
        self.cadena=cadena

#
    def  recorrerCadena(self):
        print()
        print("Recorrer y presentar los datos de una cadena")
        print()
        for x in self.cadena:
            print(x,'',end='')
        
#
    def  buscarCaracter(self,buscado):
        print()
        print("Buscar un carácter en una cadena")
        print()
        acum=0
        for x,i in enumerate(self.cadena):
            if i== buscado:
                acum=acum+1
        print("Su caracter se encuentra {} veces, dentro de la cadena".format(acum))
        print()
#
      
        print("Retornar una lista con la posiciones dado un carácter de la cadena")
        print()
        acum=0
        aux=[]
        for x,i in enumerate(self.cadena):
            acum=acum+1
            if i == caracter:
                aux.append(acum)
                lista=aux
        print(lista)        
                
#
    def listaPalabras(self):
        pass
#
    def cadenaLista(self):
        pass
#
    def insertarDato(self,buscado,posicion):
        pass
#
    def eliminarOcurrencias(buscado):
        pass
#
    def retornaValor(posicion):
        pass
#
    def concatenarCadena(dato):
        pass
#

cadena='hola mundo como esta el futuro de la patria '
cad= Cadena(cadena)
cad.listaPosiciones('p')