"""Persistencia: memoria de largo plazo (disco duro)"""

import csv


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:
    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def update(self, name, phone, email):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                contact.phone = phone
                contact.email = email
                self._save()
                break
        else:
            self._not_found()

    # guardar en disco
    def _save(self):
        with open('contacts.csv', 'w') as filepy:
            writer = csv.writer(filepy)
            writer.writerow(('name', 'phone', 'email'))

            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def _not_found(self):
        print('*******')
        print('¡No encontrado!')
        print('*******')


def run():
    contact_book = ContactBook()
    # leer
    try:
        with open('contacts.csv', 'r') as f:
            reader = csv.reader(f)
            for index, row in enumerate(reader):
                if len(row) == 0:
                    continue
                if index == 0:
                    # Salta la primera fila que tiene los nombres de los campos 'name,phone,email'.
                    continue
                contact_book.add(row[0], row[1], row[2])
    except FileNotFoundError:
        print('No existe el archivo \'contacts.csv\'. Debe añadir un nuevo contacto para crearlo.')

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el tel del contacto: '))
            email = str(input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)

        elif command == 'ac':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el teléfono del contacto: '))
            email = str(input('Escribe el email del contacto: '))
            contact_book.update(name, phone, email)

        elif command == 'b':
            name = str(input('Escribe el nombre del contacto: '))
            contact_book.search(name)

        elif command == 'e':
            name = str(input('Escribe el nombre del contacto: '))
            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('B I E N V E N I D O  A  L A  A G E N D A')
    run()
