###############################################################################################################
"""
ROBLES PADILLA OSWALDO  16590592
PALOMA VICTORIANO ARAEL 16590505

Combinaciones <Comprensión de listas> 30pts

	Una tienda de ropa quiere saber cuantos conjuntos se pueden crear 
	a partir de un grupo de 5 camisas (roja,negra,azul,morada y cafe),      
	4 pantalones (negro, azul, cafe obscuro y crema) y uno de 4 accesorios
	posibles (cinturon, tirantes, lentes, fedora)
	
	1) Obtenga una lista con todos los conjuntos posibles e imprimala en pantalla
	2) imprima un mensaje donde mencione la cantidad de conjuntos posibles
	
"""
C=['ROJA','NEGRA','AZUL','MORADA','CAFE']
P=['NEGRO','AZUL','CAFE','OBSCURO','CREMA']
A=['CINTURON','TIRANTES', 'LENTES', 'FEDORA']

print([(x,y,z) for x in C for y in P for z in A if x ==y or x!=y])
R=[(x, y, z) for x in C for y in P for z in A if x == y or x!=y]
print("el numero total de  combinaciones posibles es")
print(len(R))
#####################################################################################################################
"""
ROBLES PADILLA OSWALDO  16590592
PALOMA VICTORIANO ARAEL 16590505
 
¿Fedora?  <Comprensión de listas >  15 pts

	Del problema anterior imprima una lista que tenga todos los conjuntos
	que incluyen un sombrero fedora y tambien despliegue su longitud
	
	
"""
C=['ROJA','NEGRA','AZUL','MORADA','CAFE']
P=['NEGRO','AZUL','CAFE','OBSCURO','CREMA']
A=['FEDORA']

print([(x,y,z) for x in C for y in P for z in A  if x == y or x!=y])
R=[(x, y, z) for x in C for y in P for z in A if x == y or x!=y]



print("el numero de combinaciones posibles es")
print(len(R))
#####################################################################################################################
"""
ROBLES PADILLA OSWALDO  16590592
PALOMA VICTORIANO ARAEL 16590505
Bada Boom!!! <generadores> 20 pts
	
	Defina un generador que reciba un numero entero positivo mayor a 0 N,
	dicho generador proporciona numero de 1 hasta N
	con las siguientes condiciones:
		1) si es multiplo de 3 coloque la cadena "Bada"
		2) si es multiplo de 5 coloque la cadena "Boom!!"
		3) si es multiplo de 3 y 5 coloque "Bada Boom!!"
		
	def genBadaBoom(N):
		pass
		
	a = genBadaBoom(10)
	z = [e for e in a]
	print(z)
	#[1,2,"Bada",4,"Boom","Bada",7,8,"Bada","Boom"]
"""
def genBadaBoom(N):
	i=1
	while i<N:
		if i%3 ==0 and i%5==0:
			yield "Bada Boom!!"
		elif i%3==0:
			yield "Bada"
		elif i%5==0:
			yield "Boom"
		else:
			yield i
		i = i + 1

a = genBadaBoom(31)
z = [e for e in a]
print(z)
#####################################################################################################################
"""
ROBLES PADILLA OSWALDO  16590592
PALOMA VICTORIANO ARAEL 16590505

 Primos  <generadores>  30 pts

	Realice una generador que devuelva  de todos lo numeros primos
	existentes de 0 hasta n-1 que cumpla con el siguiente prototipo:
	
	def gprimo(N):
		pass
	
	
	a = gprimo(10)
	z = [e for e in a]
	print(z)
	# [2, 3 ,5 ,7 ]
"""
def geprimo(M):
	j=1
	i=1
	c=0
	while i<(M+1):
		while j<(M+1):
			if i%j==0:
				c=c+1
			j=j+1
		if c == 2:
			yield i
		c=0
		i=i+1
		j=1
a=[z for z in geprimo(20)]
print("los numeros primos son : ")
print(a)
