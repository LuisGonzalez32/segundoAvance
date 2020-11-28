import pymysql
from logic.dx_logic import Logic
from datetime import datetime
from prettytable import PrettyTable

class InsertProducto(Logic):
    def __init__(self):
        super().__init__()

   # inserta la categoria a la tabla categorias
    def insertarCategoria(self, categoria):
        
        database = self.database
        sql = f"""INSERT INTO categorias
        (categoria) VALUES ('{categoria}') """

        categoria = database.executeNonQueryBool(sql)
        if categoria == True:
            print("")
            print("La categoria ha sido insertada correctamente")

        


    # valida si la categoria esta en la tabla categorias, si esta devuelve su id
    def validarCategoria(self, categoria):
        
        try:

            database = self.database
            sql = f"""select * from categorias where categoria = '{categoria}'"""
            
            record = database.executeQueryRows(sql)

            for row in record:
                if row["id"]:
                    return row["id"]
                elif not row["id"]:
                    pass

        except pymysql.connector.Error as error:
                print("La informacion no es correcta, intente otravez")

        finally:
            pass


    # ver todas las categorias
    def viewCategorias(self):
        
        database = self.database
        sql = "select * from categorias"
        
        record = database.executeQueryRows(sql) # fetchall
        x = PrettyTable(["categorias"])

        if not record:
            print("No hay ningun producto disponible")
            return None
        else:            
            for categoria in record:
                x.add_row([categoria["categoria"]])

            print(x)

        
    

    # inserta un nuevo producto
    def insertarProducto(self, nombre, id_categoria, descripcion, precio, cantidad):
    
        database = self.database
        current_Date = datetime.now()
        date = current_Date.strftime("%Y-%m-%d %H:%M:%S")
            
            
        sql = f"""INSERT INTO productos
        (nombre,id_categoria,descripcion,precio,cantidad_disponible,
        ultima_actualizacion) VALUES (
        '{nombre}',{id_categoria}, '{descripcion}', {precio}, {cantidad}, '{date}') """

            
        producto = database.executeNonQueryBool(sql)
        if producto == True:
            print("")
            print("El producto ha sido insertado correctamente")
    

