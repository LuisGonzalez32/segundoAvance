from backend.carrito import CarritoDb
carrito = CarritoDb()


from backend.updateyDelete import UpdateYDelete
UpdateyDelete = UpdateYDelete()

class Carrito():
    def __init__(self):
        super().__init__()


    def getCarrito(self, idNombre):

        nombreProducto = input("ponga el nombre del producto que quiere: ")
        idProducto = carrito.getIdProducto(nombreProducto)
        while (idProducto is None):
            print("")
            nombreProducto = input("Error, ponga un nombre que este en la lista: ")
            idProducto = carrito.getIdProducto(nombreProducto)
        cantidad = int(input("ponga la cantidad que quiere: "))
        costoTotal = carrito.costoTotalProducto(cantidad, nombreProducto)
        nuevaCantidad = carrito.getCantidadCarrito(cantidad, nombreProducto)

        while nuevaCantidad < 0:
            cantidad = int(input("No hay existencias, ponga otra cantidad: "))
            costoTotal = carrito.costoTotalProducto(cantidad, nombreProducto)
            nuevaCantidad = carrito.getCantidadCarrito(cantidad, nombreProducto)

        carrito.agregarCarrito(idNombre, idProducto, cantidad, costoTotal)


    def deleteCarrito(self, idNombre):
        producto = input("Ponga el producto que quiere eliminar de su carrito: ")
        idProducto = carrito.getIdProducto(producto)
        while (idProducto is None):
            print("")
            nombreProducto = input("Error, ponga un nombre que este en la lista: ")
            idProducto = carrito.getIdProducto(nombreProducto)
        
        UpdateyDelete.deleteProductoCarrito(idNombre, idProducto)
        