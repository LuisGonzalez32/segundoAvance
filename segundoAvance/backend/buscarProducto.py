from logic.dx_logic import Logic
from prettytable import PrettyTable

class BuscarProductoDb(Logic):
    def __init__(self):
        super().__init__()


    def getAllCategorias(self):

        database = self.database               # el select esta asi porque solo queremos categorias que tengan productos
        sql = """select distinct categorias.categoria   
        from categorias inner join productos
        on productos.id_categoria = categorias.id"""

        record = database.executeQueryRows(sql) # fetchall
        x = PrettyTable(["categorias"])

        if not record:
            print("No hay ningun producto disponible")
            return None
        else:            
            for categoria in record:
                x.add_row([categoria["categoria"]])

            print(x)


    def getIdCategoria(self, categoria):     

        
        database = self.database     
        sql = f"""select * from categorias
        where categoria =  '{categoria}'"""
            
        record = database.executeQueryRows(sql) # fetchall

        if not record:
            print("Esa categoria no existe")
            return None
        else:            
            for producto in record:
                return producto["id"]
                
            return True


    # para buscar un producto por categorias
    def getProducto(self, idCategoria):     

        database = self.database     
        sql = f"""select * from productos
        where id_categoria =  {idCategoria}"""
        
        record = database.executeQueryRows(sql) # fetchall
        x = PrettyTable(["productos"])

        if not record:
            print("No hay ningun producto disponible")
            return None
        else:            
            for producto in record:
                if producto["cantidad_disponible"] > 0:
                    x.add_row([producto["nombre"]])
            

            print(x)
            return True

            
            

        

