import sqlite3


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
                break

class Alumno:
    def __init__(self, nombre_alumno, apellido_alumno, dni_alumno, direccion_alumno, telefono_alumno, mail_alumno, nacionalidad_alumnno, residencia_alumno, 
                    hermanos_alumno, tel_padre_alumno, tel_madre_alumno, tel_adicional_alumno):
        self.nombre_alumno = nombre_alumno
        self.apellido_alumno = apellido_alumno
        self.dni_alumno = dni_alumno
        self.direccion_alumn = direccion_alumno
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
        conexion.miCursor.execute("INSERT INTO ALUMNOS VALUES('{}', '{}')".format(self.nombre_alumno, self.apellido_alumno))
        conexion.miConexion.commit()
        conexion.cerrarConexion()
    
    
class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Colegio Chester")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()


            
programa = ProgramaPrincipal()
programa.menu()