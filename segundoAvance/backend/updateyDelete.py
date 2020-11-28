import pymysql
from logic.dx_logic import Logic
from datetime import datetime


class UpdateYDelete(Logic):
    def __init__(self):
        super().__init__()

    def updateObjeto(self, campo, nombreActual, nuevoNombre):

        try:
            database = self.database
            current_Date = datetime.now()
            formatted_date = current_Date.strftime("%Y-%m-%d %H:%M:%S")

            sql = f"""UPDATE productos SET `{campo}` = '{nuevoNombre}',
            ultima_actualizacion = '{formatted_date}' WHERE nombre = '{nombreActual}';"""
            
            count = database.executeNonQueryRows(sql)

            if count > 0:
                print("El campo ha sido actualizado correctamente")
            else:
                print("no se pudo actualizar, intente de nuevo")

        except Exception:
            print()
            print("no se pudo actualizar correctamente")

        finally:
            pass

    def deleteProducto(self, nombre):

        try:
            database = self.database
            sql = f"DELETE FROM productos WHERE nombre = '{nombre}'"

            database.executeNonQueryRows(sql)

        except Exception:
            print()
            print("No se pudo eliminar, ya se han hecho compras con ese producto")

        finally:
            pass

    def deleteProductoCarrito(self, idNombre, idProducto):

        try:
            database = self.database
            sql = f"DELETE FROM carrito WHERE id_cliente = '{idNombre}' and id_producto = '{idProducto}'"

            rowCount = database.executeNonQueryRows(sql)
            if rowCount > 0:
                print(rowCount, "producto eliminado del carrito")
            else: 
                print()
                print("No se pudo eliminar el porducto del carrito\n")
        
        except Exception:
            print()
            print("No se pudo eliminar el porducto del carrito")

        finally:
            pass
