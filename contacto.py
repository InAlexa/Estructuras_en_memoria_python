class Contacto:
    def __init__(self, apellidos: str, nombres: str, numero: int):
        self.apellidos = apellidos
        self.nombres = nombres
        self.numero: int = numero

    def mostrar(self):
        return f'{self.apellidos}, {self.nombres}, {self.numero}'