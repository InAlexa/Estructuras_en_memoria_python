from contacto import Contacto
class Node:
    def __init__(self, contacto: Contacto):
        self.contacto: Contacto = contacto
        self.next: Node | None = None
