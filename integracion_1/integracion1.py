    #------1------
def mcd(numA,numB):
    """Prints and returns mcd between numA and numB"""
    if numA < numB:
        greater = numB
    else:
        greater = numA

    for num in range(1,greater+1):   #
        if (numA % num) == 0 and (numB % num) == 0:
            res = num

    print(res)
    return res      #return res but not use it

#num1 = int(input("Ingrese el primer n°: "))
#num2 = int(input("Ingrese el segundo n°: "))
#mcd(num1,num2)



    #------2------
def mcm(numA,numB):
    """Prints and returns mcm between numA and numB"""
    if numA < numB:
        greater = numB
    else:
        greater = numA

    for num in range(greater,numA*numB +1):   #worst case mcm is the parameters multiplication
        if (num % numA) == 0 and (num % numB) == 0:
            res = num
            break      #can use return too

    print(res)
    return res      

#num1 = int(input("Enter first n°: "))
#num2 = int(input("Enter second n°: "))
#mcm(num1,num2)



    #------3/4------
def contar_palabras(cadena) -> dict:
    dic_palabras_frecuencia = dict()
    cadena_dividida = cadena.split()            #me lo divide en palabras individuales
    cadena_set = set(cadena_dividida)
    for palabra in cadena_set:
        frecuencia = cadena_dividida.count(palabra)
        dic_palabras_frecuencia.update({palabra: frecuencia})
    
    return dic_palabras_frecuencia

def mas_frecuente(diccionario) -> str:
    frecuencia = 0
    palabra_frecuente = ""
    for palabra in diccionario:
        if diccionario.get(palabra) > frecuencia:
            palabra_frecuente = palabra
            frecuencia = diccionario.get(palabra)
    
    print(f"La palabra más frecuente es '{palabra_frecuente}' con {frecuencia} apariciones")

#diccionario = contar_palabras(input("Ingrese el texto a contar: "))
#print(diccionario)
#mas_frecuente(diccionario)


    #------5------
def get_int():
    while True:
        try:
            num = int(input("Ingresa un n° entero: "))
            return num
        except ValueError:
            print("Error: el valor ingresado no es un entero válido")

def get_int2():
    try:
        num = int(input("Ingrese un n° entero: "))
        return num
    except ValueError:
        print("Error: el valor ingresado no es un entero válido")
        return get_int2()
    
#get_int()
#get_int2()

