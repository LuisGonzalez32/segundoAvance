from backend.comprar import ComprarDb

comprar = ComprarDb()

class Comprar():
    def __init__(self):
        super().__init__()


    def comprar(self, idNombre):
        carrito = comprar.verificarCarrito(idNombre)

        if carrito is None:
            print("no hay productos en el carrito, no se puede hacer la compra\n")
        else:
            pais = input("Introduzca su pais: ")
            ciudad = input("Introduzca su ciudad: ")
            direccion = input("Introduzca su direccion: ")
            tarjeta = input("Introduzca su tarjeta de credito: ")
            comprar.detallesPago(idNombre, pais, ciudad, direccion, tarjeta)
            idDetalles = comprar.idDetallesPago()
            pago = comprar.pago(idNombre, idDetalles)
            costo = comprar.sumarCosto(idNombre)
            comprar.factura(idDetalles, costo)
            comprar.restarCantidadProducto(idNombre)
            comprar.truncateCarrito(idNombre)
    

