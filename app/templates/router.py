# Este archivo ayudará a manejar las rutas

class RouterManager:
    def __init__(self):

        # La ventana actual nos ayuda a determinar la ventana origen
        self.ventana_actual = None

    def acceder_login(self, ventana_anterior=None):
        from pagina_login import LoginWindow

        self.ventana_actual = LoginWindow()
        self.ventana_actual.show()
        ventana_anterior.close()


    def acceder_registro(self, ventana_anterior=None):
        from pagina_registro import PaginaRegistro

        self.ventana_actual = PaginaRegistro()
        self.ventana_actual.show()
        ventana_anterior.close()

    def acceder_principal(self, ventana_anterior=None,nombre_usuario=""):
       from pagina_principal import Pagina_principal
    # creamos un objeto de la ventana nueva que queremos mostrar aplicamos el método show para que se muestre
       self.ventana_actual = Pagina_principal(nombre_usuario=nombre_usuario)
       self.ventana_actual.show()
       ventana_anterior.close()

# if __name__ == "__main__":
#     pass
