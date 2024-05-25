#Control Santiago Rivas (335103)

from os import system
system ("cls")

from datetime import datetime,date

#Definición de las estructuras
lista_alumnos = [["276423", "Ana", "Gomez","Contador Público"],["335103", "Santiago", "Rivas","Licenciatura en Economía"]]
lista_libros = [["3421", "Adam Smith","La Riqueza de las Naciones","Licenciatura en Economía"],["5617", "Jesús Omeñaca","Contabilidad General","Contador Público"]]
lista_prestamos = [["276423", "La lógica contable",date(2024,2,12),date(2024,5,13)],["335103", "Del oro al Bitcoin",date(2024,3,27),date(2024,8,3)]]

def mostrar_menu():
    #Despliega el menú de opciones
    print("Menú")
    print("1. Registrar alumno")
    print("2. Registrar nuevo libro")
    print("3. Registrar nuevo préstamo")
    print("4. Libros disponibles en la biblioteca")
    print("5. Libros disponibles por esudiante")
    print("6. Libros prestados por estudiante")
    print("0. Salir")

def seleccionar_opcion():
    #Permite seleccionar una opción en el menú                                 
    opcion = int(input("Ingrese una opción: "))
    while opcion not in [0,1,2,3,4,5,6]: #Mientras no se digite una opción dentro la lista no sigue el proceso
        print("La opción ingresada no es válida.")
        opcion = int(input("Seleccione otra opción: "))
    return opcion

def mostrar_alumno():
    print("Lista de alumnos registrados")
    #Imprime los alumnos que se encuentran en la lista
    for alumno in lista_alumnos:
        print("Número de estudiante:",alumno[0],"--- Nombre:",alumno[1],"--- Apellido:",alumno[2],"--- Carrera:",alumno[3])

def buscar_alumno(numero_de_estudiante):
    alumno_encontrado = None
    #Recorre la lista en busca de un número de estudiante duplicado
    for alumno in lista_alumnos:
        if alumno[0] == numero_de_estudiante:
            alumno_encontrado = alumno
            break #Rompe el bucle del for, no sigue iterando si se encuentra un número de estudiante correcto
    return alumno_encontrado

def registrar_alumno():
    while True:
        numero_de_estudiante = input("Ingrese el número de estudiante (6 dígitos): ")
        #Mientras no se digite un número del estudiante con una cantidad de dígitos diferentes de 6 la función no sigue
        while len(numero_de_estudiante) != 6:
            print("Error. Usted ingresó un número que no contiene 6 dígitos.")
            numero_de_estudiante = input("Ingrese un número de estudiante válido: ")
        #Comprueba si existe algún alumno con el número de estudiante ingresado por el usuario
        if buscar_alumno(numero_de_estudiante) is not None:
            print("Error. Ya existe un alumno registrado con ese número de estudiante.")
        else:
            nombre = str.capitalize(input("Ingrese nombre del alumno: "))
            apellido = str.capitalize(input("Ingrese apellido del alumno: "))
            carrera = input("Ingrese carrera del alumno: ")
            nuevo_contacto = [numero_de_estudiante,nombre,apellido,carrera]
            lista_alumnos.append(nuevo_contacto)
            print("El alumno se agregó correctamente.")
            mostrar_alumno()
            return #Finaliza la ejecución de la función

def mostrar_libro():
    print("Lista de libros registrados")
    #Imprime los libros que se encuentran en la lista
    for libro in lista_libros:
        print("Código identificador:",libro[0],"--- Autor:",libro[1],"--- Título:",libro[2],"--- Carrera:",libro[3])

def buscar_libro(codigo_identificador):
    libro_encontrado = None
    #Recorre la lista en busca de un código identificador duplicado
    for libro in lista_libros:
        if libro[0] == codigo_identificador:
            libro_encontrado = libro
            break #Rompe el bucle del for, no sigue iterando si se encuentra un código identificador correcto
    return libro_encontrado

def registrar_nuevo_libro():
    while True: 
        codigo_identificador = input("Ingrese el código del libro (4 dígitos): ")
        #Mientras no se digite un código identificador con una cantidad de dígitos diferentes de 4 la función no sigue
        while len(codigo_identificador) != 4:
            print("Error. Usted ingresó un número que no contiene 4 dígitos.")
            codigo_identificador = input("Ingrese un código válido: ")
        #Comprueba si existe algún libro con el código identificador ingresado por el usuario
        if buscar_libro(codigo_identificador) is not None:
            print("Error. Ya existe un libro con ese código identificador.")
        else:    
            autor = str.capitalize(input("Ingrese el autor del libro: "))
            titulo_libro = str.capitalize(input("Ingrese el título del libro: "))
            carrera = input("Ingrese carrera del alumno: ")
            nuevo_libro = [codigo_identificador,autor,titulo_libro,carrera]
            lista_libros.append(nuevo_libro)
            print("El libro se agregó correctamente.")
            mostrar_libro()
            return #Finaliza la ejecución de la función

def mostrar_prestamo():
    print("Lista de préstamos por estudiante:")
    #Imprime los préstamos que se encuentran en la lista
    for prestamo in lista_prestamos:
        print("Número de estudiante:",prestamo[0],"--- Carrera:",prestamo[1],"--- Fecha de préstamo",prestamo[2],"--- Fecha de devolución:",prestamo[3])

def buscar_libro_por_titulo(titulo_libro):
    libro_encontrado = None
    #Recorre la lista de libros para verificar que se encuentre en la lista
    for libro in lista_libros:
        if libro[2] == titulo_libro:
            libro_encontrado = libro
            break #Rompe el bucle del for, no sigue iterando si se encuentra el libro
    return libro_encontrado

def registrar_nuevo_prestamo():
    while True:
        numero_de_estudiante = input("Ingrese el número de estudiante que se encuentra en nuestro sistema (6 dígitos): ")
        #Comprueba si existe algún alumno con el número de estudiante ingresado por el usuario
        if buscar_alumno(numero_de_estudiante) is not None:
            print("El alumno se encuentra en nuestra base de datos.")
            break #No sigue iterando si se encuentra un número de estudiante correcto
        else:
            print("Error. El alumno no se encuentra en nuestra base de datos.")
    while True:
        titulo_libro = input("Ingrese el título del libro: ")
        #Comprueba si existe algún libro con el código identificador ingresado por el usuario
        if buscar_libro_por_titulo(titulo_libro) is not None:
            print("El libro se encuentra en nuestra biblioteca.")
            break #No sigue iterando si se encuentra un código identificador correcto
        else:
            print("Error. El libro no se encuentra en nuestra biblioteca.") 
    fecha_desde = datetime.strptime(input("Ingrese la fecha en que lo toma prestado (aaaa/m/dd): "), '%Y/%m/%d') #datetime.strptime pasa de un formato string a una fecha (ChatGPT)
    fecha_hasta = datetime.strptime(input("Ingrese la fecha de devolución (aaaa/m/dd): "),'%Y/%m/%d')
    fecha_desde_sin_segundos = fecha_desde.strftime('%Y-%m-%d') #strftime sirve para que no me imprima los segundos en la consola (ChatGPT)
    fecha_hasta_sin_segundos = fecha_hasta.strftime('%Y-%m-%d')
    
    nuevo_prestamo = [numero_de_estudiante,titulo_libro,fecha_desde_sin_segundos,fecha_hasta_sin_segundos]
    lista_prestamos.append(nuevo_prestamo)

    print("El préstamo se concretó de manera exitosa.")
    mostrar_prestamo()

def mostrar_libros_biblioteca():
    #Recorre la lista de los libros y nos trae el autor, título y carrera del estudiante
    for libro in lista_libros:
        print("Autor: " + libro[1] + " --- Título: " + libro[2] + " --- Carrera: " + libro[3])

def libros_estudiante():
    numero_de_estudiante = input("Ingrese el número de estudiante que se encuentra en nuestro sistema (6 dígitos): ")
    carrera_estudiante = 0
    #Recorre la lista de los alumnos en busca de que coincidan los números de estudiantes y la carrera 
    for estudiante in lista_alumnos:
        if numero_de_estudiante == estudiante[0]:
            carrera_estudiante = estudiante[3]
            break
    libros_disponibles = [] #Seteamos la nueva lista de libros que estarán disponibles
    #Recorre la lista de los libros y si coincide con el título y la carrera se agrega al final de la lista creada para los libros disponibles
    for libro in lista_libros:
        if libro[3] == carrera_estudiante:
            libros_disponibles.append(libro)
    for libro in libros_disponibles:
        print("Libros disponibles para el estudiante: ")
        for libro in libros_disponibles:
            print("Autor: " + libro[1] + " --- Título: " + libro[2] + " --- Carrera: " + libro[3])
    
def libros_prestados():
    numero_de_estudiante = input("Ingrese el número de estudiante que se encuentra en nuestro sistema (6 dígitos): ")
    libros_prestados = []
    for prestamo in lista_prestamos:
    #Recorre la lista de los préstamos y si coincide el número de estudiante se agrega al final de la lista creada para los libros prestados
        if prestamo[0] == numero_de_estudiante:
            libros_prestados.append(prestamo) 
    if libros_prestados:
        print("Libros prestados al estudiante: ")
        titulos_impresos = [] #Evita duplicados
        for libro in libros_prestados:
            #Si el título del libro se imprimió, se agrega a la lista de títulos impresos
            if libro[1] not in titulos_impresos:
                titulos_impresos.append(libro[1])
                print("Título: " + libro[1] + " --- Fecha de préstamo: " + str(libro[2]) + " --- Fecha de devolución: " + str(libro[3])) #Fecha en formato str sino arroja error
    

mostrar_menu()
opcion = seleccionar_opcion()

while opcion != 0:
    if opcion == 1:
        registrar_alumno()

    elif opcion == 2:
        registrar_nuevo_libro()

    elif opcion == 3:
        registrar_nuevo_prestamo()

    elif opcion == 4:
        mostrar_libros_biblioteca()
    
    elif opcion == 5:
        libros_estudiante()
    
    elif opcion == 6:
        libros_prestados()

    input("Presione enter para continuar...")
    mostrar_menu()
    opcion = int(input("Ingrese una opción: "))