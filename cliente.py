class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar_perfil(self):
        return f"Cliente: {self.nombre} - Email: {self.email}"