class Cliente:
    def __init__(self, cedula, nombre, email, telefono):
        self.cedula = cedula
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def mostrar_perfil(self):
        return f"Cliente: {self.nombre} | Contacto: {self.email}"