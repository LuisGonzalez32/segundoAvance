from logic.dx_logic import Logic


class Cuenta(Logic):
    def __init__(self):
        super().__init__()


    def crearCuenta(self, nombre, apellido, usuario, contrasenia, correo):

        database = self.database
        sql = f"""INSERT INTO cliente (nombre, apellido, usuario, contrasenia, correo) VALUES (
        '{nombre}', '{apellido}', '{usuario}', '{contrasenia}', '{correo}') """
      
        cuenta = database.executeNonQueryBool(sql)
        if cuenta == True:
            print("")
            print("La cuenta fue creada correctamente\n")


    def validarCuenta(self, usuario, contrasenia):
        
        database = self.database
        sql = f"""select * from cliente where usuario = '{usuario}'
        and contrasenia = '{contrasenia}'"""
            
        record = database.executeQueryRows(sql)
        for row in record:
            if row["id"]:
                print("")
                print("La cuenta es correcta")
                print("")
                return (row["id"])
            elif not row["id"]:
                return None