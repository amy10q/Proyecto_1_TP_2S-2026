# ------------- DATOS -------------
areas = []        # lista de tuplas (codigo, nombre)
contactos = []    # lista de listas
configuracion = [] # Guardar el area y el tipo de telefono por omision
TIPOS_TELEFONO = ("M", "Móvil", "C", "Casa", "T", "Trabajo", "O", "Otro")
# ------------- FIN DATOS -------------

# ---------------------------------- INICIO REGISTRAR AREAS -------------------------------------------
# ------------- FUNCIONES AUXILIARES DE ÁREAS -------------
def buscar_area(areas, codigo): # devuelve la posición dentro de la lista
    # Busca un código dentro de la lista de áreas
    # Devuelve la posición si lo encuentra, o -1 si no existe
    posicion = -1 # Indica que el área no se ha encontrado

    for i in range(len(areas)):
        if areas[i][0] == codigo: # [i][0], [i] = cuál tupla de la lista se va a revisar y [0] = cual posiscion de la tupla se va a revisar
            posicion = i

    return posicion

def existe_area(areas, codigo):
     # Comprueba si el código se encuentra registrado 
     # Devuelve True si existe y False si no existe

    posicion = buscar_area(areas, codigo)

    if posicion == -1:
        existe = False
    else:
        existe = True

    return existe

# ------------- AGREGAR ÁREA -------------

def agregar_area():
    while True:
        print("\n      REGISTRAR ÁREAS: AGREGAR\n")

        codigo = input("Ingrese el número de área: ").strip() # .strip() Es para eliminar los espacios en blanco

        # Si el usuario escribe C, regresa al menú anterior
        if codigo == "C":
            return

        # Validar que el código sean solamente números
        if codigo.isdigit():

            codigo = int(codigo)

            # Validar que esté entre 1 y 999
            if codigo >= 1 and codigo <= 999:

                # Revisar si el código ya existe
                if existe_area(areas, codigo):
                    print("ALERTA: El área ya está registrada.")

                else:
                    nombre = input("Ingrese el nombre del área: ")

                    # Validar que el nombre tenga entre 1 y 40 caracteres
                    nombre = nombre.strip()

                    if len(nombre) >= 1 and len(nombre) <= 40:

                        # Crear la tupla
                        area = (codigo, nombre)

                        # Confirmar si desea registrar o cancelar el área
                        opcion = input("¿DESEA REGISTRAR EL AREA? A-ACEPTAR C-CANCELAR: ")

                        while opcion != "A" and opcion != "C":
                            print("ERROR: OPCIÓN NO VÁLIDA.")
                            opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

                        if opcion == "A":
                            areas.append(area)
                            print("Área registrada correctamente.")
                        else:
                            print("Registro cancelado")

                    else:
                        print("ERROR: El nombre debe tener entre 1 y 40 caracteres.")

            else:
                print("ERROR: El número de área debe estar entre 1 y 999.")

        else:
            print("ERROR: El número de área debe contener solamente números.")

# ------------- FIN DE AGREGAR ÁREA -------------

# ------------- CONSULTAR ÁREA -------------

def consultar_area():
    while True:
        print("\n      REGISTRAR ÁREAS: CONSULTAR\n")

        codigo = input("Ingrese el número de área: ").strip() # .strip() Es para eliminar los espacios en blanco

        # Si escribe C, regresa al menú anterior
        if codigo == "C":
            return

        # Validar que el código sea numérico
        if codigo.isdigit():

            codigo = int(codigo)

            # Validar que el código esté entre 1 y 999
            if codigo >= 1 and codigo <= 999:

                posicion = buscar_area(areas, codigo)

                # Comprobar si el área está registrada
                if posicion == -1:
                    print("ALERTA: El área no está registrada, no se puede consultar.")

                else:
                    print("Código:", areas[posicion][0])
                    print("Nombre:", areas[posicion][1])

                    # Aceptar la consulta para continuar
                    opcion = input("OPCIÓN A-ACEPTAR: ")

                    while opcion != "A":
                        print("ERROR: OPCIÓN NO VÁLIDA.")
                        opcion = input("OPCIÓN A-ACEPTAR: ")

            else:
                print("ERROR: El número de área debe estar entre 1 y 999.")

        else:
            print("ERROR: El número de área debe contener solamente números.")

# ------------- FIN DE CONSULTAR ÁREA -------------

# ------------- MODIFICAR ÁREA -------------

def modificar_area():
    while True:
        print("\n      REGISTRAR ÁREAS: MODIFICAR\n")

        codigo = input("Ingrese el número de área: ").strip() # .strip() Es para eliminar los espacios en blanco

        # Regresar al menú anterior
        if codigo == "C":
            return

        if codigo.isdigit():

            codigo = int(codigo)

            if codigo >= 1 and codigo <= 999:

                posicion = buscar_area(areas, codigo)

                if posicion == -1:
                    print("ALERTA: El área no está registrada.")

                else:
                    print("Código de área:", areas[posicion][0])
                    print("Nombre:", areas[posicion][1])

                    nuevo_nombre = input("Modificación del nombre: ")

                    nuevo_nombre = nuevo_nombre.strip()

                    # Si no se escribe nada, conservar el nombre anterior
                    if nuevo_nombre == "":
                        nuevo_nombre = areas[posicion][1]

                    # Validar longitud del nombre
                    if len(nuevo_nombre) >= 1 and len(nuevo_nombre) <= 40:

                        opcion = input("¿DESEA MODIFICAR EL ÁREA? A-ACEPTAR C-CANCELAR: ")

                        while opcion != "A" and opcion != "C":
                            print("ERROR: OPCIÓN NO VÁLIDA.")
                            opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

                        if opcion == "A":
                            areas[posicion] = (codigo, nuevo_nombre)
                            print("Área modificada correctamente.")
                        else: 
                            print("Modificación cancelada")

                    else:
                        print("ERROR: El nombre debe tener entre 1 y 40 caracteres.")

            else:
                print("ERROR: El número de área debe estar entre 1 y 999.")

        else:
            print("ERROR: El número de área debe contener solamente números.")

# ------------- FIN DE MODIFICAR ÁREA -------------

# ------------- ELIMINAR ÁREA -------------

def eliminar_area():
    while True:
        print("\n      REGISTRAR ÁREAS: ELIMINAR\n")

        codigo = input("Ingrese el número de área: ").strip() # .strip() Es para eliminar los espacios en blanco

        # Regresar al menú anterior
        if codigo == "C":
            return

        if codigo.isdigit():

            codigo = int(codigo)

            if codigo >= 1 and codigo <= 999:

                posicion = buscar_area(areas, codigo)

                if posicion == -1:
                    print("ALERTA: El área no está registrada.")

                else:
                    print("Código de área:", areas[posicion][0])
                    print("Nombre:", areas[posicion][1])

                    # Confirmar si se desea eliminar el área

                    opcion = input("¿DESEA ELIMINAR EL ÁREA? A-ACEPTAR C-CANCELAR: ")

                    while opcion != "A" and opcion != "C":

                        print("ERROR: OPCIÓN NO VÁLIDA.")
                        opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

                    if opcion == "A":
                        areas.pop(posicion)
                        print("Área eliminada correctamente.")

                    else:
                        print("Eliminación cancelada")

            else:
                print("ERROR: El número de área debe estar entre 1 y 999.")

        else:
            print("ERROR: El número de área debe contener solamente números.")

# ------------- FIN DE ELIMINAR ÁREA -------------

# ---------------------------------- INICIO MENU REGISTRAR AREAS -------------------------------------------

def menu_regitrar_areas():
    while True:
        print("\n      REGISTRAR ÁREAS\n")
        print("1. Agregar áreas")
        print("2. Consultar áreas")
        print("3. Modificar áreas")
        print("4. Eliminar áreas")
        print("0. Fin")

        opcion = input("\nOPCIÓN: ")

        match opcion:
            case "1":
                agregar_area()
            case "2":
                consultar_area()
            case "3":
                modificar_area()
            case "4":
                eliminar_area()
            case "0":
                break
            case _:
                print("ERROR: OPCIÓN NO VÁLIDA")

# ---------------------------------- FIN MENU REGISTRAR AREAS -------------------------------------------


# ------------- CONFIGURACIÓN DE CONTACTOS -------------

def configurar_lista_contactos():
    print("\n      CONFIGURACIÓN DE LA LISTA DE CONTACTOS\n")

    # Comprobar que existan áreas registradas antes de configurar
    if len(areas) == 0:
        print("No hay áreas registradas. Primero debe registrar un área.")
        return # Esto no estaba indicado en las instrucciones, pero me parecio importante, ya que si entra a configuración, estaría en bucle pidiendo código

    # Solicitar el código de área hasta que se ingrese uno válido
    while True:
        codigo = input("Área por omisión: ").strip() # .strip() Es para eliminar los espacios en blanco

        if codigo.isdigit():
            codigo = int(codigo)

            posicion = buscar_area(areas, codigo)

             # Si la posición es -1, el área no está registrada
            if posicion == -1:
                print("ESTA ÁREA NO ESTÁ REGISTRADA, NO SE PUEDE SELECCIONAR")

            else:
                # Mostrar el nombre del área encontrada
                print("Nombre del área:", areas[posicion][1])
                break

        else:
            print("ERROR: El código debe contener solamente números.")

    # Solicitar y validar el tipo de teléfono por omisión
    while True:
        tipo = input("\nTipo de teléfono por omisión (M:Móvil, C:Casa, T:Trabajo, O:Otro): ")

        # Comprobar que el tipo ingresado sea uno de los códigos permitidos
        # Las posiciones 0, 2, 4 y 6 contienen las letras M, C, T y O
        if (tipo == TIPOS_TELEFONO[0] or
            tipo == TIPOS_TELEFONO[2] or
            tipo == TIPOS_TELEFONO[4] or
            tipo == TIPOS_TELEFONO[6]):
            break

        else:
            # Si el tipo no existe, mostrar error y solicitarlo nuevamente
            print("ESTE TIPO DE TELÉFONO NO EXISTE, NO SE PUEDE SELECCIONAR")

    # Confirmar si desea guardar la configuración
    opcion = input("\n¿DESEA GUARDAR LA CONFIGURACIÓN? A-ACEPTAR C-CANCELAR: ")

    # Repetir la pregunta si no se ingresa A o C
    while opcion != "A" and opcion != "C":
        print("ERROR: OPCIÓN NO VÁLIDA.")
        opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

    # Guardar los valores solamente si el usuario acepta
    if opcion == "A":

        # Si la lista está vacía, agregar los primeros valores
        if len(configuracion) == 0:
            configuracion.append(codigo)
            configuracion.append(tipo)

        else:
            # Si ya existe una configuración, reemplazar sus valores
            configuracion[0] = codigo
            configuracion[1] = tipo

        print("\nConfiguración guardada correctamente.\n")

    else:
        # Al cancelar, no modificar los valores guardados
        print("\nConfiguración cancelada.\n")


# ------------- FIN DE CONFIGURACIÓN DE CONTACTOS -------------

def menu_registrar_contactos():
    while True:
        print("\n      REGISTRAR ÁREAS\n")
        print("1. Agregar contactos")
        print("2. Consultar contactos")
        print("3. Modificar contactos")
        print("4. Eliminar contactos")
        print("0. Fin")

        opcion = input("\nOPCIÓN: ")

        match opcion:
            case "1":
                pass # Llamada a funcion de el menu de agregar contactos
            case "2":
                pass # Llamada a funcion de el menu de Consultar contactos
            case "3":
                pass # Llamada a funcion de el menu de Modificar contactos
            case "4":
                pass # Llamada a funcion de el menu de Eliminar contactos
            case "0":
                print("Programa finalizado.")
                break
            case _:
                print("ERROR: OPCIÓN NO VÁLIDA")        

def menu_administrar_grupos_de_contactos():
    while True:
        print("\n      REGISTRAR ÁREAS\n")
        print("1. Agregar grupos")
        print("2. Agregar contactos a los grupos ")
        print("3. Modificar grupos")
        print("4. Eliminar grupos")
        print("5. Eliminar contactos de los grupos")
        print("0. Fin")

        opcion = input("\nOPCIÓN: ")

        match opcion:
            case "1":
                pass # Llamada a funcion de el menu de agregar contactos
            case "2":
                pass # Llamada a funcion de el menu de Consultar contactos
            case "3":
                pass # Llamada a funcion de el menu de Modificar contactos
            case "4":
                pass # Llamada a funcion de el menu de Eliminar contactos
            case "0":
                print("Programa finalizado.")
                break
            case _:
                print("ERROR: OPCIÓN NO VÁLIDA")  
# ---------------------------------- MENU PRINCIPAL -------------------------------------------
def menu_principal():
    while True:
        print("\n      LISTA DIGITAL DE CONTACTOS\n")
        print("1. Registrar áreas")
        print("2. Configuración de lista de contactos")
        print("3. Registrar contactos")
        print("4. Administrar grupos de contactos")
        print("5. Lista de contactos")
        print("6. Ayuda")
        print("7. Acerca de")
        print("0. Fin")

        opcion = input("\nOPCIÓN: ")

        match opcion:
            case "1":
                menu_regitrar_areas()
            case "2":
                configurar_lista_contactos()
            case "3":
                menu_registrar_contactos()
            case "4":
                menu_administrar_grupos_de_contactos()
            case "5":
                pass # Llamada a funcion de el menu de Lista de contactos
            case "6":
                pass # Llamada a funcion de el menu de Ayuda
            case "7":
                pass # Llamada a funcion de el menu de Acerca de
            case "0":
                print("Programa finalizado.")
                break
            case _:
                print("ERROR: OPCIÓN NO VÁLIDA")

menu_principal()
