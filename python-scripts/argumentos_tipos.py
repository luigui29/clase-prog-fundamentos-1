# Primer tipo: Argumentos posicionales
# Este tipo de argumento es el más común en Python, dictado por su posición.
def mi_primer_suma(num1, num2, num3):
    total = num1 + num2 + num3
    return print("Total de la primer suma: ", total)

mi_primer_suma(3, 4, 5)

# Segundo tipo: Argumentos de palabra clave (keywords)
# Son argumentos a los cuales le puedes dedicar un nombre específico.
# Siempre deben ir después del último argumento posicional.
def mi_segunda_suma(num1, num2, num3, mensaje):
    total = num1 + num2 + num3
    return print(mensaje, total)

mi_segunda_suma(1, 2, 3, mensaje="Total de la segunda suma: ")

# Tercer tipo: Argumentos arbitrarios (*args)
# Los *args le permiten a tu funcion aceptar cualquier numero de argumentos
# posicionales. Puedes llamar al argumento como gustes, pero si o si debes
# colocar un asterisco * antes del nombre.
def mi_tercera_suma(*nums):
    total = 0
    
    for num in nums: # El argumento arbitrario devuelve una tupla
        total += num
    
    return print("Total de la tercera suma: ", total)

mi_tercera_suma(1, 2, 3, 4, 5, 6)

# Cuarto tipo: Argumentos de palabra clave arbitrarios (**kwargs)
# De manera similar, si no sabes cuantos argumentos keyword necesita tu
# función, puedes declararlos como argumentos arbitrarios usando dos
# asteriscos.
def mi_cuarta_suma(**nums):
    total = 0
    
    for key, value in nums.items(): # El argumento devuelve un diccionario
        print(key, " = ", value)
        total += value
    
    return print("Total de la cuarta suma: ", total)

mi_cuarta_suma(num1=5, num2=3, num3=8)

# Es posible usar argumentos posicionales, *args y **kwargs en una misma
# función. Debes de seguir este orden: primero, argumentos posicionales;
# segundo, argumentos arbitrarios; de último, argumentos keyword
# arbitrarios.
def mi_ultima_funcion(a, b, *args, **kwargs):
    print("Numero de gatos = ", a)
    print("Numero de dueños = ", b)
    
    for arg in args:
        print("Gato = ", arg)
    
    for key, value in kwargs.items():
        print(key, " = ", value)

# También puedes pasar directamente tuplas y diccionarios como argumentos
# siempre y cuando los antecedas de asteriscos * y ** respectivamente
gatos = ["Atigrado", "Siamés", "Persa", "Esfinge"]
personas = {'Colombia':"Agatha", 'Venezuela':"Eric", 'Guatemala':"Liz"}

mi_ultima_funcion(4, 3, *gatos, **personas)