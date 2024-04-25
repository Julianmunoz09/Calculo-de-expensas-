import sys
UVT = 47065
Cf = 10.1*UVT
Cv = 20.02*UVT
m = 0.938
metros_obra = float(input("ingrese el numero de metros cuadrados del proyecto : "))
Tipo_licencia = input("La licencia requerida es para parcelacion, urbanizacion o construccion (si o no) : ")
if Tipo_licencia == "no":
    Tipo_licencia_2 = input("Su licencia es de subdivisión en la modalidad de reloteo (si o no) : ")
    if Tipo_licencia_2 == "si":
        if 0 < metros_obra and  metros_obra <= 1000:
            print("El costo directo de su licencia es $86.666 ")
            sys.exit()
        elif 1001 <= metros_obra and  metros_obra <= 5000:
            print("El costo directo de su licencia es $650.000 ")
            sys.exit()
        elif 5001 <= metros_obra and  metros_obra <= 10000:
            print("El costo directo de su licencia es $1'300.000 ")
            sys.exit()
        elif 10001 <= metros_obra and  metros_obra <= 20000:
            print("El costo directo de su licencia es $1'950.000 ")
            sys.exit()
        else:
            print("El costo directo de su licencia es $2'600.000 ")
            sys.exit()
Tipo_licencia_3 = input("Ingrese que tipo de licencia necesita (parcelacion, urbanizacion o construccion) : ")
Tipo_Proyecto = input("Ingrese el tipo de uso que se le dara al suelo (vivienda, institucional, comercial o industrial) : ")
#Calculo factor i
i = 0
if Tipo_Proyecto == "vivienda":
    estrato = int(input("Ingrese el estrato al cual pertenece la vivienda : "))
    if estrato == 1:
        i = 0.5
    elif estrato == 2:
        i = 0.5
    elif estrato == 3:
        i = 1
    elif estrato == 4:
        i = 1.5
    elif estrato == 5:
        i = 2
    else:
        i = 2.5
else:
    if 1 <= metros_obra and  metros_obra <= 300:
        i = 2.9
    elif 301 <= metros_obra and  metros_obra <= 1000:
        i = 3.2
    else:
        i = 4
#Calculo factor j
j = 0
if Tipo_licencia_3 == "construccion" and metros_obra <= 100:
    j = 0.45
elif Tipo_licencia_3 == "construccion" and 100 < metros_obra and  metros_obra <= 11000:
    j = (3.8)/(0.12+(800/metros_obra))
elif Tipo_licencia_3 == "construccion" and 11000 < metros_obra:
    j = (2.2)/(0.018+(800/metros_obra))
elif Tipo_licencia_3 == "urbanizacion" or Tipo_licencia == "parcelacion" :
    j = (4)/(0.025+(2000/metros_obra))
E = (Cf*i*m)+(Cv*i*j*m)
print("El costo directo de su licencia mas IVA es $",E+(E*0.19))
