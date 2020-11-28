from backend.insertProducto import InsertProducto
insertProducto = InsertProducto()

class InsertProducto():
    def __init__(self):
        super().__init__()


    def getInsertCategoria(self):
        insertProducto.viewCategorias()
        categoria = input("inserte la nueva categoria: ")
        insertProducto.insertarCategoria(categoria)
        insertProducto.viewCategorias()
        idCategoria = insertProducto.validarCategoria(categoria)
        while (idCategoria is None):
            categoria = input("Error, inserte la nueva categoria: ")
            insertProducto.insertarCategoria(categoria)
            idCategoria = insertProducto.validarCategoria(categoria)
        nombre = input("escriba el nombre del objeto: ")
        descripcion = input("escriba una descripcion del objeto: ")
        precio = float(input("escriba el precio del objeto: "))
        cantidad = int(input("escriba la cantidad de productos: "))
        insertProducto.insertarProducto(nombre, idCategoria, descripcion, precio, cantidad)



    def getInsertProducto(self):
        print("Presione 1 si quiere añadir una nueva categoria: ")
        print("Presione 2 si la categoria ya existe: ")
        opcion = input("")
        if opcion== "1":
            self.getInsertCategoria()
        elif opcion == "2":
            insertProducto.viewCategorias()
            print("")
            categoria = input("Escriba la categoria del producto: ")
            idCategoria = insertProducto.validarCategoria(categoria)

            while (idCategoria is None):
                insertProducto.viewCategorias()
                categoria = input("Escriba una categoria que este registrada: ")
                idCategoria = insertProducto.validarCategoria(categoria)
    
            nombre = input("escriba el nombre del objeto: ")
            descripcion = input("escriba una descripcion del objeto: ")
            precio = input("escriba el precio del objeto: ")
            precio = float(precio)
            cantidad = int(input("escriba la cantidad de productos: "))
            insertProducto.insertarProducto(nombre,idCategoria, descripcion, precio, cantidad)

        else:
            print("escriba un numero que este disponible")
            getInsertProducto()
