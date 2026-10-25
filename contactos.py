import re # Permite utilizar expresiones regulares para validar el correo
import datetime # Permite comprobar que una fecha exista de verdad
# ------------- DATOS -------------
areas = []        # lista de tuplas (codigo, nombre)
contactos = []    # lista de listas
configuracion = [] # Guardar el area y el tipo de telefono por omision
TIPOS_TELEFONO = ("M", "Móvil", "C", "Casa", "T", "Trabajo", "O", "Otro")
grupos = []                 # lista con los nombres de los grupos (strings)
contactos_por_grupo = []    # lista de listas de tuplas (telefono, area)
# ------------- FIN DATOS -------------

# ---------------------------------- INICIO REGISTRAR AREAS -------------------------------------------
# ------------- FUNCIONES AUXILIARES DE ÁREAS -------------

# Función: buscar_area
# Propósito: Buscar un código dentro de la lista de áreas
# Entrada (E): Lista de áreas y código que se desea buscar
# Salida (S): Devuelve la posición del área si existe o -1 si no existe

def buscar_area(areas, codigo): # devuelve la posición dentro de la lista
    # Busca un código dentro de la lista de áreas
    # Devuelve la posición si lo encuentra, o -1 si no existe
    posicion = -1 # Indica que el área no se ha encontrado

    for i in range(len(areas)):
        if areas[i][0] == codigo: # [i][0], [i] = cuál tupla de la lista se va a revisar y [0] = cual posiscion de la tupla se va a revisar
            posicion = i

    return posicion


# Función: existe_area
# Propósito: Comprobar si un código de área está registrado
# Entrada (E): Lista de áreas y código que se desea comprobar
# Salida (S): Devuelve True si el área existe o False si no existe

def existe_area(areas, codigo):
     # Comprueba si el código se encuentra registrado 
     # Devuelve True si existe y False si no existe

    posicion = buscar_area(areas, codigo)

    if posicion == -1:
        existe = False
    else:
        existe = True

    return existe

# Función: area_en_uso
# Propósito: Comprobar si algún contacto está usando un código de área
# Entrada (E): Lista de contactos y código de área que se desea revisar
# Salida (S): Devuelve True si al menos un contacto usa el área
#             o False si ningún contacto la usa

def area_en_uso(contactos, codigo):
    en_uso = False

    for i in range(len(contactos)):
        # [i] indica cuál contacto de la lista estamos revisando
        # [1] es la posición del área dentro del contacto
        if contactos[i][1] == codigo:
            en_uso = True

    return en_uso

# ------------- AGREGAR ÁREA -------------

# Función: agregar_area
# Propósito: Permitir registrar nuevas áreas en la lista
# Entrada (E): Solicita el código del área, su nombre y la confirmación A/C
# Salida (S): Agrega una tupla (codigo, nombre) a la lista areas si se acepta
#             Muestra mensajes de error, confirmación o cancelación
#             No devuelve un valor

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
                    print("ESTA ÁREA YA ESTÁ REGISTRADA, NO SE PUEDE AGREGAR")

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

# ------------- CONSULTAR ÁREA -------------

# Función: consultar_area
# Propósito: Permitir consultar la información de un área registrada
# Entrada (E): Solicita el código del área y la confirmación A para continuar
# Salida (S): Muestra el código y nombre del área si existe
#             Muestra mensajes de error si los datos son incorrectos
#             No modifica la lista de áreas ni devuelve un valor

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
                    print("ESTA ÁREA NO ESTÁ REGISTRADA, NO SE PUEDE CONSULTAR")

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

# ------------- MODIFICAR ÁREA -------------

# Función: modificar_area
# Propósito: Permitir modificar el nombre de un área registrada
# Entrada (E): Solicita el código del área, el nuevo nombre y la
#              confirmación A/C
# Salida (S): Reemplaza la tupla del área con el nuevo nombre si
#             el usuario acepta. Muestra mensajes de error o
#             cancelación. No devuelve un valor

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
                    print("ESTA ÁREA NO ESTÁ REGISTRADA, NO SE PUEDE MODIFICAR")

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


# ------------- ELIMINAR ÁREA -------------

# Función: eliminar_area
# Propósito: Permitir eliminar un área registrada
# Entrada (E): Solicita el código del área y la confirmación A/C
# Salida (S): Elimina el área de la lista si el usuario acepta
#             Muestra mensajes de error o cancelación
#             No devuelve un valor
#             No elimina el área si algún contacto la está usando

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
                    print("ESTA ÁREA NO ESTÁ REGISTRADA, NO SE PUEDE ELIMINAR")
                 # Si algún contacto usa el área, no se puede eliminar
                elif area_en_uso(contactos, codigo):
                    print("EN ESTA ÁREA HAY CONTACTOS REGISTRADOS, NO SE PUEDE ELIMINAR")

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

# ---------------------------------- FIN REGISTRAR AREAS -------------------------------------------

# ---------------------------------- INICIO MENU REGISTRAR AREAS -------------------------------------------

# Función: menu_regitrar_areas
# Propósito: Mostrar el menú de Registrar áreas y permitir
#            seleccionar las operaciones disponibles
# Entrada (E): Solicita al usuario una opción del menú
# Salida (S): Ejecuta la función correspondiente a la opción elegida
#             Muestra un error si la opción no es válida
#             Regresa al menú principal cuando se selecciona 0
#             No devuelve un valor

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

# Función: configurar_lista_contactos
# Propósito: Establecer el área y tipo de teléfono por omisión
# Entrada (E): Solicita el código de un área registrada, el tipo
#              de teléfono (M, C, T, O) y la confirmación A/C
#              Utiliza las listas areas y configuracion
# Salida (S): Guarda o actualiza los valores en configuracion
#             cuando el usuario acepta
#             Si cancela, conserva los valores anteriores
#             Muestra mensajes de error o confirmación
#             No devuelve un valor

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

# ---------------------------------- INICIO REGISTRAR CONTACTOS -------------------------------------------
# ------------- FUNCIONES AUXILIARES DE CONTACTOS -------------

# Función: existe_contacto
# Propósito: Comprobar si un contacto está registrado utilizando
#            su número de teléfono y su código de área
# Entrada (E): Lista de contactos, código de área y teléfono
# Salida (S): Devuelve True si encuentra ambos datos en un mismo
#             contacto o False si no existe

def existe_contacto(contactos, area, telefono):
    existe = False

    for i in range(len(contactos)):
        # [i] indica cuál contacto de la lista estamos revisando
        # [0] es la posición del teléfono y [1] es la posición del área
        if contactos[i][0] == telefono and contactos[i][1] == area:
            existe = True       

    return existe

# ------------- BUSCAR CONTACTO -------------

# Función: buscar_contacto
# Propósito: Buscar un contacto por su número de teléfono y área.
# Entrada (E): Lista de contactos, código de área y teléfono.
# Salida (S): Devuelve la posición del contacto si existe
#             o -1 si no está registrado.

def buscar_contacto(contactos, area, telefono): # La posición (0, 1, 2...) o -1
    posicion = -1

    for i in range(len(contactos)):
        # [i] indica cuál contacto de la lista estamos revisando
        # [0] es la posición del teléfono y [1] es la posición del área
        if contactos[i][0] == telefono and contactos[i][1] == area:
            posicion = i

    return posicion

# ------------- AGREGAR CONTACTO -------------

# Función: agregar_contacto
# Propósito: Permitir registrar nuevos contactos
# Entrada (E): Solicita por teclado teléfono, área, tipo, nombre, correo,
#              dirección, fecha de nacimiento, pasatiempos, notas y la
#              confirmación A/C
# Salida (S): Agrega a la lista contactos una lista con los 9 datos
#             si el usuario acepta; si cancela, no agrega nada
#             Muestra mensajes de error, confirmación o cancelación
#             No devuelve un valor

def agregar_contacto():

    # Comprobar que exista una configuración guardada
    if len(configuracion) == 0:
        print("Primero debe configurar la lista de contactos.")
        return

    # Repetir la ventana de agregar hasta que el usuario escriba C en el teléfono
    while True:
        # Repetir teléfono y área si se encuentra un contacto duplicado
        while True:
            print("\n      REGISTRAR CONTACTOS: AGREGAR\n")

            # Solicitar y validar el teléfono
            while True:
                telefono = input("Teléfono: ").strip()

                # Regresar al menú anterior
                if telefono == "C":
                    return

                # Validar que solamente contenga números
                if telefono.isdigit():

                    # Validar la cantidad de dígitos
                    if len(telefono) >= 5 and len(telefono) <= 12:
                        telefono = int(telefono)

                        # Validar que sea mayor que cero
                        if telefono > 0:
                            break
                        else:
                            print("ERROR: El teléfono debe ser mayor que cero.")

                    else:
                        print("ERROR: El teléfono debe tener entre 5 y 12 dígitos.")

                else:
                    print("ERROR: El teléfono debe contener solamente números.")

            # Solicitar y validar el área
            while True:
                area = input("Área: ").strip()

                # Usar el área por omisión cuando el campo esté vacío
                if area == "":
                    area = str(configuracion[0])

                # Validar que el área sea numérica
                if area.isdigit():
                    area = int(area)

                    # Buscar el área registrada
                    posicion = buscar_area(areas, area)

                    if posicion == -1:
                        print("ESTA ÁREA NO ESTÁ REGISTRADA, NO SE PUEDE SELECCIONAR")

                    else:
                        print("Nombre del área:", areas[posicion][1])
                        break

                else:
                    print("ERROR: El código de área debe contener solamente números.")

            # Verificar que la combinación de teléfono y área sea única
            if existe_contacto(contactos, area, telefono):
                print("ESTE TELÉFONO YA ESTÁ REGISTRADO, NO SE PUEDE AGREGAR")

            else:
                break

        # Solicitar y validar el tipo de teléfono
        while True:
            tipo = input("Tipo de teléfono (M:Móvil, C:Casa, T:Trabajo, O:Otro): ").strip()

            # Utilizar el tipo por omisión si el campo está vacío
            if tipo == "":
                tipo = configuracion[1]

            # Comprobar que el tipo exista en TIPOS_TELEFONO
            if (tipo == TIPOS_TELEFONO[0] or
                tipo == TIPOS_TELEFONO[2] or
                tipo == TIPOS_TELEFONO[4] or
                tipo == TIPOS_TELEFONO[6]):
                break

            else:
                print("ESTE TIPO DE TELÉFONO NO EXISTE, NO SE PUEDE SELECCIONAR")

        # Solicitar y validar el nombre del contacto
        while True:
            nombre = input("Nombre contacto: ").strip()

            # Comprobar que tenga entre 1 y 50 caracteres
            if len(nombre) >= 1 and len(nombre) <= 50:
                break

            else:
                print("ERROR: El nombre debe tener entre 1 y 50 caracteres.")

        # Solicitar y validar el correo electrónico
        while True:
            correo = input("Correo electrónico: ")

            # Validar el formato parte1@parte2 sin espacios en blanco
            if re.fullmatch(r"[^@\s]+@[^@\s]+", correo):
                break

            else:
                print("ERROR: El correo debe tener el formato parte1@parte2, sin espacios.")

        # Solicitar y validar la dirección física (puede quedar vacía)
        while True:
            direccion = input("Dirección física: ").strip()

            # Comprobar que tenga como máximo 80 caracteres
            if len(direccion) <= 80:
                break

            else:
                print("ERROR: La dirección debe tener máximo 80 caracteres.")

        # Solicitar y validar la fecha de nacimiento (dd/mm/aaaa)
        # Si se deja vacía, la fecha queda como 0
        while True:
            fecha = input("Fecha de nacimiento (dd/mm/aaaa): ").strip()

            # Sin fecha: el dato queda con 0
            if fecha == "":
                fecha = 0
                break

            # Separar el texto en día, mes y año usando la "/"
            partes = fecha.split("/")

            # Validar el formato: 3 partes con 2, 2 y 4 dígitos
            if (len(partes) == 3 and
                len(partes[0]) == 2 and partes[0].isdigit() and
                len(partes[1]) == 2 and partes[1].isdigit() and
                len(partes[2]) == 4 and partes[2].isdigit()):

                dia = int(partes[0])
                mes = int(partes[1])
                anio = int(partes[2])

                # El año 0000 significa "año desconocido"
                # datetime no acepta el año 0, por eso se usa 2000 (bisiesto) solo para revisar día y mes
                if anio == 0:
                    anio_prueba = 2000
                else:
                    anio_prueba = anio

                # datetime da error (ValueError) si la fecha no existe
                try:
                    datetime.date(anio_prueba, mes, dia)
                    break

                except ValueError:
                    print("ERROR: La fecha no es válida.")

            else:
                print("ERROR: La fecha debe tener el formato dd/mm/aaaa.")

        # Solicitar y validar los pasatiempos (pueden quedar vacíos)
        while True:
            pasatiempos = input("Pasatiempos: ").strip()

            # Comprobar que tengan como máximo 60 caracteres
            if len(pasatiempos) <= 60:
                break

            else:
                print("ERROR: Los pasatiempos deben tener máximo 60 caracteres.")

        # Solicitar y validar las notas (pueden quedar vacías)
        while True:
            notas = input("Notas: ").strip()

            # Comprobar que tengan como máximo 60 caracteres
            if len(notas) <= 60:
                break

            else:
                print("ERROR: Las notas deben tener máximo 60 caracteres.")

        # Confirmar si desea registrar o cancelar el contacto
        opcion = input("¿DESEA REGISTRAR EL CONTACTO? A-ACEPTAR C-CANCELAR: ")

        while opcion != "A" and opcion != "C":
            print("ERROR: OPCIÓN NO VÁLIDA.")
            opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

        if opcion == "A":
            # Crear el contacto como una lista con los 9 datos
            contacto = [telefono, area, tipo, nombre, correo, direccion, fecha, pasatiempos, notas]
            contactos.append(contacto)
            print("Contacto registrado correctamente.")

        else:
            print("Registro cancelado")


# ------------- CONSULTAR CONTACTO -------------

# Función: consultar_contacto
# Propósito: Permitir consultar los datos de un contacto registrado
# Entrada (E): Solicita teléfono, área y la confirmación A para continuar
# Salida (S): Muestra los nueve datos del contacto si existe
#             Muestra un mensaje si el contacto no está registrado
#             No modifica la lista contactos ni devuelve un valor

def consultar_contacto():

    # Comprobar que exista una configuración guardada
    if len(configuracion) == 0:
        print("Primero debe configurar la lista de contactos.")
        return

    # Repetir la ventana de consultar hasta que el usuario escriba C en el teléfono
    while True:
        # Repetir teléfono y área si el contacto no está registrado
        while True:
            print("\n      REGISTRAR CONTACTOS: CONSULTAR\n")

            # Solicitar y validar el teléfono
            while True:
                telefono = input("Teléfono: ").strip()

                # Regresar al menú anterior
                if telefono == "C":
                    return

                # Validar que solamente contenga números
                if telefono.isdigit():

                    # Validar la cantidad de dígitos
                    if len(telefono) >= 5 and len(telefono) <= 12:
                        telefono = int(telefono)

                        # Validar que sea mayor que cero
                        if telefono > 0:
                            break
                        else:
                            print("ERROR: El teléfono debe ser mayor que cero.")

                    else:
                        print("ERROR: El teléfono debe tener entre 5 y 12 dígitos.")

                else:
                    print("ERROR: El teléfono debe contener solamente números.")

            # Solicitar y validar el área
            while True:
                area = input("Área: ").strip()

                # Usar el área por omisión cuando el campo esté vacío
                if area == "":
                    area = str(configuracion[0])

                # Validar que el área sea numérica
                if area.isdigit():
                    area = int(area)
                    break

                else:
                    print("ERROR: El código de área debe contener solamente números.")

            # Buscar el contacto por teléfono y área
            posicion = buscar_contacto(contactos, area, telefono)

            # Si no está registrado, se vuelven a pedir teléfono y área
            if posicion == -1:
                print("ESTE CONTACTO NO ESTA REGISTRADO, NO SE PUEDE CONSULTAR")

            else:
                break

        # Mostrar los datos del contacto 
        print("Teléfono:", contactos[posicion][0])
        print("Área:", contactos[posicion][1])
        print("Tipo de teléfono:", contactos[posicion][2])
        print("Nombre:", contactos[posicion][3])
        print("Correo electrónico:", contactos[posicion][4])
        print("Dirección física:", contactos[posicion][5])
        print("Fecha de nacimiento:", contactos[posicion][6])
        print("Pasatiempos:", contactos[posicion][7])
        print("Notas:", contactos[posicion][8])

        # Aceptar la consulta para continuar
        opcion = input("OPCIÓN A-ACEPTAR: ")

        while opcion != "A":
            print("ERROR: OPCIÓN NO VÁLIDA.")
            opcion = input("OPCIÓN A-ACEPTAR: ")

# ------------- ELIMINAR CONTACTO -------------

# Función: eliminar_contacto
# Propósito: Permitir eliminar un contacto registrado
# Entrada (E): Solicita teléfono, área, la opción A/C y la confirmación SI/NO
# Salida (S): Elimina el contacto de la lista contactos si el usuario acepta
#             y confirma; si cancela, no elimina nada
#             Muestra mensajes de error, confirmación o cancelación
#             No devuelve un valor

def eliminar_contacto():

    # Comprobar que exista una configuración guardada
    if len(configuracion) == 0:
        print("Primero debe configurar la lista de contactos.")
        return

    # Repetir la ventana de eliminar hasta que el usuario escriba C en el teléfono
    while True:
        # Repetir teléfono y área si el contacto no está registrado
        while True:
            print("\n      REGISTRAR CONTACTOS: ELIMINAR\n")

            # Solicitar y validar el teléfono
            while True:
                telefono = input("Teléfono: ").strip()

                # Regresar al menú anterior
                if telefono == "C":
                    return

                # Validar que solamente contenga números
                if telefono.isdigit():

                    # Validar la cantidad de dígitos
                    if len(telefono) >= 5 and len(telefono) <= 12:
                        telefono = int(telefono)

                        # Validar que sea mayor que cero
                        if telefono > 0:
                            break
                        else:
                            print("ERROR: El teléfono debe ser mayor que cero.")

                    else:
                        print("ERROR: El teléfono debe tener entre 5 y 12 dígitos.")

                else:
                    print("ERROR: El teléfono debe contener solamente números.")

            # Solicitar y validar el área
            while True:
                area = input("Área: ").strip()

                # Usar el área por omisión cuando el campo esté vacío
                if area == "":
                    area = str(configuracion[0])

                # Validar que el área sea numérica
                if area.isdigit():
                    area = int(area)
                    break

                else:
                    print("ERROR: El código de área debe contener solamente números.")

            # Buscar el contacto por teléfono y área
            posicion = buscar_contacto(contactos, area, telefono)

            # Si no está registrado, se vuelven a pedir teléfono y área
            if posicion == -1:
                print("ESTE CONTACTO NO ESTÁ REGISTRADO, NO SE PUEDE ELIMINAR")

            else:
                break

        # Mostrar los datos del contacto que se va a eliminar
        print("Teléfono:", contactos[posicion][0])
        print("Área:", contactos[posicion][1])
        print("Tipo de teléfono:", contactos[posicion][2])
        print("Nombre:", contactos[posicion][3])
        print("Correo electrónico:", contactos[posicion][4])
        print("Dirección física:", contactos[posicion][5])
        print("Fecha de nacimiento:", contactos[posicion][6])
        print("Pasatiempos:", contactos[posicion][7])
        print("Notas:", contactos[posicion][8])

        # Aceptar o cancelar la eliminación
        opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

        while opcion != "A" and opcion != "C":
            print("ERROR: OPCIÓN NO VÁLIDA.")
            opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

        if opcion == "A":
            # PENDIENTE (Grupos): aquí se rechazará la eliminación
            # si el contacto pertenece a algún grupo

            # Pedir confirmación antes de eliminar
            confirmacion = input("CONFIRMA LA ELIMINACIÓN (SI/NO): ")

            while confirmacion != "SI" and confirmacion != "NO":
                print("ERROR: OPCIÓN NO VÁLIDA.")
                confirmacion = input("CONFIRMA LA ELIMINACIÓN (SI/NO): ")

            if confirmacion == "SI":
                contactos.pop(posicion)
                print("Contacto eliminado correctamente.")

            else:
                print("Eliminación cancelada")

        else:
            print("Eliminación cancelada")

# ------------- MODIFICAR CONTACTO -------------

# Función: modificar_contacto
# Propósito: Permitir modificar el nombre, correo, dirección, fecha de
#            nacimiento, pasatiempos y notas de un contacto registrado
#            El teléfono, el área y el tipo de teléfono no se modifican
# Entrada (E): Solicita el teléfono y el área del contacto, el nuevo valor
#              de cada dato (con Enter se conserva el valor actual) y la
#              confirmación A/C
# Salida (S): Reemplaza los datos del contacto en la lista contactos si el
#             usuario acepta. Si cancela, el contacto no cambia
#             Muestra mensajes de error, confirmación o cancelación
#             No devuelve un valor

def modificar_contacto():

    # Comprobar que exista una configuración guardada
    if len(configuracion) == 0:
        print("Primero debe configurar la lista de contactos.")
        return

    # Repetir la ventana de modificar hasta que el usuario escriba C en el teléfono
    while True:
        # Repetir teléfono y área si el contacto no está registrado
        while True:
            print("\n      REGISTRAR CONTACTOS: MODIFICAR\n")

            # Solicitar y validar el teléfono
            while True:
                telefono = input("Teléfono: ").strip()

                # Regresar al menú anterior
                if telefono == "C":
                    return

                # Validar que solamente contenga números
                if telefono.isdigit():

                    # Validar la cantidad de dígitos
                    if len(telefono) >= 5 and len(telefono) <= 12:
                        telefono = int(telefono)

                        # Validar que sea mayor que cero
                        if telefono > 0:
                            break
                        else:
                            print("ERROR: El teléfono debe ser mayor que cero.")

                    else:
                        print("ERROR: El teléfono debe tener entre 5 y 12 dígitos.")

                else:
                    print("ERROR: El teléfono debe contener solamente números.")

            # Solicitar y validar el área
            while True:
                area = input("Área: ").strip()

                # Usar el área por omisión cuando el campo esté vacío
                if area == "":
                    area = str(configuracion[0])

                # Validar que el área sea numérica
                if area.isdigit():
                    area = int(area)
                    break

                else:
                    print("ERROR: El código de área debe contener solamente números.")

            # Buscar el contacto por teléfono y área
            posicion = buscar_contacto(contactos, area, telefono)

            # Si no está registrado, se vuelven a pedir teléfono y área
            if posicion == -1:
                print("ESTE CONTACTO NO ESTÁ REGISTRADO, NO SE PUEDE MODIFICAR")

            else:
                break

        # Mostrar los datos que no se pueden modificar
        posicion_area = buscar_area(areas, contactos[posicion][1])
        print("Nombre del área:", areas[posicion_area][1])
        print("Tipo de teléfono:", contactos[posicion][2])

        # Nombre del contacto: se muestra el actual y se pide el nuevo valor
        print("Nombre contacto:", contactos[posicion][3])

        while True:
            nuevo_nombre = input("MODIFICACIÓN: ").strip()

            # Si no escribe nada, se conserva el valor anterior
            if nuevo_nombre == "":
                nuevo_nombre = contactos[posicion][3]

            # Comprobar que tenga entre 1 y 50 caracteres
            if len(nuevo_nombre) >= 1 and len(nuevo_nombre) <= 50:
                break

            else:
                print("ERROR: El nombre debe tener entre 1 y 50 caracteres.")

        # Correo electrónico: se muestra el actual y se pide el nuevo valor
        print("Correo electrónico:", contactos[posicion][4])

        while True:
            nuevo_correo = input("MODIFICACIÓN: ")

            # Si no escribe nada, se conserva el valor anterior
            if nuevo_correo == "":
                nuevo_correo = contactos[posicion][4]

            # Validar el formato parte1@parte2 sin espacios en blanco
            if re.fullmatch(r"[^@\s]+@[^@\s]+", nuevo_correo):
                break

            else:
                print("ERROR: El correo debe tener el formato parte1@parte2, sin espacios.")

        # Dirección física: se muestra la actual y se pide el nuevo valor
        print("Dirección física:", contactos[posicion][5])

        while True:
            nueva_direccion = input("MODIFICACIÓN: ").strip()

            # Si no escribe nada, se conserva el valor anterior
            if nueva_direccion == "":
                nueva_direccion = contactos[posicion][5]

            # Comprobar que tenga como máximo 80 caracteres
            if len(nueva_direccion) <= 80:
                break

            else:
                print("ERROR: La dirección debe tener máximo 80 caracteres.")

        # Fecha de nacimiento: se muestra la actual y se pide el nuevo valor
        print("Fecha de nacimiento:", contactos[posicion][6])

        while True:
            nueva_fecha = input("MODIFICACIÓN: ").strip()

            # Si no escribe nada, se conserva el valor anterior
            if nueva_fecha == "":
                nueva_fecha = contactos[posicion][6]
                break

            # Separar el texto en día, mes y año usando la "/"
            partes = nueva_fecha.split("/")

            # Validar el formato: 3 partes con 2, 2 y 4 dígitos
            if (len(partes) == 3 and
                len(partes[0]) == 2 and partes[0].isdigit() and
                len(partes[1]) == 2 and partes[1].isdigit() and
                len(partes[2]) == 4 and partes[2].isdigit()):

                dia = int(partes[0])
                mes = int(partes[1])
                anio = int(partes[2])

                # El año 0000 significa "año desconocido"
                # datetime no acepta el año 0, por eso se usa 2000 solo para revisar día y mes
                if anio == 0:
                    anio_prueba = 2000
                else:
                    anio_prueba = anio

                # datetime da error (ValueError) si la fecha no existe
                try:
                    datetime.date(anio_prueba, mes, dia)
                    break

                except ValueError:
                    print("ERROR: La fecha no es válida.")

            else:
                print("ERROR: La fecha debe tener el formato dd/mm/aaaa.")

        # Pasatiempos: se muestran los actuales y se pide el nuevo valor
        print("Pasatiempos:", contactos[posicion][7])

        while True:
            nuevos_pasatiempos = input("MODIFICACIÓN: ").strip()

            # Si no escribe nada, se conserva el valor anterior
            if nuevos_pasatiempos == "":
                nuevos_pasatiempos = contactos[posicion][7]

            # Comprobar que tengan como máximo 60 caracteres
            if len(nuevos_pasatiempos) <= 60:
                break

            else:
                print("ERROR: Los pasatiempos deben tener máximo 60 caracteres.")

        # Notas: se muestran las actuales y se pide el nuevo valor
        print("Notas:", contactos[posicion][8])

        while True:
            nuevas_notas = input("MODIFICACIÓN: ").strip()

            # Si no escribe nada, se conserva el valor anterior
            if nuevas_notas == "":
                nuevas_notas = contactos[posicion][8]

            # Comprobar que tengan como máximo 60 caracteres
            if len(nuevas_notas) <= 60:
                break

            else:
                print("ERROR: Las notas deben tener máximo 60 caracteres.")
        # Confirmar y guardar los cambios
        opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

        while opcion != "A" and opcion != "C":
            print("ERROR: OPCIÓN NO VÁLIDA.")
            opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

        if opcion == "A":
            contactos[posicion][3] = nuevo_nombre
            contactos[posicion][4] = nuevo_correo
            contactos[posicion][5] = nueva_direccion
            contactos[posicion][6] = nueva_fecha
            contactos[posicion][7] = nuevos_pasatiempos
            contactos[posicion][8] = nuevas_notas
            print("Contacto modificado correctamente.")

        else:
            print("Modificación cancelada")

# ---------------------------------- MENU REGISTRAR CONTACTOS -------------------------------------------

# Función: menu_registrar_contactos
# Propósito: Mostrar el menú para administrar los contactos
# Entrada (E): Solicita al usuario una opción del menú
# Salida (S): Permite seleccionar las opciones de agregar,
#             consultar, modificar y eliminar contactos
#             Muestra un error si la opción no es válida
#             Regresa al menú principal al seleccionar 0
#             No devuelve un valor

def menu_registrar_contactos():
    while True:
        print("\n      REGISTRAR CONTACTOS\n")
        print("1. Agregar contactos")
        print("2. Consultar contactos")
        print("3. Modificar contactos")
        print("4. Eliminar contactos")
        print("0. Fin")

        opcion = input("\nOPCIÓN: ")

        match opcion:
            case "1":
                agregar_contacto()
            case "2":
                consultar_contacto()
            case "3":
                modificar_contacto()
            case "4":
                eliminar_contacto()
            case "0":
                break
            case _:
                print("ERROR: OPCIÓN NO VÁLIDA")        

# ---------------------------------- INICIO ADMINISTRAR GRUPOS DE CONTACTOS -------------------------------------------
# ------------- FUNCIONES AUXILIARES DE GRUPOS -------------

# Función: buscar_grupo
# Propósito: Buscar un grupo por su nombre dentro de la lista de grupos
# Entrada (E): Lista de grupos y nombre del grupo que se desea buscar
# Salida (S): Devuelve la posición del grupo si existe
#             o -1 si no está registrado

def buscar_grupo(grupos, nombre):
    posicion = -1

    for i in range(len(grupos)):
        # [i] indica cuál grupo de la lista se está revisando
        if grupos[i] == nombre:
            posicion = i

    return posicion

# ------------- AGREGAR GRUPO -------------

# Función: agregar_grupo
# Propósito: Permitir registrar nuevos grupos de contactos
# Entrada (E): Solicita el nombre del grupo y la confirmación A/C
# Salida (S): Agrega el nombre a la lista grupos y una lista vacía a
#             contactos_por_grupo si el usuario acepta
#             Si cancela, no agrega nada
#             Muestra mensajes de error, confirmación o cancelación
#             No devuelve un valor

def agregar_grupo():

    # Repetir la ventana de agregar hasta que el usuario escriba C
    while True:
        print("\n      ADMINISTRAR GRUPOS DE CONTACTOS")
        print("      Agregar grupos\n")

        # Solicitar y validar el nombre del grupo
        while True:
            nombre = input("Nombre del grupo: ").strip()

            # Regresar al menú anterior
            if nombre == "C":
                return

            # Comprobar que tenga entre 1 y 40 caracteres
            if len(nombre) >= 1 and len(nombre) <= 40:

                # Comprobar que el grupo no esté registrado
                posicion = buscar_grupo(grupos, nombre)

                if posicion == -1:
                    break

                else:
                    print("ESTE GRUPO YA ESTÁ REGISTRADO, NO SE PUEDE AGREGAR")

            else:
                print("ERROR: El nombre del grupo debe tener entre 1 y 40 caracteres.")

        # Confirmar si desea registrar o cancelar el grupo
        opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

        while opcion != "A" and opcion != "C":
            print("ERROR: OPCIÓN NO VÁLIDA.")
            opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

        if opcion == "A":
            # Las dos listas se actualizan juntas para mantener la relación 1:1
            grupos.append(nombre)
            contactos_por_grupo.append([])
            print("Grupo registrado correctamente.")

        else:
            print("Registro cancelado")

# ---------------------------------- FIN ADMINISTRAR GRUPOS DE CONTACTOS -------------------------------------------

# ---------------------------------- FIN MENU REGISTRAR CONTACTOS -------------------------------------------

# ---------------------------------- MENU ADMINISTRAR GRUPOS DE CONTACTOS -------------------------------------------

# Función: menu_administrar_grupos_de_contactos
# Propósito: Mostrar el menú para administrar grupos de contactos
# Entrada (E): Solicita al usuario una opción del menú
# Salida (S): Muestra las opciones para agregar, modificar y eliminar
#             grupos, además de agregar o eliminar contactos de ellos
#             Muestra un error si la opción no es válida
#             Regresa al menú principal al seleccionar 0
#             Las operaciones de grupos aún no están implementadas
#             No devuelve un valor

def menu_administrar_grupos_de_contactos():
    while True:
        print("\n      ADMINISTRAR GRUPOS DE CONTACTOS\n")
        print("1. Agregar grupos")
        print("2. Agregar contactos a los grupos ")
        print("3. Modificar grupos")
        print("4. Eliminar grupos")
        print("5. Eliminar contactos de los grupos")
        print("0. Fin")

        opcion = input("\nOPCIÓN: ")

        match opcion:
            case "1":
                agregar_grupo()
            case "2":
                pass # Llamada a funcion de el menu de Consultar contactos
            case "3":
                pass # Llamada a funcion de el menu de Modificar contactos
            case "4":
                pass # Llamada a funcion de el menu de Eliminar contactos
            case "5":
                pass # Llamada a la función para eliminar contactos de los grupos
            case "0":
                break
            case _:
                print("ERROR: OPCIÓN NO VÁLIDA")  

# ---------------------------------- FIN MENU ADMINISTRAR GRUPOS DE CONTACTOS -------------------------------------------

#  ---------------------------------- MENU PRINCIPAL -------------------------------------------

# Función: menu_principal
# Propósito: Mostrar el menú principal y permitir al usuario
#            seleccionar las diferentes funcionalidades del programa
# Entrada (E): Solicita al usuario una opción del menú
# Salida (S): Llama a la función correspondiente según la opción
#             seleccionada y muestra un error si la opción no existe
#             Finaliza el menú cuando el usuario selecciona 0
#             No devuelve un valor

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

#  ---------------------------------- FIN MENU PRINCIPAL -------------------------------------------

menu_principal() # Mostrará el menú principal al ejecutar el programa
