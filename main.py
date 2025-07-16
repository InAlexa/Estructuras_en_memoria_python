from lista_enlazada import Lista_enlazada
from contacto import Contacto
def main():
    lista = Lista_enlazada()
    bandera = 0
    while (bandera == 0):
        print('Menú'
              '\n1. Agregar contacto (appellidos, nombres, número)'
              '\n2. Listar contactos'
              '\n3. Buscar contacto por nombre'
              '\n4. Eliminar contacto'
              '\n5. Salir')
        opcion = input('Escoja una opción: ')

        match opcion:
            case '1':
                apellidos = input('Ingrese los apellidos: ')
                nombres = input('Ingrese los nombres: ')
                numero = int(input('Ingrese el número: '))
                nuevo_contacto = Contacto(apellidos, nombres, numero)
                lista.append(nuevo_contacto)
                print(f'Contacto: {nuevo_contacto.mostrar()}. Añadido con éxito.')

            case '2':
                lista.mostrar_lista()

            case '3':
                contacto_a_buscar = input('Ingrese el nombre del contacto '
                                          'que desee buscar: ')
                lista.buscar_contacto(contacto_a_buscar)

            case '4':
                contacto_a_eliminar = input('Ingrese el nombre del contacto que desee eliminar: ')
                lista.eliminar_contacto(contacto_a_eliminar)

            case '5':
                print('Saliendo del programa...')
                bandera = 1
            case _:
                print('Ingrese una de las opciones.')


main()