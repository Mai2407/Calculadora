import math

print("Hola")

print(""" 
1- Sumar
2- Restar
3- Multiplicar
4- Dividir
""")

peticion = input("Que quiere realiza ?").lower()

#Suma
if peticion == "sumar" or "1":

      a = float(input("Introduce el primer valor: "))

      b = float(input("Introduce el segundo valor: "))

      d = a + b 

      print(d)

      porciento = input("Desea sacar el 18 '%' del resultado de la suma? [Si/No] ").lower()

      if porciento == "si":

          porciento = d * 0.18 

          print(porciento, "Gracias por utilizar!!!")


      elif porciento == "no":    

           print(""" De acuerdo
           
           Gracias por utilizar!!! """) 
           

      else:
           print("Opción no válida")  


#Resta
elif peticion == "resta" or "2":
     
     a = float(input("Introduce el primer valor: "))

     b = float(input("Introduce el segundo valor: "))

     d = a + b 

     print(d, "Gracias por utilizar!!!")

#Multiplicar
elif peticion == "multiplicar" or "3":

       a = float(input("Introduce el primer valor: "))

       b = float(input("Introduce el segundo valor: "))

       d = a + b 

       print(d)

       raiz_Cuadrada = input("Desea sacar la raíz cuadrada del resultado de la multiplicación? [Si/No] ").lower()

       if raiz_Cuadrada == "si":  

           print(math.sqrt(d), "Gracias por utilizar!!!")


       elif raiz_Cuadrada == "no":    

           print(""" De acuerdo
           
           Gracias por utilizar!!! """) 


       else:

           print("Opción no válida")  

#Dividir
elif peticion == "dividir" or "4":

     a = float(input("Introduce el primer valor: "))

     b = float(input("Introduce el segundo valor: "))

     d = a / b

     print(d, "Gracias por utilizar!!!") 


else:

    print("Opción no válida")                
