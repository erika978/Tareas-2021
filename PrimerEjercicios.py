def bonoDocente():
  #definir Variables
  bonoObtenido=0.0
  #Datos de Entrada
  salarioMinimo=float(input("ingrese el salario minimo:"))
  puntuacionObtenida=float(input("Ingrese la puntuacion que ha obtenido:"))
  #Proceso
  if puntuacionObtenida<=100 and puntuacionObtenida>=0:
    bonoObtenido=salarioMinimo
  elif puntuacionObtenida >=101 and puntuacionObtenida<=150:
    bonoObtenido=salarioMinimo*2
  elif puntuacionObtenida>150:
    bonoObtenido=salarioMinimo*3   
  # Datos de salida
  print("El docente obtendra un bono de:", bonoObtenido )
def paquetes():
  #Definir Variables
  resulpaquete="" 
  #Datos de Entrada
  montoRvDic=float(input("Ingrese el monto que recibe en diciembre:"))
  #Proceso
  if montoRvDic>=50000:
    resultPaquete="Paquete A"
  elif montoRvDic>=20000 and montoRvDic<50000:
    resultPaquete="Paquete B"
  elif montoRvDic>=10000 and montoRvDic<20000:
    resultPaquete="paquete C"
  else:
    resultPaquete="paquete D"
  #Datos de salida
  print("la persona comprara el:", resultPaquete)


#bonoDocente() 
#paquetes()