import re # Permite utilizar expresiones regulares para validar el correo
import datetime # Permite comprobar que una fecha exista de verdad
import os # Permite ubicar y abrir el archivo PDF del manual de usuario
import importlib.util # Permite comprobar si la biblioteca fpdf2 está instalada

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

# BUSCAR ÁREA
# Busca un código en la lista de áreas
# E: la lista de áreas y el código que se busca
# S: la posición del área en la lista, o -1 si no está

def buscar_area(areas, codigo): # devuelve la posición dentro de la lista
    # Busca un código dentro de la lista de áreas
    # Devuelve la posición si lo encuentra, o -1 si no existe
    posicion = -1 # Indica que el área no se ha encontrado

    for i in range(len(areas)):
        if areas[i][0] == codigo: # [i][0], [i] = cuál tupla de la lista se va a revisar y [0] = cuál posición de la tupla se va a revisar
            posicion = i

    return posicion


# EXISTE ÁREA
# Revisa si un código de área ya está registrado
# E: la lista de áreas y el código
# S: True si el área existe, False si no

def existe_area(areas, codigo):
     # Comprueba si el código se encuentra registrado 
     # Devuelve True si existe y False si no existe

    posicion = buscar_area(areas, codigo)

    if posicion == -1:
        existe = False
    else:
        existe = True

    return existe

# ÁREA EN USO
# Revisa si algún contacto tiene ese código de área
# E: la lista de contactos y el código de área
# S: True si algún contacto la usa, False si ninguno

def area_en_uso(contactos, codigo):
    en_uso = False

    for i in range(len(contactos)):
        # [i] indica cuál contacto de la lista estamos revisando
        # [1] es la posición del área dentro del contacto
        if contactos[i][1] == codigo:
            en_uso = True

    return en_uso

# ------------- AGREGAR ÁREA -------------

# AGREGAR ÁREA
# Pide el código y el nombre de un área y la guarda si se acepta
# E: código, nombre y opción A/C 
# S: agrega la tupla (codigo, nombre) a la lista areas

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

# CONSULTAR ÁREA
# Muestra el código y el nombre de un área registrada
# E: el código del área y la opción A 
# S: muestra los datos del área o el mensaje de error

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

# MODIFICAR ÁREA
# Cambia el nombre de un área registrada
# E: código, nuevo nombre y opción A/C 
# S: cambia la tupla del área en la lista areas si se acepta

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

# ELIMINAR ÁREA
# Elimina un área si ningún contacto la está usando
# E: el código del área y la opción A/C 
# S: quita el área de la lista areas si se acepta

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

# MENÚ REGISTRAR ÁREAS
# Muestra las opciones de áreas y llama a la que se elija
# E: la opción del menú 
# S: ejecuta la opción elegida, con 0 vuelve al menú principal

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

# CONFIGURACIÓN DE LA LISTA DE CONTACTOS
# Guarda el área y el tipo de teléfono que se usan por omisión
# E: código de área, tipo de teléfono y opción A/C 
# S: guarda los dos valores en la lista configuracion si se acepta

def configurar_lista_contactos():
    print("\n      CONFIGURACIÓN DE LA LISTA DE CONTACTOS\n")

    # Comprobar que existan áreas registradas antes de configurar
    if len(areas) == 0:
        print("No hay áreas registradas. Primero debe registrar un área.")
        return # El enunciado no lo indica, se agregó para evitar un ciclo infinito pidiendo un código de área cuando no hay áreas registradas

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

# EXISTE CONTACTO
# Revisa si un contacto está registrado con ese teléfono y esa área
# E: la lista de contactos, el área y el teléfono
# S: True si el contacto existe, False si no

def existe_contacto(contactos, area, telefono):
    existe = False

    for i in range(len(contactos)):
        # [i] indica cuál contacto de la lista estamos revisando
        # [0] es la posición del teléfono y [1] es la posición del área
        if contactos[i][0] == telefono and contactos[i][1] == area:
            existe = True       

    return existe

# ------------- BUSCAR CONTACTO -------------

# BUSCAR CONTACTO
# Busca un contacto por su teléfono y su área
# E: la lista de contactos, el área y el teléfono
# S: la posición del contacto en la lista, o -1 si no está

def buscar_contacto(contactos, area, telefono): # La posición (0, 1, 2...) o -1
    posicion = -1

    for i in range(len(contactos)):
        # [i] indica cuál contacto de la lista estamos revisando
        # [0] es la posición del teléfono y [1] es la posición del área
        if contactos[i][0] == telefono and contactos[i][1] == area:
            posicion = i

    return posicion

# ------------- AGREGAR CONTACTO -------------

# AGREGAR CONTACTO
# Pide los 9 datos de un contacto, los valida y lo guarda si se acepta
# E: teléfono, área, tipo, nombre, correo, dirección, fecha, pasatiempos, notas y opción A/C 
# S: agrega el contacto a la lista contactos

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

            # Revisa que el correo sea parte1@parte2, con una sola @ y sin espacios
            # [^@\s]+ significa: uno o más caracteres que no sean @ ni espacio
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

# CONSULTAR CONTACTO
# Muestra todos los datos de un contacto registrado
# E: teléfono, área y la opción A 
# S: muestra los datos del contacto o el mensaje de error

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

# ELIMINAR CONTACTO
# Elimina un contacto si no pertenece a ningún grupo
# E: teléfono, área, opción A/C y confirmación SI/NO 
# S: quita el contacto de la lista contactos si se confirma

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

            # No se puede eliminar un contacto que pertenece a algún grupo
            if contacto_en_algun_grupo(contactos_por_grupo, telefono, area):
                print("ESTE CONTACTO PERTENECE A UN GRUPO, NO SE PUEDE ELIMINAR")

            else:
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

# MODIFICAR CONTACTO
# Cambia los datos de un contacto; con Enter se deja el dato como estaba
# E: teléfono, área, los datos nuevos y opción A/C 
# S: guarda los cambios en la lista contactos si se acepta

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

            # Revisa que el correo sea parte1@parte2, con una sola @ y sin espacios
            # [^@\s]+ significa: uno o más caracteres que no sean @ ni espacio
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

# MENÚ REGISTRAR CONTACTOS
# Muestra las opciones de contactos y llama a la que se elija
# E: la opción del menú 
# S: ejecuta la opción elegida; con 0 vuelve al menú principal

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

# ---------------------------------- FIN MENU REGISTRAR CONTACTOS -------------------------------------------

# ---------------------------------- INICIO ADMINISTRAR GRUPOS DE CONTACTOS -------------------------------------------
# ------------- FUNCIONES AUXILIARES DE GRUPOS -------------

# BUSCAR GRUPO
# Busca un grupo por su nombre
# E: la lista de grupos y el nombre
# S: la posición del grupo en la lista, o -1 si no está

def buscar_grupo(grupos, nombre):
    posicion = -1

    for i in range(len(grupos)):
        # [i] indica cuál grupo de la lista se está revisando
        if grupos[i] == nombre:
            posicion = i

    return posicion

# BUSCAR CONTACTO EN GRUPO
# Busca un contacto dentro de la lista de un grupo
# E: la lista de tuplas (teléfono, área) del grupo, el teléfono y el área
# S: la posición del contacto en el grupo, o -1 si no está

def buscar_contacto_en_grupo(contactos_del_grupo, telefono, area):
    posicion = -1

    for i in range(len(contactos_del_grupo)):
        # [i] indica cuál tupla del grupo estamos revisando
        # [0] es el teléfono y [1] es el área dentro de la tupla
        if contactos_del_grupo[i][0] == telefono and contactos_del_grupo[i][1] == area:
            posicion = i

    return posicion

# CONTACTO EN ALGÚN GRUPO
# Revisa si un contacto pertenece al menos a un grupo
# E: la lista contactos_por_grupo, el teléfono y el área
# S: True si está en algún grupo, False si no

def contacto_en_algun_grupo(contactos_por_grupo, telefono, area):
    en_grupo = False

    for i in range(len(contactos_por_grupo)):
        # [i] indica cuál grupo (lista de tuplas) se está revisando
        if buscar_contacto_en_grupo(contactos_por_grupo[i], telefono, area) != -1:
            en_grupo = True

    return en_grupo

# ------------- AGREGAR GRUPO -------------

# AGREGAR GRUPO
# Pide el nombre de un grupo nuevo y lo guarda si se acepta
# E: nombre del grupo y opción A/C 
# S: agrega el nombre a grupos y una lista vacía a contactos_por_grupo

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

# ------------- AGREGAR CONTACTO A UN GRUPO -------------

# AGREGAR CONTACTO A GRUPO
# Agrega un contacto registrado a un grupo que ya existe
# E: nombre del grupo, teléfono, área y opción A/C 
# S: agrega la tupla (telefono, area) a la lista del grupo

def agregar_contacto_a_grupo():

    # Comprobar que exista una configuración guardada
    if len(configuracion) == 0:
        print("Primero debe configurar la lista de contactos.")
        return

    # Repetir la ventana hasta que el usuario escriba C en el nombre del grupo
    while True:
        print("\n      ADMINISTRAR GRUPOS DE CONTACTOS")
        print("      Agregar contactos a los grupos\n")

        # Solicitar y validar el nombre del grupo
        while True:
            nombre_grupo = input("Nombre del grupo: ").strip()

            # Regresar al menú anterior
            if nombre_grupo == "C":
                return

            posicion_grupo = buscar_grupo(grupos, nombre_grupo)

            if posicion_grupo == -1:
                print("ESTE GRUPO NO EXISTE, NO PUEDE AGREGARLE CONTACTOS")

            else:
                break

        # Repetir teléfono y área si el contacto no existe o ya está en el grupo
        while True:

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

            if posicion == -1:
                print("ESTE CONTACTO NO EXISTE, NO PUEDE AGREGARLO AL GRUPO")

            # Los grupos no pueden tener contactos repetidos
            elif buscar_contacto_en_grupo(contactos_por_grupo[posicion_grupo], telefono, area) != -1:
                print("ESTE CONTACTO YA ESTÁ EN EL GRUPO, NO SE PUEDE AGREGAR")

            else:
                break

        # Mostrar el nombre del área y el nombre del contacto
        posicion_area = buscar_area(areas, area)
        print("Nombre del área:", areas[posicion_area][1])
        print("Nombre contacto:", contactos[posicion][3])

        # Confirmar si desea agregar o cancelar
        opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

        while opcion != "A" and opcion != "C":
            print("ERROR: OPCIÓN NO VÁLIDA.")
            opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

        if opcion == "A":
            # Se guarda la tupla en la lista del grupo (misma posición que en grupos)
            contactos_por_grupo[posicion_grupo].append((telefono, area))
            print("Contacto agregado al grupo correctamente.")

        else:
            print("Operación cancelada")

# ------------- MODIFICAR GRUPO -------------

# MODIFICAR GRUPO
# Cambia el nombre de un grupo; si el nombre nuevo ya existe, pasa los contactos a ese grupo
# E: nombre del grupo, nombre nuevo y opción A/C 
# S: actualiza las listas grupos y contactos_por_grupo si se acepta

def modificar_grupo():

    # Repetir la ventana de modificar hasta que el usuario escriba C
    while True:
        print("\n      ADMINISTRAR GRUPOS DE CONTACTOS")
        print("      Modificar grupos\n")

        # Solicitar y validar el nombre del grupo
        while True:
            nombre_grupo = input("Nombre del grupo: ").strip()

            # Regresar al menú anterior
            if nombre_grupo == "C":
                return

            posicion_grupo = buscar_grupo(grupos, nombre_grupo)

            if posicion_grupo == -1:
                print("GRUPO NO ESTÁ REGISTRADO, NO SE PUEDE MODIFICAR")

            else:
                break

        # Solicitar y validar el nuevo nombre
        while True:
            nuevo_nombre = input("MODIFICACIÓN: ").strip()

            # Si no escribe nada, se conserva el nombre actual
            if nuevo_nombre == "":
                nuevo_nombre = nombre_grupo

            # Comprobar que tenga entre 1 y 40 caracteres
            if len(nuevo_nombre) >= 1 and len(nuevo_nombre) <= 40:
                break

            else:
                print("ERROR: El nombre del grupo debe tener entre 1 y 40 caracteres.")

        # Buscar si el nuevo nombre ya existe en otro grupo
        posicion_nuevo = buscar_grupo(grupos, nuevo_nombre)

        if posicion_nuevo != -1 and posicion_nuevo != posicion_grupo:
            print("GRUPO YA EXISTE, EN CASO DE ACEPTAR LA OPERACIÓN LOS CONTACTOS SE LE AGREGARÁN")

        # Confirmar si desea modificar o cancelar
        opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

        while opcion != "A" and opcion != "C":
            print("ERROR: OPCIÓN NO VÁLIDA.")
            opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

        if opcion == "A":

            # El nombre es nuevo (o no cambió): solo se reemplaza el nombre
            if posicion_nuevo == -1 or posicion_nuevo == posicion_grupo:
                grupos[posicion_grupo] = nuevo_nombre

            # El nombre ya existe: los contactos pasan al otro grupo
            else:
                for i in range(len(contactos_por_grupo[posicion_grupo])):
                    # [i] indica cuál tupla (teléfono, área) del grupo actual se pasa
                    contacto_grupo = contactos_por_grupo[posicion_grupo][i]

                    # En un grupo no hay contactos repetidos
                    if buscar_contacto_en_grupo(contactos_por_grupo[posicion_nuevo], contacto_grupo[0], contacto_grupo[1]) == -1:
                        contactos_por_grupo[posicion_nuevo].append(contacto_grupo)

                # El grupo modificado se elimina de las dos listas (relación 1:1)
                grupos.pop(posicion_grupo)
                contactos_por_grupo.pop(posicion_grupo)

            print("Grupo modificado correctamente.")

        else:
            print("Modificación cancelada")

# ------------- ELIMINAR GRUPO -------------

# ELIMINAR GRUPO
# Elimina un grupo; sus contactos siguen registrados
# E: nombre del grupo, opción A/C y confirmación SI/NO 
# S: quita el grupo de grupos y de contactos_por_grupo si se confirma

def eliminar_grupo():

    # Repetir la ventana de eliminar hasta que el usuario escriba C
    while True:
        print("\n      ADMINISTRAR GRUPOS DE CONTACTOS")
        print("      Eliminar grupos\n")

        # Solicitar y validar el nombre del grupo
        while True:
            nombre = input("Nombre del grupo: ").strip()

            # Regresar al menú anterior
            if nombre == "C":
                return

            posicion_grupo = buscar_grupo(grupos, nombre)

            if posicion_grupo == -1:
                print("ESTE GRUPO NO ESTÁ REGISTRADO, NO SE PUEDE ELIMINAR")

            else:
                break

        # Aceptar o cancelar la eliminación
        opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

        while opcion != "A" and opcion != "C":
            print("ERROR: OPCIÓN NO VÁLIDA.")
            opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

        if opcion == "A":
            # Pedir confirmación antes de eliminar
            confirmacion = input("CONFIRMA LA ELIMINACIÓN (SI/NO): ")

            while confirmacion != "SI" and confirmacion != "NO":
                print("ERROR: OPCIÓN NO VÁLIDA.")
                confirmacion = input("CONFIRMA LA ELIMINACIÓN (SI/NO): ")

            if confirmacion == "SI":
                # Se elimina de las dos listas con la misma posición (relación 1:1)
                grupos.pop(posicion_grupo)
                contactos_por_grupo.pop(posicion_grupo)
                print("Grupo eliminado correctamente.")

            else:
                print("Eliminación cancelada")

        else:
            print("Eliminación cancelada")

# ------------- ELIMINAR CONTACTO DE UN GRUPO -------------

# ELIMINAR CONTACTO DE GRUPO
# Quita un contacto de un grupo, sin borrarlo de la lista contactos
# E: nombre del grupo, teléfono, área, opción A/C y confirmación SI/NO 
# S: quita la tupla del contacto de la lista del grupo si se confirma

def eliminar_contacto_de_grupo():

    # Comprobar que exista una configuración guardada
    if len(configuracion) == 0:
        print("Primero debe configurar la lista de contactos.")
        return

    # Repetir la ventana hasta que el usuario escriba C en el nombre del grupo
    while True:
        print("\n      ADMINISTRAR GRUPOS DE CONTACTOS")
        print("      Eliminar contactos de los grupos\n")

        # Solicitar y validar el nombre del grupo
        while True:
            nombre_grupo = input("Nombre del grupo: ").strip()

            # Regresar al menú anterior
            if nombre_grupo == "C":
                return

            posicion_grupo = buscar_grupo(grupos, nombre_grupo)

            if posicion_grupo == -1:
                print("ESTE GRUPO NO EXISTE, NO PUEDE ELIMINARLE CONTACTOS")

            else:
                break

        # Repetir teléfono y área si el contacto no está en el grupo
        while True:

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

            # Buscar el contacto dentro de la lista de ese grupo
            posicion_en_grupo = buscar_contacto_en_grupo(contactos_por_grupo[posicion_grupo], telefono, area)

            if posicion_en_grupo == -1:
                print("ESTE CONTACTO NO EXISTE EN EL GRUPO, NO PUEDE ELIMINARLO")

            else:
                break

        # Mostrar el nombre del área y el nombre del contacto
        posicion = buscar_contacto(contactos, area, telefono)
        posicion_area = buscar_area(areas, area)
        print("Nombre del área:", areas[posicion_area][1])
        print("Nombre contacto:", contactos[posicion][3])

        # Confirmar si desea eliminar o cancelar
        opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

        while opcion != "A" and opcion != "C":
            print("ERROR: OPCIÓN NO VÁLIDA.")
            opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

        if opcion == "A":

            # Pedir confirmación de eliminar
            confirmacion = input("CONFIRMA LA ELIMINACIÓN (SI/NO): ")

            while confirmacion != "SI" and confirmacion != "NO":
                print("ERROR: OPCIÓN NO VÁLIDA.")
                confirmacion = input("CONFIRMA LA ELIMINACIÓN (SI/NO): ")

            if confirmacion == "SI":
                # Solo se quita la tupla del grupo; el contacto sigue en contactos
                contactos_por_grupo[posicion_grupo].pop(posicion_en_grupo)
                print("Contacto eliminado del grupo correctamente.")

            else:
                print("Eliminación cancelada")

        else:
            print("Eliminación cancelada")

# ---------------------------------- FIN ADMINISTRAR GRUPOS DE CONTACTOS -------------------------------------------

# ---------------------------------- MENU ADMINISTRAR GRUPOS DE CONTACTOS -------------------------------------------

# MENÚ ADMINISTRAR GRUPOS DE CONTACTOS
# Muestra las opciones de grupos y llama a la que se elija
# E: la opción del menú 
# S: ejecuta la opción elegida; con 0 vuelve al menú principal

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
                agregar_contacto_a_grupo()
            case "3":
                modificar_grupo()
            case "4":
                eliminar_grupo()
            case "5":
                eliminar_contacto_de_grupo()
            case "0":
                break
            case _:
                print("ERROR: OPCIÓN NO VÁLIDA")  

# ---------------------------------- FIN MENU ADMINISTRAR GRUPOS DE CONTACTOS -------------------------------------------

# ---------------------------------- INICIO LISTA DE CONTACTOS -------------------------------------------
# ------------- FUNCIONES AUXILIARES DE LA LISTA DE CONTACTOS -------------

# COINCIDE CON FILTRO
# Revisa si un dato cumple un filtro, sin importar mayúsculas y aceptando el comodín %
# E: el dato y el filtro (textos)
# S: True si cumple, False si no (un filtro vacío siempre cumple)

def coincide_con_filtro(dato, filtro):
    if filtro == "":
        cumple = True

    else:
        # Separa el filtro en los pedazos que quedan entre los %
        partes = filtro.split("%")

        # re.escape hace que símbolos como . o ( se tomen como texto normal
        for i in range(len(partes)):
            partes[i] = re.escape(partes[i])

         # Cada % se cambia por .* (cualquier cantidad de caracteres)
        patron = ".*".join(partes)

        # fullmatch revisa todo el dato y re.IGNORECASE ignora mayúsculas y minúsculas
        # Si no coincide devuelve None, por eso se compara con "is not None"
        cumple = re.fullmatch(patron, dato, re.IGNORECASE) is not None

    return cumple

# CONTACTO CUMPLE GRUPO
# Revisa si un contacto está en algún grupo cuyo nombre cumple el filtro
# E: las listas grupos y contactos_por_grupo, el teléfono, el área y el filtro de grupo
# S: True si cumple, False si no (un filtro vacío siempre cumple)

def contacto_cumple_grupo(grupos, contactos_por_grupo, telefono, area, filtro_grupo):
    if filtro_grupo == "":
        cumple = True

    else:
        cumple = False

        for i in range(len(grupos)):
            # [i] indica cuál grupo se está revisando (grupos y contactos_por_grupo van en paralelo)
            if coincide_con_filtro(grupos[i], filtro_grupo):
                if buscar_contacto_en_grupo(contactos_por_grupo[i], telefono, area) != -1:
                    cumple = True

    return cumple

# FILTRAR CONTACTOS
# Busca los contactos que cumplen los seis filtros a la vez
# E: las listas contactos, grupos y contactos_por_grupo, y la lista con los 6 filtros
# S: una lista con los contactos que cumplen todos los filtros

def filtrar_contactos(contactos, grupos, contactos_por_grupo, filtros):
    encontrados = []

    for i in range(len(contactos)):
        # [i] indica cuál contacto se está revisando
        contacto = contactos[i]

        # Teléfono, área y fecha pueden ser números, por eso se pasan a texto con str()
        # Posiciones: [0] teléfono, [1] área, [3] nombre, [6] fecha, [7] pasatiempos
        # El contacto solo se agrega si cumple los 6 filtros a la vez (por eso los and)
        if (coincide_con_filtro(contacto[3], filtros[0]) and
            coincide_con_filtro(str(contacto[0]), filtros[1]) and
            coincide_con_filtro(str(contacto[1]), filtros[2]) and
            coincide_con_filtro(str(contacto[6]), filtros[3]) and
            coincide_con_filtro(contacto[7], filtros[4]) and
            contacto_cumple_grupo(grupos, contactos_por_grupo, contacto[0], contacto[1], filtros[5])):

            encontrados.append(contacto)

    return encontrados

# NOMBRE DEL TIPO
# Da la descripción de un tipo de teléfono (M -> Móvil, C -> Casa...)
# E: el código del tipo
# S: la descripción, o el mismo código si no existe

def nombre_tipo(tipo):
    nombre = tipo

    # TIPOS_TELEFONO = ("M", "Móvil", "C", "Casa", "T", "Trabajo", "O", "Otro")
    # Por eso se recorre de 2 en 2 (0, 2, 4, 6) y el nombre está en i + 1
    for i in range(0, len(TIPOS_TELEFONO), 2):
        if TIPOS_TELEFONO[i] == tipo:
            nombre = TIPOS_TELEFONO[i + 1]

    return nombre


# TEXTO PARA EL PDF
# Pasa un dato a texto y cambia por ? lo que el PDF no puede mostrar
# E: un dato del contacto (texto o número)
# S: el dato como texto listo para el PDF

def texto_pdf(dato):
    # Se pasa a texto porque algunos datos son números (por ejemplo, la fecha 0)
    texto = str(dato)

    # La letra del PDF solo conoce letras, números, tildes, ñ, ¿ y ¡ (latin-1)
    # encode cambia por ? lo que no conoce (como un emoji) y decode lo deja como texto otra vez
    texto = texto.encode("latin-1", "replace").decode("latin-1")
    return texto


# EMITIR LISTADO
# Crea el PDF con los contactos que cumplen los filtros
# E: la lista de contactos encontrados
# S: guarda lista_contactos_N.pdf en la carpeta del programa

def emitir_listado(encontrados):
    if len(encontrados) == 0:
        print("No hay contactos que cumplan con los filtros.")

    # Antes de usar fpdf2 se revisa que esté instalada (si no está, find_spec devuelve None)
    elif importlib.util.find_spec("fpdf") is None:
        print("ERROR: Falta instalar la biblioteca fpdf2. Escriba en la terminal: python -m pip install fpdf2")

    else:
        
        from fpdf import FPDF

        # Documento nuevo en hoja horizontal ("L") para que quepan las 8 columnas
        pdf = FPDF(orientation="L")
        pdf.add_page()

        # Título en negrita ("B") y centrado ("C")
        # new_x y new_y hacen que lo siguiente se escriba en la línea de abajo
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, "LISTA DIGITAL DE CONTACTOS - LISTA DE CONTACTOS", new_x="LMARGIN", new_y="NEXT", align="C")

        # Cantidad de contactos con letra normal
        pdf.set_font("Helvetica", size=10)
        pdf.cell(0, 8, "Contactos encontrados: " + str(len(encontrados)), new_x="LMARGIN", new_y="NEXT")

        # Tabla con letra más pequeña; col_widths es el ancho de cada columna
        # Todo lo que va dentro del with son las filas; al terminar, la tabla se dibuja en el PDF
        pdf.set_font("Helvetica", size=8)
        with pdf.table(col_widths=(35, 30, 18, 45, 45, 22, 40, 42), text_align="LEFT") as tabla:

            # La primera fila es el encabezado y se repite en cada página
            encabezado = tabla.row()
            for titulo in ("Nombre", "Teléfono y área", "Tipo", "Correo electrónico",
                           "Dirección física", "Fecha de nacimiento", "Pasatiempos", "Notas"):
                encabezado.cell(texto_pdf(titulo))

            # Una fila por cada contacto, con un dato en cada celda
            for i in range(len(encontrados)):
                contacto = encontrados[i]
                fila = tabla.row()
                fila.cell(texto_pdf(contacto[3]))                                       # nombre
                fila.cell(texto_pdf(str(contacto[0]) + " (" + str(contacto[1]) + ")"))  # teléfono (área)
                fila.cell(texto_pdf(nombre_tipo(contacto[2])))                          # tipo
                fila.cell(texto_pdf(contacto[4]))                                       # correo
                fila.cell(texto_pdf(contacto[5]))                                       # dirección
                fila.cell(texto_pdf(contacto[6]))                                       # fecha de nacimiento
                fila.cell(texto_pdf(contacto[7]))                                       # pasatiempos
                fila.cell(texto_pdf(contacto[8]))                                       # notas

        # Carpeta donde está contactos.py
        carpeta = os.path.dirname(os.path.abspath(__file__))

        # Busca un nombre libre (lista_contactos_1.pdf, _2, ...) para no reemplazar un listado anterior
        numero = 1
        ruta = os.path.join(carpeta, "lista_contactos_" + str(numero) + ".pdf")
        while os.path.exists(ruta):
            numero = numero + 1
            ruta = os.path.join(carpeta, "lista_contactos_" + str(numero) + ".pdf")

        # Guarda el PDF y muestra dónde quedó
        pdf.output(ruta)

        # os.path.basename(ruta) muestra solo el nombre del archivo, sin la carpeta
        print("Contactos encontrados:", len(encontrados))
        print("Listado generado:", os.path.basename(ruta))
        print("Se guardó en la carpeta:", carpeta)

# ------------- LISTA DE CONTACTOS -------------

# LISTA DE CONTACTOS
# Pide los 6 filtros y emite el listado si se acepta; con C en el primer filtro vuelve al menú
# E: los 6 filtros y la opción A/C (se piden con input)
# S: emite el listado en PDF o lo cancela

def lista_contactos():

    # Repetir la ventana hasta que el usuario escriba C en el primer filtro
    while True:
        print("\n      LISTA DE CONTACTOS\n")

        nombre = input("FILTROS: Nombre contacto: ").strip()

        # Regresar al menú anterior
        if nombre == "C":
            return

        telefono = input("Teléfono: ").strip()
        area = input("Área: ").strip()
        fecha = input("Fecha de nacimiento: ").strip()
        pasatiempos = input("Pasatiempos: ").strip()
        grupo = input("Grupo: ").strip()

        # Aceptar o cancelar la emisión del listado
        opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

        while opcion != "A" and opcion != "C":
            print("ERROR: OPCIÓN NO VÁLIDA.")
            opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")

        if opcion == "A":
            filtros = [nombre, telefono, area, fecha, pasatiempos, grupo]
            encontrados = filtrar_contactos(contactos, grupos, contactos_por_grupo, filtros)
            emitir_listado(encontrados)

        else:
            print("Listado cancelado")

# ---------------------------------- FIN LISTA DE CONTACTOS -------------------------------------------

# ---------------------------------- INICIO ACERCA DE -------------------------------------------

# ACERCA DE
# Muestra el nombre del programa, la versión, la fecha de creación y el autor
# E: nombre, versión, fecha y autor
# S: muestra los datos en pantalla

def acerca_de(nombre, version, fecha, autor):
    print("\n      ACERCA DE\n")
    print("Programa:", nombre)
    print("Versión:", version)
    print("Fecha de creación:", fecha)
    print("Autor:", autor)

# ---------------------------------- FIN ACERCA DE -------------------------------------------

# ---------------------------------- INICIO AYUDA -------------------------------------------

# AYUDA
# Abre el manual de usuario en PDF
# E: el nombre del archivo del manual
# S: abre el manual, o muestra un error si no está en la carpeta

def ayuda(nombre_archivo):
    print("\n      AYUDA\n")

    # Carpeta donde está contactos.py (ahí debe estar el manual)
    carpeta = os.path.dirname(os.path.abspath(__file__))

    # Une la carpeta con el nombre del manual para tener la ruta completa
    ruta = os.path.join(carpeta, nombre_archivo)

    # Revisa que el manual exista antes de abrirlo
    if os.path.exists(ruta):
        print("Abriendo el manual de usuario...")
        # Abre el PDF con el visor de Windows; el programa vuelve al menú sin esperar
        os.startfile(ruta)
    else:
        print("ERROR: No se encontró el manual de usuario (" + nombre_archivo + ").")
        print("Debe estar en la misma carpeta que contactos.py.")

# ---------------------------------- FIN AYUDA -------------------------------------------

#  ---------------------------------- MENU PRINCIPAL -------------------------------------------

# MENÚ PRINCIPAL
# Muestra el menú principal y llama a la opción que se elija
# E: la opción del menú 
# S: ejecuta la opción elegida; con 0 termina el programa

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
                lista_contactos()
            case "6":
                ayuda("manual_de_usuario_contactos.PDF")
            case "7":
                acerca_de("Lista Digital de Contactos", "1.0", "04/10/2026", "Amy Jimena Morataya Sandoval")
            case "0":
                print("Programa finalizado.")
                break
            case _:
                print("ERROR: OPCIÓN NO VÁLIDA")

#  ---------------------------------- FIN MENU PRINCIPAL -------------------------------------------

menu_principal() # Mostrará el menú principal al ejecutar el programa