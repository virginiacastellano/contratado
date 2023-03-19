from tkinter import  messagebox
import sqlite3

#esta esla conexión de la base de datos 
class ConexionDB:
    def __init__(self):
        self.base_datos= 'database/contratos.db'
        self.conexion= sqlite3.connect(self.base_datos)
        self.cursor= self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()


def crear_tabla():
    conexion = ConexionDB()

    sql = '''
        CREATE TABLE contratados(
        id_contratado INTEGER,
        nombre VARCHAR(100),
        cuil VARCHAR(11),
        nacimiento VARCHAR(10),
        monto VARCHAR(100),
        modificacion VARCHAR(100),
        duracion VARCHAR(100),
        area_de_trabajo VARCHAR(100),
        funcion VARCHAR(100),
        domicilio VARCHAR(100),
        telefono VARCHAR(100),
        mail VARCHAR(100),
        otros_trabajos VARCHAR(100),
        PRIMARY KEY(id_contratado AUTOINCREMENT)
    )'''
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Se creo la tabla en la base datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya esta creada'
        messagebox.showwarning(titulo, mensaje)
    



def borrar_tabla():
    conexion = ConexionDB()
 
    #borrar una tabla
    sql= 'DROP TABLE contratados '
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje = 'La tabla de la base de datos se borro con éxito'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Borrar Registro'
        mensaje = 'No hay tabla para borrar'
        messagebox.showerror(titulo, mensaje)

# modelo de empleados 
class Contratado:
    def __init__ (self, nombre , cuil , nacimiento, monto, modificacion, 
                  duracion, area_de_trabajo, funcion,domicilio,telefono,
                  mail, otros_trabajos):
        self.id_contratado= None
        self.nombre = nombre
        self.cuil = cuil
        self.nacimiento = nacimiento
        self.monto = monto
        self.modificacion = modificacion
        self.duracion= duracion
        self.area_de_trabajo = area_de_trabajo
        self.funcion = funcion
        self.domicilio = domicilio
        self.telefono = telefono
        self.mail = mail
        self.otros_trabajos = otros_trabajos

    def __str__ (self):
        return f'Contratado[{self.nombre},{self.cuil},{self.nacimiento},{self.monto},{self.modificacion},{self. duracion}, {self.area_de_trabajo}, {self.funcion},{self.domicilio}, {self.telefono}, {self.mail},{self.otros_trabajos}]'

def guadar(contratado):
    conexion = ConexionDB()

    sql= f"""INSERT INTO contratados (nombre , cuil , nacimiento, monto, modificacion,
            duracion,area_de_trabajo, funcion,domicilio,telefono, mail, otros_trabajos)  
    VALUES('{contratado.nombre}', '{contratado.cuil}','{contratado.nacimiento}', '{contratado.monto}', '{contratado.modificacion}','{contratado.duracion}','{contratado.area_de_trabajo}','{contratado.funcion}','{contratado.domicilio}','{contratado.telefono}','{contratado.mail}','{contratado.otros_trabajos}')"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla de contratados no esta creado en la base de datos'
        messagebox.showerror(titulo, mensaje)

def listar():
    conexion = ConexionDB()
    #recuperacion 
    lista_contratado = []
    sql = 'SELECT * FROM contratados'

    try: 
        conexion.cursor.execute(sql)
        lista_contratado = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro '
        mensaje = 'Crea la tabla en la Base de datos desde inicio'
        messagebox.showwarning(titulo, mensaje)

    return lista_contratado

def editar(contratado, id_contratado):
    conexion = ConexionDB()

    sql = f""" UPDATE contratados 
    SET nombre='{contratado.nombre}' , 
    cuil='{contratado.cuil}' , 
    nacimiento='{contratado.nacimiento}', 
    monto='{contratado.monto}',
    modificacion= '{contratado.modificacion}', 
    duracion='{contratado.duracion}', 
    area_de_trabajo= '{contratado.area_de_trabajo}', 
    funcion= '{contratado.funcion}',
    domicilio= '{contratado.domicilio}',
    telefono='{contratado.telefono}', 
    mail='{contratado.mail}',
    otros_trabajos= '{contratado.otros_trabajos}'
    WHERE id_contratado = {id_contratado} """

    try: 
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except:
        titulo = 'Edición de datos'
        mensaje = 'No se ha podido editar este registro'
        messagebox.showerror(titulo, mensaje)

def eliminar(id_contratado):
    conexion = ConexionDB()
    sql = f'DELETE FROM contratados WHERE id_contratado = {id_contratado}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Eliminar Datos'
        mensaje = 'No se pudo eliminar el registro'
        messagebox.showerror(titulo, mensaje)
