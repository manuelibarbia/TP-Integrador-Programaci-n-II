import sqlite3

# miConexion = sqlite3.connect("Colegio_Chester")
# miCursor = miConexion.cursor()
# # miCursor.execute("CREATE TABLE ALUMNOS (LEGAJO VARCHAR(7), NOMBRE VARCHAR(30), APELLIDO VARCHAR(30), DNI VARCHAR(10), DIRECCIÓN VARCHAR(50), TEL_ALUMNO VARCHAR(30), MAIL VARCHAR(30), NACIONALIDAD VARCHAR(20), RESIDENCIA VARCHAR(20), HERMANOS INTEGER, TEL_PADRE VARCHAR(30), TEL_MADRE VARCHAR(30), TEL_ADI VARCHAR(30))")
# # miCursor.execute("CREATE TABLE DOCENTES (LEGAJO VARCHAR(7), NOMBRE VARCHAR(30), APELLIDO VARCHAR(30), DOMICILIO VARCHAR(30), DNI VARCHAR(10), TEL_DOCENTE VARCHAR(30), TEL_URGENCIA VARCHAR(30), TITULO VARCHAR(30), MATERIA VARCHAR (30))")
# # miCursor.execute("CREATE TABLE PERSONAL (LEGAJO VARCHAR(7), NOMBRE VARCHAR(30), APELLIDO VARCHAR(30), TELEFONO VARCHAR(30), DOMICILIO VARCHAR(30), TAREA VARCHAR(20))")
# miCursor.execute("CREATE TABLE DIRECTIVOS (LEGAJO VARCHAR(7), NOMBRE VARCHAR(30), APELLIDO VARCHAR(30), DNI VARCHAR(10), DOMICILIO VARCHAR(30), TEL_DIRECTIVO VARCHAR(30), TEL_URGENCIA VARCHAR(30), ES_DOCENTE VARCHAR(3))")
# miConexion.commit()
# miConexion.close()

# miConexion = sqlite3.connect("Colegio_Chester")
# miCursor = miConexion.cursor()
# miCursor.execute("DELETE FROM ALUMNOS WHERE LEGAJO = 123")
# miConexion.commit()
# miConexion.close()

# miConexion = sqlite3.connect("Colegio_Chester")
# miCursor = miConexion.cursor()
# miCursor.execute("DELETE FROM DOCENTES WHERE LEGAJO = 124")
# miConexion.commit()
# miConexion.close()

class ProgramaPrincipal:
    
    def menu(self):
        while True:
            print("Menu de opciones Colegio Chester")
            print("1- Cargar alumno")
            print("2- Cargar docente")
            print("3- Cargar personal")
            print("4- Cargar director")
            print("0- Salir de menu")
            nro = int(input("Elija una opción: "))

            if nro == 1:
                nombre_alumno = input("Ingrese el nombre del alumno: ")
                apellido_alumno = input("Ingrese el apellido del alumno: ")
                dni_alumno = input("Ingrese el DNI del alumno: ")
                direccion_alumno = input("Ingrese la dirección del alumno: ")
                telefono_alumno = input("Ingrese el telefono del alumno: ")
                mail_alumno = input("Ingrese el mail del alumno: ")
                nacionalidad_alumnno = input("Ingrese la nacionalidad del alumno: ")
                residencia_alumno = input("Ingrese el lugar de residencia del alumno: ")
                hermanos_alumno = int(input("Ingrese la cantidad de hermanos inscriptos del alumno: "))
                tel_padre_alumno = input("Ingrese el teléfono del padre del alumno: ")
                tel_madre_alumno = input("Ingrese el teléfono de la madre del alumno: ")
                tel_adicional_alumno = input("Ingrese teléfono adicional de un familiar del alumno: ")

                nuevo_alumno = Alumno(nombre_alumno, apellido_alumno, dni_alumno, direccion_alumno, telefono_alumno, mail_alumno, nacionalidad_alumnno, residencia_alumno, 
                    hermanos_alumno, tel_padre_alumno, tel_madre_alumno, tel_adicional_alumno)
                nuevo_alumno.cargar_alumno()
                print("Alumno cargado exitosamente")
                self.menu()
            elif nro == 2:
                nombre_docente = input("Ingrese el nombre del docente: ")
                apellido_docente = input("Ingrese el apellido del docente: ")
                domicilio_docente = input("Ingrese el domicilio del docente: ")
                dni_docente = input("Ingrese el DNI del docente: ")
                telefono_docente = input("Ingrese el teléfono del docente: ")
                telefono_urgencia = input("Ingrese el teléfono de urgencia del docente: ")
                titulo_docente = input("Ingrese, si lo hay, título del docente, caso contrario ingrese NO: ")
                materia_docente = input("Ingrese la materia que enseña el docente: ")

                nuevo_docente = Docente(nombre_docente, apellido_docente, domicilio_docente, dni_docente, telefono_docente, telefono_urgencia, titulo_docente, materia_docente)
                nuevo_docente.cargar_docente()
                print("Docente cargado exitosamente.")
                self.menu()
            elif nro == 3:
                nombre_personal = input("Ingrese el nombre del personal: ")
                apellido_personal = input("Ingrese el apellido del personal: ")
                telefono_personal = input("Ingrese el teléfono del personal: ")
            break

class Alumno:
    def __init__(self, nombre_alumno, apellido_alumno, dni_alumno, direccion_alumno, telefono_alumno, mail_alumno, nacionalidad_alumnno, residencia_alumno, 
                    hermanos_alumno, tel_padre_alumno, tel_madre_alumno, tel_adicional_alumno):
        self.legajo_alumno = 123
        self.nombre_alumno = nombre_alumno
        self.apellido_alumno = apellido_alumno
        self.dni_alumno = dni_alumno
        self.direccion_alumno = direccion_alumno
        self.telefono_alumno = telefono_alumno
        self.mail_alumno = mail_alumno
        self.nacionalidad_alumnno = nacionalidad_alumnno
        self.residencia_alumno = residencia_alumno
        self.hermanos_alumno = hermanos_alumno
        self.tel_padre_alumno = tel_padre_alumno
        self.tel_madre_alumno = tel_madre_alumno
        self.tel_adicional_alumno = tel_adicional_alumno
        
    def cargar_alumno(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("INSERT INTO ALUMNOS VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.legajo_alumno, self.nombre_alumno, self.apellido_alumno, self.dni_alumno, self.direccion_alumno, self.telefono_alumno, self.mail_alumno, self.nacionalidad_alumnno, self.residencia_alumno, self.hermanos_alumno, self.tel_padre_alumno, self.tel_madre_alumno, self.tel_adicional_alumno))
        conexion.miConexion.commit()
        conexion.cerrarConexion()

class Docente:
    def __init__(self, nombre_docente, apellido_docente, domicilio_docente, dni_docente, telefono_docente, telefono_urgencia, titulo_docente, materia_docente):
        self.legajo_docente = 124
        self.nombre_docente = nombre_docente
        self.apellido_docente = apellido_docente
        self.domicilio_docente = domicilio_docente
        self.dni_docente = dni_docente
        self.telefono_docente = telefono_docente
        self.telefono_urgencia = telefono_urgencia
        self.titulo_docente = titulo_docente
        self.materia_docente = materia_docente

    def cargar_docente(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("INSERT INTO DOCENTES VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.legajo_docente, self.nombre_docente, self.apellido_docente, self.domicilio_docente, self.dni_docente, self.telefono_docente, self.telefono_urgencia, self.titulo_docente, self.materia_docente))
        conexion.miConexion.commit()
        conexion.cerrarConexion()

class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Colegio_Chester")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()


            
programa = ProgramaPrincipal()
programa.menu()