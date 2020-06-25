import numpy
caracteres=['!', ' " '[1], '#', '%', "'", '(', ')', '*', '+', '·', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\ '[0], ']', '^', '_', '{', '}', '~', 'ñ', 'Ñ', '¿', '¡', 'á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
abecedario=' ,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'.split(',') #ponemos un espacio vacio para que los letras empiecen en 1


tabla=[]
for i in range(-52,53):
  tabla.append([])
  for j in range(-52,53):
    tabla[i+52].append(((i)*(j)))
    if tabla[i+52][-1] <0:
      tabla[i+52][-1]= -53 + (tabla[i+52][-1]%53)
    else:
      tabla[i+52][-1]= tabla[i+52][-1]%53

print('Sistema de Encriptación de Longitud Determinada y Matriz.')
print('')
print('SELDYM es un sistema de encriptación de clave simétrica, con un cifrado de matriz en su algoritmo que hace que dos mensajes que se diferencien en una sola letra, al ser encriptados con la misma clave su resultado cambie por completo. Además la longitud del mensaje final es determinada por el usuario. El mensaje cifrado estará compuesto unicamente de letras minúsculas y mayúsculas del alfabeto inglés, pero el mensaje antes de cifrar y la contraseña pueden presentar esta serie de caracteres '+ "".join(caracteres))
print('')

while 1==1:
  print('')
  print('')
  print("Escriba 'e' para encriptar un mensaje y 'd' para desencriptarlo.")
  ed=input()
  if ed=='e':
    mensaje=[]
    for i in input('Escribe el mensaje que deseas cifrar: '):
      mensaje.append(caracteres.index(i)-52)
    clave=[]
    for i in input('Escribe la contraseña que deseas emplear para cifrarlo: '):
      clave.append(caracteres.index(i)-52)
    largominimo=len(str(len(mensaje)*52))*len(mensaje) + 1 + len(str(len(mensaje)))
    print("Tu mensaje final puede ocupar entre "+str(largominimo)+" e infinitos caracteres.")
    largo=int(input("Elige el largo de tu mensaje encriptado: "))
    print('')
    if largo < largominimo:
      largo=largominimo
    z=0
    for i in range(len(clave)):
      z+=clave[i]
      if clave[i]<0:
        clave[i]= 0 -clave[i]
    if z%2==0:
      z=-1
    else:
      z=1
    ternario4cifras=[]
    for i in range(len(clave)):
      ternario4cifras.append('')
      for j in range(4):
        ternario4cifras[i]+=str(clave[i]//(3**(3-j)))
        clave[i]-= (clave[i]//(3**(3-j)))*(3**(3-j))

    primeraclave=[]
    clave1=False
    segundaclave=[]
    clave2=False
    terceraclave=[]
    clave3=False

    ternarioadecimal=lambda x: int(x[0])*9 + int(x[1])*3 + int(x[2])

    while clave1==False or clave2==False or clave3==False:
      ternariosecuencia=""
      for i in ternario4cifras:
        ternariosecuencia+=i
      del ternario4cifras
      while len(ternariosecuencia)%3 != 0:
        ternariosecuencia+='0'
        
      if len(ternariosecuencia)>len(mensaje)**2 and clave1==False:
        del primeraclave
        primeraclave=[]
        for i in ternariosecuencia:
          if i=='0':
            primeraclave.append(z)
          elif i=='1':
            primeraclave.append(0-z)
          else:
            primeraclave.append(0)
        m1=0
        while m1 <= len(primeraclave)-(len(mensaje)**2) and clave1==False:
          m2=[]
          m3=[]
          for i in range(len(mensaje)):
            m2.append([])
            m3.append(0)
            for j in range(len(mensaje)):
              m2[i].append(primeraclave[m1+(i*len(mensaje))+j])
            for j in range(len(mensaje)):
              m3[i]+=m2[i][j]*(j+1)
          m4=numpy.array(m2)
          m5=numpy.array(m3)
          try:
            m6=numpy.linalg.solve(m2,m3)
            primeraclave=primeraclave[m1:m1+(len(mensaje)**2)]
            clave1=True
          except:
            if m1== len(primeraclave)-(len(mensaje)**2):
              m1+=1
            else:
              m1+=1
          del m2
          del m3
          del m4
          del m5
      ternario3cifras=[]
      for i in range(len(ternariosecuencia)//3):
        ternario3cifras.append('')
        for j in range(3):
          ternario3cifras[i]+=ternariosecuencia[3*i+j]
      del ternariosecuencia
            
      if len(ternario3cifras)>=21 and clave2==False:
        clave2=True
        for i in range(21):
          b=ternarioadecimal(ternario3cifras[i])
          while b in segundaclave:
            b+=1
          segundaclave.append(b)
        del b
        for i in range(21):
          segundaclave[i]=abecedario[segundaclave[i]+1]
                
      if len(ternario3cifras)>largo and clave3==False:
        clave3=True
        for i in range(largo):
          terceraclave.append(ternarioadecimal(ternario3cifras[i])+1)
            
      ternario4cifras=[]
            
      for i in ternario3cifras:
        if i[2]!='0':
          ternario4cifras.append('1'+i[0]+i[1]+str(int(i[2])-1))
        elif i[1]!='0':
          ternario4cifras.append('1'+i[0]+str(int(i[1])-1)+'2')
        elif i[0]!='0':
          ternario4cifras.append('1'+str(int(i[0])-1)+'22')
        else:
          ternario4cifras.append('0222')
            
    del ternario3cifras

    segundomensaje=[]
    for i in range(len(mensaje)):
      segundomensaje.append(tabla[mensaje[i]+52][terceraclave[i]+52])
    sumatorios=[]
    for i in range(len(mensaje)):
      sumatorios.append(0)
      for j in range(len(mensaje)):
        sumatorios[i] += primeraclave[len(mensaje)*i+j] * segundomensaje[j]

    cifras=[]
    a=largo - 1 - len(str(len(mensaje)))
    for i in range(len(mensaje)):
      cifras.append(a//(len(mensaje)-i))
      a-=cifras[i]

    del a

    numerosalargados=[]

    for i in range(len(mensaje)):
      numerosalargados.append(sumatorios[i]* ((int('9'*cifras[i]))//(52*len(mensaje))))

    secuencia=''
    for i in numerosalargados:
      i=str(i)
      if '-' not in i:
        while len(i)<cifras[numerosalargados.index(int(i))]:
          i='0'+i
        for j in i:
          secuencia+=segundaclave[int(j)]
      else:
        i=i[1:]
        while len(i)<cifras[numerosalargados.index(0-int(i))]:
          i='0'+i
        for j in i:
          secuencia+=segundaclave[int(j)+10]

    secuencia += segundaclave[20]
    for i in str(len(mensaje)):
      secuencia+=segundaclave[int(i)]
    resultado=''
    for i in range(largo):
      resultado+=abecedario[tabla[abecedario.index(secuencia[i])+52][terceraclave[i]+52]]
    print(resultado)


  elif ed=='d':
    mensaje=[]
    for i in input('Inserte el mensaje cifrado: '):
      mensaje.append(abecedario.index(i))

    clave=[]
    for i in input('Inserte la clave con la que se ha cifrado el mensaje: '):
      clave.append(caracteres.index(i)-52)

    largo=len(mensaje)

    z=0
    for i in range(len(clave)):
      z+=clave[i]
      if clave[i]<0:
        clave[i]= 0-clave[i]
    if z%2==0:
      z=-1
    else:
      z=1

    ternario4cifras=[]

    for i in range(len(clave)):
      ternario4cifras.append('')
      for j in range(4):
        ternario4cifras[i]+=str(clave[i]//(3**(3-j)))
        clave[i]-= (clave[i]//(3**(3-j)))*(3**(3-j))

    claveenternario=ternario4cifras

    primeraclave=[]
    clave1=False
    segundaclave=[]
    clave2=False
    terceraclave=[]
    clave3=False

    ternarioadecimal=lambda x: int(x[0])*9 + int(x[1])*3 + int(x[2])

    while clave2==False or clave3==False:
        #aun no sabemos el largo del mensaje original,asi que no podemos saber la clave 1
        ternariosecuencia=""
        for i in ternario4cifras:
          ternariosecuencia+=i
        del ternario4cifras
              
        while len(ternariosecuencia)%3 != 0:
          ternariosecuencia+='0'
                  
        ternario3cifras=[]
              
        for i in range(len(ternariosecuencia)//3):
          ternario3cifras.append('')
          for j in range(3):
            ternario3cifras[i]+=ternariosecuencia[3*i+j]
              
        del ternariosecuencia
              
              
        if len(ternario3cifras)>=21 and clave2==False:
          clave2=True
          for i in range(21):
            b=ternarioadecimal(ternario3cifras[i])
            while b in segundaclave:
              b+=1
            segundaclave.append(b)
          del b
          for i in range(21):
            segundaclave[i]=abecedario[segundaclave[i]+1]
                  
        if len(ternario3cifras)>largo and clave3==False:
          clave3=True
          for i in range(largo):
            terceraclave.append(ternarioadecimal(ternario3cifras[i])+1)
              
        ternario4cifras=[]
              
        for i in ternario3cifras:
          if i[2]!='0':
            ternario4cifras.append('1'+i[0]+i[1]+str(int(i[2])-1))
          elif i[1]!='0':
            ternario4cifras.append('1'+i[0]+str(int(i[1])-1)+'2')
          elif i[0]!='0':
            ternario4cifras.append('1'+str(int(i[0])-1)+'22')
          else:
            ternario4cifras.append('0222')
              
        del ternario3cifras
              


    secuencia=''
    for i in range(largo):
      secuencia+=abecedario[tabla[terceraclave[i]+52].index(mensaje[i])-52]
    cifras=[]
    a=largo -1 -len(secuencia.split(segundaclave[20])[1])

    c=''
    for i in secuencia.split(segundaclave[20])[1]:
      c+=str(segundaclave.index(i))

    for i in range(int(c)):
      cifras.append(a//(int(c)-i))
      a-=cifras[i]
    del a
    matriz=[]
    b=0
    for i in range(len(cifras)):
      matriz.append('')
      if segundaclave.index(secuencia[b])<10:
        for j in range(cifras[i]):
          matriz[i]+=str(segundaclave.index(secuencia[b+j]))
        b+=cifras[i]
      else:
        matriz[i]+='-'
        for j in range(cifras[i]):
          matriz[i]+=str(segundaclave.index(secuencia[b+j])-10)
        b+=cifras[i]
      matriz[i]=int(matriz[i])

    for i in range(len(cifras)):
      matriz[i] = (matriz[i] // ((int('9'*cifras[i]))//(52*len(cifras))))

    ternario4cifras=claveenternario

    while clave1==False:
        ternariosecuencia=""
        for i in ternario4cifras:
            ternariosecuencia+=i
        del ternario4cifras
              
        while len(ternariosecuencia)%3 != 0:
            ternariosecuencia+='0'
              
        if len(ternariosecuencia)>len(cifras)**2 and clave1==False:
          del primeraclave
          primeraclave=[]
          for i in ternariosecuencia:
              if i=='0':
                  primeraclave.append(z)
              elif i=='1':
                   primeraclave.append(0-z)
              else:
                  primeraclave.append(0)
          m1=0
          while m1 <= len(primeraclave)-(len(cifras)**2) and clave1==False:
            m2=[]
            m3=[]
            for i in range(len(cifras)):
              m2.append([])
              m3.append(0)
              for j in range(len(cifras)):
                m2[i].append(primeraclave[m1+(i*len(cifras))+j])
              for j in range(len(cifras)):
                m3[i]+=m2[i][j]*(j+1)
            m4=numpy.array(m2)
            m5=numpy.array(m3)
            try:
              m6=numpy.linalg.solve(m2,m3)
              primeraclave=primeraclave[m1:m1+(len(cifras)**2)]
              clave1=True
            except:
              if m1== len(primeraclave)-(len(cifras)**2):
                m1+=1
              else:
                m1+=1
            del m2
            del m3
            del m4
            del m5
              
        ternario3cifras=[]
              
        for i in range(len(ternariosecuencia)//3):
          ternario3cifras.append('')
          for j in range(3):
            ternario3cifras[i]+=ternariosecuencia[3*i+j]
              
        del ternariosecuencia
              
        ternario4cifras=[]
              
        for i in ternario3cifras:
          if i[2]!='0':
            ternario4cifras.append('1'+i[0]+i[1]+str(int(i[2])-1))
          elif i[1]!='0':
            ternario4cifras.append('1'+i[0]+str(int(i[1])-1)+'2')
          elif i[0]!='0':
            ternario4cifras.append('1'+str(int(i[0])-1)+'22')
          else:
            ternario4cifras.append('0222')
              
        del ternario3cifras
          
    matrizprimeraclave=[]
    for i in range(len(cifras)):
      matrizprimeraclave.append([])
      for j in range(len(cifras)):
        matrizprimeraclave[i].append(primeraclave[j+(i*len(cifras))])
    x=numpy.array(matrizprimeraclave)
    y=numpy.array(matriz)
    incognitas=numpy.linalg.solve(x,y)

    mensajedescifrado=''
    for i in range(len(cifras)):
      mensajedescifrado+=caracteres[tabla[terceraclave[i]+52].index(round(incognitas[i]))]
    print(mensajedescifrado)

  else:
    break
