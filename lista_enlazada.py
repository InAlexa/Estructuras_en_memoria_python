from node import Node

class Lista_enlazada:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size = 0
        self.aux: Node | None = None

    def is_empty(self):
        return self.head is None and self.tail is None

    def append(self, contacto):
        nuevo_nodo = Node(contacto)
        if self.is_empty():
            self.head = nuevo_nodo
        else:
            self.tail.next = nuevo_nodo

        self.tail = nuevo_nodo
        self.size += 1

    def mostrar_lista(self):
        aux = self.head
        if not aux:
            print('La lista está vacía')
            return
        while aux:
            print(f'- {aux.contacto.mostrar()}')
            aux =  aux.next

    def buscar_contacto(self, persona: str):
        aux = self.head
        while aux is not None:
            if aux.contacto.nombres == persona:
                print('Contacto encontrado:',aux.contacto.mostrar())
                return True
            aux = aux.next
        print("Contacto no encontrado.")
        return False

    def eliminar_contacto(self, persona: str):
        aux = self.head
        anterior = None

        while aux is not None:
            if aux.contacto.nombres == persona:
                if anterior is None:
                    self.head = aux.next
                    if aux == self.tail:
                        self.tail = None
                else:
                    anterior.next = aux.next
                    if aux == self.tail:
                        self.tail = anterior

                self.size -= 1
                print('Contacto eliminado.')
                return

            anterior = aux
            aux = aux.next

        print('Contacto no encontrado.')


