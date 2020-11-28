from datetime import datetime
from logic.dx_logic import Logic
from prettytable import PrettyTable
from backend.comprar import ComprarDb

comprardb = ComprarDb()

class CarritoDb(Logic):
    def __init__(self):
        super().__init__()    


    def getIdProducto(self, nombre):
        try:
            database = self.database
            sql = f"""select * from productos where nombre = '{nombre}'"""
            
            record = database.executeQueryRows(sql)

            if record:
                for producto in record:
                    return producto["id"]
            else:
                return None

        except Exception:
            print()
            print("El producto no se encuentra en la base de datos")

        finally:
            pass


    # el precio del producto multiplicado por la cantidad de productos
    def costoTotalProducto(self, cantidad, nombreProducto):

        database = self.database
        sql = f"""select * from productos where nombre = '{nombreProducto}'"""
        
        record = database.executeQueryRows(sql)

        for producto in record:
            return cantidad * producto["precio"]

        

    # para verificar si la cantidad que queremos poner en el carrito esta permitida
    def getCantidadCarrito(self, cantidad, nombre):
        
        database = self.database
        sql = f"""select * from productos where nombre = '{nombre}'"""
        
        record = database.executeQueryRows(sql)

        for producto in record:
            return producto["cantidad_disponible"] - cantidad

        
    # agrega el producto al carrito
    def agregarCarrito(self, idCliente, idProducto, cantidad, total):
        
        try:
            database = self.database
            sql = f"""INSERT INTO carrito
            (id_cliente,id_producto,cantidad,costo_total)
            VALUES ({idCliente}, {idProducto}, {cantidad}, {total}) """
                    
            row = database.executeNonQueryBool(sql)

            if row>0:
                print("")
                print("El producto fue agregado al carrito")
                print("")
        
        except Exception:
            print()
            print("No se pudo agregar el producto al carrito")

        finally:
            pass

        

    def verCarrito(self, idCliente):
       
        database = self.database
        sql = f"select * from view_carrito where idCliente = '{idCliente}'"
        
        record = database.executeQueryRows(sql) # fetchall
        x = PrettyTable(["producto", "cantidad", "total"])

        if not record:
            print("No hay ningun producto disponible")
            return None
        else:     

            costoTotal = comprardb.sumarCosto(idCliente)

            for carrito in record:
                x.add_row([carrito["nombreProducto"], carrito["cantidad"], carrito["costo_total"]])

            print(x)
            
            print()
            print("El costo total es ",costoTotal,"\n")
