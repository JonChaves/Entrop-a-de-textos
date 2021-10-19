import numpy as np
import matplotlib.pyplot as plt

def entropia1(inputfile):
  with open(inputfile, "r") as file1:
    MD=file1.read()

#Usamos su posición decimal de unicode 
#para asignar su posición en el array
#aprovechando que las letras tienen valores contiguos (excepto el espacio)
  p_1 = np.zeros(27)
  for i in range (0,len(MD)):
      c = MD[i]
      resta = ord(c) - ord("a") #resta de los valores en unicode
      if (ord(c)== 32):         #caso especial del espacio
        p_1[26]=p_1[26]+1
      else:
        p_1[resta]=p_1[resta]+1
  
  p_1=p_1/len(MD)

  fig = plt.figure()
  ax = fig.add_axes([0,0,1,1])
  langs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','space'] 
  ax.bar(langs,p_1)
  plt.show()

  s1=0
  
#cálculo de la entropía
  for i in range (0,27):
    if (p_1[i]!=0):
      s1 = -p_1[i]*np.log2(p_1[i]) + s1
      
  return s1

def entropia2(inputfile):
  with open(inputfile, "r") as file1:
    MD=file1.read()

#Lo mismo que antes pero consideramos un array 2-D
  p_2 = np.zeros((27, 27))
  for i in range (0, len(MD)-1):
    c = MD[i]
    resta2 = ord(c) - ord("a")
    b = MD[i + 1]
    resta1 = ord(b) - ord("a")
    if (ord(c) == 32):
      if (ord(b) == 32):
        p_2[26, 26] = p_2[26, 26] + 1
      else:
        p_2[26, resta1] = p_2[26, resta1] + 1
    elif (ord(b) == 32):
      p_2[resta2, 26] = p_2[resta2, 26] + 1
    else:
      p_2[resta2, resta1] = p_2[resta2, resta1] + 1

  p_2 = p_2/(len(MD)-1)
  s22 = 0

#Primero calculamos la entropía de la diagonal
  for i in range(0, 27):
    if (p_2[i, i] != 0):
      s22 = - p_2[i, i] * np.log2(p_2[i, i]) + s22

#Sumamos las componentes que faltan
  for i in range(0, 27):
    for j in range(0, 27):
      if (j == i):
        continue
      else:
        if (p_2[i, j] != 0):
          s22 = - p_2[i, j]*np.log2(p_2[i, j]) + s22
  return s22

def entropia3(inputfile):
  with open(inputfile, "r") as file1:
    MD=file1.read()
  #crear diccionario
  corr_3={}

  for i in range(0, len(MD)-2):
    a = MD[i]
    b = MD[i+1]
    c = MD[i+2]
    #crea un string con las tres letras
    key=a+b+c
    #chequea si la key existe
      #Si existe le sumamos 1 
      #Si no lo agregamos con valor 1
    if (corr_3.get(key) != None):
      corr_3[key] = corr_3.get(key)+1
    else:
      corr_3[key] = 1

  #Normalizacion
  for k, v in corr_3.items():
    corr_3[k]=v/(len(MD)-2)

  #Calculo de entropia
  s3=0
  for k, v in corr_3.items():
    s3=s3 - v*np.log2(v)
  return s3

