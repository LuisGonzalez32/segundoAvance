from backend.updateyDelete import UpdateYDelete
updateyDelete = UpdateYDelete()

from backend.buscarProducto import BuscarProductoDb
buscar = BuscarProductoDb()

class UpdateYDeleteProducto():
    def __init__(self):
        super().__init__()

    def getUpdateProducto(self):
        print("Oprima 1 si quiere cambiar el nombre del producto")
        print("Oprima 2 si quiere cambiar la descripcion del producto")
        print("Oprima 3 si quiere cambiar el precio del producto")
        print("Oprima 4 si quiere cambiar las existencias del producto")
        print("")
        opcion = input("")
        if opcion == "1":
            buscar.seleccionarTodosProductos()
            nombreActual = input("Seleccione el nombre actual: ")
            nuevoNombre = input("Ponga el nuevo nombre: ")
            nombre = "nombre"
            updateyDelete.updateObjeto(nombre, nombreActual, nuevoNombre)
        elif opcion == "2":
            buscar.seleccionarTodosProductos()
            nombreActual = input("Seleccione el nombre actual: ")
            nuevaDescripcion = input("Ponga la nueva descripcion: ")
            descripcion = "descripcion"
            updateyDelete.updateObjeto(descripcion, nombreActual, nuevaDescripcion)
        elif opcion == "3":
            buscar.seleccionarTodosProductos()
            nombreActual = input("Seleccione el nombre actual: ")
            nuevoPrecio = input("Ponga el nuevo precio: ")
            precio = "precio"
            updateyDelete.updateObjeto(precio, nombreActual, nuevoPrecio)
        elif opcion == "4":
            buscar.seleccionarTodosProductos()
            nombreActual = input("Seleccione el nombre actual: ")
            nuevaCantidad = input("Ponga la nueva cantidad: ")
            cantidad = "cantidad_disponible"
            updateyDelete.updateObjeto(cantidad, nombreActual, nuevaCantidad)


    def getDeleteProducto(self):
        print("")
        nombre = input("ponga el nombre del producto que quiere eliminar: ")
        updateyDelete.deleteProducto(nombre)
