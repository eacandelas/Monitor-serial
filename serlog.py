import time
import serial

# Inicializacion de variables
rx = 0
rxBuf =""
datos = 0
lecturas = 0

#Puerto serial a utilizar
numPuerto = ''

#datos para la cracion del archivo
rutaArchivo = ""
identificador = ""

#Creacion de puerto
puerto = serial.Serial(numPuerto, 9600)

print ("\nInicio \n")

# Se mantiene el programa corriendo siempre
while 1:
  
	#Si hay datos en el buffer de entrada recibe linea por linea en rx
	#Se guarda en la variable rxBuff
	while puerto.inWaiting() > 0:
		rx = puerto.readline()
		#print (rx)
		rxBuf += str(rx) + "\n" 
		if datos == 0:
			print ("Recibiendo datos")
			datos = 1

	#Espera para recibir mas datos
	time.sleep(0.1)
	
	#SI no hay datos en buffer y acaba de salir del while
	if (puerto.inWaiting() == 0) and (datos == 1)  :
		
		lecturas += 1
		
		#Desplegamos la infor en pantalla
		print (rxBuf)
		print("---------------")
		print("Lecturas: " + str(lecturas) + "-" + time.strftime("%H:%M:%S", time.localtime()))
		print("---------------")

		#creamos la estructura del archivo.
		fecha = time.strftime("%m%d%y", time.localtime())
		nombreArchivo = RutaArchivo + identificador + '-' + fecha
		
		#creamos el archivo
		#al cambiar el dia se creara un archivo nuevo 
		archivo = open(nombreArchivo, "a")
		archivo.write(rxBuf)
		archivo.write("---------------")	
		archivo.write("Lecturas:" + str(lecturas) + " - " + time.strftime("%H:%M:%S", time.localtime()))
		archivo.write("---------------")
		archivo.write("\n")
		archivo.close()

		rxBuf = ""

		datos = 0
