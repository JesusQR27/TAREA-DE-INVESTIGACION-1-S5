class TratamientoListas():
    
    def __init__(self,lista):
        self.lista=lista
        
#

    def PresentarLista(self):
        print("Recorrer y presentar los datos de una lista")
        for list in self.lista:
            print(list,end='   ')
        print() 

#
    def buscarLista(self,buscado):
        print("Buscar un valor en una lista")
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele==buscado:
                enc=True
                break
        if enc==True:
           print("Su valor si se encuentra en la lista, se encuentra en la posicion: {}".format(pos+1))
        else:
            print("Su valor no se encuentra en la lista")

#
    
    def ListaFactorial(self):
        print("Retornar una lista con los factoriales")
        for pos,i in enumerate(self.lista): 
            if i >= 0:
                acu=1
                for num in range(i,1,-1):
                    acu =acu*num
                print("numero:  {}  ,Factorial:  {} ".format(i,acu))
        print()           

  
#   
    def listaPrimo(self):
        print("Retornar la lista de números primos")
        listaprimo=[]
        for pos,i in enumerate(self.lista): 
            if i >= 0:
                primo=True
                divisor=2
                while divisor < i and primo ==True :
                    Res= i%divisor
                    if Res == 0:
                        primo+=1
                    divisor+=1
                if primo ==True:
                    listaprimo.append(i)
            else:
                print("Su nmumero es negativo ")
        print()
        print("lista de numeros Primos: ")    
        print(listaprimo)

        

#  
    
    def listaNotas(self,listaNotasDicccionario):
        print("Recorrer una lista de diccionario con notas de alumnos")
        for nom in listaNotasDicccionario:
            for clave,valor in nom.items():
                print(clave,":",valor,end="  ")
            print()

#  
    
    def insertarLista(self,valor,posicion):
        print("Inserte un dato en una Lista dada la Posición")
        print()
        auxlista=[]        
        for pos,ele in enumerate(self.lista):
            if valor < ele:
                break
        for i in range(posicion):
            auxlista.append(self.lista[i])
        auxlista.append(valor)

        for j in range(posicion,len(self.lista)):
            auxlista.append(self.lista[j])
        self.lista=auxlista
        return self.lista

#  
    
    def eliminarLista(self,lista):
        print("Elimine todas las ocurrencias en una Lista")
        print()
        lista2 = {}
        for i in lista:
            if i in lista2:
                lista2[i] += 1
            else:
                lista2[i] = 1 
        print("Quedan los siguiente:",lista2)
        print("En total son {} elementos sin contar las repeticiones".format(len(lista2)))
        lista3 = []        
        for clave, valor in enumerate(lista2):
            lista3.append(valor)
        return (lista3)   

        
#  
    
    def retornaValorLista(self,lista):
        print(" Retorne cualquier valor de una lista eliminándolo ")
        print()
        n=int(input("Que valor desea  eliminar: "))      
        for x,i in enumerate(lista):
            if i == n:
                del lista[x]  
        return (lista)
#   
    def copiarTuplaLista(self):
        print(" Copiar cada elemento de una tupla en una lista ")
        aux1=list(self.lista)
        return aux1      

#  
    
    def vueltoLista(self,listaClientesDiccionario):
        print(" entregar el vuelto a varios clientes ")
        pago=float(input("Ingrese  el pago del cliente: "))
        nom=(input("Ingrese el  nombre del cliente: ")).capitalize()
        print(nom)
        for x in listaClientesDiccionario:
            for clave, valor in x.items():     
                if clave == nom:
                    if valor > 0:
                        cambio=pago-valor
                        print(cambio)
                    else:
                        cambio=pago
        if cambio <= -1:                
            print(" EL mantiene una deuda de:",cambio,"$ con nosotros")
        else:
            print("el  cambio es: ",cambio, "$ no tiene deuda con nosotros")  
#  
 

# lista=[1,2,3,4,5]
lista=(22,23,24,25)
listaClientesDiccionarios=[{'Josue':100},{'Maria':80},{'Ruth':50}]
ord1= TratamientoListas(lista)
#orde1.PresentarLista()
#orde1.buscarLista(40)
# orde1.ListaFactorial()
#orde1.listaPrimo()
# orde1.listaNotas(listaClientesDiccionarios)
# print(orde1.insertarLista(400,5))
# print()
# lista1 = []       
# num = int(input("Cuantos elementos desea en su lista?: "))
# for x in range(num):
#     valor = int(input("Ingrese el elemento:")) 
#     lista1.append(valor)
# auxi=lista1
# print(ord1.eliminarLista(aux))
# lista2 = []       
# num = int(input("Cuantos elementos desea en su lista?: "))
# for x in range(num):
#     valor = int(input("Ingrese un elemento:")) 
#     lista2.append(valor)
# auxi=lista2
# print(orde1.retornaValorLista(auxi))
# print(orde1.copiarTuplaLista())
diccionario={}
lista=[]
num=int(input("ingrese los diccionarios desea ingresar: "))
for x in range(num):
    clave=(input("ingrese la clave para el diccionario: ")).capitalize()
    valor=int(input("ingrese el valor de  clave para el diccionario: "))

    diccionario[clave]=valor
    lista.append(diccionario)
    diccionario={} 
ord1.vueltoLista(lista)