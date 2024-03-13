import os
import pyodbc

# Cambiar los @SQL por las respectivas credenciales que tienes en tu maquina

continuar = True
server = '@SQL_SERVER'
db = 'Crud1'
user = '@SQL_USER'
passw = "@SQL_USER_PASSWROD"


def Limpiar():
    os.system('cls')

def Agregar():
    Limpiar()
    Mostrar()
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+server+'; DATABASE='+db+';UID='+user+';PWD='+passw+';')
        cursor = conexion.cursor()

        cedula = input("Digite aqui la cedula: ")
        nombre = input("Digite aqui el nombre: ")
        apellido = input("Digite aqui el apellido: ")
        edad = input("Digite aqui la edad: ")

        sql = "insert into Datos values ('"+str(cedula)+"','"+str(nombre)+"','"+str(apellido)+"','"+str(edad)+"')"
        cursor.execute(sql)

        conexion.commit()
        conexion.close()

        print("Datos agregados, enter para continuar..")
        input("")
    
    except:
        print("Ha habido un error, volviendo al menu principal, enter para confirmar...")
        input("")

def Modificar():
    Limpiar()
    Mostrar()
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+server+'; DATABASE='+db+';UID='+user+';PWD='+passw+';')
        cursor = conexion.cursor()

        id = input("Digite aqui el id del registro a modificar: ")
        cedula = input("Digite aqui la cedula: ")
        nombre = input("Digite aqui el nombre: ")
        apellido = input("Digite aqui el apellido: ")
        edad = input("Digite aqui la edad: ")

        sql = "update Datos set cedula='"+str(cedula)+"', nombre='"+str(nombre)+"', apellido='"+str(apellido)+"', edad='"+str(edad)+"' where id="+str(id)+""
        cursor.execute(sql)


        conexion.commit()
        conexion.close()

        print("Datos modificados, enter para continuar..")
        input("")
    
    except:
        print("Ha habido un error, volviendo al menu principal, enter para confirmar...")
        input("")


def Eliminar():
    Limpiar()
    Mostrar()
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+server+'; DATABASE='+db+';UID='+user+';PWD='+passw+';')
        cursor = conexion.cursor()

        id = input("Digite aqui el id del registro a eliminar: ")

        sql = "delete from Datos where id="+str(id)+""
        cursor.execute(sql)


        conexion.commit()
        conexion.close()

        print("Datos eliminados, enter para continuar..")
        input("")
    
    except:
        print("Ha habido un error, volviendo al menu principal, enter para confirmar...")
        input("")

def Mostrar():
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+server+'; DATABASE='+db+';UID='+user+';PWD='+passw+';')
        cursor = conexion.cursor()

        sql = "Select * from Datos"
        cursor.execute(sql)

        datos = cursor.fetchall()
        for dato in datos:
            print("-Id:", dato[0], "-Cedula:", dato[1], "-Nombre:", dato[2], "-Apellido:", dato[3], "-Edad:", dato[4],)


        conexion.commit()
        conexion.close()
    
    except:
        print("Ha habido un error, volviendo al menu principal, enter para confirmar...")
        input("")


while continuar:
    os.system('color 0c')
    Limpiar()
    print("Que desea hacer: ")
    print("1. Agregar")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Mostrar registros")
    print("5. Salir")
    tmp = input("Digite aqui la opcion: ")
    if tmp == '1':
        Agregar()
    elif tmp == '2':
        Modificar()
    elif tmp == '3':
        Eliminar()
    elif tmp == '4':
        Mostrar()
        input("Enter para volver...")
    elif tmp == '5':
        print("Gracias por usar el programa, Presione enter para salir...")
        input('')
        continuar = False
        os.system('color 07')
        os.system('cls')
    else:
        print("Lo siento, esa opcion no existe, Presione enter para continuar...")
        input('')

