from backend.buscarProducto import BuscarProductoDb

buscar = BuscarProductoDb()

class BuscarProducto():
    def __init__(self):
        super().__init__()

    
        
        

    def getNombreProducto(self):
        buscar.getAllCategorias()
        opcion = input("seleccione una categoria: ")
        idCategoria = buscar.getIdCategoria(opcion)

        while not idCategoria:
            opcion = input("Error, seleccione una categoria: ")
            idCategoria = buscar.getIdCategoria(opcion)
        buscar.getProducto(idCategoria)
            
