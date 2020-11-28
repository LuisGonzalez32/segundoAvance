from datetime import datetime
from logic.dx_logic import Logic
from prettytable import PrettyTable

class ComprarDb(Logic):
    def __init__(self):
        super().__init__()

    def verificarCarrito(self, idNombre):
        
        try:
            database = self.database
            sql = f"""select * from carrito where id_cliente = {idNombre}"""
                
            record = database.executeQueryRows(sql)

            if record:
                return record
            else:
                return None
            
        except Exception:
            print()
            #print("No hay productos en el carrito")
            return None

        finally:
            pass

    # inserta la tabla detallesPago
    def detallesPago(self, idNombre, pais, ciudad, direccion, tarjeta):  
        try:
            database = self.database
            current_Date = datetime.now()
            date = current_Date.strftime("%Y-%m-%d %H:%M:%S")

            sql = f"""INSERT INTO detalles_pago
            (id, id_cliente, pais, ciudad, direccion, tarjeta_credito, hora_compra) VALUES (0,
            '{idNombre}', '{pais}', '{ciudad}', '{direccion}', {tarjeta}, '{date}') """

            database.executeNonQueryBool(sql)

        except Exception:
            print()
            print("No se pudo obtener los datos del pago")

        finally:
            pass
        
    # saca el ultimo id de la tabla detallesPago  
    def idDetallesPago(self):
        
        try:
            database = self.database          
            sql = f"""SELECT max(id) as id FROM detalles_pago"""
                
            record = database.executeQueryRows(sql)

            for detallesPago in record:
                return detallesPago["id"]

        except Exception:
            print()
            print("no se pudo seleccionar el ultimo de id_detalles_pago")

        finally:
            pass

        
    def pago(self, idNombre, idDetalles):
        
        try:
            database = self.database
            sql = f"""select * from carrito where id_cliente = {idNombre}"""
                
            record = database.executeQueryRows(sql)

            if record:
                for carrito in record:
                    self.compras(0, idDetalles, carrito["id_producto"], carrito["cantidad"], carrito["costo_total"])
                print()
                print("La compra se guardo\n")
                
            else:
                print()
                print("No hay productos en el carrito, no se puede hacer la compra\n")
                return None
            
        except Exception:
            print()
            print("no se pudo hacer el pago")

        finally:
            pass

        
    def compras(self, id, idDetalles, idProducto, cantidad, total):
        
        try:
            database = self.database
            sql = f"""INSERT INTO compras
            (id,id_detalles_pago,id_producto,cantidad,costo_total)
            VALUES ({id}, {idDetalles}, {idProducto}, {cantidad}, {total}) """
            
            database.executeNonQueryBool(sql)

        except Exception:
            print()
            print("No se pudo hacer em metodo compras")

        finally:
            pass


    def sumarCosto(self, idNombre):

        try:    
            database = self.database
            costo_total = 0
            sql = f"""select * from carrito where id_cliente = {idNombre} """
            
            record = database.executeQueryRows(sql)

            for carrito in record:
                costo_total = costo_total + carrito["costo_total"]

            return costo_total

        except Exception:
            print()
            print("No se pudo hacer em metodo sumarCosto")

        finally:
            pass


    def factura(self, idDetalles, costo):
        try:
            database = self.database
            sql = f"""INSERT INTO factura
            (id_detalles_pago,total_pago)
            VALUES ({idDetalles}, {costo}) """
                
            database.executeNonQueryBool(sql)

        except Exception:
            print()
            print("No se pudo hacer em metodo factura")

        finally:
            pass

 #------------------------------------------------------------------------------------------------------------------------

    def getCantidadActual(self, idProducto):
         
        try:
            database = self.database
            sql = f"""select * from productos where id = {idProducto}"""
            
            record = database.executeQueryRows(sql)

            for producto in record:
                return producto["cantidad_disponible"]

        except Exception:
            print()
            print("No se pudo hacer em metodo getCantidadActual")

        finally:
            pass


    def restarCantidadProducto(self, idNombre):
        try:
            database = self.database

            sql = f"""select * from carrito where id_cliente = {idNombre}"""
            
            record = database.executeQueryRows(sql)

            for carrito in record:
                cantidadActual = self.getCantidadActual(carrito["id_producto"])
                self.updateCantidad(carrito["id_producto"], cantidadActual, carrito["cantidad"])

        except Exception:
            print()
            print("No se pudo hacer em metodo restarCantidadProducto")

        finally:
            pass
        
    def updateCantidad(self, idProducto, cantidadActual, cantidadComprada):
        
        try:
            database = self.database
            current_Date = datetime.now()
            date = current_Date.strftime("%Y-%m-%d %H:%M:%S")
        
            sql = f"""Update productos set cantidad_disponible = {cantidadActual - cantidadComprada},
            ultima_actualizacion = '{date}' where id = {idProducto}"""

            row = database.executeNonQueryRows(sql)

        except Exception:
            print()
            print("No se pudo hacer em metodo updateCantidad")
        
        

    

 #...........................................................................................................
    
    def truncateCarrito(self, idNombre):
        try:
            database = self.database
            sql = f"""DELETE FROM carrito WHERE id_cliente = {idNombre}"""
            
            row = database.executeNonQueryRows(sql)

        except Exception:
            print()
            print("No se pudo hacer em metodo truncateCarrito")

        finally:
            pass

    



    def verCompras(self):
        database = self.database
        sql = "SELECT * FROM tienda.view_compras order by hora_compra"
        
        record = database.executeQueryRows(sql) # fetchall
        x = PrettyTable(["nombre", "producto", "cantidad", "costo total", "tarjeta de credito", 
                         "pais", "ciudad", "direccion", "hora de compra"])

        if not record:
            print("No hay ningun producto disponible")
            
        else:            
            for compras in record:
                x.add_row([compras["nombreCliente"], compras["nombreProducto"], compras["cantidad"], 
                           compras["costo_total"], compras["tarjeta_credito"], compras["pais"], 
                           compras["ciudad"], compras["direccion"], compras["hora_compra"]])

            print(x)


    def verComprasCliente(self, idCliente):
        database = self.database
        sql = f"select * from view_compras where idCliente = {idCliente}"
        
        record = database.executeQueryRows(sql) # fetchall
        x = PrettyTable(["producto", "cantidad", "costo total", "tarjeta de credito", "pais", "ciudad", 
                        "direccion", "hora de compra"])

        if not record:
            print("No hay ningun producto disponible")
            
        else:            
            for compras in record:
                x.add_row([compras["nombreProducto"], compras["cantidad"], 
                           compras["costo_total"], compras["tarjeta_credito"], compras["pais"], 
                           compras["ciudad"], compras["direccion"], compras["hora_compra"]])

            print(x)
        
